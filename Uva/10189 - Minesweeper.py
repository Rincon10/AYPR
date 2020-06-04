from sys import stdin

movements = [ (1,0) ,(-1,0) ,(0,1) ,(0,-1) ,(1,-1) ,(-1,1) ,(1,1) ,(-1,-1) ]

##Author: Ivan Camilo Rincon Saavedra


"""
Funcion que se encarga de la solucion la solucion del problema
@Param minesweeper String[], buscaminas con el cual se trabajara para implementar la solucion
@Param answ String, cadena en la cual se almacenara la respuesta
@Return String, retorna la cadena con la solucion final 
"""
def solution( minesweeper , answ):
    global m,n

    for row in range( m ):
        for column in range( n ):
            if( minesweeper[row][column] == "*"):
                answ+="*"
            else:
                mines = 0
                for move in movements:
                    tempRow, tempColumn = row + move[0], column + move[1]
                    if( ( 0<= tempRow < m ) and ( 0<= tempColumn < n ) ):
                        if( minesweeper[tempRow][tempColumn] == "*"):
                            mines+=1
                answ+=str(mines)
        answ+="\n"
    return answ


"""
Funcion principal que se encarga de leer la entrada y generar la salida del problema
"""
def main():
    global m,n
    
    m, n  = [ int(x) for x in stdin.readline().strip().split()]
    case = 1
    while( m!= 0  and n!=0):
        minesweeper = [ ]
        for x in range( m ):
            minesweeper.append(stdin.readline().strip())
        answ =solution(minesweeper, "" )
        m, n  = [ int(x) for x in stdin.readline().strip().split()]
        
        print( ( "Field #"+str(case)+":\n"+answ.strip() ) if( ( m == 0 ) and ( n == 0 ) ) else ( "Field #"+str(case)+":\n"+answ ) )
        case+=1
    
main()
