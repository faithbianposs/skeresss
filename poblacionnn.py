"en una ciudad hay N habitantes el 1 de enero. al finalizar el año (el 31 de diciembre) la poblacion ha variado"
#el 2% de la poblacion ha emigrado a otras ciudades.
#hubo un aumento del 1,8% por inmigraciones.
#hubo el aumento del 1,7% por nacimientos.
#el 1,1% de la poblacion fallecio.

poblacion_incial = int(input('ingrese la cantidad de habitantes inciales'))

emigracion = poblacion_incial * 0.02
inmigracion = poblacion_incial * 0.018
nacimientos =poblacion_incial * 0.017
fallecimientos = poblacion_incial * 0.011

aumento = inmigracion + nacimientos
disminucion = emigracion + fallecimientos

aumento_mensual = aumento/ 12
disminucion_mensual = disminucion / 12
poblacion_final = poblacion_incial + aumento - disminucion

print('el aumento mensual fue de' ,aumento_mensual, 'personas.')
print('la disminucion mensual fue de' ,disminucion_mensual, 'personas.')
print('la poblacion al final de año fue de:' ,poblacion_final, 'personas.')
 