def BFS(adj, source):
    """traverse the graph layer by layer
    you will have unreachable area if the graph is not fully connected

    Args:
        adj:dict(int, set(int)) -> adjacency list
        source:int -> starting node
    Returns:
        parent:dict(int, int) -> parenthood dict
        distance: dict(int, int) -> distance of every node to source
    """
    batch = [source]
    parent = {source: None}
    distance = {source: 0}

    while batch:
        new_batch = []
        for node in batch:
            # for each node in a batch
            # 1. add all it's neightbors 2. process distance 3. process parenthood
            for neighbor in adj[node]:
                if neighbor not in distance:  # don't process visited nodes
                    new_batch.append(neighbor)
                    distance[neighbor] = distance[node] + 1
                    parent[neighbor] = node
        batch = new_batch

    return parent, distance


# batch is conceptually clean, you could achieve the same exploration order
# by using FIFO queue
def BFS_q(adj, source):
    q = [source]
    parent = {source: None}
    distance = {source: 0}

    while q: # process 1 node at a iteration
        node = q.pop()
        for neighbor in adj[node]:
            if neighbor not in distance:
                q = [neighbor] + q
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1

    return parent, distance
