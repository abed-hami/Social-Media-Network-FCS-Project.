from user import User
from graph import Graph


def main():

    print("Welcome to the FCS Social Network!")
    print("\nCreate and Visualize relations using our comprehensive application using NetworkX!")
    print("\nFell free to choose an option from our menu below")
    print("\nOur Control Menu:")
    
    Id=1
    
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
        print("18. Binary search by id")
        print("19. Binary search by name")
        print("-------------------------")
        print("GRAPH STATS/RECOMMENDATION ACTIONS:")
        print("20. View graph stats")
        print("21. Matuality based friends recommendation")
        print("22. Interests based friends recommendation")
        print("-------------------------")
        print("GRAPH VISUALIZATION:")
        print("23. View graph visualization")
        print("-------------------------")
        print("24. Exit")
        try:
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
               
            if choice==8:
                id1=int(input("Enter id of user to access the account: "))
                id2=int(input("Enter id of user you want to add: "))
                weight=int(input("Enter friendship weight: "))
                graph.add_friendship(id1,id2,weight)
                
            if choice==9:
                id1=int(input("Enter id of user to access the account: "))
                id2=int(input("Enter id of user you want to add"))
                graph.remove_friend(id1,id2)
                
            if choice==10:
                graph.print_graph()
               
            if choice==11:
                id=int(input("Enter Id of user to start BFS from: "))
                user=graph.binary_search_by_id(id)
                print(f"BFS starting from {user.name}: {graph.bfs(user)}")
                
            if choice==12:
                id=int(input("Enter Id of user to start DFS from: "))
                user=graph.binary_search_by_id(id)
                print(f"DFS starting from {user.name}: {graph.dfs(user)}")
                
            if choice==13:
                id1=int(input("Enter Id of user1 for Dijkstra: "))
                id2=int(input("Enter Id of user2 for Dijkstra: "))
                user1=graph.binary_search_by_id(id1)
                user2=graph.binary_search_by_id(id2)
                distance, path = graph.dijkstra(user1, user2)
                print(f"\nShortest path distance: {distance}")
                print(f"Path: {[user.name for user in path]}")
                
            if choice==14:
                components = graph.connected_components()
                print("\nConnected components in the graph:")
                for component in components:
                    print(component)
                
            if choice==15:
                print(f"\nGraph after sorting by name: {graph.sort_graph_by_name()}")
                
            if choice==16:
                print(f"\nGraph after sorting by Id number:{graph.sort_graph_by_id()}")
                
            if choice==17:
                print(f"\nGraph after sorting by friends number:{graph.sort_graph_by_friends()}")
                
            if choice==18:
                id=int(input("Enter id of user to access the account: "))
                user= graph.binary_search_by_id(id)
                print(f"Account with Id {id} is {user.name} and has:\ncontact info:{user.email}\nposts: {user.posts}\nand these interests:{user.interests} ")

            if choice==19:
                name=input("Enter name of the user you want to search: ")
                user=graph.binary_search_by_name(name)
                print(f"{name}'s account has:\ncontact info:{user.email}\nposts: {user.posts}\nand these interests:{user.interests} ")
                
            if choice==20:
                print(f"\n display stats {graph.display_statistics()}")
                
            if choice==21:
                print("recommended friends for each user based on matuality:")
                print(graph.recommend_friends_by_connection())
                
            if choice==22:
                print("recommended friends for each user based on common intersts:")
                print(graph.recommend_friends_by_interests())
            
            if choice==23:
                graph.visualize_graph()
                
            if(choice==24):
                break

            print("\ndo you want to continue?")
               
            answer=input("y/n")
            if(answer=="n"):
                break
            

        except Exception as e:
            print("Invalid input! Please enter a number")
        
if __name__ == "__main__":
    main()