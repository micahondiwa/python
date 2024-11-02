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

    node = stack.pop(-1)
    print(node)
    for neigbour in graph[node]:
        stack.append(neigbour)