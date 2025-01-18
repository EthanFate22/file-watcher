import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('input.txt'):
            print(f"Le fichier {event.src_path} a été modifié !")
            # Lecture du contenu modifié
            try:
                with open(event.src_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                print("Nouveau contenu :")
                print(content)
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier : {e}")

def watch_file(file_path):
    # Vérifier si le fichier existe
    if not os.path.exists(file_path):
        print(f"Le fichier {file_path} n'existe pas !")
        return

    # Créer l'observateur et le gestionnaire
    event_handler = FileChangeHandler()
    observer = Observer()
    
    # Obtenir le dossier contenant le fichier
    path = os.path.dirname(os.path.abspath(file_path))
    
    # Démarrer la surveillance
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    
    print(f"Surveillance du fichier {file_path} démarrée...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nSurveillance arrêtée.")
    
    observer.join()

if __name__ == "__main__":
    file_path = r"C:\Users\Wills\Desktop\Dev\ClaudeIntegration\input.txt"
    watch_file(file_path)
