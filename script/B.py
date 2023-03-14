def B(Documento):
    tipos = [0, 1, 2]
    # 0 = b, 1 = a, 2 = 0
    cierres = Documento.getElementsByTagName('CierreDiarioContextoTipoComprobante')
    cierre_b = cierres[0].getElementsByTagName('CalificadorComprobante')[0].firstChild.data.strip()


    comprobantes = Documento.getElementsByTagName('CierreDiarioInformacionDocumento')
    primer_b = comprobantes[0].getElementsByTagName('PrimerComprobante')[0].firstChild.data.strip()
    try:
        primer_detalle = comprobantes[2].getElementsByTagName('PrimerComprobante')[0].firstChild.data.strip()
    except IndexError:
        primer_detalle = 0.00


    ultimo_b = comprobantes[0].getElementsByTagName('UltimoComprobante')[0].firstChild.data.strip()
    try:
        ultimo_detalle = comprobantes[2].getElementsByTagName('UltimoComprobante')[0].firstChild.data.strip()
    except IndexError:
        ultimo_detalle = 0.00
    


    generado_b = comprobantes[0].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()
    generado_global = comprobantes[1].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()
    try:
        generado_detalle = comprobantes[2].getElementsByTagName('CantidadEmitidos')[0].firstChild.data.strip()
    except IndexError:
        generado_detalle = 0.00


    cancelados_b = comprobantes[0].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()
    cancelados_global = comprobantes[1].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()
    try:
        cancelados_detalle = comprobantes[2].getElementsByTagName('CantidadCancelados')[0].firstChild.data.strip()
    except IndexError:
        cancelados_detalle = 0.00


    # 0=b, 1=a, 2=info global, 3,4=?,
    totales = Documento.getElementsByTagName('CierreDiarioTotales')
    gravado_b = totales[0].getElementsByTagName('TotalGravado')[0].firstChild.data.strip()
    gravado_global = totales[1].getElementsByTagName('TotalGravado')[0].firstChild.data.strip()


    no_gravado_b = totales[0].getElementsByTagName('TotalNoGravado')[0].firstChild.data.strip()
    no_gravado_global = totales[1].getElementsByTagName('TotalNoGravado')[0].firstChild.data.strip()


    ######### ver, los tickes que vi dicen importe gfinal de comprobantes no fiscales 0, cuando haya
    ######### 1 que no sea 0 hay que ver cual de los siguientes es 
    exento_b = totales[0].getElementsByTagName('TotalExento')[0].firstChild.data.strip()
    exento_global = totales[0].getElementsByTagName('TotalExento')[0].firstChild.data.strip()


    ######### ver, los tickes que vi dicen importe gfinal de comprobantes no fiscales 0, cuando haya
    ######### 1 que no sea 0 hay que ver cual de los siguientes es 
    descuentos_b = totales[0].getElementsByTagName('TotalBonificaciones')[0].firstChild.data.strip()
    descuentos_global = totales[1].getElementsByTagName('TotalBonificaciones')[0].firstChild.data.strip()


    total_iva_b = totales[0].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    total_iva_global = totales[1].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()


    importe_total_b = totales[0].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()
    # importe_total_ = totales[2].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()


    ######### ver, los tickes que vi dicen importe gfinal de comprobantes no fiscales 0, cuando haya
    ######### 1 que no sea 0 hay que ver cual de los siguientes es 
    # importe_total = totales[3].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()
    # importe_total = totales[4].getElementsByTagName('TotalFinal')[0].firstChild.data.strip()


    # B  0=21 ,1=10 
    # A 2=10 ,3=21 
    # global 4=10, 5=21
    totalivas = []
    cierres_iva = Documento.getElementsByTagName('CierreDiarioIVA')
    for cierre in cierres_iva:        
        tasa_iva = float(cierre.getElementsByTagName('TasaIVA')[0].childNodes[0].nodeValue)
        total_iva = float(cierre.getElementsByTagName('TotalIVA')[0].childNodes[0].nodeValue)
        if tasa_iva == 10.5 or tasa_iva == 21:
            totalivas.append([f'{tasa_iva}%', total_iva])
        else:
            totalivas.append([f'{tasa_iva}%', 0])
                    


    if len(totalivas) == 2:
        disciminacion_iva_b1 = [totalivas[0][0], totalivas[0][1]]
        disciminacion_iva_b2 = ['','']
        disciminacion_iva_global1 = [totalivas[1][0], totalivas[1][1]]
        disciminacion_iva_global2 = ['','']
            
    else:
        try:
            disciminacion_iva_b1 = [totalivas[0][0], totalivas[0][1]]
        except IndexError:
            disciminacion_iva_b1 = 0.00
        try:
            disciminacion_iva_b2 = [totalivas[1][0], totalivas[1][1]]
        except IndexError:
            disciminacion_iva_b2 = 0.00
        try:
            disciminacion_iva_global1 = [totalivas[2][0], totalivas[2][1]]
        except IndexError:
            disciminacion_iva_global1 = 0.00
        try:
            disciminacion_iva_global2 = [totalivas[3][0], totalivas[3][1]]
        except IndexError:
            disciminacion_iva_global2 = 0.00
         
    # try:
    #     # tasa_iva_b1 = iva[0].getElementsByTagName('TasaIVA')[0].firstChild.data.strip()
    #     disciminacion_iva_b1 = iva[0].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    # except IndexError:
    #     # tasa_iva_b1 = 0.00
    #     disciminacion_iva_b1 = 0.00
    # try:
    #     # tasa_iva_b2 = iva[1].getElementsByTagName('TasaIVA')[0].firstChild.data.strip()
    #     # if disciminacion_iva_b1 == iva[1].getElementsByTagName('TotalIVA')[0].firstChild.data.strip():
    #         # print('es el mismo')
    #     disciminacion_iva_b2 = iva[1].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    # except IndexError:
    #     # tasa_iva_b2 = 0.00
    #     disciminacion_iva_b2 = 0.00
    # try:
    #     # tasa_iva_global1 = iva[4].getElementsByTagName('TasaIVA')[0].firstChild.data.strip()
    #     disciminacion_iva_global1 = iva[2].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    # except IndexError:
    #     # tasa_iva_global1 = 0.00
    #     disciminacion_iva_global1 = 0.00
    # try:
    #     # tasa_iva_global2 = iva[5].getElementsByTagName('TasaIVA')[0].firstChild.data.strip()
    #     disciminacion_iva_global2 = iva[3].getElementsByTagName('TotalIVA')[0].firstChild.data.strip()
    # except IndexError:
    #     # tasa_iva_global2 = 0.00
    #     disciminacion_iva_global2 = 0.00
    
    
    B = {
        # B
        'cierre_b': cierre_b,
        'primer_b': primer_b,
        'ultimo_b': ultimo_b,
        'gravado_b': gravado_b,
        'no_gravado_b': no_gravado_b,
        'exento_b': exento_b,
        'descuentos_b': descuentos_b,
        'generado_b': generado_b,
        'cancelados_b': cancelados_b,
        'disciminacion_iva_b1': disciminacion_iva_b1,
        'disciminacion_iva_b2': disciminacion_iva_b2,
        'total_iva_b':total_iva_b,
        'importe_total_b':importe_total_b,
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
        'ultimo_detalle': ultimo_detalle,
        'generado_detalle': generado_detalle,
    }

    return B