#!/usr/bin/env python3
"""
Correction complète des frontmatters YAML dans tous les articles.
Corrige:
1. Ligne vide après --- (déjà fixé, mais sécurité)
2. Clés YAML dupliquées (garde la première occurrence de chaque clé)
3. Lignes invalides dans le frontmatter
"""
import os
import re

articles_dir = "src/content/articles"
fixed_count = 0
files_fixed = 0

for filename in sorted(os.listdir(articles_dir)):
    if not filename.endswith('.md'):
        continue

    filepath = os.path.join(articles_dir, filename)

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    if not content.startswith('---'):
        continue

    # Trouver la fin du frontmatter (le second ---)
    rest_after_open = content[3:]  # après le premier ---
    end_match = re.search(r'\n---(\n|$)', rest_after_open)
    if not end_match:
        continue

    frontmatter_raw = rest_after_open[:end_match.start()]
    body = rest_after_open[end_match.end():]

    # Traiter le frontmatter ligne par ligne pour supprimer les doublons
    lines = frontmatter_raw.split('\n')
    seen_keys = set()
    new_lines = []
    skip_multiline = False
    changes = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Ligne vide = garder
        if line.strip() == '':
            new_lines.append(line)
            i += 1
            continue

        # Check si c'est une clé YAML (key: value)
        key_match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*:', line)
        if key_match:
            key = key_match.group(1)
            if key in seen_keys:
                # Clé dupliquée - supprimer cette ligne et ses éventuelles suites
                changes += 1
                # Skip aussi les lignes de continuation (indentées)
                i += 1
                while i < len(lines) and lines[i].startswith(' '):
                    i += 1
                continue
            else:
                seen_keys.add(key)
                new_lines.append(line)
                i += 1
                # Garder les lignes de continuation
                while i < len(lines) and (lines[i].startswith(' ') or lines[i].startswith('\t')):
                    new_lines.append(lines[i])
                    i += 1
                continue

        # Ligne de liste YAML (commence par -)
        if line.lstrip().startswith('- ') or line.strip() == '-':
            new_lines.append(line)
            i += 1
            continue

        # Ligne invalide (ni clé, ni liste, ni vide, ni continuation)
        # La supprimer
        changes += 1
        i += 1

    if changes > 0:
        new_frontmatter = '\n'.join(new_lines)
        # S'assurer qu'il n'y a pas de ligne vide au début du frontmatter
        new_frontmatter = new_frontmatter.lstrip('\n')
        new_content = '---\n' + new_frontmatter + '\n---\n' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        files_fixed += 1
        fixed_count += changes

print(f"Fichiers corrigés: {files_fixed}")
print(f"Problèmes résolus: {fixed_count}")
