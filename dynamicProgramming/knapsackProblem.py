import math

def disp( array, label=None ):
    strr="" if label==None else label
    print( strr )
    for i in range( 0, len(array) ):
        print( array[i] )
    print()

def knapsack( choices, weight ):
    weight=math.floor( weight )
    n=len( choices )
    table=init2d( n+1 , weight+1, 0 )
    
    for i in range( weight+1 ):
        table[0][i]=i
       
    w, b = 0, 1
    ti=1
    for i in range( n-1, -1, -1 ):
        for j in range( 1, weight+1 ):
            #print( "i=%d, j=%d" % ( i, j ) )
            if i==n-1:
                if choices[i][w]<= table[0][j]:
                    table[ti][j]=choices[i][b]
            elif choices[i][w]<= table[0][j]:
                table[ti][j]=max( table[ti-1][j], choices[i][b] + table[ti-1][ j-choices[i][w] ] )
            else:
                table[ti][j]=table[ti-1][j]
        ti=ti+1
    return table

def knapsack_call( I, weight ):
    disp( I, "input data" )
    table = knapsack( I, weight )
    disp( table, "table" )
    print( "max value", table[-1][-1] )
    best=traceKnapsack( I, weight, table )
    disp( best, "Best arrangement:" )

def traceKnapsack( choices, weight, table ):
    i,j = len( choices ), weight
    iGet=0;
    bestVal=table[-1][-1]
    accVal=0;
    out = []
    while 1:
        while table[i][j] == table[i-1][j]:
            i-=1
            iGet+=1
        out.append( choices[iGet])
        accVal +=choices[iGet][1]
        if accVal>=bestVal:
            out.reverse()
            return out
        j -= choices[iGet][0]
        i-=1
        iGet+=1
    out.reverse()
    return out

def init2d( x, y, init ):    
    return [i[:] for i in [[init] * y] * x]

def main():
    # List of items to put in your knapsack as ( weight, value, name )
    I = [(2, 2, "cat"), (2, 3, "dog"),(2, 7, "wolf"),(6, 5, "chicken"), 
         (5, 4, "pigeon"), (4, 6, "otter")]
    # Find best arrangement of animals for the highest value within the 
    # given weight of 10
    knapsack_call( I, 10 )

if __name__ == '__main__':
    main()
