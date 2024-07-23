from collections import deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from user import User
import typer

class Graph:

    def __init__(self):
        self.graph = {}

    def view_users(self):
        users_list=[]
        for user in self.graph.keys():
            users_list.append(user.name)
        return users_list

    def add_user(self, user):
        #if user doesn't exits in the graph add a dictionairy as a value
        if user not in self.graph:
            self.graph[user] = {}
            print("user added to the graph")
        else:
            print("user already in the graph")

    def remove_user(self, user):
        #if the user is in the graph delete it
        if user in self.graph:
            del self.graph[user]
            #loops over the values of the graph
            for friends in self.graph.values():
                #if the desired user is a friend with other users, remove that user
                if user in friends:
                    del friends[user]
            print("user was removed!")
        else:
            print("user not in the graph")

    def add_friendship(self, user1:User, user2:User, weight):
        #if both users are in the graph add them to each other and assign a weight to their relationship
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1][user2] = weight
            self.graph[user2][user1] = weight
            #if they are not friends, add them to the list of friends of each other
            if user1 not in user2.friends:
                user2.friends.append(user1.name)
            if user2 not in user1.friends:
                user1.friends.append(user2.name)
            else:
                 print(f"{user1.name} and {user1.name} are already friends")

            print("friendship was created between users!")
        else:
            print("one or both users not in the graph")

    def remove_friend(self, user1, user2):
        #if both users are in the graph remove them from each other
        if user1 in self.graph and user2 in self.graph:
            if user2 in self.graph[user1]:
                del self.graph[user1][user2]
            else:
                print(f"{user2.name} not in {user1.name}'s friends")
            if user1 in self.graph[user2]:
                del self.graph[user2][user1]
            else:
                 print(f"{user1.name} not in {user2.name}'s friends")

            print("friendship was removed between users")
        else:
            print("one or both users not in the graph")

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
    
    
    def sort_graph_by_name(self):
        # Create an empty list to store the users
        users = []

        # Loop through each user in the graph
        for user in self.graph:
            # Add the user to the list
            users.append(user)

        # Sort the list of users by their names
        users.sort(key=lambda x: x.name)
        return [user.name for user in users]

    def sort_graph_by_friends(self):
        # Create a list of users and their friend counts
        user_friend_counts = []
        for user, friends in self.graph.items():
            user_friend_counts.append((user.name, len(friends)))

        # Sort the list in ascending order based on friend counts
        user_friend_counts.sort(key=lambda x: x[1])
        
        return user_friend_counts
    
    def sort_graph_by_id(self):
        # Create a list of users and their IDs
        user_ids = []
        #loop over the keys of the dictionary
        for user in self.graph.keys():
            #append the user name alongside the id to the list
            user_ids.append((user.name, user.id))
        #sort it based on id 
        user_ids.sort(key=lambda x:x[1])
        return user_ids
    
    def binary_search_by_id(self, user_id):
        #get the sorted list by id
        sorted_list=self.sort_graph_by_id()
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid][1] == user_id:
                return sorted_list[mid][0]
            elif sorted_list[mid][1] < user_id:
                left = mid + 1
            else:
                right = mid - 1
        return "User doesn't exist"
    
    def binary_search_by_name(self, name):
        sorted_list=sorted(self.graph.keys(), key=lambda user: user.name.lower())
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid].name.lower() == name.lower():
                return (sorted_list[mid].id,sorted_list[mid].name,sorted_list[mid].email,sorted_list[mid].posts,sorted_list[mid].interests)
            elif sorted_list[mid].name.lower() < name.lower():
                left = mid + 1
            else:
                right = mid - 1
        return "User Not Found"
    
    def average_friends(self):
        #get the total sum of friendships
        sum_of_friends = sum(len(friends) for friends in self.graph.values())
        #get the number of users
        users_num = len(self.graph)
        #return the average
        return sum_of_friends/users_num
    
    def network_density(self):
        #get the total sum of friendships
        actual_connections = sum(len(friends) for friends in self.graph.values())
        #get the number of users
        users_num = len(self.graph)
        #get the number of possible connections using th network_density equation
        possible_connections= (users_num*(users_num)-1)/2
        return actual_connections/possible_connections
    
    def clustering_coeff(self, user):
        # Get a list of the user's friends
        friends = list(self.graph[user])
        
        # Initialize a variable to count the number of links between friends
        links = 0
        
        # Iterate over each friend
        for i in range(len(friends)):
            # Iterate over each friend that comes after the current friend
            for j in range(i + 1, len(friends)):
                # Check if friend j is a friend of friend i
                if friends[j] in self.graph[friends[i]]:
                    # If they are friends, increment the links count
                    links += 1
        
        # Calculate the total number of possible links between friends
        possible_links = len(friends) * (len(friends) - 1) / 2
        
        # If there are possible links, return the ratio of actual links to possible links
        if possible_links > 0:
            return links / possible_links
        # If there are no possible links, return 0
        else:
            return 0
        
    def average_clustering_coefficient(self):
        total_clustering = sum(self.clustering_coeff(user) for user in self.graph)
        return total_clustering / len(self.graph)
    
    def display_statistics(self):
        avg_friends = self.average_friends()
        density = self.network_density()
        avg_clustering = self.average_clustering_coefficient()
        print(f"Average number of friends per user: {avg_friends:.2f}")
        print(f"Network density: {density:.2f}")
        print(f"Average clustering coefficient: {avg_clustering:.2f}")

    def recommend_friends_by_connection(self):
        #loop over all the users in the graph
        for user in self.graph.keys():
            #store the user's friends in list
            friends = list(self.graph[user])
            #create a recommendation list
            recommendation=[]
            #iterate over each friend from the friends list
            for friend in friends:
                #iterate over the friend's friends
                for other_friends in self.graph[friend]:
                    #check if the other friend is not in the user's friends list and not  the user itself
                    if other_friends not in friends and other_friends!=user:
                        #append tuple having both the name and email in the list 
                        recommendation.append((other_friends.name,other_friends.email))
            print(f"{user.name}'s recommendation based on matuality: {recommendation} ") 
    
    def recommend_friends_by_interests(self):
        #loop over all the users in the graph
        for user in self.graph.keys():
            recommendation=[]
            #create a set containing the inetersts of the user
            user_interests=set(user.interests)
            #iterate over all the users in the graph
            for friend in self.graph.keys():
                #check if the user is not the current user
                if user!=friend:
                    #create interests that have te common interests they share
                    interests= user_interests.intersection(friend.interests)
                    #if similar interest occur append to the recommendation list
                    if interests:
                        recommendation.append((friend.name,friend.email))
            print(f"{user.name}'s recommendation based on interests: {recommendation} ") 
    
    def to_networkx_graph(self):
        # Create a new NetworkX graph object
        G = nx.Graph()

        # Iterate over each user in the self.graph data structure
        for user in self.graph:
            # Add a node to the NetworkX graph with the user's name
            G.add_node(user.name)
            
            # Iterate over each friend of the user and their corresponding weight
            for friend, weight in self.graph[user].items():
                # Add an edge to the NetworkX graph between the user and their friend with the given weight
                G.add_edge(user.name, friend.name, weight=weight)

        # Return the constructed NetworkX graph
        return G

    def visualize_graph(self):
        # Convert the self.graph data structure to a NetworkX graph object
        network = self.to_networkx_graph()
        
        # Calculate the positions of the nodes in the graph using the spring layout algorithm
        pos = nx.spring_layout(network)  
        
        # Create a new figure with a specified size
        plt.figure(figsize=(10, 8))

        # Draw the nodes in the graph with a specified size and color
        nx.draw_networkx_nodes(network, pos, node_size=1000, node_color='skyblue')
        
        # Draw the edges in the graph with a specified width
        nx.draw_networkx_edges(network, pos, width=2)
        
        # Draw the labels for the nodes in the graph with a specified font size and color
        nx.draw_networkx_labels(network, pos, font_size=12, font_color='black')
        
        # Get the edge attributes (weights) from the NetworkX graph
        edge_labels = nx.get_edge_attributes(network, 'weight')
        
        # Draw the edge labels in the graph with a specified font color
        nx.draw_networkx_edge_labels(network, pos, edge_labels=edge_labels, font_color='red')

        # Set the title of the graph
        plt.title("Social Network Graph")
        
        # Display the graph
        plt.show()