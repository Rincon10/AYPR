from sys import stdin
import math


##Author: Iván Camilo Rincón Saavedra

"""
Funcion que se encargara de decir si un numero es primo
@Param number int, numero a verificar si es primo o no
@Return boolean, que dice si number es primo o no
"""
def prime( number ):
    stop =int( math.sqrt( number ) )
    cont = 1
    for x in range( 2,stop + 1 ):
        if( number % x == 0):
            cont = 2
            break
    return ( cont == 1 )



"""
Funcion que se encarga de validar la solucion parcial actual
@Param phase int , la phase actual que se va a validar
@Param solp List, lista que representa a la solucion parcial a validar
@Return boolean, que dice si la solucion es valida o no
"""
def valid( phase, solp ):
    if( phase != 0 ):
        aft = ( phase - 1 ) % len(solp)
        
    
        if( not prime( solp[phase]+ solp[aft] ) ):
            return False

    return True 
        


"""
Funcion que se encarga de realizar backTracking con las opciones proporcionadas
(imprime todas la permutaciones validas)
@Param phase int , numero que indicara la fase actual de la solucion parcial 
@Param options list , las opciones a permutar
@Param solp list ,solucion parcial actual
@Param answ String, cadena que almacenara la solucion parcial y/o final
"""    
def backTracking( phase, options, solp, answ ):
    global number

    if( phase < number ):
        for x in range( len( options ) ):
            mOptions = options[:]
            element = mOptions.pop(x)
            
            mSolp = solp[:]
            mSolp.append( element )
            
            mAnsw = answ[:]
            mAnsw += str(element)+ " "
            
    
            if( mSolp[0] == 1 and valid( phase, mSolp ) ):
                if( phase < (number - 1 ) ):
                    backTracking( phase + 1, mOptions, mSolp, mAnsw )
                else:
                    if( prime( mSolp[-1]+ mSolp[0] ) ):
                        print( mAnsw.strip())
    
    
"""
Funcion que se encarga en la lectura del problema
"""
def main():
    global number
    number, cont  = stdin.readline().strip(), 1
    
    while( number ):
        number = int( number )
        
        print("Case "+str(cont)+":" )
        backTracking(0,[x for x in range(1,number+1)],[],"" )
        number = stdin.readline().strip()
        
        if( number ):
            print()
        cont+=1
    
main()
