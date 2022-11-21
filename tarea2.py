# EJERCISIO 1 :menor que
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese un numero: "))
if numero1 < numero2:
    print(f"numero menor {numero1}")
else:
    print(f"numero menor  {numero2}");

# EJERCISIO 2 : mayor que
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese un numero: "))
numero3=int(input("ingrese un numero "))
numero4=int(input("ingrese un numero"))
if numero1 >=numero2 and numero1 >=numero3 and numero1 >=numero4:
    print(f"numero mayor {numero1}")
elif numero2 >=numero1 and numero2 >=numero3 and numero2 >=numero4:
    print(f"numero mayor {numero2}")
elif numero3 >=numero1 and numero3 >=numero2 and numero3 >=numero4:
    print(f"numero mayor {numero3}")
elif numero1 == numero2 and numero1 ==numero3 and numero1 == numero4:
    print("error")
elif numero2 == numero3 and numero2 ==numero4:
    print("error")
elif numero3 == numero4:
    print("error")
else:
    print(f"numero menor  {numero4}");

#EJERCISIO 3 : max numero
num1=int(input("ingrese un numero"))
num2=int(input("ingrese un numero"))
num3=int(input("ingrese un numero"))
if num1 > num2 and num2 < num3 and num1 > num3:
    print(f"numero mayor {numero1}")
elif num2 > num1 and num1 < num3 and num2 > num3:
    print(f"numero mayor {numero2}")
elif num3 > num1 and num2 < num1 and num3 > num1:
     print(f"numero mayor {numero3}")
if num1 == num2 or num2 == num3:
    print("son numeros iguales")
else:
    print("no son numeros iguales")

#Ejercisio 4 min numero
num1=int(input("ingrese un numero"))
num2=int(input("ingrese un numero"))
num3=int(input("ingrese un numero"))
if num1 < num2 and num2 > num3 and num3 > num1:
    print(f"numero menor {numero1}")
else:
    print(f"numero menor {numero2}")
    
if num1 == num2 or num2 == num3:
    print("son numeros iguales")
else:
    print("no son numeros iguales")
#ejercisio 5 true
print("dime una vocal")
vocal=input()
if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal =='o' or vocal == 'u' :
    print("TRUE") 
elif vocal == 'A' or vocal == 'E' or vocal == 'I' or vocal =='O' or vocal == 'U':
    print("False")
#ejercisio 6 simple
nombre = input("ingrese su nombre")
apellido = input("por favor ingrese su edad")
print("que tengas un excelente dia " (nombre+apellido));
#ejercisio 7 lista mayor
lista=[9,1,2,3,4,8,6,7]

def mayor (lista):
    min = lista[0]
    for x in lista:
        if x > min:
            min = x
            return min

def main(lista):
    print ("La lista es ", lista)    
    print ("El número mayor es: ", min(lista))
 
main(lista)
#ejercisio  multiplicar
def multiplicar_lista(numeros):
    producto =1
    for numero in numeros:
        producto*= numero
    return producto
numeros=[1,2,3,4,5]
print(multiplicar_lista(numeros))



        





