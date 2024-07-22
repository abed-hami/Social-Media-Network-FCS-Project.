from user import User
from graph import Graph

user1 = User(1, "Alice","alice@gmail.com")
user2 = User(2, "Bob","bob@gmail.com")
user3 = User(3, "Charlie","charlie@gmail.com")
user4 = User(4, "David","david@gmail.com")
user5 = User(5, "moe","moe@gmail.com")
user6 = User(6, "Alex","alex@gmail.com")
user7 = User(7, "Marwan","marwan@gmail.com")
user6.add_interest("reading")
user5.add_interest("writing")
user5.add_interest("reading")
user7.add_interest("writing")
user6.add_post("hello hope u are doing well")
       
graph = Graph()

        
graph.add_user(user1)
graph.add_user(user2)
graph.add_user(user3)
graph.add_user(user4)
graph.add_user(user6)
graph.add_user(user5)
graph.add_user(user7)
      
graph.add_friendship(user1, user4,1)
graph.add_friendship(user2, user3,1)
graph.add_friendship(user4, user2,4)
graph.add_friendship(user2, user1,1)
graph.add_friendship(user2, user5,4)
graph.add_friendship(user3, user6,4)  
graph.add_friendship(user7, user6,4)  
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


print(f"\nGraph after sorting by name: {graph.sort_graph_by_name()}")

print(f"\nGraph after sorting by friends number:{graph.sort_graph_by_friends()}")

print(f"\nGraph after sorting by id number:{graph.sort_graph_by_id()}")

print(f"\nbinary search by id is {graph.binary_search_by_id(2)}")
print(f"\nbinary search by name is {graph.binary_search_by_name('Bob')}")

print(f"\n display stats {graph.display_statistics()}")
print(graph.recommend_friends_by_connection())
print(graph.recommend_friends_by_interests())

graph.visualize_graph()