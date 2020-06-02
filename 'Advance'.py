def costo(ancho, largo, precio):
    '''
    
    :param ancho: en metros
    :param largo: en metros
    :param precio: el precio que hay que ingresar es por metro cuadrado
    :return: el precio total
    '''
    area = ancho * largo
    total = area * precio
    return f'${total}'



# print(costo(2, 2, 150))


def hipoteca(prestamo, periodo, pago):
    tasa = 0
    if periodo >= 10 and periodo < 20:
        tasa = 0.10
    elif periodo >= 20 and periodo < 30:
        tasa = 0.20
    elif periodo >= 30 and periodo < 40:
        tasa = 0.30
    elif periodo >= 40 and periodo < 50:
        tasa = 0.40
    elif periodo >= 50 and periodo <= 60:
        tasa = 0.50

    a_pagar = prestamo + prestamo * tasa
    if 'men' in pago:
        monto_particionado = a_pagar / (periodo * 12)
    elif 'bim' in pago:
        monto_particionado = a_pagar / (periodo * 6)
    elif 'sem' in pago:
        monto_particionado = a_pagar / (periodo * 52)
    return f'\n${round(monto_particionado, 2)}'




while True:
    prestamo = int(input('\nCuanto dinero quiere pedir prestado?:\n>'))
    periodo = int(input('\nEn cuantos anios quiere pagar el prestamo?:\n>'))
     while periodo < 10 or periodo > 60:
        periodo = int(input('\nPeriodo invalido. Se puede desde un minimo de 10 anios hasta un maximo de 60.\n>'))


    pago = input('\nElija cada cuanto desea pagar: bimestral, mensual, semanal:\n>').lower()
    while 'bimestral' not in pago and 'mensual' not in pago and 'semanal' not in pago:
        pago = input('Periodo invalido. Los pagos pueden ser bimestrales, mensuales o semanales. Ingrese nuevamente:\n>')

    print(hipoteca(prestamo, periodo, pago))
    respuesta = input('\nDesea calcular otra hipoteca?:\n>').lower()
    while respuesta != 'si' and respuesta != 'no':
        respuesta = input('\nRespuesta invalida, ingrese si o no:\n>')
    if respuesta == 'no':
        break




