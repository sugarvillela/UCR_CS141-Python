# Assignment2.py
# David Swanson 06/09/17
#
import sys
import re
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(\\d+)")

vertices=[]
edges=[]
e=[]#This is copied as-is from the file. Looks like: [[u, v, w],...]
             
def bfSingleSource( iSource, lowestIndex ):
    d=[]#distances
    for i in range( len( vertices ) ):
        d.append( float("inf") )
    d[ iSource ]=0
    for i in range( 0, len( vertices )-1 ):
        for j in range( 0, len( e ) ):
            u=e[j][0]-lowestIndex #lowestIndex=0 if zero-index
            v=e[j][1]-lowestIndex
            w=e[j][2]
            if d[u] + w < d[v]:
                d[v] = d[u] + w
    #check for negative cycle
    for j in range( 0, len( e ) ):
        u=e[j][0]-lowestIndex
        v=e[j][1]-lowestIndex
        w=e[j][2]
        if d[u] + w < d[v]:
            print( "Negative Cycle")
            return []
    return d
    
def BellmanFord(G):
    #decide if the file is zero-indexed or one-indexed
    #ignore negative min
    lowestIndex=float( "inf" )
    for i in range( len( vertices ) ):
        temp=min( lowestIndex, e[i][0], e[i][1] )
        if temp>=0:
            lowestIndex=temp
    H=[] 
    for i in range( len( vertices ) ):
        H.append( bfSingleSource( i, lowestIndex ) )
    return toPathPairs( H )

def FloydWarshall( Gtuple ):
    # Fill in your Floyd-Warshall algorithm here
    G=Gtuple[1]
    LEN=len( G )
    #Need to initialize the diagonal with zeroes
    for i in range( 0, LEN ):
        G[i][i]=0
    for k in range( 0, LEN ):
        for j in range( 0, LEN ):
            for i in range( 0, LEN ):
                G[i][j] = min( 
                            G[i][j],
                            G[i][k] + G[k][j]
                        )
    #check for negative cycle
    for i in range( 0, LEN ):
        if G[i][i]<0:
            print( "Negative Cycle")
            return []                       
    return toPathPairs( G )
    
def toPathPairs( G ):
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    pathPairs=[]
    for i in range( 0, len( G ) ):
        for j in range( 0, len( G ) ):
            if i != j:
                pathPairs.append( (( vertices[i], vertices[j] ), G[i][j]) )
    return pathPairs            

def readFile(filename):
    global vertices
    global edges
    global e
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))#make a list the size of the first number in line1
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            # Added the line below to copy file after line1 to a different list
            e.append( [ int( source ), int( sink ), int( weight ) ] )#build e to look exactly like file in
            # Changed line below from ...weight to ...int( weight ) because
            # weight comes from the file as a string
            edges[int(source)-1][int(sink)-1]=int( weight )
    #Debugging
    #for i in G:
        #print(i)
    return (vertices,edges)
                
def main( filename, algorithm ):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    if algorithm == 'b' or algorithm == 'B':
        print( "Bellman-Ford" )
        print( BellmanFord(G) )
    if algorithm == 'f' or algorithm == 'F':
        print( "Floyd-Warshall" )
        print( FloydWarshall(G) )
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
        FloydWarshall(G)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
