from sys import stdin


class Grafo:
    def __init__( self, size ):
        self.data = {};
        self.size = size;
        self.friends = {};
        self._friends = 0;
        self.addVertex();

    def addVertex( self ):
        for c in range( 1, self.size + 1 ):
            self.data[ c ] = [];
            
    def addEdge( self, initV, lastV ):
        if( lastV not in self.data[initV] ):
            self.data[initV].append( lastV );
            
    def print( self ):
        print( self.data );

    def dfs( self , currentNode, route ):
        route+=[ currentNode ];
        print(route )
        fst, lst = route[0], route[-1];
        if( fst != lst ):
            key1 = str( ( fst, lst ) );
            key2 = str( ( lst, fst ) );

            if( key1 not in self.friends.keys() ):
                self._friends+=1;
                
            elif( key2 not in self.friends.keys() ):
                self._friends+=1;

            self.friends[ key1 ] = -1
            self.friends[ key2 ] = -1
            

            
        for element in self.data[ currentNode ]:
            if( element not in route ):
                self.dfs(  element, route[:] );

    def getFriend( self ):
        return self._friends;
            
        
        
        

def main():
     N = int( stdin.readline().strip() );

     for x in range( N ):
         n, m = [ int( y ) for y in stdin.readline().strip().split() ];
         grafo = Grafo(n);
         for z in range( m ):
             init, last = [ int( y ) for y in stdin.readline().strip().split() ];
             grafo.addEdge( init, last );

         for y in range( 1, n + 1 ):
             grafo.dfs( y, [] );
             
         print( grafo.getFriend(),"\n" );
         
     
main() 
