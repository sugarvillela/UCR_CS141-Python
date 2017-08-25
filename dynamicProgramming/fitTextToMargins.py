import sys

#helpers
def disp( array, label=None ):
    strr="" if label==None else label
    print( strr )
    for i in range( 0, len(array) ):
        print( array[i] )
    print()

def init1d( n, init ):
    return [ init ] * n

def init2d( x, y, init ):    
    return [i[:] for i in [[init] * y] * x]

def prettyOut( p, n, W, out, i ):
    if( i> len( p ) ):
        return 0
    if (p[n] == 1):
        k = 0
    else:
        k = prettyOut(p, p[n]-1, W, out, i+1 )+1
    temp=""
    for j in range( p[n]-1, n ):
        temp+=W[j]+" "
    out.append( temp)
    return k

# Based on an algorithm by Thomas H. Cormen (CLRS) 
# Introduction to Algorithms(August 2009) 
# Time O(n^2) Space O(n^2)  
def fitToMargins ( W, L ):
    W = W.split()
    n = len( W )
    lens=[]
    for i in range( n  ):
        lens.append( len( W[i] ) )
    
    #calculate slack
    slacks=init2d( n+1, n+1, 0 )
    for i in range( 1, n+1 ):
        slacks[i][i] = L - lens[i-1]
        for j in range( i+1, n+1 ):
            slacks[i][j] = slacks[i][j-1] - lens[j-1] - 1
    #minimize square of slack
    minimizeMe=init2d( n+1, n+1, 0 )
    for i in range( 1, n+1 ):
        for j in range( i, n+1 ):
            if slacks[i][j] < 0:
                minimizeMe[i][j] = sys.maxsize
            elif j == n and slacks[i][j] >= 0:
                minimizeMe[i][j] = 0
            else:
                minimizeMe[i][j] = slacks[i][j]*slacks[i][j]
    #find optimal arrangements
    totals=init1d( n+1, 0 )#
    printOrder=init1d( n+1, 0 ) 
    for j in range( 1, n+1 ):
        totals[j] = sys.maxsize
        for i in range( 1, j+1 ):
            if (
                    totals[i-1] != sys.maxsize and 
                    minimizeMe[i][j] != sys.maxsize and 
                    (totals[i-1] + minimizeMe[i][j] < totals[j]) 
                ):
                totals[j] = totals[i-1] + minimizeMe[i][j]
                printOrder[j] = i
    out=[]            
    prettyOut( printOrder, n, W, out, 0)
    return out

def main():
    # Unformatted text
    W="""Call me Ishmael. Some years ago, never mind how long precisely, 
    having little or no money in my purse, and nothing particular to 
    interest me on shore, I thought I would sail about a little and see 
    the watery part of the world."""
    
    # Length between margins
    L=39
    
    # Algorithm returns an array of formatted strings
    disp( fitToMargins( W, L ) )

if __name__ == '__main__':
    main()
