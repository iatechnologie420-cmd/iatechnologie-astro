import os
import re
import csv
import html

articles_dir = 'src/content/articles'
gsc_csv = 'scripts/gsc_data.csv'
files = [f for f in os.listdir(articles_dir) if f.endswith('.md')]

# Mots FR uniques (marqueurs forts)
fr_markers = set(['le', 'les', 'des', 'est', 'sont', 'pour', 'dans', 'avec', 'mais', 'par', 'sur', 'qui', 'que', 'pourquoi', 'comment', 'votre', 'notre', 'tout', 'tous', 'très', 'cette', 'ceux', 'ainsi', 'dont'])
# Mots ES (Espagnol) markers
es_markers = set(['el', 'los', 'las', 'del', 'es', 'son', 'para', 'en', 'con', 'pero', 'por', 'que', 'quien', 'porque', 'como', 'vuestro', 'nuestro', 'todo', 'todos', 'esta', 'estos'])

# 1. Cartographie GSC
gsc_map = {}
if os.path.exists(gsc_csv):
    with open(gsc_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or 'http' not in row[0]: continue
            url = row[0].strip().rstrip('/')
            match = re.search(r'iatechnologie\.com/([a-z]{2})/(.*)', url)
            if match:
                lang = match.group(1)
                slug = match.group(2).split('/')[-1]
                gsc_map[slug] = lang
            else:
                match_fr = re.search(r'iatechnologie\.com/(.*)', url)
                if match_fr:
                    slug = match_fr.group(1).split('/')[-1]
                    if slug: gsc_map[slug] = 'fr'

def detect_lang_advanced(content, filename_slug):
    # a. GSC est prioritaire
    if filename_slug in gsc_map:
        return gsc_map[filename_slug]
    
    # b. Détection par suffixes de catégories (ex: ["tech-es"])
    categories_match = re.search(r'categories: \[(.*)\]', content)
    if categories_match:
        cats = categories_match.group(1).split(',')
        suffixes = []
        for cat in cats:
            match = re.search(r'-([a-z]{2})"', cat)
            if match: suffixes.append(match.group(1))
        if suffixes:
            # On prend le suffixe le plus fréquent
            best_guess = max(set(suffixes), key=suffixes.count)
            return best_guess

    # c. Détection par ratio textuel strict
    words = re.findall(r'\b[a-z]{2,15}\b', content.lower())
    if words:
        fr_score = sum(1 for w in words if w in fr_markers)
        es_score = sum(1 for w in words if w in es_markers)
        if fr_score > es_score and fr_score / len(words) > 0.05:
            return 'fr'
        if es_score > fr_score and es_score / len(words) > 0.05:
            return 'es'
            
    # d. Fallback : si on ne sait pas, on marque comme 'other' pour ne pas polluer le blog FR
    return 'other'

def clean_html_entities(text):
    # Unescape common entities and replace specifically requested ones
    text = html.unescape(text)
    # Reste manuel pour les cas persistants
    replacements = {
        '&#8217;': "'",
        '&#8211;': "–",
        '&#8220;': "“",
        '&#8221;': "”",
        '&#8230;': "…",
        '&#038;': "&",
        '&#8212;': "—",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

print(f"🧹 Nettoyage HTML et marquage de {len(files)} articles...")

count_fr = 0
count_other = 0

for f in files:
    path = os.path.join(articles_dir, f)
    with open(path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    # 1. Nettoyage HTML dans titre et contenu
    content = clean_html_entities(content)
    
    # 2. Détection Langue
    filename_slug = f.replace('.md', '')
    lang = detect_lang_advanced(content, filename_slug)
    
    if lang == 'fr': count_fr += 1
    else: count_other += 1

    # Remplacement ou ajout du tag lang
    if 'lang:' in content:
        content = re.sub(r'lang: ".*"', f'lang: "{lang}"', content)
    else:
        content = content.replace('---\n', f'---\nlang: "{lang}"\n', 1)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"✅ Opération terminée : {count_fr} FR identifiés, {count_other} mis à l'écart.")
print("💡 Tous les titres et contenus ont été purgés des entités HTML (&#8217;, etc.)")
