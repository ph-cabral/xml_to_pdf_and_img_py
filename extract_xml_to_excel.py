import jinja2
import pdfkit
from xml.dom import minidom
from script.AB import AB
from script.B import B
from script.base import base
import os
from wand.image import Image
import openpyxl

# armo una lista con los xmls que estan dentro de las carpetas
ñ1 = sorted([f for f in os.listdir("./xmls/ñ1") if f.endswith(".xml")])
ñ2 = sorted([f for f in os.listdir("./xmls/ñ2") if f.endswith(".xml")])

# Crear un nuevo libro de Excel
workbook = openpyxl.Workbook()

# Seleccionar la hoja activa
sheet = workbook.active

# Escribir los encabezados en la pimera fila
header = ['FECHA', 'TIPO', 'B', 'DESDE', 'HASTA', 'A', 'DESDE', 'HASTA', 'PV', 'NUMERO', 
          'DENOMINACION', 'NG TOTAL', 'IVA TOTAL', 'NG 10.5%', 'IVA 10.5%',
          'NG 21%', 'IVA 21%', 'NG 21%', 'IVA 21%', 'TOTAL']
for i, head in enumerate(header):
    sheet.cell(row=1, column=i+1, value=head)

# recorro la lista 
for k, v in {'ñ1': ñ1, 'ñ2' : ñ2}.items():
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
        
        cierre_b =  context.get('cierre_b', '')
        primer_b =  context.get('primer_b' , '')
        ultimo_b =  context.get('ultimo_b', '')

        disciminacion_iva_b1 =  context.get('disciminacion_iva_b1', '')
        disciminacion_iva_b2 =  context.get('disciminacion_iva_b2', '')
        total_iva_b = context.get('total_iva_b', '')
        importe_total_b = context.get('importe_total_b', '')
        
        # A
        cierre_a =  context.get('cierre_a','')
        primer_a =  context.get('primer_a','')
        ultimo_a =  context.get('ultimo_a','')

        disciminacion_iva_a1 = context.get('disciminacion_iva_a1', '')
        disciminacion_iva_a2 = context.get('disciminacion_iva_a2', '')
        total_iva_a = context.get('total_iva_a', '')
        importe_total_a = context.get('importe_total_a', '')
        
        # global
        disciminacion_iva_global1 = context.get('disciminacion_iva_global1', '')
        disciminacion_iva_global2 = context.get('disciminacion_iva_global2', '')
        total_iva_global = context.get('total_iva_global', '')
        # detalle
        primer_detalle = context.get('primer_detalle', '')
        ultimo_detalle = context.get('ultimo_detalle', '')
        generado_detalle = context.get('generado_detalle', '')
            
        print(context['numero_z'])
        # Write the data to the Excel sheet
        row = [context['fecha_jornada'], 
               'cierre z',  cierre_b, primer_b, ultimo_b,
               cierre_a, primer_a, ultimo_a,
               context['pv'], 
               context['numero_z'], 
               'CONSUMIDOR FINAL',
               
        # disciminacion_iva_b1,
        # disciminacion_iva_b2,
        # total_iva_b,
        # importe_total_b,
        # # A
       
        # disciminacion_iva_a1,
        # disciminacion_iva_a2,
        # total_iva_a,
        # importe_total_a,
        
        # disciminacion_iva_global1,
        # disciminacion_iva_global2,
        # total_iva_global,
        # # detalle
        # primer_detalle,
        # ultimo_detalle,
        # generado_detalle,
] 

        sheet.append(row)

# # Save the Excel file
    workbook.save(f'{k}.xlsx')