def find_reachable_vertex(graph, n):
    def dfs(v, visited):
        stack = [v]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    # Step 1: Check the first vertex and see if we can reach all vertices
    visited = [False] * n
    dfs(0, visited)
    
    # If not all vertices are reachable, return -1
    if not all(visited):
        return -1
    
    # Step 2: Check if all vertices can reach the first vertex
    # Create a reversed graph
    reversed_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            reversed_graph[v].append(u)
    
    visited = [False] * n
    dfs(0, visited)
    
    if all(visited):
        return 1  # Return 1-based index of the vertex
    else:
        return -1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    k = int(data[0])  # number of graphs
    results = []
    index = 1

    for _ in range(k):
        n, m = map(int, data[index].split())
        index += 1
        
        # Create the graph as an adjacency list
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, data[index].split())
            graph[u - 1].append(v - 1)  # Convert to 0-based indexing
            index += 1
        
        result = find_reachable_vertex(graph, n)
        results.append(result)

    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()
