
# number of nodes
n =  12

#start node 
start = '0'

graph  = {
   '0' : ['1','9'],
   '1' : ['0', '8' ],
   '2' : ['3'],
   '3' : ['4','5','7'],
   '4' : [ '3'],
   '5' : [ '3', '6' ],
   '6' : ['5' ,'7'],
   '7' : ['3','6','8','10','11'],
   '8' : ['1','7','9'],
   '9' : ['0','8'],
   '10' : ['7','11' ],
   '11' : ['7' , '10'],
   '12' : []
}

visited = set();

def recursiveDfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for adjacent in graph[node]:
            recursiveDfs(visited,graph, adjacent)

print("Following is the Depth-First Search")
recursiveDfs(visited, graph, start)