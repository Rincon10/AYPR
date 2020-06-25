from sys import stdin


"""
Clase que representa al objeto grafo
@Author Iván Camilo Rincón Saavedra
@Version 1.0 24/06/2020.
"""
class Grafo:
    """
    Constructor de la clase grafo
    @Param length int, representara el numero de nodos que tendra el grafo
    """
    def __init__( self, length ):
        self.data = {};
        self.length = length;

    """
    Metodo que se encarga de añadir los nodos a el grafo
    """
    def addVertex( self  ):
        for vertex in range( self.length ):
            self.data[ vertex ] = [];

    """
    Metodo que se encarga de añadir las aristas entre cada nodo con su respectivo peso
    @Param fstVertex int , nodo a el cual se le añadira la arista con su peso
    @Param scndVertex int , nodo vecino de fstVertex
    @Param weigth int , peso de la arista entre los nodos fstVertex y scndVertex
    """
    def addEdge( self, fstVertex, scndVertex, weigth ):
        self.data[ fstVertex ].append( [ scndVertex, weigth ] );

    """
    Metodo que se encarga de ejecutar el algoritmo de disjkstra a la clase Grafo
    """
    def dijkstra( self ):
        time, cont, stop   =  [ float("inf") ] * self.length, 0 , False ;
        time[ 0 ] = 0;
        qp = [ [0, 0] ] ;

        while ( qp ):
            currentNode = qp.pop(0)

            for element in self.data[ currentNode[0] ]:
                if ( time[ element[0] ] > time[ currentNode[0] ] + element[1] ):
                    time[element[0] ] = time[ currentNode[0] ] + element[1];
                    cont+=1;
                    qp.append( element );

                if( cont > 2000 ):
                    stop = True;
                    break;

            if( stop ):
                break;

        print( 'possible' if ( stop ) else 'not possible' );
         

"""
Función principal que se encarga la lectura del problema a resolver.
"""
def main():
    c = int( stdin.readline().strip() );
    for cases in range( c ):
        n, m = [ int( x ) for x in stdin.readline().strip().split() ];
        grafo = Grafo( n );
        grafo.addVertex();
        for edges in range( m ):
            fstVertex, scndVertex, weigth = [ int( x ) for x in stdin.readline().strip().split() ];
            grafo.addEdge( fstVertex, scndVertex, weigth );
        grafo.dijkstra(  );

main()
