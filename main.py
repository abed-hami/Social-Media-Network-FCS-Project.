from user import User
from graph import Graph


def main():

    print("Welcome to the FCS Social Network!")
    print("\nCreate and Visualize relations using our comprehensive application using NetworkX!")
    print("\nFell free to choose an option from our menu below")
    print("\nOur Control Menu:")
    Id=10
    
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
        print("6. Remove user to the network")
        print("7. View users list")
        print("8. Add friendship between 2 users with wight")
        print("9. Remove friendship")
        print("10. Print users and their friends' list")
        print("-------------------------")
        print("GRAPH ALGORITHMS ACTIONS:")
        print("11. Use BFS")
        print("12. Use DFS")
        print("13. Use Dijkstra between 2 users")
        print("14. View connected components")
        print("-------------------------")
        print("GRAPH SORTING AND SEARCHING ACTIONS:")
        print("15. Sort graph by name")
        print("16. Sort graph by id")
        print("17. Sort graph by number of friends")
        print("18. User binary search by id")
        print("19. User binary search by name")
        print("-------------------------")
        print("GRAPH STATS/RECOMMENDATION ACTIONS:")
        print("20. View graph stats")
        print("21. View user stats")
        print("22. Matuality based friends recommendation")
        print("23. Interests based friends recommendation")
        print("-------------------------")
        print("GRAPH VISUALIZATION:")
        print("24. View graph visualization")
        print("-------------------------")
        print("25. Exit")

        choice = int(input("\nEnter a choice: "))
        if choice == 1:
            name = input("Name: ")
            email = input("Email: ")
            user=User(Id,name,email)
            graph.add_user(user)
            Id+=1
        if choice==2:
            id=int(input("Enter id of user to access the account: "))
            user= graph.binary_search_by_id(id)
            post = input("Enter post: ")
            user.add_post(post)
        if choice==3:
            id=int(input("Enter id of user to access the account: "))
            user= graph.binary_search_by_id(id)
            interest = input("Enter interest: ")
            user.add_interest(interest)
        if choice==4:
            id=int(input("Enter id of user to access the account: "))
            user= graph.binary_search_by_id(id)
            name=input("enter new name: ")
            user.update_name(name)
        if choice==5:
            id=int(input("Enter id of user to access the account: "))
            user= graph.binary_search_by_id(id)
            name=input("enter new email: ")
            user.update_email(email)
        if choice==6:
            id=int(input("Enter id of user to access the account: "))
            user= graph.binary_search_by_id(id)
            print("Are you sure you want to delete your account?")
            answer=input("\ny/n")
            if(answer=="y"):
                graph.remove_user(user)
        if choice==7:
            print(graph.view_users())
            print("do you want to continue?")
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==8:
            id1=int(input("Enter id of user to access the account: "))
            id2=int(input("Enter id of user you want to add"))
            weight=int(input("Enter friendship weight"))
            graph.add_friendship(id1,id2,weight)
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==9:
            id1=int(input("Enter id of user to access the account: "))
            id2=int(input("Enter id of user you want to add"))
            graph.remove_friend(id1,id2)
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==10:
            graph.print_graph()
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==11:
            id=int(input("Enter Id of user to start BFS from: "))
            user=graph.binary_search_by_id(id)
            print(f"BFS starting from {user.name}: {graph.bfs(user)}")
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==12:
            id=int(input("Enter Id of user to start DFS from: "))
            user=graph.binary_search_by_id(id)
            print(f"DFS starting from {user.name}: {graph.dfs(user)}")
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==13:
            id1=int(input("Enter Id of user1 for Dijkstra: "))
            id2=int(input("Enter Id of user2 for Dijkstra: "))
            user1=graph.binary_search_by_id(id1)
            user2=graph.binary_search_by_id(id2)
            print(f"Using Dijkstra algorithms: {graph.dijkstra(user1,user2)}" )
            answer=input("\ny/n")
            if(answer=="n"):
                break
        if choice==14:
            components = graph.connected_components()
            print("\nConnected components in the graph:")
            for component in components:
                print(component)
            answer=input("\ny/n")
            if(answer=="n"):
                break
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
        
    graph.add_friendship(1, 2,1)
    graph.add_friendship(2, 3,1)
    
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
    userss=graph.binary_search_by_id(2)
    print(f"\nbinary search by id is {userss.name}")
    print(f"\nbinary search by name is {graph.binary_search_by_name('Bob')}")

    print(f"\n display stats {graph.display_statistics()}")
    print(graph.recommend_friends_by_connection())
    print(graph.recommend_friends_by_interests())

    graph.visualize_graph()

if __name__ == "__main__":
    main()