def divisores(num):
    if(isinstance(num,int) and num>0):
        return divisores_aux(num,num)
    else:
        return "El número debe ser mayor a cero y positivo"

def divisores_aux(num,contador):   
    if contador==0:
        return None
    else:
        if(num%contador)==0:
            print(contador)
        return divisores_aux(num,contador-1)
#------------------------------------------------------------------------------------------------------    
def multiplicarRecursivo(num,factor):
    if(isinstance(num,int) and isinstance(factor,int)):
        return multiplicar_aux(num,factor)
    else:
        return "El número debe ser un entero positivo"

def multiplicar_aux(num,factor):
    if(factor==0):
        return 0
    else:
        return num+multiplicar_aux(num,factor-1)
#--------------------------------------------------------------------------------------------------------
"""
#divisor    = 6
#dividendo  = 2
#contador   = 0
#fin -> contador == divisor

1 + (10 | 2 | 0+2)                      -> contador = 2 | 1
1 + (1 + (10 | 2 | 2+2))                -> contador = 4 | 1 + (1)
1 + (1 + (1 + (10 | 2 | 4+2)))          -> contador = 6 | 1 + (1 + (1))
1 + (1 + (1 + (1 + (10 | 2 | 6+2))))    -> contador = 8 | 0 + (1 + (1 + (1))) = 3
1 + (1 + (1 + (1 + (1 + (10 | 2 | 6+2)))))
1 + (1 + (1 + (1 + (1 + (1 + (10 | 2 | 8+2))))))
1 + (1 + (1 + (1 + (1 + (1 + (1 + (10 | 2 | 8+2)))))))
"""

def divisionRecursivo(divisor,dividendo):
    if(isinstance(divisor,int) and isinstance(dividendo,int)):
        return divisionRecursivo_aux(divisor,dividendo,0)
    else:
        return "El número debe ser entero positivo"

def divisionRecursivo_aux(divisor,dividendo,contador):
    if(contador<=divisor):
        return 0
    elif(contador>divisor):
        return -1
    else:
        return 1+divisionRecursivo_aux(divisor,dividendo,contador+dividendo)

    
    
    
