import os
import sys
from PIL import Image
import boto3
from botocore.config import Config
import mimetypes

# === CONFIGURATION OPTIMISATION ===
MAX_SIZE = (1200, 1200)
QUALITY = 85
OPTIMIZED_DIR = "/Users/vincentoliviero/.gemini/antigravity/scratch/images_optimized/blog"
SOURCE_DIR = "/Users/vincentoliviero/.gemini/antigravity/scratch/images_backup/blog"

# === CONFIGURATION R2 ===
ACCOUNT_ID = "fb767f48f088df691b4539018ac780b1"
ACCESS_KEY_ID = "9b48a5c58a388496b036944507d5c2d5"
SECRET_ACCESS_KEY = "dee2ceee2ef7762e924502fdad37a4e4cda5f893903c04e4784c54a750d9e8a8"
BUCKET_NAME = "iatechnologie-images"
R2_ENDPOINT = f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com"

os.makedirs(OPTIMIZED_DIR, exist_ok=True)

# Connexion R2
s3 = boto3.client(
    "s3",
    endpoint_url=R2_ENDPOINT,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(signature_version="s3v4")
)

# Liste des images
files = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
print(f"--- Optimisation et Upload de {len(files)} images ---")

optimized_count = 0
uploaded_count = 0
errors = 0

for i, filename in enumerate(files):
    source_path = os.path.join(SOURCE_DIR, filename)
    optimized_path = os.path.join(OPTIMIZED_DIR, filename)
    r2_key = f"images/blog/{filename}"

    try:
        # 1. Optimiser l'image
        with Image.open(source_path) as img:
            # Convertir en RGB si nécessaire (pour JPEG)
            if img.mode in ("RGBA", "P") and filename.lower().endswith(('.jpg', '.jpeg')):
                img = img.convert("RGB")
            
            # Redimensionner
            img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
            
            # Sauvegarder avec compression
            if filename.lower().endswith('.png'):
                # Palette optimization for smaller PNGs
                if img.mode != "P":
                  img_small = img.convert("P", palette=Image.ADAPTIVE, colors=256)
                  img_small.save(optimized_path, "PNG", optimize=True)
                else:
                  img.save(optimized_path, "PNG", optimize=True)
            else:
                img.save(optimized_path, optimize=True, quality=QUALITY)
        
        optimized_count += 1
        
        # 2. Upload vers R2
        content_type, _ = mimetypes.guess_type(filename)
        if not content_type: content_type = "image/jpeg"
        
        s3.upload_file(
            optimized_path, BUCKET_NAME, r2_key,
            ExtraArgs={"ContentType": content_type}
        )
        uploaded_count += 1
        
        # Afficher progression
        if (i+1) % 50 == 0 or (i+1) == len(files):
            print(f"  [{i+1}/{len(files)}] ✅ {uploaded_count} re-uploadés | ❌ {errors} erreurs")
            
    except Exception as e:
        errors += 1
        print(f"  ❌ Erreur pour {filename}: {e}")

print(f"\n--- TERMINE ! ---")
print(f"Images optimisées et uploadées : {uploaded_count}")
print(f"Erreurs : {errors}")
