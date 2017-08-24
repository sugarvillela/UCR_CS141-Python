import sys

#helpers
def disp( array, label=None ):
    strr="" if label==None else label
    print( strr )
    for i in range( 0, len(array) ):
        print( array[i] )
    print()

def init2d( x, y, init ):    
    return [i[:] for i in [[init] * y] * x]

def locationCostPlan( AB, M, i, bias, table ):
    # Base case: last index
    # We've reached the 'leaf' of our decision tree
    # Decide which location to put in the last element
    if i>=len( AB[0] )-1:
        if not table[bias][i]<sys.maxsize:
            stay=AB[bias][i][0]
            go=AB[not bias][i][0]+M
            table[bias][i]=go if( go < stay ) else stay
        return
    
    # 'Short circuit' points:
    # If current decision branch has been traversed before, the element will
    # be set and we can proceed. Else, call recursively until all are set
    if not table[bias][i+1]<sys.maxsize:
        locationCostPlan(  AB, M, i+1, bias, table )
    if not table[not bias][i+1]<sys.maxsize:
        locationCostPlan(  AB, M, i+1, not bias, table )
    
    # Make a decision based on data at the current index
    stay=table[bias][i+1]
    go=table[not bias][i+1]+M
    best = go if go < stay else stay
    table[bias][i]=best + AB[bias][i][0]

def locationCostPlan_call(  A, B, M, names  ):
    # This is the non-recursive call for the algorithm   
    LEN=len( A )
    if LEN != len( B ):
        print("Input error")
        
    # Set up A and B as a single array
    # So it can be accessed using 'bias' 0 or 1
    AB=[ A, B ]                                     #A, B into 2-d table
    disp( AB )
    
    # Memoization table for dynamic programming traceback
    #initialize 2*n table to infinity 
    table=init2d( 2, LEN, sys.maxsize )
    
    #call recursive portion        
    locationCostPlan(  AB, M, 0, False, table )  #this runs 2n-1 times
    locationCostPlan(  AB, M, 0, True, table )   #this only runs once
    
    # Finished memoization table
    disp( table, "table" )
    
    # Traceback to display results
    p1_trace( AB, M, names, table )
    

def p1_trace( AB, M, names, table ):
    print(
          "Best cost is %d, with this plan..." %
          ( min( table[0][0], table[1][0] ) ) 
      )
    last=0
    for j in range( 0, len( table[0] )):
        i = ( table[0][j] > table[1][j] )
        if j and i != last:
            print("Move location, $%d cost" % ( M ))
        print("%s in %s" % ( names[i], AB[i][j][1] ))
        last=i
  
def main():
    # Uncomment below for different input set
#     A=[
#         [ 15,'Jan' ],
#         [ 6,'Feb' ],
#         [ 6,'Mar' ],
#         [ 6,'Apr' ],
#          
#         ]
#     B=[
#         [ 14,'Jan' ],
#         [ 15,'Feb' ],
#         [ 15,'Mar' ],
#         [ 15,'Apr' ],
#     ]
    A=[
        [ 1,'Jan' ],
        [ 3,'Feb' ],
        [ 20,'Mar' ],
        [ 30,'Apr' ],
        [ 15,'may' ],
        [ 6,'jun' ],
    ]
    B=[
        [ 50,'Jan' ],
        [ 20,'Feb' ],
        [ 2,'Mar' ],
        [ 4,'Apr' ],
        [ 9,'may' ],
        [ 36,'jun' ],
    ]
    costOfMoving=10
    ABnames=["NY","SF"]
    locationCostPlan_call( A, B, costOfMoving, ABnames )

if __name__ == '__main__':
    main()
