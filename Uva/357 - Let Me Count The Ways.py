from sys import stdin
import sys


##Author : Ivan Camilo Rincon Saavedra

deno  = [ 1, 5, 10, 25, 50 ]
lenght = len( deno )
sys.setrecursionlimit(2000)

def print_( ways ):
    """
    PRE:parametros
    @Param ways int, numero de posibilidades que se puede devolver en cambio de n
    POST: muestra por pantalla el outPut solicitado por el problema
    """
    global n
    if( ways == 1 ):
         print("There is only 1 way to produce "+str(n)+" cents change.")
    else:
        print("There are "+str(ways)+" ways to produce "+str(n)+" cents change.")
    

def recu( phase,acu ):
    """
    PRE:parametros
    @Param phase int, indice que representara la seleccion de la denominacion actual
    @Param acu int, parametro que representa el acumulado actual de la sumatoria de las denominaciones
    POST: determina el numero de diferentes combinacion es de monedas tal que produzcan la cantidad dada
    """
    global n
    
    if ( ( phase == lenght ) or ( acu > n ) ):
        return 0

    
    elif ( ( deno[ phase ] == n ) or ( acu == n ) ):
        return 1

    elif ( acu < n ):
        return recu( phase, acu + deno[ phase ] ) + recu( phase + 1 , acu )
            

def main():
    global n
    n = int( stdin.readline().strip() )
    
    while ( n ):        
        ways = recu( 0,0  )
        
        print_(ways)
        n = int( stdin.readline().strip() )
main()
