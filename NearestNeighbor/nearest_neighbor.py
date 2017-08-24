import sys
from math import sqrt
import math
import re
import time

pointRE=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

min_distance=sys.maxsize
outFileName="input_10.txt"
# For runtime analysis display    
bfCount=0 
rCount=0
bcCount=0
mCount=0;

# Standard mergeSort, but inputs are 2-element point arrays; 
# sorts by i=0 for x, or i=1 for y
def mergeSort( all, i ): #sorts on value at 0 index of each subarray
    if len(all) < 2:
        return all
    else:
        middle = math.floor( len(all)/2 )
        left = mergeSort( all[:middle], i )
        right = mergeSort( all[middle:], i )
        return merge( left, right, i )
        
def merge( left, right, i ):
    out = []
    while len( left ) and len( right ):
        if left[0][i] < right[0][i] :
            out.append( left[0] )
            left.remove( left[0] )
        else:
            out.append( right[0] )
            right.remove( right[0] )
    if len( left ) == 0:
        out += right
    else:
        out += left
    return out
        
def dist(a, b):#a, b are 2-element arrays: 0=x,1=y
    return sqrt(pow( a[0]-b[0], 2 ) + pow( a[1]-b[1], 2 ) )
 
#Divide-and-conquor nearest neighbor 
def nearest_neighbor( points ):
    global min_distance
    min_distance=sys.maxsize
    # sort by the the x coordinate
    points=mergeSort( points, 0 )
    nearest_neighbor_recursion( points, 0 )
    write_file( outFileName, [ min_distance ])
    return min_distance   
    
def nearest_neighbor_recursion( points, medianX ):
    global rCount
    rCount=rCount+1
    LEN = len( points ) # Gonna be using this a lot
    
    # Base case: set min_distance for small arrays of 2 or 3 elements
    # Also sort by y
    if LEN <= 3:
        return baseCase( points, 1 )
    
    # Split the array for n/2
    middle=math.floor( LEN/2 )
    left=points[:middle]
    right=points[middle:]
    
    #Cases >3, set medianX
    medianX=points[middle][0]
    
    left = nearest_neighbor_recursion( left, medianX )
    right = nearest_neighbor_recursion( right, medianX )
    return mergeY( left, right, medianX )

def baseCase( points, p ): #brute force for length 2 or 3 with sort
    global min_distance
    global bcCount # For runtime analysis display
    LEN=len(points)
    for i in range( 0, LEN ):
        for j in range( i, LEN ):
            bcCount=bcCount+1
            curr = dist( points[i], points[j] )
            if curr and curr<min_distance:
                min_distance=curr
            if points[j][p]<points[i][p]:
                temp=points[j]
                points[j]=points[i]
                points[i]=temp
    return points

def mergeY( oldLeft, oldRight, medianX ):
    global min_distance
    global mCount # For runtime analysis display
    mCount=mCount+len( oldLeft )+len( oldRight )
    loX=math.floor( medianX - min_distance )
    hiX=math.ceil( medianX + min_distance )
    
    # Remove left elements that are out of range (can't contain a better min)
    left = []
    for point in oldLeft:
        if point[0] > loX and point[0] < hiX:
            left.append( point )
            
    # Remove right elements that are out of range (can't contain a better min)    
    right = []
    for point in oldRight:
        if point[0] > loX and point[0] < hiX:
            right.append( point )

    # Reassemble left and right, sorting by y coordinate
    out = []
    while len( left ) and len( right ):
        if left[0][1] < right[0][1] :
            out.append( left[0] )
            left.remove( left[0] )
        else:
            out.append( right[0] )
            right.remove( right[0] )
    if len( left ) == 0:
        out += right
    else:
        out += left
        
    # Try to find a better min using a linear method
    if len( out ) :# Gotta check this for the next instruction to work
        last=out[0]
        for i in range(1, len( out )):
            curr = dist( out[i], last )
            if curr and curr<min_distance:
                min_distance=curr
            last=out[i]
    return out
  
#Brute force version of the nearest neicghbor algorithm, O(n**2)
def brute_force_nearest_neighbor( points ):
    global bfCount # For runtime analysis display
    min=sys.maxsize
    LEN=len(points)
    curr=0
    for i in range( 0, LEN ):
        for j in range( i, LEN ):
            bfCount=bfCount+1;
            #print( 'checking %d %d' % (ia, ib) )
            curr = dist( points[i], points[j] )
            if curr and curr<min:
                min=curr
    write_file( outFileName, [ min ])
    return min;            

def read_file(filename):
    points=[]
    # File format 3.3
    # x1 y1
    # x2 y2
    # ...
    in_file=open(filename,'r')
    for line in in_file.readlines():
        line = line.strip()
        point_match=pointRE.match(line)
        if point_match:
            x = point_match.group(1)
            y = point_match.group(2)
            points.append([ float( x ), float( y ) ] )
    #print(points)
    return points
    
def write_file( filename, array ):
    file=open(filename,'w')
    for line in array:
        file.write( str( line ) ) 
    file.close()      
                
def main( filename,algorithm ):
    # Create outFileName based on input file name
    global outFileName
    outFileName=filename.split(".")[0]+"_distance.txt"

    #algorithm=algorithm[1:]
    points=read_file( filename )
    if algorithm =='dc':
        print("Divide and Conquer: ", nearest_neighbor(points))
    if algorithm == 'bf':
        print("Brute Force: ", brute_force_nearest_neighbor(points))
    if algorithm == 'both':
        print("Divide and Conquer: ", nearest_neighbor(points))
        print("Brute Force: ", brute_force_nearest_neighbor(points))
        
#     print("filename: ", filename)
#     n=len( points )
#     print( "n =", n )
#     print( )
#     start = time.time()
#     print("Divide and Conquer: ", nearest_neighbor(points))
#     print( "Recursive T(n) = %.2f + %.2fn + %.2fn" % ( rCount, bcCount/n, mCount/n ) )
#     end = time.time()
#     elapsed = end - start
#     print("time=", elapsed )
#     print( )
#     return
#     start = time.time()
#     print( "Brute Force: ", brute_force_nearest_neighbor( points ) )
#     print("Brute Force T(n) =", bfCount )
#     end = time.time()
#     elapsed = end - start
#     print("time=", elapsed )

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    if len(sys.argv[1]) < 2:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
    