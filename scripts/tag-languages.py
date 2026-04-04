import os
import re
import csv

articles_dir = 'src/content/articles'
gsc_csv = 'scripts/gsc_data.csv'
files = [f for f in os.listdir(articles_dir) if f.endswith('.md')]

# Mots FR communs STRİCTS
fr_markers = set(['le', 'la', 'les', 'des', 'un', 'une', 'est', 'sont', 'pour', 'dans', 'avec', 'plus', 'fait', 'donc', 'mais', 'par', 'sur', 'qui', 'que', 'qui', 'pourquoi', 'comment', 'votre', 'notre', 'tout', 'tous', 'dans', 'votre', 'très', 'cette', 'ceux'])

# 1. Cartographie GSC (La source de vérité pour le trafic et les langues)
gsc_map = {}
if os.path.exists(gsc_csv):
    with open(gsc_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or 'http' not in row[0]: continue
            url = row[0].strip().rstrip('/')
            # On cherche /lang/slug/
            match = re.search(r'iatechnologie\.com/([a-z]{2})/(.*)', url)
            if match:
                lang = match.group(1)
                slug = match.group(2).split('/')[-1]
                gsc_map[slug] = lang
            else:
                # C'est probablement du FR si pas de préfixe ou site racine
                match_fr = re.search(r'iatechnologie\.com/(.*)', url)
                if match_fr:
                    slug = match_fr.group(1).split('/')[-1]
                    if slug: gsc_map[slug] = 'fr'

print(f"🗺️  Map GSC chargée ({len(gsc_map)} slugs)")

def detect_lang_safe(text, filename_slug):
    # Si c'est dans GSC, c'est prioritaire
    if filename_slug in gsc_map:
        return gsc_map[filename_slug]
    
    # Sinon, détection par fréquence
    words = re.findall(r'\b[a-z]{2,15}\b', text.lower())
    if not words: return 'unknown'
    
    fr_score = sum(1 for w in words if w in fr_markers)
    ratio = fr_score / len(words)
    
    if ratio > 0.08: # Si assez de marqueurs FR
        return 'fr'
    
    return 'other'

print(f"🏷️  Marquage de {len(files)} articles...")

count_fr = 0
count_other = 0

for f in files:
    path = os.path.join(articles_dir, f)
    with open(path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    filename_slug = f.replace('.md', '')
    lang = detect_lang_safe(content, filename_slug)
    
    if lang == 'fr': count_fr += 1
    else: count_other += 1

    # Remplacement ou ajout du tag lang
    if 'lang:' in content:
        new_content = re.sub(r'lang: ".*"', f'lang: "{lang}"', content)
    else:
        new_content = content.replace('---\n', f'---\nlang: "{lang}"\n', 1)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(new_content)

print(f"✅ Marquage terminé : {count_fr} FR, {count_other} étrangers/autres.")
