from sys import stdin

#Author: Ivan Camilo Rincon Saavedra

def main():
    n = int( stdin.readline().strip() )
    for x in range( n ) :
        string = stdin.readline().strip().split()
        left, current = -1, len( string )
        right = -1 
        while( (")" in string) or ( current >= 0 ) ):
            current -= 1
            if( left != -1 and right != -1 ):
                op = string[left + 2  ]
                op1, op2 = float( string[left+1] ), float( string[left+3] )
                if( op == "+" ):
                    string[left:right + 1] = [str(round(op1+op2,2))]
                    
                elif( op == "-"):
                    string[left:right + 1] = [str(round(op1-op2,2))]
                elif( op == "*"):
                    string[left:right + 1] = [str(round(op1*op2,2))]
                else:
                    string[left:right + 1] = [str(round(op1/op2,2))]
                        
                    
                left, right = -1, -1
                current = len( string ) - 1
                    
            if( string[current] == ")"):
                right = current
            elif( string[current] == "(" ):
                left = current
        
        print(string[0]+"0" if (string[0][-2] == ".") else string[0])

             
     
main()
