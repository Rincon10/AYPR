from sys import stdin 

## Author: Iván Camilo Rincón Saavedra
## 31/07/2020
##Solución por el metodo e backTracking




"""
Función que se encarga de validar si la solucion parcial es valida
@Param w int, peso parcial.
@Return boolean, el cual dice si el peso parcial es valido ( si es mayor o igual a 0 )
"""
def valid( w ):
    return (w >= 0)

"""
Función que se encarga de  hacer backtracking del problema botin
@Param utility ArrayList< int >,lista la cual representara el beneficio de cada objeto
@Param weight ArrayList< int >,lista la cual representara el peso de cada objeto
@Return int, la cantidad maxima que se puede llevar en el cofre
"""
def backTracking( N, W, z, w, utility, weight ):
    if( len( utility ) ):
        answ = 0
        for x in range( len( utility ) ):
            
            u,cW = utility.pop(0), weight.pop(0)
            
            mUtility = utility[:]
            mWeight =  weight[:]

            

            if ( valid( w - cW ) ):
                if ( len( utility ) > 1 ):
                    answ = max( z + u , backTracking( N, W, z + u , w - cW, mUtility[:], mWeight[:] ), backTracking( N, W, z , W , mUtility[:], mWeight[:] ) )
                else:
                    answ = max( z + u  , answ)
                    
    return answ
            
    

"""
Función que se encarga de generar la lectura para el problema, botin
"""
def main():
    
    n = int( stdin.readline().strip() )
    for x in range( n ):
        N, W = [ int( z ) for z in stdin.readline().strip().split() ]
        utility, weight = [ int( z ) for z in stdin.readline().strip().split() ], [ int( z ) for z in stdin.readline().strip().split() ]

        
        print( backTracking( N, W, 0, W, utility, weight )  ) 
        
        
main()
