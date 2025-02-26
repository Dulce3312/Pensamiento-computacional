num = int(input("ingrese un numero de cinco digitos: "))

d1 = (num//10000)
d2 = (num//1000)%10
d3 = (num//100)%10
d4 = (num//10)%10
d5 = (num%10)

if (d1<d2) or (d1<d3) or (d1<d4) and (d1<d5): 
    print(d1, d2, d3, d4, d5)
elif (d2<d1) or (d2<d3) or (d2<d4) and (d2<d5):
    print(d2, d3, d4, d5, d1)
elif (d3<d1) and (d3<d2) and (d3<d4) and (d3<d5): 
    print(d3, d1, d2, d4, d5)
elif (d4<d1) and (d4<d2) and (d4<d3) and (d4<d5): 
    print(d4, d1, d2, d3, d5)
else :(d5<d1) and (d5<d2) and (d5<d3) and (d5<d4)
    print:  