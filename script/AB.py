def AB(Documento):
    tipos = [0, 1, 2]
    # 0 = b, 1 = a, 2 = 0
    cierres = Documento.getElementsByTagName('CierreDiarioContextoTipoComprobante')
    cierre_b = cierres[0].getElementsByTagName('CalificadorComprobante')[0].firstChild.data.strip()
    cierre_a = cierres[1].getElementsByTagName('CalificadorComprobante')[0].firstChild.data.strip()


    comprobantes = Documento.getElementsByTagName('CierreDiarioInformacionDocumento')
    primer_b = comprobantes[0].getElementsByTagName('PrimerComprobante')[0].firstChild.data.strip()
    primer_a = comprobantes[1].getElementsByTagName('PrimerComprobante')[0].firstChild.data.strip()
    primer_detalle = comprobantes[3].getElementsByTagName('PrimerComprobante')[0].firstChild.data.strip()


    ultimo_b = comprobantes[0].getElementsByTagName('UltimoComprobante')[0].firstChild.data.strip()
    ultimo_a = comprobantes[1].getElementsByTagName('UltimoComprobante')[0].firstChild.data.strip()
    ultimo_detalle = comprobantes[3].getElementsByTagName('UltimoComprobante')[0].firstChild.data.strip()


    generado_b = comprobantes[0].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()
    generado_a = comprobantes[1].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()
    generado_global = comprobantes[2].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()
    generado_detalle = comprobantes[3].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()


    cancelados_b = comprobantes[0].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()
    cancelados_a = comprobantes[1].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()
    cancelados_global = comprobantes[2].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()
    cancelados_detalle = comprobantes[3].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()


    # 0=b, 1=a, 2=info global, 3,4=?,
    totales = Documento.getElementsByTagName('CierreDiarioTotales')
    gravado_b = totales[0].getElementsByTagName('TotalGravado')[0].firstChild.data.strip()
    gravado_a = totales[1].getElementsByTagName('TotalGravado')[0].firstChild.data.strip()
    gravado_global = totales[2].getElementsByTagName('TotalGravado')[0].firstChild.data.strip()


    no_gravado_b = totales[0].getElementsByTagName('TotalNoGravado')[0].firstChild.data.strip()
    no_gravado_a = totales[1].getElementsByTagName('TotalNoGravado')[0].firstChild.data.strip()
    no_gravado_global = totales[2].getElementsByTagName('TotalNoGravado')[0].firstChild.data.strip()


    ######### ver, los tickes que vi dicen importe gfinal de comprobantes no fiscales 0, cuando haya
    ######### 1 que no sea 0 hay que ver cual de los siguientes es 
    exento_b = totales[0].getElementsByTagName('TotalExento')[0].firstChild.data.strip()
    exento_a = totales[0].getElementsByTagName('TotalExento')[0].firstChild.data.strip()
    exento_global = totales[0].getElementsByTagName('TotalExento')[0].firstChild.data.strip()


    ######### ver, los tickes que vi dicen importe gfinal de comprobantes no fiscales 0, cuando haya
    ######### 1 que no sea 0 hay que ver cual de los siguientes es 
    descuentos_b = totales[0].getElementsByTagName('TotalBonificaciones')[0].firstChild.data.strip()
    descuentos_a = totales[1].getElementsByTagName('TotalBonificaciones')[0].firstChild.data.strip()
    descuentos_global = totales[2].getElementsByTagName('TotalBonificaciones')[0].firstChild.data.strip()


    total_iva_b = totales[0].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    total_iva_a = totales[1].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    total_iva_global = totales[2].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()


    importe_total_b = totales[0].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()
    importe_total_a = totales[1].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()
    
    # # Obtener todas las etiquetas de <CierreDiarioContextoTipoComprobante>
    comprobante = Documento.getElementsByTagName("CierreDiarioContextoTipoComprobante")

    # # Crear diccionario para agrupar los resultados
    # resultados = {}

    # Iterar sobre las etiquetas de <CierreDiarioContextoTipoComprobante>
    # for comprobante in tipo_comprobante:
        # Obtener el valor de la etiqueta <CalificadorComprobante>
    calificador = comprobante[1].getElementsByTagName("CalificadorComprobante")[0].childNodes[0].nodeValue
    iva = [elem for elem in comprobante[0].parentNode.childNodes if elem.nodeName == "CierreDiarioIVA"]
    tipos = ('B', 'A', 'SinCalificador')
    tasas_iva = [elem.getElementsByTagName("TasaIVA")[0].childNodes[0].nodeValue for elem in iva]
    totales_iva = [elem.getElementsByTagName("TotalIVA")[0].childNodes[0].nodeValue for elem in iva]
    diccionario = {}
    
    # Crear un diccionario para almacenar las tasas y totales de IVA por tipo de comprobante
    diccionario = {}

    i = 0
    for clave in tipos:
        diccionario[clave] = []
    for num1, num2 in zip(tasas_iva, totales_iva):
        if len(diccionario[tipos[i]]) == 0:
            diccionario[tipos[i]].append(num1)
            diccionario[tipos[i]].append(num2)
        elif num1 in diccionario[tipos[i]]:
            diccionario[tipos[i+1]].append(num1)
            diccionario[tipos[i +1]].append(num2)
            i+=1
        else:
            diccionario[tipos[i]].append(num1)
            diccionario[tipos[i]].append(num2)
    

    try:
        disciminacion_iva_b1 = diccionario['B'][1]
    except IndexError:
        disciminacion_iva_b1 = 0.00
    try:
        disciminacion_iva_b2 = diccionario['B'][3]
    except IndexError:
        disciminacion_iva_b2 = 0.00
        
    try:
       disciminacion_iva_a1 = diccionario['A'][1]
    except IndexError:
        disciminacion_iva_a1 = 0.00
    try:
        disciminacion_iva_a2 = diccionario['A'][3]
    except IndexError:
        disciminacion_iva_a2 = 0.00
        
    try:
        disciminacion_iva_global1 = diccionario['SinCalificador'][1]
    except IndexError:
        disciminacion_iva_global1 = 0.00
    try:
        disciminacion_iva_global2 = diccionario['SinCalificador'][3]
    except IndexError:
        disciminacion_iva_global2 = 0.00
    
    
    AB = {
        # B
        'cierre_b': cierre_b,
        'primer_b': primer_b,
        'ultimo_b': ultimo_b,
        'gravado_b': gravado_b,
        'no_gravado_b': no_gravado_b,
        'exento_b': exento_b,
        'descuentos_b': descuentos_b,'generado_b': generado_b,'cancelados_b': cancelados_b,
        'disciminacion_iva_b1': disciminacion_iva_b1,
        'disciminacion_iva_b2': disciminacion_iva_b2,
        'total_iva_b':total_iva_b,
        'importe_total_b':importe_total_b,
        # A
        'cierre_a': cierre_a,
        'primer_a': primer_a,
        'ultimo_a': ultimo_a,
        'gravado_a': gravado_a,
        'no_gravado_a': no_gravado_a,
        'exento_a': exento_a,
        'descuentos_a': descuentos_a,
        'generado_a': generado_a,
        'cancelados_a': cancelados_a,
        'disciminacion_iva_a1': disciminacion_iva_a1,
        'disciminacion_iva_a2': disciminacion_iva_a2,
        'total_iva_a':total_iva_a,
        'importe_total_a':importe_total_a,
        # global
        'gravado_global': gravado_global,
        'no_gravado_global': no_gravado_global,
        'exento_global': exento_global,
        'descuentos_global': descuentos_global,
        'generado_global': generado_global,
        'cancelados_global': cancelados_global,
        'disciminacion_iva_global1': disciminacion_iva_global1,
        'disciminacion_iva_global2': disciminacion_iva_global2,
        'total_iva_global': total_iva_global,
        # detalle
        'primer_detalle': primer_detalle,
        'ultimo_detalle': ultimo_detalle,'generado_detalle': generado_detalle,
}

    return AB