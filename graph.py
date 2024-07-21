from collections import deque
import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = {}

    def remove_user(self, user):
        if user in self.graph:
            del self.graph[user]
            for friends in self.graph.values():
                if user in friends:
                    del friends[user]

    def add_friend(self, user1, user2, weight):
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1][user2] = weight
            self.graph[user2][user1] = weight

    def remove_friend(self, user1, user2):
        if user1 in self.graph and user2 in self.graph:
            if user2 in self.graph[user1]:
                del self.graph[user1][user2]
            if user1 in self.graph[user2]:
                del self.graph[user2][user1]

    def print_graph(self):
        for user, friends in self.graph.items():
            friends_list = [friend.name for friend in friends]
            print(f"User {user.name} has friends: {friends_list}")

    def bfs(self, start_user):
        visited = set()
        queue = deque([start_user])
        traversal = []

        while queue:
            user = queue.popleft()
            if user not in visited:
                visited.add(user)
                traversal.append(user.id)
                queue.extend(self.graph[user].keys())

        return traversal

    def dfs(self, start_user):
        visited = set()
        stack = [start_user]
        traversal = []

        while stack:
            user = stack.pop()
            if user not in visited:
                visited.add(user)
                traversal.append(user.id)
                stack.extend(self.graph[user].keys())

        return traversal

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
                        stack.extend(self.graph[current_user].keys())
                components.append(component)

        return components

    def dijkstra(self, start_user, end_user):
        if start_user not in self.graph or end_user not in self.graph:
            return float('inf'), []

        distances = {user: float('inf') for user in self.graph}
        distances[start_user] = 0
        previous_nodes = {user: None for user in self.graph}
        priority_queue = [(0, start_user)]

        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)

            if current_distance > distances[current_user]:
                continue

            for neighbor, weight in self.graph[current_user].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_user
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current_node = end_user
        while previous_nodes[current_node] is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.insert(0, start_user)

        return distances[end_user], path
