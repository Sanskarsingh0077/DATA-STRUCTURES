class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(adj, src,des, visited, product):
            if src in visited:
                return
            visited.add(src)

            if src == des:
                return product
            
            for v,val in adj[src]:
                res = dfs(adj,v,des,visited,product*val)
                if res is not None:
                    return res
            return None

        n = len(equations)
        adj = {}

        for i in range(n):
            u = equations[i][0]
            v = equations[i][1]

            val = values[i]

            if u not in adj:
                adj[u] = []

            if v not in adj:
                adj[v] = []

            adj[u].append((v,val))
            adj[v].append((u,1.0/val))

        result = []

        for query in queries:
            src, des = query

            ans = -1.0
            product = 1.0

            if src in adj:
                visited = set()
                res = dfs(adj, src, des, visited, product)
                if res is not None:
                    ans = res

            result.append(ans)

        return result

        '''
        Key Idea: Model the problem as a weighted graph
            •	Each variable (like a, b, c) is a node in a graph.
            •	Each equation a / b = 2.0 creates two directed edges:
            •	From a to b with weight 2.0
            •	From b to a with weight 1 / 2.0 = 0.5

            This allows us to represent relationships and their values as connections with weights.

        Step 1: Build the graph (Adjacency list)
            •	Use a dictionary (adj) where keys are variables (nodes).
            •	Each key maps to a list of tuples (neighbor, weight).
            •	For each equation u / v = val, add:
            •	(v, val) to adj[u]
            •	(u, 1/val) to adj[v]

        Example after building graph: adj = {
                                            'a': [('b', 2.0)],
                                            'b': [('a', 0.5), ('c', 3.0)],
                                            'c': [('b', 0.3333)]
                                            }

        Step 2: Answer queries with DFS
            •	For each query src / des, run Depth-First Search (DFS) on the graph:
            •	Start from src with a running product = 1.0
            •	Recursively explore neighbors, multiplying edge weights along the path
            •	Keep track of visited nodes to avoid infinite loops (cycles)
            •	If you reach des, return the current product (which is the answer)
            •	If no path found, return -1.0

        DFS details:
            •	dfs(adj, src, des, visited, product):
                •	If src == des, return product (found answer)
                •	If src is visited, return None (avoid cycles)
                •	Mark src as visited
                •	For each neighbor (v, val) of src:
                •	Recursively call DFS with updated product: product * val
                •	If recursive call returns a non-None value, propagate it upwards (stop search early)
                •	If no neighbor leads to des, return None

        Step 3: Collect and return results
            •	For each query, if src not in graph, answer is -1.0
            •	Otherwise, run DFS and set answer to the returned value if found
            •	Append answers to a result list
            •	Return the list after processing all queries



        '''

        #Short Solution


        '''
        def calcEquation(self, equations, values, queries):
            from collections import defaultdict
            
            # Build graph: node -> list of (neighbor, weight)
            graph = defaultdict(list)
            for (u, v), val in zip(equations, values):
                graph[u].append((v, val))
                graph[v].append((u, 1 / val))
            
            def dfs(src, dst, visited, product):
                if src not in graph or src in visited:
                    return -1.0
                if src == dst:
                    return product
                
                visited.add(src)
                for neighbor, weight in graph[src]:
                    result = dfs(neighbor, dst, visited, product * weight)
                    if result != -1.0:
                        return result
                return -1.0
            
            results = []
            for src, dst in queries:
                results.append(dfs(src, dst, set(), 1.0))
            
            return results
        '''