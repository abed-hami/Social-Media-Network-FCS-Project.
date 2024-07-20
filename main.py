from user import User
from graph import Graph

user1 = User(1, "Alice","alice@gmail.com")
user2 = User(2, "Bob","bob@gmail.com")
user3 = User(3, "Charlie","charlie@gmail.com")
user4 = User(4, "David","david@gmail.com")

       
graph = Graph()

        
graph.add_user(user1)
graph.add_user(user2)
graph.add_user(user3)
graph.add_user(user4)

      
graph.add_friend(user1, user2)
graph.add_friend(user2, user3)
graph.add_friend(user3, user4)

        
print("Graph after adding users and relationships:")
graph.print_graph()

        
bfs_traversal = graph.bfs(user1)
print("\nBFS Traversal starting from User 1:")
print(bfs_traversal)

       
dfs_traversal = graph.dfs(user1)
print("\nDFS Traversal starting from User 1:")
print(dfs_traversal)

       
distances = graph.dijkstra(user1)
print("\nShortest distances from User 1 using Dijkstra's algorithm:")
for user, distance in distances.items():
    print(f"User {user.name}: {distance}")

        
