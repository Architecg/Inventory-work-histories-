# Inventory-work-histories-
## Enviroment  setup 

Create the conda environment and activate it: 

```bash
conda env create -f enviroment.yml
conda activate ocr_env
```

## OCR utilities
The script ocr_utils.py normalizes OCR text and classifies with the patterns defined in expresiones.py

```bash
python ocr_utils.py input.json output.json
```

The output JSON includes the raw and normalized text along with any pattern matches for each page.
