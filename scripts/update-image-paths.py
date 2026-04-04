#!/usr/bin/env python3
"""
Met à jour les chemins featuredImage dans tous les articles
de /images/blog/... vers l'URL R2 publique.
"""
import os
import re

ARTICLES_DIR = "src/content/articles"
R2_BASE = "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev"
OLD_PREFIX = "/images/"
NEW_PREFIX = f"{R2_BASE}/images/"

updated_files = 0
updated_fields = 0

for filename in sorted(os.listdir(ARTICLES_DIR)):
    if not filename.endswith('.md'):
        continue
    
    filepath = os.path.join(ARTICLES_DIR, filename)
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Remplacer les chemins featuredImage dans le frontmatter
    new_content = content.replace(
        f'"/images/',
        f'"{R2_BASE}/images/'
    )
    
    # Aussi remplacer dans le corps HTML (img src="/images/...)
    new_content = new_content.replace(
        'src="/images/',
        f'src="{R2_BASE}/images/'
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files += 1
        count = content.count('"/images/') + content.count('src="/images/')
        updated_fields += count

print(f"✅ {updated_files} fichiers mis à jour")
print(f"✅ {updated_fields} chemins d'images remplacés")
print(f"✅ Ancien préfixe: /images/")
print(f"✅ Nouveau préfixe: {R2_BASE}/images/")
