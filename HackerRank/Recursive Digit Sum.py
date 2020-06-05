from sys import stdin


"""
Metodo que se encarga de calcular el digit number

@Param num str, numero al que se le calculara el digit number
@Param lenght int, la longitud del num actual
@Return int, el digit number de num
"""
def super_digit( num, lenght ):
    if( lenght == 1 ):
        return num

    acu = 0
    for element in num:
        acu+=int(element)
    string = str(acu )
    return super_digit( string , len( string ) )
    

def main():
    num, lenght = stdin.readline().strip().split()
    lenght = int( lenght )
    print ( super_digit(num*lenght, lenght*len(num)) )
main()
