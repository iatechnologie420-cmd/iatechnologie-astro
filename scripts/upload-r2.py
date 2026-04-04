#!/usr/bin/env python3
"""
Upload images to Cloudflare R2 and update article frontmatter paths.
"""
import os
import sys
import warnings
warnings.filterwarnings('ignore')
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
import mimetypes

# === CONFIGURATION R2 ===
ACCOUNT_ID = "fb767f48f088df691b4539018ac780b1"
ACCESS_KEY_ID = "9b48a5c58a388496b036944507d5c2d5"
SECRET_ACCESS_KEY = "dee2ceee2ef7762e924502fdad37a4e4cda5f893903c04e4784c54a750d9e8a8"
BUCKET_NAME = "iatechnologie-images"
R2_ENDPOINT = f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com"
PUBLIC_URL = "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev"

IMAGES_DIR = "/Users/vincentoliviero/.gemini/antigravity/scratch/images_backup/blog"

# === CONNEXION R2 ===
s3 = boto3.client(
    "s3",
    endpoint_url=R2_ENDPOINT,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(signature_version="s3v4")
)

# Test connexion
print("=== Test de connexion R2 ===")
try:
    resp = s3.list_objects_v2(Bucket=BUCKET_NAME, MaxKeys=1)
    print(f"✅ Connecté au bucket '{BUCKET_NAME}'")
except Exception as e:
    print(f"❌ Erreur: {e}")
    sys.exit(1)

# === UPLOAD DES IMAGES ===
files = sorted([f for f in os.listdir(IMAGES_DIR) if os.path.isfile(os.path.join(IMAGES_DIR, f))])
print(f"\n=== Upload de {len(files)} images vers R2 ===")

uploaded = 0
skipped = 0
errors = 0

for i, filename in enumerate(files):
    local_path = os.path.join(IMAGES_DIR, filename)
    r2_key = f"images/blog/{filename}"
    
    # Vérifier si déjà uploadé
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=r2_key)
        skipped += 1
    except ClientError:
        # Pas encore uploadé → upload
        content_type, _ = mimetypes.guess_type(filename)
        if not content_type:
            content_type = "image/jpeg"
        try:
            s3.upload_file(
                local_path, BUCKET_NAME, r2_key,
                ExtraArgs={"ContentType": content_type}
            )
            uploaded += 1
        except Exception as e:
            errors += 1
            print(f"  ❌ {filename}: {e}")
    
    if (i + 1) % 50 == 0 or (i + 1) == len(files):
        print(f"  [{i+1}/{len(files)}] ✅ {uploaded} uploadés | ⏭ {skipped} déjà là | ❌ {errors} erreurs")

print(f"\n✅ Upload terminé!")
print(f"  → {uploaded} nouvelles images sur R2")
print(f"  → {skipped} déjà présentes")
print(f"  → URL publique: {PUBLIC_URL}/images/blog/FICHIER.png")
