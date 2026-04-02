import os
import re
import urllib.parse
import unicodedata

ARTICLES_DIR = '/Users/vincentoliviero/.gemini/antigravity/scratch/iatechnologie-astro/src/content/articles'

def slugify(value):
    value = urllib.parse.unquote(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value).strip('-')
    return value

def sanitize():
    print("🚀 Démarrage de la sanitisation Python...")
    if not os.path.exists(ARTICLES_DIR):
        print(f"❌ Dossier non trouvé: {ARTICLES_DIR}")
        return
        
    files = [f for f in os.listdir(ARTICLES_DIR) if f.endswith('.md')]
    print(f"Nombre d'articles à traiter: {len(files)}")

    renamed_count = 0
    updated_count = 0

    for filename in files:
        file_path = os.path.join(ARTICLES_DIR, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            decoded_name = urllib.parse.unquote(filename.replace('.md', ''))
            clean_slug = slugify(decoded_name)
            
            if not clean_slug:
                clean_slug = "article-" + filename.replace('.md', '')[:10]
            
            orig_slug = clean_slug
            counter = 1
            while clean_slug != filename.replace('.md', '') and os.path.exists(os.path.join(ARTICLES_DIR, clean_slug + ".md")):
                 clean_slug = f"{orig_slug}-{counter}"
                 counter += 1

            new_filename = clean_slug + ".md"
            new_path = os.path.join(ARTICLES_DIR, new_filename)

            slug_pattern = r'(slug:\s*["\'])(.+?)(["\'])'
            match = re.search(slug_pattern, content)
            
            new_content = content
            if match:
                if match.group(2) != clean_slug:
                    start, end = match.span()
                    new_content = content[:start] + f'slug: "{clean_slug}"' + content[end:]
                    updated_count += 1
            else:
                new_content = re.sub(r'---', f'---\nslug: "{clean_slug}"', content, count=1)
                updated_count += 1
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

            if filename != new_filename:
                os.rename(file_path, new_path)
                renamed_count += 1
        except Exception as e:
            print(f"❌ Erreur sur {filename}: {e}")

    print(f"✅ Terminé ! Renommés: {renamed_count}, Slugs mis à jour: {updated_count}")

if __name__ == "__main__":
    sanitize()
