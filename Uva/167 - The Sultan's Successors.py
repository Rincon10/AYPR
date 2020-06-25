from sys import stdin

##Author : Ivan Camilo Rincon Saavedra


"""
Funcion que se encarga de validar la solucion parcial actual

@Param solp List, lista que representa a la solucion parcial a validar
@Param phase int , la phase actual que se va a validar
@Return boolean, que dice si la solucion es valida o no
"""
def valid( phase, solp ):
    
    for  x in range( phase ):
        if( ( solp[phase] == solp[x] ) or ( abs( solp[phase]-solp[x]) == abs( x - phase ) ) ):
            return False
    return True
            


"""
Funcion que se encarga de realizar todas las posibles soluciones

@Param phase int , la phase actual a validar
@Param solp List, lista que representa a la solucion parcial actual
@Param acu, la sumatoria de las posiciones del tablero en que se colocaran las reinas
@Return int, el numero de posibilidades de ubicar las reinas en un tablero sin que se maten y sean validas
"""
def backTracking( phase, solp, acu ):
    global sizeBoard,board,answ 

    if( phase < sizeBoard ):
        for x in range( sizeBoard ):
            solp[ phase ] = x
            mSolp = solp[:]

            if( valid( phase, mSolp ) ):
                if ( phase < sizeBoard - 1  ):
                    
                    backTracking( phase + 1, mSolp[:],acu + int(board[phase][mSolp[phase]]))
                else:
                    
                    answ = max(answ , acu + int(board[phase][mSolp[phase]]) )
        
        
"""
Funcion principal que se encarga de la lectura del problema
"""
def main():
    global sizeBoard,board, answ  
    cases,sizeBoard = int( stdin.readline().strip() ), 8
    
    for x in range( cases ):
        board = []
        for x in range( 8 ):
            board.append( stdin.readline().strip().split() )
        answ = -1
        backTracking(0,[ -1 for x in range( sizeBoard ) ] , 0)
        answ = str(answ)
        print(" "*(5-len(answ))+answ)
main()
