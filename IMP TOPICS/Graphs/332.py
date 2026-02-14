class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itnry = defaultdict(list)

        for u, v in sorted(tickets, reverse = True):
            itnry[u].append(v)

        res = []

        def dfs(node):
            while itnry[node]:
                dfs(itnry[node].pop())

            res.append(node)

        dfs("JFK")
        res.reverse()

        return res




        '''
        # make graph by making adjacency list
        ticket_graph = {}

        for u,v in tickets:
            if u not in ticket_graph:
                ticket_graph[u] = []
            
            ticket_graph[u].append(v)

        # Sort dict values so that can get lexical
        for node in ticket_graph:
            ticket_graph[node].sort()
        
        final_itinerary = [] # Answers will be stored in this
        no_of_tickets = len(tickets)

        def dfs(from_loc: str, path: List[str]):
            nonlocal final_itinerary
            path.append(from_loc)

            if len(path) == no_of_tickets + 1:
                final_itinerary = path[:]
                return True

            # Explore neighbors : use .get(key, default_val) if key present return val , else return default_val
            neighbors = ticket_graph.get(from_loc, [])

            for i in range(len(neighbors)):
                to_city = neighbors[i]

                # avoid cycle by backtracking
                remove = neighbors.pop(i) #remove
                if dfs(to_city, path): #explore
                    return True

                neighbors.insert(i, remove) # put back

            path.pop() # If not possible
            return False
        
        dfs("JFK", []) # Start DFS form JFK
        return final_itinerary

        '''