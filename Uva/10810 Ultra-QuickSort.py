from sys import stdin

##Author: Ivan Camilo Rincon Saavedra



"""
Función que se encargara de ordenar una lista de elementos usando el algoritmo MergeSort
@Param li List, lista a ordenar
@Return List, retorna la lista ordenada ; calculando a su vez el número de pasos realizados.
"""
def sort( li ):

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


"""
Función principal que ejecuta el algoritmo para leer la entrada de Problem : 10810
"""
def main():
    global steps
    
    n = stdin.readline().strip() 
    while ( n  ):
        steps = 0
        lis = [ ]
        for x in range( int(n) ):
            lis.append( int( stdin.readline().strip() ) )

        sort( lis)
        print(steps)
        n = stdin.readline().strip() 

main()
