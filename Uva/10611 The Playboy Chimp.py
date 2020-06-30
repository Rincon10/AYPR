from sys import stdin

## Author:Ivan Camilo Rincon Saavedra 

stdin.readline()
M, new, last = [int(x) for x in stdin.readline().strip().split()], [], -1
stdin.readline()
for el in M:
    if el != last:
        new.append(el)
        last = el
lon = len(new)



"""
Función que se encarga de realizar una busqueda de un elemento, con el algoritmo de busqueda binaria
@Param el int, elementa a buscar en una lista
@Return int,int ;los indices que se encuentran por izquierda y derecha del elemento 
"""
def binarySearch( el ):
    iz, der = 0, lon-1

    while ( iz <= der ):
        m =(iz + der)//2

        if (new[m] == el):
            return m -1 , m+1

        else:
            if (new[m] > el):
                der = m - 1
            else:
                iz = m + 1
    
    return  min(iz,der), max(iz,der)
    
"""
Función principal que se encarga de la lectura del problema.
"""
def main():
    
    N = [int(x) for x in stdin.readline().strip().split()]
    last = -1
    for el in N:
        iz, der = binarySearch(el)
        print( (new[iz] if 0<= iz < lon else 'X'),( new[der] if 0<= der < lon else 'X' ))
        
    
main()
