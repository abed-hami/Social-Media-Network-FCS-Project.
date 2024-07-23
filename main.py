from user import User
from graph import Graph


def main():

    print("Welcome to the FCS Social Network!")
    print("\nCreate and Visualize relations using our comprehensive application using NetworkX!")
    print("\nFell free to choose an option from our menu below")
    print("\nOur Control Menu:")
    id=1
    
    graph = Graph()
    while True:
        print("\nUSER ACTIONS:")
        print("1. Create a new user")
        print("2. Add a post for a user")
        print("3. Add an interest")
        print("4. Update user name")
        print("5. Update user email")
        print("-------------------------")
        print("GRAPH-USER ACTIONS:")
        print("6. Add user to the network")
        print("7. Remove user to the network")
        print("8. View users list")
        print("9. Add friendship between 2 users with wight")
        print("10. Remove friendship")
        print("11. Print users and their friends' list")
        print("-------------------------")
        print("GRAPH ALGORITHMS ACTIONS:")
        print("12. Use BFS")
        print("13. Use DFS")
        print("14. Use Dijkstra between 2 users")
        print("15. View connected components")
        print("-------------------------")
        print("GRAPH SORTING AND SEARCHING ACTIONS:")
        print("16. Sort graph by name")
        print("17. Sort graph by id")
        print("18. Sort graph by number of friends")
        print("19. User binary search by id")
        print("20. User binary search by name")
        print("-------------------------")
        print("GRAPH STATS/RECOMMENDATION ACTIONS:")
        print("21. View graph stats")
        print("22. View user stats")
        print("23. Matuality based friends recommendation")
        print("24. Interests based friends recommendation")
        print("-------------------------")
        print("GRAPH VISUALIZATION:")
        print("25. View graph visualization")
        print("-------------------------")
        print("26. Exit")

        choice = int(input("\nEnter a choice: "))
        if choice == 1:
            name = input("Name: ")
            email = input("Email: ")

            id+=1


        if(choice==26):
            break

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

if __name__ == "__main__":
    main()