from user import User
from graph import Graph

user1 = User(1, "Alice","alice@gmail.com")
user2 = User(2, "Bob","bob@gmail.com")
user3 = User(3, "Charlie","charlie@gmail.com")
user4 = User(4, "David","david@gmail.com")
user5 = User(5, "moe","moe@gmail.com")
user6 = User(6, "Alex","alex@gmail.com")
       
graph = Graph()

        
graph.add_user(user1)
graph.add_user(user2)
graph.add_user(user3)
graph.add_user(user4)
graph.add_user(user6)
graph.add_user(user5)
      
graph.add_friend(user1, user4,1)
graph.add_friend(user2, user3,1)
graph.add_friend(user4, user2,4)
graph.add_friend(user2, user1,1)
graph.add_friend(user2, user5,4)
graph.add_friend(user3, user6,4)  
print("Graph after adding users and relationships:")
graph.print_graph()

        
bfs_traversal = graph.bfs(user1)
print("\nBFS Traversal starting from User 1:")
print(bfs_traversal)

       
dfs_traversal = graph.dfs(user1)
print("\nDFS Traversal starting from User 1:")
print(dfs_traversal)

       
distance, path = graph.dijkstra(user4, user2)
print(f"\nShortest path distance: {distance}")
print(f"Path: {[user.name for user in path]}")
        
components = graph.connected_components()
print("\nConnected components in the graph:")
for component in components:
    print(component)


graph.sort_graph_by_name()
print("\nGraph after sorting by name:")
graph.print_graph()

graph.sort_graph_by_friends()
print("\nGraph after sorting by friends number:")
graph.print_graph()