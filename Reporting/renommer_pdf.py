import os
import shutil
from datetime import datetime

def renommer_rapports():
    date_str = datetime.now().strftime("%d_%m_%Y")
    dossiers = ['Activite', 'Licences']
    
    for dossier in dossiers:
        if not os.path.exists(dossier):
            continue
            
        for fichier in os.listdir(dossier):
            if fichier.lower().endswith('.pdf'):
                chemin_complet = os.path.join(dossier, fichier)
                
                # Logique de renommage
                if dossier == 'Activite':
                    nouveau_nom = f'Rapport_Cible_Nettoyage_{date_str}.pdf'
                elif dossier == 'Licences':
                    nouveau_nom = f'Rapport_Stock_Licence_{date_str}.pdf'
                else:
                    continue
                
                chemin_cible = os.path.join(dossier, nouveau_nom)
                
                # Renommage
                shutil.move(chemin_complet, chemin_cible)
                print(f"Renommé : {fichier} -> {nouveau_nom}")

if __name__ == "__main__":
    renommer_rapports()
