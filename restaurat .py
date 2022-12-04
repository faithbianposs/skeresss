"el siguiente ejercicio es un menu de un restaurante de hamburguesas"
#
#   hamburguesa                                 $ 12.00
#   hamburguesa con queso                       $ 15.00   
#   hamburguesa doble                           $ 17.00
#   papa a la francesa (una orden)              $  5.00
#   maltedas                                    $  6.00
#   refrescos                                   $  5.00 
#   cafe                                        $  6.00
"escribir  un programa que lea la cantidad consumida de cada alimento y que calcule e imprima el total de la cuenta"

hamburguesa = 12
hamburguesa_con_queso =  15
hamburguesa_doble =  17
papas     = 5
maltedas   = 6
refrescos   = 5
cafe    = 6
c_hamburguesa=int(input('ingrese la cantidad de hamburguesas: '))
c_hamburguesa_con_queso=int(input('ingrese la cantidad de hamburguesas con queso: '))
c_hamburguesa_doble=int(input('ingrese la cantidad de hamburguesas dobles: '))
c_papas=int(input('ingrese la cantidad de papas: '))
c_malteadas=int(input('ingrese la cantidad de malteadas: '))
c_refrescos=int(input('ingrese la cantidad de refrescos: '))
c_cafe=int(input('ingrese la cantidad de cafe: '))

total = c_hamburguesa * hamburguesa + c_hamburguesa_con_queso * \
    hamburguesa_con_queso + c_hamburguesa_doble * hamburguesa_doble +\
    c_papas* papas +c_malteadas * maltedas + c_refrescos * refrescos +\
    c_cafe* cafe  
    
print ('el valor a pagar es:',total )
    