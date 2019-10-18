import os
import sys

graph = {}
file = sys.argv[1]
file_path = os.path.abspath(file)
f =open(file_path, "r")

#txt to graph with no cost
def TxtToGraph(path):
    for i in f:
        tmp = {}
        a = 3
        b = 5
        while(a<len(i) and b<len(i)):
            tmp[i[a]] = int(i[b][0])
            a = a+5
            b = b+5
            graph[i[0]] = tmp
    return graph

graph =  TxtToGraph(f)

no_cost_graph = {}
cost_graph = {}

for key,value in graph.items():
    tmp = []
    tmp_no_cost = {}
    for a,b in value.items():

        if (b != 0):
            tmp.append(a)
            tmp_no_cost[a] = int(b)
    no_cost_graph[key] = tmp
    cost_graph[key] = tmp_no_cost

#Breadth First Search
def bfs(graph, start, end):

    queue = [(start,[start])]
    visited = set()

    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)
        for node in graph[vertex]:
            if node == end:
                return path + [end]
            else:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))

#Depth First Search
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

#Uniform Cost Search
def ucs(graph,start,end,visited=[],distances={},predecessors={}):
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return path[::-1]

    if not visited: distances[start]=0

    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start

    visited.append(start)
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    return ucs(graph,closestnode,end,visited,distances,predecessors)

start = input("Please enter the start state : ")
goal = input("Please enter the goal state : ")

bfs_list = bfs(no_cost_graph,start,goal)
strBfs = ''.join(str(str1) for str1 in bfs_list)
print("BFS : ", end="")
print(*strBfs, sep=" - ")

dfs_list = dfs(no_cost_graph,start,goal)
strDfs = ''.join(str(str2) for str2 in dfs_list)
print("DFS : ", end="")
print(*strDfs, sep=" - ")

ucs_list = ucs(cost_graph,start,goal)
strUcs = ''.join(str(str3) for str3 in ucs_list)
print("UCS : ", end="")
print(*strUcs, sep=" - ")
