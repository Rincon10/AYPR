from sys import stdin

##Author: Ivan Camilo Rincon Saavedra

def sort( li ):
    """
    PRE: Ingresa un parametro
    @Param li List, lista a ordenar
    POST: Retorna la lista ordenada, calculando a su vez el numero de pasos realizados
    """
    global steps
    lenght = len( li )//2

    answ = []
    
    i, j ,inf = 0, 0, [ float("inf") ]
    if ( len( li ) == 1 ):
        return li


    lis, liss = sort( li[:lenght])+inf, sort( li[lenght:] )+inf
    while ( (i < len(lis) - 1 ) or ( j < len( liss ) - 1 ) ):
        
        if( lis[ i ] < liss[j ] ):
            answ.append( lis[ i ] )
            i+=1
            steps+=j
        else:
            answ.append( liss[ j ] )
            j+=1
    return answ

def main():
    """
    PRE: Funcion que no recibe ninguna parametro 
    POST: ejecuta el algoritmo para leer la entrada de Problem : 10810
    """"
    global steps
    n = int( stdin.readline().strip() )
    while ( n ):
        steps = 0
        lis = [ ]
        for x in range( n ):
            lis.append( int( stdin.readline().strip() ) )

        sort( lis)
        print(steps)
        n = int( stdin.readline().strip() )

main()
