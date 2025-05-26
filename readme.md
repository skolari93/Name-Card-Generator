# 🪪 Name Card Generator

Dieses Python-Skript erstellt personalisierte Namenskarten als PDF-Dateien basierend auf Daten aus einer Excel-Tabelle.

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

### 3. Excel-Datei vorbereiten

Die Excel-Datei (`Test.xlsx`) sollte zwei Spalten enthalten:
- `Name` – Vor- und Nachname der Person
- `Class` – Klassenbezeichnung oder andere Gruppenzugehörigkeit

### 4. Logo

Ersetze `logo.png` durch eigenes gewünschtes Logo.

### 5. Verwendung

```bash
python .\namecardgen.py
```

## Tipps
- Gutes Papier verwenden