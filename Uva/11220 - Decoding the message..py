from sys import stdin


def main():
    n= int( stdin.readline().strip() )
    stdin.readline().strip()
    for case in range( 1,n+1 ):
        line = stdin.readline().strip()
        print("Case #"+str(case)+":")
        while( line ):
            line, message, current =line.split() ,"", 0
            for element in line:
                if( len( element ) > current ):
                    message+=element[current]
                    current+=1
                    
            print(message)
            line = stdin.readline().strip()
        if( case!= n ):
                print("")
main()
