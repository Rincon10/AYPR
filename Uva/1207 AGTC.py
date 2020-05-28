from sys import stdin

##Author: Ivan Camilo Rincon Saavedra

def recu( i, j):
    """
    PRE: ingresan dos parametos
    @Param: i int, la posicion actual en la cadena X
    @Param: j int, la posicion actual en la cadena Y
    
    POST: retorna el minimo de pasos necesarios para convertir X en Y
    """
    global X,Y, dic
    answ = float("inf")
    
    key = str( (i,j) )
    if key in dic.keys():
        return dic[key]
    
    if( (i == -1  and j>=0) or (j == -1  and i>=0) ) :
        answ = (j if i == -1 else i) +1

    elif( i == -1  and j == -1 ) :
        answ = 0

    elif( X[i] == Y[j] ):
        answ = recu(i - 1 ,j - 1)

    elif( X[i] != Y[j] ):
        answ = 1+ min(recu(i - 1 ,j - 1),recu(i - 1 ,j),recu(i,j - 1) )

    dic[ key ] =  answ
    return answ
    
    

def main():
    global X,Y,dic
    """
    Metodo que se encarga de leer la entrada del problema
    """

    X = stdin.readline().strip()
    while( X ):
        i,X = X.split()
        
        dic = dict()
        j, Y =  stdin.readline().strip().split()

        print( recu( int(i) - 1, int(j) - 1 ) )
        X = stdin.readline().strip()
main()

