## script convirtiendo a de xml a json 
# SIN TERMINAR
import json
from datetime import datetime


with open('archivo.json', 'r') as archivo:
    datos = json.load(archivo)
    data = datos['Jornada']['Jornada']['Documentos']['Documento'][-1]

inicio = data['Items']['Emisor']['FechaInicioActividades']
fecha = datetime.strptime(inicio, "%Y%m%d")
fecha_formateada = datetime.strftime(datetime.strptime(inicio, "%Y%m%d"), "%d/%m/%Y")


import datetime




for k in data['Items'].keys():
    print(k,  data['Items'][k])
    print('#######################')
jornada = data['Items']['CierreDiarioEncabezado']['FechaJornada']
print('jornada',  datetime.datetime.strptime(jornada, "%y%m%d").strftime("%d/%m/%y"))
print('primer', data['Items']['CierreDiarioInformacionDocumento'][0]['PrimerComprobante'])
print('ultimo', data['Items']['CierreDiarioInformacionDocumento'][0]['UltimoComprobante'])
print('emitido', data['Items']['CierreDiarioInformacionDocumento'][0]['CantidadEmitidos'])
print('cancelado', data['Items']['CierreDiarioInformacionDocumento'][0]['CantidadCancelados'])

print('primer', data['Items']['CierreDiarioInformacionDocumento'][1]['PrimerComprobante'])
print('ultimo', data['Items']['CierreDiarioInformacionDocumento'][1]['UltimoComprobante'])
print('emitido', data['Items']['CierreDiarioInformacionDocumento'][1]['CantidadEmitidos'])
print('cancelado', data['Items']['CierreDiarioInformacionDocumento'][1]['CantidadCancelados'])

print(7, data['Items']['Apertura']['NumeroDocumento'])
# print(8, data['Items']['Apertura']['pos'])
fecha = data['Items']['Apertura']['Fecha']
print(9, datetime.datetime.strptime(fecha, "%y%m%d").strftime("%d/%m/%y"))
print(10, data['Items']['Apertura']['Hora'])

print('1:', data['Items']['Emisor']['RazonSocial'])
print('2:', data['Items']['Emisor']['CUIT'])
print('3:', data['Items']['Emisor']['IngBrutos'])
print(4, data['Items']['LineaUsuario'][0]['Texto']['Texto'])
print(5, data['Items']['LineaUsuario'][1]['Texto']['Texto'])
print('6:', fecha_formateada)
# print('4:', data['Items']['LineaUsuario']['RazonSocial'])
# print('5:', data['Items']['Emisor']['RazonSocial'])
# print('6:', datetime.strptime(data['Items']['Emisor']['FechaInicioActividades'], '%y%m%d').strftime('%d/%m/%Y')
    #   )

# Convierte el objeto datetime en una cadena de texto con el formato deseado

# print('7:', data['Items']['Emisor']['RazonSocial'])



# context.update(d)
# template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./template'))
# template = template_env.get_template(html)


# config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
# # ubicacion = f'./assets/pdfs/{k}/' + f'{numero_z}.pdf'
# pdfkit.from_string(template.render(context), 'prueba.pdf', configuration=config)
# #esta es toda la linea para convertir pdf en imagen
# #primero seleccionamos el pdf, agregamos resolution porque la imagen sino sale comprimida
# with Image(filename='prueba.pdf', resolution=300) as img:
#     #definimos el formato al que queremos convertir 
#     img.format = 'jpeg'
#     #guardamos asignamos nombre del archivo, no se porque seguida del formato
#     img.save(filename='prueba.jpeg')
