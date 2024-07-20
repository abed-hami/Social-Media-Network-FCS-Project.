from collections import deque
import heapq


class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_user(self,user):
        #check for existance of the user in the graph
        if user not in self.graph:
            #adds the user as a key and the value is an empty list to add friends in
            self.graph[user]=[]
    
    def remove_user(self,user):
        #check for existance of the user in the graph
        if user in self.graph:
            #deletes the user from the graph
            del self.graph[user]
            #loops over the values aka friens list
            for friends in self.graph.values():
                #if the user is one of the friends it is removed
                if user in friends:
                    friends.remove(user)

    def add_friend(self,user1,user2):
        if user1 in self.graph and user2 in self.graph:
            #adds the user2 to the user1 friends list
            self.graph[user1].append(user2)
            #adds the user1 to the user2 friends list
            self.graph[user2].append(user1)
    
    def remove_friend(self,user1,user2):
        #check for existance of the users in the graph
        if user1 in self.graph and user2 in self.graph:
            #if the user2 is in the user1 friends list it is removed
            if user1 in self.graph[user2]:
                self.graph[user2].remove(user1)
            #if the user1 is in the user2 friends list it is removed
            if user2 in self.graph[user1]:
                self.graph[user1].remove(user2)

    def print_graph(self):
        friends_list=[]
        for user, friends in self.graph.items():
            for friend in friends:
                friends_list.append(friend.name)
            print(f"User {user.name} has friends: {friends_list}")
           

    def bfs(self,start_user):
        visited = set()
        queue = deque([start_user])
        traversal = []

        while queue:
            user_id = queue.popleft()
            if user_id not in visited:
                visited.add(user_id)
                traversal.append(user_id.id)
                queue.extend(self.graph[user_id])

        return traversal
    
    def dfs(self, start_user):
        visited = set()
        stack = [start_user]
        traversal = []

        while stack:
            user_id = stack.pop()
            if user_id not in visited:
                visited.add(user_id)
                traversal.append(user_id.id)
                stack.extend(self.graph[user_id])

        return traversal
    
    def dijkstra(self, start_user):
        distances = {user: float('infinity') for user in self.graph}
        distances[start_user] = 0
        priority_queue = [(0, start_user)]

        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)

            if current_distance > distances[current_user]:
                continue

            for neighbor in self.graph[current_user]:
                distance = current_distance + 1  
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
    def connected_components(self):
        visited = set()
        components = []

        for user in self.graph:
            if user not in visited:
                component = []
                stack = [user]
                while stack:
                    current_user = stack.pop()
                    if current_user not in visited:
                        visited.add(current_user)
                        component.append(current_user.name)
                        stack.extend(self.graph[current_user])
                components.append(component)

        return components
    
