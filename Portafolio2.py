"""
Nombre: pasar a entero
Entrada: num
Salida: Pasar el número a entero
Restricción: Números positivos 
"""

def pasarAentero(num):
    if(isinstance(num,float) and num>0):
        return pasarAentero_aux(num)
    else:
        return "El número debe ser positivo"

def pasarAentero_aux(num): 
    if(isinstance(num,float)):
        num=num%10**10*1000000
        num=int(num)
        return pasarAentero_aux(num)
    elif(num%10==0):
        return pasarAentero_aux(num//10)
    else:
        return num

#----------------------------------------------------------------------------------------
"""
Nombre: Contar digitos flotantes
Entrada: num
Salida: Contar los digitos de los números con décimales 
Restricción: La cantida de digitos que tiene un número con décimales 
"""
def contarDigitosFlotantes(num):
    if(isinstance(num,float) and num>0):
        if (num<=100000):
            return contardigitos_aux(num)
        else:
            return "Debe tener maximo 5 decimales"
    else:
        return "El número debe ser positivo"

def contardigitos_aux(num):
    if(isinstance(num,float)):
        num=num%10**10*10000
        num=int(num)
        return contardigitos_aux(num)
    elif(num%10==0):
        return contardigitos_aux(num//10)
    elif (num<100):
        return 2
    else:
        return 1+contardigitos_aux(num//10)
#--------------------------------------------------------------------------------------------
"""
Nombre: Indice número
Entrada: num,indice
Salida: Mostrar el número dependiendo su posición
Restricción: Números positivos  y enteros
"""
def Indice(num,indice):
    if(isinstance(num,int) and num>0 and isinstance(indice,int)) :
        largo=Contardigitos(num)
        Comparacion=num-1
        return Indice_aux(num,indice+1,largo,Comparacion)
    else:
        return "El numero debe ser entero positivo"

def Contardigitos(num):
    if(num==0):
        return 0
    else:
        return 1+Contardigitos(num//10)

def Indice_aux(num,indice,largo,Comparacion):
    if(num==0):
        return 0
    else:
        if (num<Comparacion):
            return (num%10+Indice_aux(num%10//10,indice,largo,Comparacion))
        elif(indice==largo):
            return (num%10)+Indice_aux(num%10//10,indice,largo,Comparacion)
        else:
            largo=largo-indice
            return Indice_aux(num//10**largo,indice,largo,Comparacion)
        
#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Indice número 1
Entrada: num,indice,indice1
Salida: Mostrar en pantalla los dos indices dependiendo su posición
Restricción: Números positivos y enteros 
"""
def Indicenumero1(num,indice,indice1):
    if(isinstance(num,int) and num>0 and isinstance(indice,int) and isinstance(indice1,int)) :
        primerIndi=Indice(num,indice)
        secondIndi=Indice(num,indice1)
        return sumaIndi(primerIndi,secondIndi)

def sumaIndi(primerIndi,secondIndi):
    if(primerIndi==0):
        return 0
    else:
        return (primerIndi*10+secondIndi)+ sumaIndi(primerIndi//10,secondIndi)

    
