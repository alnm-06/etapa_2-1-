capital = float(input("Informe, em reais, seu capital: "))
juros = float(input("Informe, em porcentagem, os juros: "))
tempo = float(input("Informe, em meses, a duração da aplicação: "))
montante = 0
juros=juros/100
contador = 0
while contador < tempo:
    contador+=1
    montante = capital * ((1+juros)**contador)
    print(f"Mês {contador}, montante = R${montante:.2f}")
