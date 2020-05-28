from sys import stdin
import math


##Author: Ivan Camilo Rincon Saavedra

def pwSum( phase,answ,acu ):
    """
    PRE: ingresa la fase actual en la cual se evaluara la permutacion, answ sera la cadena en cual se guardara la respuesta actual, acu sera el acumulado de la sumatoria  
    POST:  un entero, el numero de posibilidades posibles de la combinacion calculada 
    """
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
