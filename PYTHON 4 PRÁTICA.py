1º

variavel = 10 

while variavel >= 1:

    print(variavel)

    variavel -= 1



-----------------------------------------------------------------------------



2º

num1=int(input("insira um número para iniciar:"))

num2=int(input("insira um número para finalizar:"))



for num1 in range(num1, num2+1):

    print(num1)

    num1+=1





-----------------------------------------------------------------------------



3º

num=int(input("insira seu numero: "))



for i in range(11):

    print(num,"X",i,"=",num*i)

    



-----------------------------------------------------------------------------



4º

num1=int(input("Insira um número:"))

num2=int(input("Insira outro número:"))



par=0

impar=0



for num1 in range(num2):

    if(num1%2==0):

        par+=1

    else:

        impar+=1

print("numeros par:",par)

print("numeros impares:",impar)



-----------------------------------------------------------------------------



5º

num=int(input("insira seu numero:"))

soma=0



for num in range(num+1):

    soma+=num

    num-=1

    

print(soma)



-----------------------------------------------------------------------------



