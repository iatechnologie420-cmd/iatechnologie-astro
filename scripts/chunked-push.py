import subprocess
import os

def run(cmd):
    print(f"Executing: {cmd}")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode(), process.returncode

def chunked_push():
    print("🚀 Démarrage du Push par morceaux (Fichiers individuels)...")
    
    # Trouver tous les fichiers dans public/images récursivement
    all_images = []
    for root, dirs, files in os.walk("public/images"):
        for file in files:
            all_images.append(os.path.join(root, file))
    
    # Ajouter .gitignore si modifié
    stdout_git, _, _ = run("git status --porcelain")
    if ".gitignore" in stdout_git:
        all_images.append(".gitignore")
        
    print(f"Total fichiers à traiter : {len(all_images)}")
    
    if not all_images:
        print("✅ Aucun fichier à envoyer.")
        return

    CHUNK_SIZE = 20 # Paquets très petits pour plus de sécurité
    for i in range(0, len(all_images), CHUNK_SIZE):
        chunk = all_images[i:i + CHUNK_SIZE]
        print(f"📦 Traitement du paquet {i // CHUNK_SIZE + 1} / {len(all_images)//CHUNK_SIZE + 1} ({len(chunk)} fichiers)...")
        
        # Ajouter les fichiers du paquet un par un
        for f in chunk:
            run(f'git add "{f}"')
        
        # Committer le paquet
        _, _, code = run(f'git commit -m "Upload images chunk {i // CHUNK_SIZE + 1}"')
        if code != 0:
            print("Rien à committer pour ce paquet.")
            continue
            
        # Pousser le paquet
        print("Envoi vers GitHub...")
        stdout_push, stderr_push, push_code = run("git push origin main")
        if push_code != 0:
            print(f"❌ Échec de l'envoi pour ce paquet : {stderr_push}")
            # On continue pour maximiser les images envoyées
            continue

    print("🏁 Fin du processus d'envoi massif.")

if __name__ == "__main__":
    chunked_push()
