import jinja2
import pdfkit
from xml.dom import minidom
from script.AB import AB
from script.B import B
from script.base import base
import os
from wand.image import Image


ñ1 = sorted([f for f in os.listdir("./xmls/ñ1") if f.endswith(".xml")])
ñ2 = sorted([f for f in os.listdir("./xmls/ñ2") if f.endswith(".xml")])


for k, v in {'ñ1': ñ1, 'ñ2': ñ2}.items():
    for xml in v:
        # print(xml)
        ruta_xml = os.path.join(f"./xmls/{k}", xml)
        Documento = minidom.parse(ruta_xml).getElementsByTagName('Documento')[-1]
        # print(Documento)
        context, numero_z = base(Documento)
        # aca si el len es 0 no tiene valores
        # len == 3, contiene ticket b
        # len == 4, contiene tickets a y b
        condicion = Documento.getElementsByTagName('CierreDiarioInformacionDocumento')
        totales = Documento.getElementsByTagName('CierreDiarioTotales')
        importe_total = totales[0].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()
        if len(condicion) == 4:
            d = AB(Documento)
            html = 'AB.html'
        elif len(condicion) == 3 or len(condicion) == 2:
            if  importe_total == 0:
                d = {
                'gravado_global': 0.00,
                'no_gravado_global': 0.00,
                'exento_global': 0.00,
                'descuentos_global': 0.00,
                'generado_global': 0.00,
                'cancelados_global': 0.00,
                'total_fiscal': 0.00,
                'total_no_fiscal': 0.00
                }
                html = 'O.html'
            else:
                d = B(Documento)
                html = 'B.html'
        else:
            d = {
                'gravado_global': 0.00,
                'no_gravado_global': 0.00,
                'exento_global': 0.00,
                'descuentos_global': 0.00,
                'generado_global': 0.00,
                'cancelados_global': 0.00,
                'total_fiscal': 0.00,
                'total_no_fiscal': 0.00
            }
            html = 'O.html'


        context.update(d)
        template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./template'))
        template = template_env.get_template(html)


        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        ubicacion = f'./assets/pdfs/{k}/' + f'{numero_z}.pdf'
        pdfkit.from_string(template.render(context), ubicacion, configuration=config)
        #esta es toda la linea para convertir pdf en imagen
        #primero seleccionamos el pdf, agregamos resolution porque la imagen sino sale comprimida
        with Image(filename=ubicacion, resolution=300) as img:
            #definimos el formato al que queremos convertir 
            img.format = 'jpeg'
            #guardamos asignamos nombre del archivo, no se porque seguida del formato
            img.save(filename=f'./assets/imgs/{k}/{numero_z}.jpeg')
