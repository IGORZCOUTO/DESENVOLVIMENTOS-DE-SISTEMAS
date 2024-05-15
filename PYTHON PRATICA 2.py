PYTHON PRATICA 2

1º
num_inteiro=int(input("insira um numero:"))
num2_inteiro=int(input("insira outro numero:"))

if(num_inteiro > num2_inteiro):
    print("o maior numero é:", num_inteiro)
else:
    print("o menor numero é", num2_inteiro)
                 

----------------------------------------------------------------------------

2º
num_inteiro=int(input("insira um numero:"))
num2_inteiro=int(input("insira outro numero:"))
 
if(num_inteiro < num2_inteiro):
    print("o menor numero é:", num_inteiro)
else:
    print("o maior numero é:", num2_inteiro)

----------------------------------------------------------------------------

3º
num_inteiro=int(input("insira um numero:"))
num2_inteiro=int(input("insira outro numero:"))
 
if(num_inteiro < num2_inteiro):
    print("o menor numero é:", num_inteiro)
elif(num2_inteiro < num_inteiro):
    print("o menor numero é:", num2_inteiro)
else: 
    print("ambos numeros são iguais",num_inteiro, num2_inteiro)

----------------------------------------------------------------------------

4º
fun1_nome=input("primeiro funcionario insira seu nome:")
fun2_nome=input("segundo funcionario insira seu nome:")
fun1_salario_inteiro=int(input("primeiro funcionario insira seu salario:"))
fun2_salario_inteiro=int(input("segundo funcionario insira seu salario:"))

if(fun1_salario_inteiro > fun2_salario_inteiro):
    print(fun1_nome,"você ganha mais que o(a)",fun2_nome,"e ganha",(fun1_salario_inteiro - fun2_salario_inteiro),"a mais")
else:
    print("você",fun2_nome,"você ganha mais que o(a)",fun1_nome,"e ganha",(fun1_salario_inteiro - fun2_salario_inteiro),"a mais")

----------------------------------------------------------------------------

5º
peso_inteiro=float(input("insira seu peso:"))
altura_inteiro=float(input("insira sua altura:"))
imc=(peso_inteiro / (altura_inteiro * altura_inteiro))

if(imc <18.5):
    print("você esta abaixo do peso")
elif(imc > 18.5 and imc < 24.9):
    print("você está com peso ideal")
else:
    print("você está acima do peso")

----------------------------------------------------------------------------

6º
idade_inteiro=int(input("insira sua idade:"))
genero=input("insira seu genero:")

if(idade_inteiro >=18 and genero=="feminino" ):
    print("você e maior de idade e é do genero feminino")
elif(idade_inteiro >=18 and genero=="masculino"):
    print("você e maior de idade e não é do genero feminino")
elif(idade_inteiro <=18 and genero=="feminino"):
    print("você e menor de idade e é do genero feminino")
else:
    print("você e menor de idade e não é do genero feminino" )

----------------------------------------------------------------------------

7º
num1=int(input("insira seu primeiro numero:"))
num2=int(input("insira seu segundo numero:"))
num3=int(input("insira seu terceiro numero:"))

if(num1 > num2 and num2 > num3):
    print("os numeros organizados do maior para o menor", num1, num2, num3)

elif(num1 > num2 and num2 < num3):
    print("os numeros organizados do maior para o menor", num1, num3, num2)

elif(num2 > num1 and num1 > num3 ):
    print("os numeros organizados do maior para menor", num2, num1, num3)

elif(num2 > num1 and num1 < num3 ):
    print("os numeros organizados do maior para menor", num2, num3, num1)

elif(num3 > num2 and num2 > num1 ):
    print("os numeros organizados do maior para menor", num3, num2, num1)

else:
    print("os numeros organizados do maior para menor", num3, num1, num2)



----------------------------------------------------------------------------

8º
num1=int(input("insira seu numero:"))
num2=int(input("insira seu numero:"))
resultado=(num1 + num2)

if(resultado %2 ==0 and resultado > 0):
    print("seu número é par positivo")
elif(not(resultado %2 ==0) and resultado > 0):
    print("seu número é impar positivo")
elif(resultado  %2 ==0 and resultado < 0):
    print("seu numero é par negativo")
else:
    print("seu numero é impar negativo")

----------------------------------------------------------------------------

9º
num1=int(input("insira seu numero:"))
num2=int(input("insira seu numero:"))
resultado=(num1 + num2)

if(resultado >=25 and resultado <=33 ):
    print("È isso aí")
elif(resultado ==40):
    print("È isso aí")
else:
    print("Não é isso aí")


----------------------------------------------------------------------------

10º
idade=int(input("insira sua idade:"))

if(idade <18):
    print("você não pode entrar no bar do brasil e nem do estados unidos")
elif(idade >=18 and idade <21):
    print("você pode entrar so no bar do brasil mas não do estados unidos")
else: 
    print("você pode entrar no bar dos estados unidos e do brasil")


----------------------------------------------------------------------------

11º
idade=int(input("insira sua idade:"))
altura=float(input("insira sua altura:"))

if(altura >=1.60 and idade >=16):
    print("entrada permitida")
    
elif(altura <=1.50 and idade >=16):
    var=input("VOCÊ ESTÁ ACONPANHADO S para sim\nN para não\n\n RESPOSTA:").upper()
    if(var=="S"):
        print("Sua entrada é permitida")
    elif(var=="N"):
        print("Sua entrada não é permitida.")
    
elif(altura <1.50 and idade <18):
    print("mesmo assim você tera que assinar um termo para ir nos brinquedos")
    
else:
    print("entrada não permitida")
    

