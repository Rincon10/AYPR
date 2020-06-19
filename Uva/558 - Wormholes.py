from sys import stdin


class Grafo:
    def __init__( self, length ):
        self.data = {};
        self.length = length;

    def addVertex( self  ):
        for vertex in range( self.length ):
            self.data[ vertex ] = [];

    def addEdge( self, fstVertex, scndVertex, weigth ):
        self.data[ fstVertex ].append( [ scndVertex, weigth ] );

    def dijkstra( self ):
        time, cont, stop   =  [ float("inf") ] * self.length, 0 , False ;
        visited = [ False ] * self.length;
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
