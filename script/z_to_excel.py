import xml.etree.ElementTree as ET
from openpyxl import Workbook
import os

# Crear un nuevo libro de Excel
workbook = Workbook()
# Seleccionar la hoja activa
sheet = workbook.active

# Obtener una lista de todos los archivos XML dentro del directorio ./xmls/ñ1
lista_archivos = sorted([f for f in os.listdir("../xmls/ñ1") if f.endswith(".xml")])

# Recorrer todos los archivos XML en la lista y procesarlos
for archivo in lista_archivos:
    # Analizar el archivo XML
    tree = ET.parse(os.path.join("../xmls/ñ1", archivo))
    root = tree.getroot()
    
    # Obtener la última etiqueta "Documento"
    documentos = root.findall(".//Documento")
    ultimo_documento = documentos[-1]
    items = ultimo_documento.find('.//Items')
    linea = items.find('.//LineaUsuario')
    for l in linea :
        text = l.find('.//Texto').text
        print(text)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
# Guardar el archivo Excel
# workbook.save("datos.xlsx")
