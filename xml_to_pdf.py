import jinja2
import pdfkit
from xml.dom import minidom
from script.AB import AB
from script.B import B
from script.base import base
import os
from tqdm import tqdm

# armo una lista con los xmls que estan dentro de las carpetas
ñ1 = sorted([f for f in os.listdir("./xmls/ñ1") if f.endswith(".xml")])
ñ2 = sorted([f for f in os.listdir("./xmls/ñ2") if f.endswith(".xml")])

# recorro la lista 
for k, v in {'ñ1': ñ1, 'ñ2': ñ2}.items():
    for xml in v:
        # selecciono el xml
        ruta_xml = os.path.join(f"./xmls/{k}", xml)
        # extraigo la utlima etiqueta "Documento"
        Documento = minidom.parse(ruta_xml).getElementsByTagName('Documento')[-1]
        context, numero_z = base(Documento)

        condicion = Documento.getElementsByTagName('CierreDiarioInformacionDocumento')
        totales = Documento.getElementsByTagName('CierreDiarioTotales')
        importe_total = totales[0].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()

        if len(condicion) == 4:
            d = AB(Documento)
            html = 'AB.html'
        elif len(condicion) == 3 or len(condicion) == 2:
            if importe_total == 0:
                d = {
                    'gravado_global': ['',0.00],
                    'no_gravado_global': ['',0.00],
                    'exento_global': ['',0.00],
                    'descuentos_global': ['',0.00],
                    'generado_global': ['',0.00],
                    'cancelados_global': ['',0.00],
                    'total_fiscal': ['',0.00],
                    'total_no_fiscal': ['',0.00]
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
                'total_no_fiscal': ['',0.00]
            }
            html = 'O.html'
        context.update(d)
        
        template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./template'))
        template = template_env.get_template(html)


        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        ubicacion = f'./assets/pdfs/{k}/' + f'{numero_z}.pdf'
        pdfkit.from_string(template.render(context), ubicacion, configuration=config)
