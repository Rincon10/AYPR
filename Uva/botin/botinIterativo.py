from sys import stdin 

## Author: Iván Camilo Rincón Saavedra
## 31/07/2020
##Solución por el metodo iterativo, (botton up)

"""
Función que se encarga de  la solución del problema botin
@Param utility ArrayList< int >,lista la cual representara el beneficio de cada objeto
@Param weight ArrayList< int >,lista la cual representara el peso de cada objeto
"""
def answ( utility, weight ):
    global N, W, matrix

    for n in range( 1, N+1 ):
        for w in range( 1, W+1 ):
            if( weight[ n - 1 ] <= w ):
                matrix[ n ][ w ] = max( matrix[ n-1 ][ w ], matrix[ n-1 ][w - weight[ n - 1 ]] + utility[ n - 1 ])
            
            else:
                matrix[ n ][ w ] = matrix[ n-1 ][ w ]

"""
Función que se encarga de generar la lectura para el problema, botin
"""
def main():
    global N, W, matrix
    
    n = int( stdin.readline().strip() )
    for x in range( n ):
        N, W = [ int( z ) for z in stdin.readline().strip().split() ]
        utility, weight = [ int( z ) for z in stdin.readline().strip().split() ], [ int( z ) for z in stdin.readline().strip().split() ]

        matrix = [ [ 0 for x in range( W + 1 ) ] for t in range( N + 1 ) ]
        answ( utility, weight )

        """
        for el in matrix:
            print( el )
        """
        print( matrix[-1][-1] )
        
        
main()
