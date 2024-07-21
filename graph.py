from collections import deque
import heapq

class Graph:
    
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        #if user doesn't exits in the graph add a dictionairy as a value
        if user not in self.graph:
            self.graph[user] = {}

    def remove_user(self, user):
        #if the user is in the graph delete it
        if user in self.graph:
            del self.graph[user]
            #loops over the values of the graph
            for friends in self.graph.values():
                #if the desired user is a friend with other users, remove that user
                if user in friends:
                    del friends[user]

    def add_friend(self, user1, user2, weight):
        #if both users are in the graph add them to each other and assign a weight to their relationship
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1][user2] = weight
            self.graph[user2][user1] = weight

    def remove_friend(self, user1, user2):
        #if both users are in the graph remove them from each other
        if user1 in self.graph and user2 in self.graph:
            if user2 in self.graph[user1]:
                del self.graph[user1][user2]
            if user1 in self.graph[user2]:
                del self.graph[user2][user1]

    def print_graph(self):
        #prints users and their friends list
        for user, friends in self.graph.items():
            friends_list = [friend.name for friend in friends]
            print(f"User {user.name} has friends: {friends_list}")

    def bfs(self, start_user):
        #create a set to hold the visited elements
        visited = set()
        #create a double ended quueque
        queue = deque([start_user])
        #create a list for teh traversed users
        traversal = []

        while queue:
            #deque a user from the queue
            user = queue.popleft()
            #if the dequed user is not vistied before
            if user not in visited:
                #add it to the vistied users
                visited.add(user)
                #add it to the traversed list
                traversal.append(user.id)
                #add the neighbors of the user to the queue to continue
                queue.extend(self.graph[user].keys())
        
        return traversal

    def dfs(self, start_user):
        visited = set()
        #create a list to hold the nodes as a stack
        stack = [start_user]
        traversal = []

        while stack:
            #pop a user from the satck
            user = stack.pop()
            #check if it is not visited 
            if user not in visited:
                #if not add it to the visited set
                visited.add(user)
                #add the id of the user to the travesed list
                traversal.append(user.id)
                #add the neighbors of the user to the stack to continue
                stack.extend(self.graph[user].keys())

        return traversal

    def connected_components(self):
        visited = set()
        components = []
        #loop the users in the graph
        for user in self.graph:
            #if the user is not visited before
            if user not in visited:
                #create a component for it
                component = []
                #create a stack that stores that user
                stack = [user]
                while stack:
                    #pop a user and store in current_user
                    current_user = stack.pop()
                    #if the current user is not visited before
                    if current_user not in visited:
                        #add it to the visited set
                        visited.add(current_user)
                        #add the id of the current user to the component
                        component.append(current_user.name)
                        #add the neighbors of the current user to the stack to continue
                        stack.extend(self.graph[current_user].keys())
                #add the component to the components list
                components.append(component)

        return components

    def dijkstra(self, start_user, end_user):
        # Check if the start and end users exist in the graph
        if start_user not in self.graph or end_user not in self.graph:
            # If not, return infinity as the distance and an empty path
            return float('inf'), []

        # Initialize the distances dictionary with infinity for all users
        distances = {user: float('inf') for user in self.graph}
        
        # Set the distance of the start user to 0
        distances[start_user] = 0
        
        # Initialize the previous nodes dictionary to keep track of the shortest path
        previous_nodes = {user: None for user in self.graph}
        
        # Create a priority queue with the start user and a distance of 0
        priority_queue = [(0, start_user)]

        # Continue the process until the priority queue is empty
        while priority_queue:
            # Extract the user with the minimum distance from the priority queue
            current_distance, current_user = heapq.heappop(priority_queue)

            # If the extracted distance is greater than the current distance, skip it
            if current_distance > distances[current_user]:
                continue

            # Iterate over the neighbors of the current user
            for neighbor, weight in self.graph[current_user].items():
                # Calculate the distance to the neighbor
                distance = current_distance + weight
                
                # If the calculated distance is less than the current distance, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_user
                    # Add the neighbor to the priority queue
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Build the shortest path from the end user to the start user
        path = []
        current_node = end_user
        while previous_nodes[current_node] is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.insert(0, start_user)

        # Return the shortest distance and the shortest path
        return distances[end_user], path