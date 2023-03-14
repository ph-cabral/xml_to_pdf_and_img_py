from datetime import datetime

def base(Documento):
    LineaUsuario = Documento.getElementsByTagName('LineaUsuario')

    texto = LineaUsuario[2].getElementsByTagName('Texto')
    nombre = texto[1].firstChild.data.strip()

    texto = LineaUsuario[0].getElementsByTagName('Texto')
    direccion = texto[1].firstChild.data.strip()

    texto = LineaUsuario[1].getElementsByTagName('Texto')
    lugar = texto[1].firstChild.data.strip()


    ing_brutos = Documento.getElementsByTagName('IngBrutos')[0].firstChild.data.strip()
    cuit = Documento.getElementsByTagName('CUIT')[0].firstChild.data.strip()
    razon_social = Documento.getElementsByTagName('RazonSocial')[0].firstChild.data.strip()
    inicio = Documento.getElementsByTagName('FechaInicioActividades')[0].firstChild.data.strip()
    numero_z = Documento.getElementsByTagName('NumeroCompleto')[0].firstChild.data.strip()
    fecha_cierre = Documento.getElementsByTagName('FechaCierre')[0].firstChild.data.strip()
    fecha_cierre = datetime.strptime(fecha_cierre, '%y%m%d').strftime('%d/%m/%Y')
    hora_cierre = Documento.getElementsByTagName('HoraCierre')[0].firstChild.data.strip()
    hora_cierre = datetime.strptime(hora_cierre, '%H%M%S').strftime('%H:%M:%S')
    pv = Documento.getElementsByTagName('POS')[0].firstChild.data.strip()
    fecha_jornada = Documento.getElementsByTagName('FechaJornada')[0].firstChild.data.strip()
    fecha_jornada = datetime.strptime(fecha_jornada, '%y%m%d').strftime('%d/%m/%Y')
    
    context = {
        'nombre': nombre,
        'razon_social':razon_social ,
        'cuit':cuit ,
        'ing_brutos': ing_brutos ,
        'direccion': direccion,
        'lugar': lugar,
        'inicio':inicio,
        #
        'numero_z': numero_z,
        'pv':pv ,
        'fecha_cierre':fecha_cierre,
        'hora_cierre':hora_cierre,
        #
        'fecha_jornada':fecha_jornada,
        'tipo': 'viendo',
        }
    return context, numero_z