# import jinja2
# import pdfkit
# from xml.dom import minidom
# from script.AB import AB
# from script.B import B
# from script.base import base
# import os

# import xml.etree.ElementTree as ET

# tree = ET.parse('./xmls/1566.xml')

# # Cargar el archivo XML
# root = tree.getroot()

# # Encontrar la última etiqueta Documento
# documento = root.find('.//Documento[last()]')

# # Obtener los valores de las etiquetas requeridas dentro de la última etiqueta Documento
# tipo_comprobante = documento.find('.//CierreDiarioContextoTipoComprobante/TipoComprobante').text
# informacion_documento = documento.find('.//CierreDiarioInformacionDocumento')
# totales = documento.find('.//CierreDiarioTotales')

# print('Tipo de Comprobante:', tipo_comprobante)
# print('Información del Documento:')
# print('  Primer Comprobante:', informacion_documento.find('PrimerComprobante').text)
# print('  Último Comprobante:', informacion_documento.find('UltimoComprobante').text)
# print('  Cantidad Emitidos:', informacion_documento.find('CantidadEmitidos').text)
# print('  Cantidad Cancelados:', informacion_documento.find('CantidadCancelados').text)
# print('Totales:')
# print('  Total Gravado:', totales.find('TotalGravado').text)
# print('  Total No Gravado:', totales.find('TotalNoGravado').text)
# print('  Total Exento:', totales.find('TotalExento').text)
# print('  Total IVA:', totales.find('TotalIVA').text)


import jinja2
import pdfkit
from xml.dom import minidom
from script.AB import AB
from script.B import B
from script.base import base
import os
from wand.image import Image


# ñ1 = sorted([f for f in os.listdir("./xmls/ñ1") if f.endswith(".xml")])
# ñ2 = sorted([f for f in os.listdir("./xmls/ñ2") if f.endswith(".xml")])


# for k, v in {'ñ1': ñ1, 'ñ2': ñ2}.items():
    # for xml in v:
        # print(xml)
ruta_xml = os.path.join(f"./xmls/ñ2/1600.xml")
xmlDoc = minidom.parse(ruta_xml)
root = xmlDoc.documentElement

etiquetas = root.getElementsByTagName("*")
for etiqueta in etiquetas:
    print(etiqueta.nodeName)


Documento = minidom.parse(ruta_xml).getElementsByTagName('Documento')
print(Documento)
context, numero_z = base(Documento)
# aca si el len es 0 no tiene valores
# len == 3, contiene ticket b
# len == 4, contiene tickets a y b
condicion = Documento.getElementsByTagName('CierreDiarioInformacionDocumento')
totales = Documento.getElementsByTagName('CierreDiarioTotales')
importe_total = totales[0].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()
print(condicion)

if len(condicion) == 4:
    d = AB(Documento)
    html = 'AB.html'
elif len(condicion) == 3 or len(condicion) == 2:
    if importe_total == 0:
        d = {
            'gravado_global': ['',1],
            'no_gravado_global': ['',1],
            'exento_global': ['',1],
            'descuentos_global': ['',1],
            'generado_global': ['',1],
            'cancelados_global': ['',1],
            'total_fiscal': ['',1],
            'total_no_fiscal': ['',1]
        }
        html = 'O.html'
    else:
        d = B(Documento)
        html = 'B.html'
else:
    d = {
        'gravado_global': ['',0.00],
        'no_gravado_global': ['',0.00],
        'exento_global': ['',0.00],
        'descuentos_global': ['',0.00],
        'generado_global': ['',0.00],
        'cancelados_global': ['',0.00],
        'total_fiscal': ['',0.00],
        'total_no_fiscal': ['',3333]
    }
    html = 'O.html'


context.update(d)
print(context)
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./template'))
template = template_env.get_template(html)


config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
# ubicacion = f'./assets/pdfs/{k}/' + f'{numero_z}.pdf'
pdfkit.from_string(template.render(context), 'prueba.pdf', configuration=config)
#esta es toda la linea para convertir pdf en imagen
#primero seleccionamos el pdf, agregamos resolution porque la imagen sino sale comprimida
with Image(filename='prueba.pdf', resolution=300) as img:
    #definimos el formato al que queremos convertir 
    img.format = 'jpeg'
    #guardamos asignamos nombre del archivo, no se porque seguida del formato
    img.save(filename='prueba.jpeg')
