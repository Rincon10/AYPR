from sys import stdin

##Author: Ivan Camilo Rincon Saavedra

def valid( solp ):
    global lenght, pairs
    """
    metodo que se encarga de validar la solucion parcial actual
    PRE:
    @Param solp lista, lista que representa la solucion parcial a vallidar
    POST:
    @Return boolean, que dice si la solp es valida 
    """
    
    if( len( solp ) > 1 ):
        for element in pairs:
            isE1, isE2  = ( element[0] in solp),( element[1] in solp)
            if( isE2 and not( isE1 ) ):
                return False
            if( isE1 and isE2 ):
                index1, index2 = solp.index(element[0]),solp.index(element[1])
                if( index1 > index2 ):
                    
                    return False
    
    return True 

def backTracking( phase,options , solp ,string ):
    global lenght, pairs
    """
    metodo que se encarga de realizar backTracking con las opciones proporcionadas
    PRE: 
    @Param phase int , numero que indicara la fase actual de la solucion parcial 
    @Param options list , las opciones a permutar
    @Param solp list ,solucion parcial actual
    @Param string String, cadena que almacenara la solucion parcial
    POST:
    imprime todas la permutaciones validas
    """
    if ( phase < lenght ):
        for x in range( len( options ) ):
            
            mOptions  = options[:]
            element = mOptions.pop(x)
            
            
            mSolp = solp[:]
            mSolp.append( element )
            
            mString = string[:]
            mString+=element
            

            if( valid( mSolp ) ):
                
                if( phase < (lenght - 1) ):
                    backTracking( phase + 1,mOptions[:] , mSolp[:],mString )
                else:
                    print( mString )

def main():
    global lenght, pairs
    
    case = stdin.readline().strip()
    while( case ):
        case = case.split()
        lenght = len( case )
        p, pairs = stdin.readline().strip().split() , []
        while p:
            pairs.append((p[0],p[1]))
            p = p[2:]
        case.sort()
        backTracking( 0,case[:],[],"")
        case = stdin.readline().strip()
        if (case):print("")
        
main()
