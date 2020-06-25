from  sys import stdin


"""
Clase que representa un grafo
@Author Ivan Camilo Rincon Saavedra
@Version 1.0 22/06/2020
"""
class Grafo:

    """
    Constructor de la clase Grafo
    @Param length, int que represeta la cantidad de nodos que el grafo tendra
    """
    def __init__( self, length ):
        self.data = {};
        self.length = length;

    """
    Metodo que se encarga de agregar los vertices ( Nodos ) al grafo
    """
    def addVertex( self  ):
        for vertex in range( self.length ):
            self.data[ vertex ] = [];

    """
    Metodo que se encarga de agregar las aristas correspondientes deñ grafo
    @Param fstVertex int, representa el primer nodo al que se le añadira la arista
    @Param scndVertex int,representa el segundo nodo al que se le añadira la arista
    """ 
    
    def addEdge( self,fstVertex , scndVertex):
        self.data[ fstVertex ].append( scndVertex );
        self.data[ scndVertex ].append( fstVertex );
        

    """
    Metodo que se encarga de ejecutar el algoritmo dfs
    @Param seed int, nodo raiz para la ejecucion del algoritmo
    """
    def dfs( self, seed ):
        parent = [ -1 ] * self.length;
        parent[ seed ] =0 ;
        
        qp = [ seed ];
        stop = False;

        while( qp ):
            current = qp.pop(0);
            for element in self.data[ current ]:
                if( parent[ element ] == -1 ):
                    parent[ element ] = parent[ current ] + 1;
                    qp.append( element );
                    
                elif( parent[ current ] == parent[ element ] ):
                    stop = True;
                    break;
                
            if( stop ):
                break;
        print( 'NOT BICOLORABLE.' if ( stop ) else 'BICOLORABLE.' );


"""
Funcion principal para la lectura del problema
"""
def main():
    n = int( stdin.readline().strip() );
    while( n ):
        grafo = Grafo( n );
        grafo.addVertex();
        for x in range( int(stdin.readline().strip()) ):
            fstVertex, scndVertex = [ int( t ) for t in stdin.readline().strip().split() ];
            grafo.addEdge(fstVertex, scndVertex);

        grafo.dfs( 0 );
            
        n = int( stdin.readline().strip() );
    

main() 

@Param 
