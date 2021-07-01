def valor_deuda( contrato: str,valor1: float, valor2: float, valor3: float,valor4: float, valor5: float,valor6: float,tasa_cambio: float)->str:
    val1 = valor1*0.05 + valor1
    val2 = valor2*0.05 + valor2
    val3 = valor3*0.05 + valor3
    val4 = valor4*0.05 + valor4
    val5 = valor5*0.05 + valor5
    val6 = valor6*0.05 + valor6

    valor_pesos = (val1 + val2 + val3 + val4 + val5 + val6)

    valor_dolar = valor_pesos / tasa_cambio
    valor_pesos = round(valor_pesos,2)
    valor_dolar = round(valor_dolar,2)
    return "El contrato {} adeuda un valor de: ${} COP y un valor ${} USD".format(contrato,valor_pesos,valor_dolar)

a = valor_deuda("B102548L",125000,125000,125000,125000,125000,125000,3600.52)
print(a)







