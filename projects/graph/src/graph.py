"""
Simple graph implementation
"""

from collections import deque


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            raise IndexError("That vertex already exists")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = deque()
        # Put the starting vertex in our Queue
        q.append(starting_vertex_id)
        # Create an empty set of visited vertices
        visited = set()
        # While the queue is not empty....
        while len(q) > 0:
            # Dequeue the first node from the queue
            v = q.popleft()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.append(neighbor)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = deque()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.append(starting_vertex_id)
        # While the stack is not empty....
        while len(s) > 0:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.append(neighbor)

    # def dft_rec(self, node, visited=set(), path=[]):
    def dft_rec(self, node, path=[]):
        # semi-hybrid method that didn't have visited or path in the method init
        # s = deque()
        # visited = set()
        # s.append(node)

        # def depth_recursion():
        #     if len(s) <= 0:
        #         return
        #     vert = s.pop()
        #     if vert not in visited:
        #         print(vert)
        #         visited.add(vert)
        #         for peer in self.vertices[vert]:
        #             s.append(peer)
        #     depth_recursion()

        # depth_recursion()

        # Cleaner pure DFT, with path in the method init. Removed the visited
        # set, as it was just adding extra overhead for a small performance
        # gain at this scale.
        # Add our current node to the traversal path
        # visited.add(node)
        path += node

        # Cycle through all the peers for the current node...
        for peer in self.vertices[node]:
            # Then check if each has been visited yet. If not...
            # if peer not in visited:
            if peer not in path:
                # Kick off another recursive call with the peer.
                # self.dft_rec(peer, visited, path)
                self.dft_rec(peer, path)
        # At this point, we should have hit all the accessible nodes in the
        # graph, so return our traversal path.
        return path

    def bfs(self, start_node, dest_node):
        q = deque()
        visited = set()
        q.append([start_node])

        while len(q) > 0:
            path = q.popleft()
            vert = path[-1]
            if vert not in visited:
                if vert == dest_node:
                    return path
                visited.add(vert)
                for peer in self.vertices[vert]:
                    branch_path = list(path)
                    branch_path.append(peer)
                    q.append(branch_path)
        return deque()

    def dfs(self, start_node, dest_node):
        s = deque()
        visited = set()
        s.append([start_node])

        while len(s) > 0:
            path = s.pop()
            vert = path[-1]
            if vert not in visited:
                visited.add(vert)
                if vert == dest_node:
                    return path
                for peer in self.vertices[vert]:
                    branch_path = list(path)
                    branch_path.append(peer)
                    s.append(branch_path)
