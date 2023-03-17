import json
import xmltodict

# Abrir el archivo XML
with open('./xmls/ñ2/1509.xml', 'r') as f:
    xml_string = f.read()

# Convertir el archivo XML a un diccionario de Python
xml_dict = xmltodict.parse(xml_string)

# Convertir el diccionario de Python a formato JSON
json_string = json.dumps(xml_dict)

# Escribir el archivo JSON resultante
with open('archivo.json', 'w') as f:
    f.write(json_string)