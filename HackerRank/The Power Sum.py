from sys import stdin
import math


##Author: Ivan Camilo Rincon Saavedra


"""
    Metodo que se encarga de realizar la solucion del problema
    
    @Param phase,int que representa la fase actual en la cual se evaluara la permutacion
    @Param answ, cadena de tipo String en cual se guardara la respuesta actual
    @Param acu,  int en el cual sera el acumulado de la sumatoria  
    @Return int ,numero de posibilidades posibles de la combinacion calculada 
"""
def pwSum( phase,answ,acu ):
    global x, n, stop

    if( acu == x  ):
        return 1
    
    elif( (phase == stop) or ( acu > x )  ):
        return 0
        
    return pwSum( phase + 1, answ, acu ) + pwSum( phase + 1, answ+" "+str(phase), acu +(phase**n))
    
        

    
        
def main():
    global x, n, stop
    x, n = int( stdin.readline().strip()),int( stdin.readline().strip())
    stop = math.ceil( x**(1/n)) + 1
    print( pwSum(1,"",0 ) )
main()

