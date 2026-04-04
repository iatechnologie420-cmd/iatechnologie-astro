import os
import re
import csv

articles_dir = 'src/content/articles'
gsc_csv = 'scripts/gsc_data.csv'
files = [f for f in os.listdir(articles_dir) if f.endswith('.md')]

# Charge GSC slugs
gsc_slugs = set()
if os.path.exists(gsc_csv):
    with open(gsc_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or 'http' not in row[0]: continue
            # Extract slug from URL
            url = row[0].strip().rstrip('/')
            slug = url.split('/')[-1]
            if slug: gsc_slugs.add(slug)

# Critères d'obsolescence
obsolete_years = ['2021', '2022', '2023']
obsolete_techs = ['gpt-3', 'gpt3', 'dall-e 2', 'midjourney v4', 'stablediffusion 1', 'windows 10 tips', 'iphone 13']
generic_terms = ['c est quoi', 'qu est ce que', 'definition de', 'introduction a', 'bases de l informatique']

def audit_article(filename, title, content):
    filename_slug = filename.replace('.md', '')
    title_lower = title.lower()
    
    reasons_to_cull = []
    
    # 1. Sanctuaire GSC
    if filename_slug in gsc_slugs:
        return "GARDER - Performance GSC (Top 1000)"

    # 2. Obsolescence Temporelle
    for year in obsolete_years:
        if year in title:
            reasons_to_cull.append(f"Année obsolète ({year})")
    
    # 3. Technologies Obsolètes
    for tech in obsolete_techs:
        if tech in title_lower:
            reasons_to_cull.append(f"Technologie dépassée ({tech})")
            
    # 4. Sujets trop génériques / Faible valeur ajoutée IA
    for term in generic_terms:
        if term in title_lower:
            # On vérifie si c'est vraiment générique (ex: "C'est quoi un bit?") vs spécifique IA
            if 'intelligence' not in title_lower and 'ia' not in title_lower:
                reasons_to_cull.append(f"Sujet trop générique ({term})")

    if reasons_to_cull:
        return f"SUPPRIMER - {', '.join(reasons_to_cull)}"
    
    return "GARDER - Potentiel expert (Thématique IA)"

results = []
for f in files:
    path = os.path.join(articles_dir, f)
    with open(path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    title_match = re.search(r'^title: "(.*)"', content, re.MULTILINE)
    title = title_match.group(1) if title_match else f
    
    status = audit_article(f, title, content)
    results.append(f"| {f} | {title[:60]}... | {status} |")

# Tri des résultats pour affichage
results.sort(key=lambda x: "SUPPRIMER" in x)

with open('/tmp/seo_audit_report.txt', 'w', encoding='utf-8') as f:
    f.write("# Rapport d'Audit SEO - Mega-Tri\n\n")
    f.write("| Fichier | Titre | Statut / Justification |\n")
    f.write("| :--- | :--- | :--- |\n")
    for r in results:
        f.write(r + "\n")
