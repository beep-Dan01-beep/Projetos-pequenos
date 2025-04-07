#Declação de vareáveis#
eleitores = 0
Vnulo = 0
Vbranco = 0
Vvalidos = 0

#Inserção de dados#
eleitores = int (input("Qual a quantidade de eleitores?\n"))
Vnulo = int (input("Qual a quantidade de votos nulos?\n"))
Vbranco = int (input("Qual a quantidade de votos em branco?\n"))
Vvalidos = int (input("Qual a quantidade de votos validos?\n"))


#Calculo de porcentagem#
Porcen_nulo = 100 * (Vnulo/eleitores)
Porcen_branco = 100 * (Vbranco/eleitores)
Porcen_validos = 100 * (Vvalidos/eleitores)

print("A porcentagem de votos em branco é: %",Porcen_branco,"\n","A porcentagem de votos nulos é: %",Porcen_nulo,"\n","A porcentagem de votos validos é: %", Porcen_validos)
