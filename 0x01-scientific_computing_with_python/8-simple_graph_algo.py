'''8-simple_graph_algo.py module'''

""" 
Implements both bfs and dfs
algorithms on a simple graph
"""

graph = {
    "a": ["b", "d"],
    "b": [],
    "c":[],
    "d": ["e", "g"],
    "e":["c"],
    "f":[],
    "g":['f']
}

def dfs(graph, source):
    stack = []
    stack.append(source)

    while stack:
        node = stack.pop(-1)
        print(node)
        for neigbour in graph[node]:
            stack.append(neigbour)

dfs(graph, "a")

def bfs(graph, source):
    queue = []
    queue.append(source)

    while queue:
        node = queue.pop(0)
        print(node)
        for neigbour in graph[node]:
            queue.append(neigbour)

bfs(graph, "a")


# copper['food'] = 'hay'
# del copper['age']
# for i in copper.values():
#     print(i)

# for i, j in copper.items():
#     print(f'{i}: {j}')