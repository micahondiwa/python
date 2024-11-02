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

    while stack:
        node = stack.pop(0)
