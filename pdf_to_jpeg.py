import os
from wand.image import Image
from tqdm import tqdm

pdf_directories = ['./assets/pdfs/ñ1', './assets/pdfs/ñ2']
img_directories = ['./assets/imgs/ñ1', './assets/imgs/ñ2']

for pdf_dir, img_dir in zip(pdf_directories, img_directories):
    for filename in tqdm(os.listdir(pdf_dir), desc=f"Convirtiendo archivos en {pdf_dir}"):
        if filename.endswith('.pdf'):
            # Seleccionamos el archivo PDF
            pdf_path = os.path.join(pdf_dir, filename)
            # Definimos el nombre del archivo de imagen
            img_path = os.path.join(img_dir, os.path.splitext(filename)[0] + '.jpeg')
            # Convertimos el PDF en imagen
            with Image(filename=pdf_path, resolution=300) as img:
                img.format = 'jpeg'
                img.save(filename=img_path)
