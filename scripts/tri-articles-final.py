import os
import re
import csv

articles_dir = 'src/content/articles'
gsc_csv = 'scripts/gsc_data.csv'

# Charger tous les fichiers existants
files = sorted([f for f in os.listdir(articles_dir) if f.endswith('.md')])

# Analyse GSC pour identifier les articles qui génèrent du trafic
gsc_champions = set()
if os.path.exists(gsc_csv):
    with open(gsc_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or 'http' not in row[0]: continue
            # Extraire le slug de l'URL GSC
            url = row[0].strip().rstrip('/')
            match = re.search(r'iatechnologie\.com/(.*)', url)
            if match:
                full_path = match.group(1)
                slug = full_path.split('/')[-1]
                if slug:
                    gsc_champions.add(slug)

# Mots FR communs
fr_markers = set(['le', 'la', 'les', 'des', 'un', 'une', 'est', 'sont', 'pour', 'dans', 'avec', 'plus', 'fait', 'donc', 'mais', 'par', 'sur', 'qui', 'fait', 'ces', 'ses', 'ce', 'que', 'qui', 'pourquoi', 'comment', 'votre', 'notre', 'tout', 'tous'])

# Champions manuels
manual_keywords = ['wawacity', 'discord-ps5', 'logiciels-ia-marketing', 'comment-marche-ia', 'theoreme-de-bayes', 'ia-definition', 'outil-ia-gratuit', 'histoire-de-lia']

to_keep = []
to_delete = []
kept_reasons = {} # Pour le debug

print(f"📊 Analyse de {len(files)} articles...")

for f in files:
    filename_no_ext = f.replace('.md', '')
    
    # 1. Est-ce un champion ?
    is_champion = (filename_no_ext in gsc_champions) or \
                  any(kw in f for kw in manual_keywords)
    
    # 2. Doublons WordPress
    if not is_champion and re.search(r'-\d+\.md$', f):
        to_delete.append(f)
        continue
        
    try:
        with open(os.path.join(articles_dir, f), 'r', encoding='utf-8', errors='replace') as cf:
            text = cf.read().lower()
            words = re.findall(r'\b[a-z]{2,15}\b', text)
            
            # 3. Qualité (articles trop courts < 80 mots)
            if not is_champion and len(words) < 80:
                to_delete.append(f)
                continue
                
            # 4. Langue (Ratio Français)
            score = sum(1 for w in words if w in fr_markers)
            ratio = score / len(words) if words else 0
            
            if is_champion:
                to_keep.append(f)
                kept_reasons[f] = "🔥 Champion GSC/Manuel"
            elif ratio >= 0.08:
                to_keep.append(f)
                kept_reasons[f] = f"🇫🇷 Français (ratio {ratio:.2f})"
            else:
                to_delete.append(f)
    except Exception as e:
        if is_champion:
            to_keep.append(f)
            kept_reasons[f] = "🔥 Champion (Erreur lecture)"
        else:
            to_delete.append(f)

print(f'\n--- RAPPORT FINAL ---')
print(f'📁 Total articles analysés : {len(files)}')
print(f'✅ Articles CONSERVÉS : {len(to_keep)}')
print(f'🗑️ Articles à SUPPRIMER : {len(to_delete)}')

# --- EXECUTION ---
perform_deletion = True 

if perform_deletion:
    print(f"\n⚠️ SUPPRESSION EN COURS...")
    for f in to_delete:
        os.remove(os.path.join(articles_dir, f))
    print(f"✅ Terminé. {len(to_delete)} fichiers supprimés.")
else:
    print(f"\n💡 MODE PREVIEW : Aucun fichier n'a été supprimé.")
    print(f"Exemple d'articles conservés :")
    for f in to_keep[:15]:
        print(f"  - {f} ({kept_reasons.get(f, 'Inconnu')})")
