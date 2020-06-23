from  sys import stdin


class Grafo:
    def __init__( self, length ):
        self.data = {};
        self.length = length;

    def addVertex( self  ):
        for vertex in range( self.length ):
            self.data[ vertex ] = [];

    def addEdge( self, fstVertex, scndVertex):
        self.data[ fstVertex ].append( scndVertex );
        self.data[ scndVertex ].append( fstVertex );
        


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
