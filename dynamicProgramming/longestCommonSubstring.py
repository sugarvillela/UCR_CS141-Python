
def disp( array, label=None ):
    strr="" if label==None else label
    print( strr )
    for i in range( 0, len(array) ):
        print( array[i] )
    print()

def LCS( X, Y ):
    table=init2d( len(X)+1, len(Y)+1, 0 )
    found=init2d( len(X)+1, len(Y)+1, 0 )
    for i in range (1, len(X)+1):
        for j in range( 1, len(Y)+1):
            if X[i-1] == Y[j-1]:
                table[i][j] = table[i-1][j-1]+1
                found[i][j] = X[i-1]
            else:
                table[i][j] = max( table[i-1][j], table[i][j-1] )
    disp( found, "found:" )
    disp( table, "table:" )
    return traceLCS(X,Y,table)

def traceLCS( X, Y, table ):
    size=table[-1][-1]
    i,j = len(X),len(Y)
    LCS = []
    while 1:
        while table[i][j] == table[i-1][j]:
            i-=1
        while table[i][j] == table[i][j-1]:
            j-= 1
        i-= 1
        j-= 1
        LCS.append(X[i])
        if( len( LCS )==size ):
            LCS.reverse()
            return LCS  
    LCS.reverse()
    return LCS


def init2d( x, y, init ):    
    return [i[:] for i in [[init] * y] * x]

def main():
#     y="printing"
#     x="springtime"
    y="BDCABA"
    x="ABCBDAB"
    print( "Longest common substring is: ",LCS( x, y ) )

if __name__ == '__main__':
    main()
