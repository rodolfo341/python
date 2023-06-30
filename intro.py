
print("Calculadora")

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))
operador = input("ingrese operador ( +, -, *, / )")
resultado = 0
Flag = True
if operador=="+":
    resultado=num1+num2
elif operador=="-":
    resultado=num1-num2
elif operador=="*":
    resultado=num1*num2
elif operador=="/":
    resultado=num1/num2
else:
    flag=False
if flag:
    print(num1 , operador, num2, " = ", resultado)
else:
    print("opcion errada")
    
    