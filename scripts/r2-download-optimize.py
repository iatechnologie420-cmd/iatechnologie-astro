import os
import boto3
from PIL import Image
from botocore.config import Config
import mimetypes
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration R2
ACCOUNT_ID = "fb767f48f088df691b4539018ac780b1"
ACCESS_KEY_ID = "9b48a5c58a388496b036944507d5c2d5"
SECRET_ACCESS_KEY = "dee2ceee2ef7762e924502fdad37a4e4cda5f893903c04e4784c54a750d9e8a8"
BUCKET_NAME = "iatechnologie-images"
R2_ENDPOINT = f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com"

# Paramètres optimisation
MAX_SIZE = (1200, 1200)
QUALITY = 85
TEMP_DIR = "/Users/vincentoliviero/.gemini/antigravity/scratch/r2_temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def get_s3():
    return boto3.client(
        "s3",
        endpoint_url=R2_ENDPOINT,
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        region_name="auto",
        config=Config(signature_version="s3v4")
    )

s3 = get_s3()

def process_one_image(key):
    filename = os.path.basename(key)
    local_path = os.path.join(TEMP_DIR, f"{os.getpid()}_{filename}")
    s3_thread = get_s3()
    
    try:
        # 1. Télécharger
        s3_thread.download_file(BUCKET_NAME, key, local_path)
        
        orig_size = os.path.getsize(local_path)
        
        # 2. Optimiser
        with Image.open(local_path) as img:
            if img.mode in ("RGBA", "P") and filename.lower().endswith(('.jpg', '.jpeg')):
                img = img.convert("RGB")
            img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
            if filename.lower().endswith('.png'):
                img.save(local_path, "PNG", optimize=True)
            else:
                img.save(local_path, optimize=True, quality=QUALITY)
        
        new_size = os.path.getsize(local_path)
        
        # 3. Uploader
        content_type, _ = mimetypes.guess_type(filename)
        if not content_type: content_type = "image/jpeg"
        s3_thread.upload_file(local_path, BUCKET_NAME, key, ExtraArgs={"ContentType": content_type})
        
        # 4. Nettoyer
        if os.path.exists(local_path): os.remove(local_path)
        return True, f"{key} ({orig_size//1024}kB -> {new_size//1024}kB)"
    except Exception as e:
        if os.path.exists(local_path): os.remove(local_path)
        return False, f"{key}: {e}"

# Lister les objets
print("--- Récupération de la liste des images R2 (Progressive) ---")
paginator = s3.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=BUCKET_NAME, Prefix="images/blog/")
all_keys = []
for page in pages:
    if "Contents" in page:
        for obj in page["Contents"]:
            if obj["Size"] > 0:
                all_keys.append(obj["Key"])

total = len(all_keys)
print(f"Total images détectées : {total}")

success_count = 0
error_count = 0

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(process_one_image, key): key for key in all_keys}
    for i, future in enumerate(as_completed(futures)):
        success, msg = future.result()
        if success:
            success_count += 1
        else:
            error_count += 1
            print(f"  ❌ {msg}")
        
        if (i+1) % 20 == 0 or (i+1) == total:
            print(f"  [{i+1}/{total}] ✅ {success_count} réussies | ❌ {error_count} erreurs")

print(f"\n--- TERMINE ! ---")
print(f"Images traitée avec succès : {success_count}")
print(f"Erreurs : {error_count}")
