numero = int(input("ingrese un número entre 1 y 10: "))
 
resultado=''

if numero<=(3): 
    resultado=(numero*'I') 
elif numero>=(5): 
    resultado= "V" + (numero-5)*'I'

if numero==(4): 
    resultado= 'IV'
    
if numero==(9): 
    resultado= 'IX'
    
if numero>9: 
    resultado=print("no válido")

print(resultado)