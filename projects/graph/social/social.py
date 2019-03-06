import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        # print(possibleFriendships[:])
        random.shuffle(possibleFriendships)
        # print(possibleFriendships[:20])
        # print(len(possibleFriendships))
        for f in possibleFriendships[:numUsers * avgFriendships]:
            # self.friendships[f[0]].add(f[1])
            self.addFriendship(f[0], f[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # DFS shenanigans
        # s = deque()
        # s.append([userID])

        # while len(s) > 0:
        #     path = s.pop()
        #     vert = path[-1]
        #     if vert not in visited:
        #         visited[vert] = path
        #         for friend in self.friendships[vert]:
        #             branch_path = list(path)
        #             branch_path.append(friend)
        #             s.append(branch_path)

        q = deque()
        q.append([userID])

        while len(q) > 0:
            path = q.popleft()
            vert = path[-1]
            if vert not in visited:
                visited[vert] = path
                for friend in self.friendships[vert]:
                    branch_path = list(path)
                    branch_path.append(friend)
                    q.append(branch_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("Friendships:")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Connections:")
    print(connections)
