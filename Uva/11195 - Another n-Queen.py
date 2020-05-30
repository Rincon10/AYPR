from sys import stdin


def valid( solp, phase,check ):
    """
    PRE: metodo que se encarga de validar la solucion parcial actual
    
    @Param solp List, lista que representa a la solucion parcial a validar
    @Param phase int , la phase actual que se va a validar
    @Param check List, fila del tablero para validar si se puede usaro no
    POST:
    @Return boolean, que dice si la solucion es valida o no
    """
    for x in range( phase ):
        if(  (solp[phase] == solp[x] )  or ( abs( phase - x ) == abs( solp[x] - solp[phase ] ) ) ):
            return False
        boolean =  ("*" in check )
        while( boolean ):
            column = check.index("*")
            if( column == phase ):
                return False
            check[column]="."
            boolean =  ("*" in check )
            
        
    return True 


def backTracking( phase, solp ):
    global N, board
    """
    PRE:metodo que se encarga de realizar todas las posibles soluciones 
    @Param solp List, lista que representa a la solucion parcial actual
    @Param phase int , la phase actual a validar
    POST:
    @Return int, el numero de posibilidades de ubicar las reinas en un tablero sin que se maten y sean validas
    """
    cont = 0
    if( phase < N ):
        for x in range( N ):
            solp[ phase ] = x
            mSolp = solp[:]
            
            if( valid( mSolp, phase, board[x][:] ) ):                
                if( phase < ( N - 1 ) ):
                    cont+=backTracking( phase + 1, mSolp)
                else:
                    cont+=1
        return cont 

def main():
    global N, board
    N, cont = int( stdin.readline().strip() ), 1
    
    while( N ):
        board = []
        
        for x in range( N ):
            board.append( [a for a in stdin.readline().strip() ])
        print( "Case "+str(cont)+":",backTracking(0 ,[-1 for x in range(N) ]) )
        cont +=1;
        N = int( stdin.readline().strip() )    
main()
    
