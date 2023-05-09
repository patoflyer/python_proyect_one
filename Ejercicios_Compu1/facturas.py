def facturas():
    fact = {}
    num = ''
    paid = 0
    miss = 0
    while num != '3':
        if num == '1':
            code = input('Número de la factura: ')
            cost = float(input('Costo de la factura: '))
            fact[code] = cost
            miss += cost
        if num == '2':
            code = input('Número de la factura a pagar: ')
            cost = fact.pop(code, 0)
            paid += cost
            miss -= cost
        print('Se ha pagado:', paid)
        print('Falta por cobrar: ', miss)
        num = input('Oprime (1) para una nueva factura, (2) para pagarla o (3) para salir: ')
facturas()
