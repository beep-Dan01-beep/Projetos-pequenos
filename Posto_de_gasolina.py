#Declaração das variaveis
alcool = float(3.99)
gasolina = float(5.89)
desconto = float (0.0)

#Estrutura de decisão
tipo = str (input("Qual o tipo de gasolina?\n Digite A para Álcool ou G para Gasolina\n"))
litros = float (input("Quantos litros seram usados?\n"))


if (tipo == 'A' and litros <=20):
   
    desconto = 3.0 / 100.0
    valor_total = alcool * litros

    pagar= valor_total - (valor_total * desconto)
    print("Seu total é: ",pagar)

elif (tipo == 'A' and litros > 20):

    desconto = 5.0 / 100.0
    valor_total = alcool * litros

    pagar= valor_total - (valor_total * desconto)
    print("Seu total é: ",pagar)

elif (tipo == 'G' and litros <=20):
   
    desconto = 4.0 / 100.0
    valor_total = gasolina * litros

    pagar= valor_total - (valor_total * desconto)
    print("Seu total é: ",pagar)

elif (tipo == 'G' and litros > 20):

    desconto = 6.0 / 100.0
    valor_total = gasolina * litros

    pagar= valor_total - (valor_total * desconto)
    print("Seu total é: ",pagar)
