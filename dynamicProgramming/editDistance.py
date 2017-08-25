
def init2d( x, y, init ):    
    return [i[:] for i in [[init] * y] * x]

def disp( array, label=None ):
    strr="" if label==None else label
    print( strr )
    for i in range( 0, len(array) ):
        print( array[i] )
    print()
 
#edit distance
def diff(a, b, i, j):
    if( j<len(b) and a[i]==b[j]):
        return 0;
    return 1;

def editDistance( a, b ):       
    if( len( b )>len( a ) ):
        temp=a;
        a=b;
        b=temp;
    m, n = len( a )+1, len( b )+1
    E=init2d( m, n, 0 );
    
    for i in range( n ):
        E[0][i]=i
    for i in range( m ):
        E[i][0]=i
        
    m1, m2, m3 = 0,0,0
    for i in range( 1, m ) :
        for j in range( 1, n ) :
            m1=E[i-1][j]+1;
            m2=E[i][j-1]+1;
            m3=E[i-1][j-1]+diff( a, b, i-1, j-1 );
            E[i][j]=min( m1, m2, m3 );

    disp( E, "E:" );
    return E[m-1][n-1]    

def main():
    a="exponential"
    b= "polynomial"
    print( editDistance( a, b ) )

if __name__ == '__main__':
    main()
