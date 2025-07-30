# AnneSu11

Application Sudoku simple pour Windows 11 réalisée en Python avec Tkinter.

## Dépendances
- Python 3 (inclus dans la plupart des distributions)

## Utilisation

```bash
python3 AnneSu11.py
```

L'application offre un Sudoku aux couleurs rose et rose pâle, un bouton d'aide et un personnage nommé *Lys* représenté par une fleur animée.

## Création d'un exécutable Windows

Installez PyInstaller puis lancez la commande suivante :

```bash
pip install pyinstaller
pyinstaller --onefile --windowed AnneSu11.py
```

Le fichier généré se trouvera dans le dossier `dist/`. Cette étape ne peut pas être exécutée automatiquement ici en raison des limitations réseau.
