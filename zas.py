"un programa  que lea un numero entero  A de cuatro cifras, y cacule e imprima "
"un numero B que resulte de leer el numero A de derecha a izquierda "
#asi por ejemplo, si el valor de A es 4538, el valor de B sera 8354.
A=int(input("ingrese un numero de cuatro cifras: ")) 

c4 = A % 10 
c3 = int((A % 100) / 10)
c2 = int((A % 1000)/ 100)
c1 = int((A - (A % 1000)) / 1000)
print(str(c4)+str(c3)+str(c2)+str(c1))