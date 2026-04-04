import os
import re

articles_dir = 'src/content/articles'
files = [f for f in os.listdir(articles_dir) if f.endswith('.md')]

# Mots FR communs pour détection
fr_markers = set(['le', 'la', 'les', 'des', 'un', 'une', 'est', 'sont', 'pour', 'dans', 'avec', 'plus', 'fait', 'donc', 'mais', 'par', 'sur', 'qui', 'fait', 'ces', 'ses', 'ce', 'que', 'qui', 'pourquoi', 'comment', 'votre', 'notre', 'tout', 'tous'])

# Dictionnaires rapides pour autres langues (échantillons)
lang_markers = {
    'it': set(['il', 'la', 'i', 'gli', 'le', 'un', 'una', 'e', 'è', 'sono', 'per', 'in', 'con', 'più', 'fatto', 'quindi', 'ma', 'da', 'su', 'che', 'chi', 'perché', 'come', 'vostro', 'nostro', 'tutto', 'tutti']),
    'es': set(['el', 'la', 'los', 'las', 'un', 'una', 'es', 'son', 'para', 'en', 'con', 'más', 'hecho', 'entonces', 'pero', 'por', 'sobre', 'que', 'quien', 'porque', 'como', 'vuestro', 'nuestro', 'todo', 'todos']),
    'en': set(['the', 'a', 'an', 'is', 'are', 'for', 'in', 'with', 'more', 'done', 'so', 'but', 'by', 'on', 'who', 'what', 'why', 'how', 'your', 'our', 'all']),
    'de': set(['der', 'die', 'das', 'ein', 'eine', 'ist', 'sind', 'für', 'in', 'mit', 'mehr', 'getan', 'also', 'aber', 'von', 'auf', 'wer', 'was', 'warum', 'wie', 'euer', 'unser', 'alle']),
}

def detect_lang(text):
    words = re.findall(r'\b[a-z]{2,15}\b', text.lower())
    if not words: return 'fr'
    
    scores = {'fr': sum(1 for w in words if w in fr_markers)}
    for l, markers in lang_markers.items():
        scores[l] = sum(1 for w in words if w in markers)
    
    best_lang = max(scores, key=scores.get)
    if scores[best_lang] == 0: return 'fr'
    return best_lang

print(f"🏷️ Marquage de {len(files)} articles...")

for f in files:
    path = os.path.join(articles_dir, f)
    with open(path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    # Détection
    lang = detect_lang(content)
    
    # Ajout du tag lang dans le frontmatter
    if 'lang:' not in content:
        # On l'ajoute juste après le premier '---'
        new_content = content.replace('---\n', f'---\nlang: "{lang}"\n', 1)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("✅ Marquage terminé.")
