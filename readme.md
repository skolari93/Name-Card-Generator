# 🪪 Name Card Generator

Dieses Python-Skript erstellt personalisierte Namenskarten als PDF-Dateien basierend auf Daten aus einer Excel-Tabelle.

## Installation

### 1. Repository klonen
```bash
git clone https://github.com/skolari93/namecardgen.git
cd namecardgen
```

### 2. Conda-Umgebung erstellen und aktivieren
Zuerst [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) installieren. Dann:
```bash
conda env create -f environment.yml
conda activate namecardgen
```

## Vorbereitung

### 3. Excel-Datei vorbereiten
Die Excel-Datei sollte zwei Spalten enthalten:
- `Name` – Vor- und Nachname der Person
- `Class` – Klassenbezeichnung oder andere Gruppenzugehörigkeit

**Standard-Datei:** `Test.xlsx` (wird automatisch verwendet)

### 4. Logo
**Standard-Logo:** `logo.png` (wird automatisch verwendet)
Ersetze `logo.png` durch dein eigenes gewünschtes Logo.

## Verwendung

### Mit Standard-Dateien (Test.xlsx und logo.png):
```bash
python namecardgen.py
```

### Mit eigener Excel-Datei:
```bash
python namecardgen.py meine_studenten.xlsx
```

### Mit eigenem Logo:
```bash
python namecardgen.py --logo mein_logo.png
```

### Mit beiden eigenen Dateien:
```bash
python namecardgen.py meine_studenten.xlsx --logo mein_logo.png
```

### Hilfe anzeigen:
```bash
python namecardgen.py --help
```

## Ausgabe
- Die PDF-Datei wird automatisch mit dem gleichen Namen wie die Excel-Datei erstellt
- Beispiel: `Test.xlsx` → `Test.pdf`
- Jede Namenskarte wird auf einer separaten Seite im Querformat (A4 landscape) erstellt

## Tipps
- Verwende gutes Papier für professionelle Ergebnisse
- Das Logo sollte quadratisch oder rechteckig sein für beste Darstellung
- Die Excel-Datei muss die Spalten "Name" und "Class" enthalten (Groß-/Kleinschreibung beachten)