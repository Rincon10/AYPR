from sys import stdin

"""
Clase que implementa una nueva clase de cola con politica de  FIFO

@Author Ivan Camilo Rincon Saavedra
@Version 1.0 04/06/2020
"""
class MyQueue:
    """
    Constructor de la clase Myqueue
    """
    def __init__( self ):
        self.data = [ ];

    """
    Metodo que se encarga de encolar un item a la cola, con politica FIFO
    @Param int item,  elemento a agregar a la cola
    """
    def enQueue( self, item ):
        self.data.append( item );

    """
    metodo que se encarga de desencolar la cola con politica FIFO
    """
    def deQueue( self ):
        if( len( self.data ) >= 1 ):
            self.data.pop(0);

    """
    metodo que se encarga de mostrar el elemento en la cabeza de la cola 
    """
    def print( self ):
        print( self.data[0] );

    """
    metodo que se encarga de retornar la cola
    @Return int[], lista de numeros que pertenecen a la cola
    """
    def getData( self ):
        return self.data
        

def main():
    n, myQueue = int( stdin.readline().strip() ), MyQueue();
    for x in range( n ):
        line = [ int(x) for x in stdin.readline().strip().split() ];
        if( line[0] == 1 ):
            myQueue.enQueue( line[1] );
            
        elif( line[0] == 3 ):
            myQueue.print();
            
        else:
            myQueue.deQueue();
main()
