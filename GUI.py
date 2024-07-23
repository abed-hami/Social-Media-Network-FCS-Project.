import tkinter as tk
from tkinter import messagebox


from graph import Graph
from user import User

class GUI:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph
        self.user_id = 1

        
        self.root.geometry("900x500")
        self.root.title("Social Network FCS")

        
        self.label = tk.Label(self.root, text="Welcome to our Social Network GUI", font=('Arial', 18))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)

      
        self.userframe = tk.Frame(self.root)
        self.userframe.grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)

        
        label = tk.Label(self.userframe, text="Enter your ID:")
        label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.id_entry = tk.Entry(self.userframe, width=20)  
        self.id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        
        label = tk.Label(self.userframe, text="Enter your name:")
        label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(self.userframe, width=20)  
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        
        label = tk.Label(self.userframe, text="Enter your email:")
        label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(self.userframe, width=20)  
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        
        self.add_button = tk.Button(self.userframe, text="Add User", command=self.add_user,width=17)
        self.add_button.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        
        self.search_button = tk.Button(self.userframe, text="Search By Id", command=self.search_user_id)
        self.search_button.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        self.bfs_button = tk.Button(self.userframe, text="BFS", command=self.bfs)
        self.bfs_button.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        self.dfs_button = tk.Button(self.userframe, text="DFS", command=self.dfs)
        self.dfs_button.grid(row=0, column=4, padx=10, pady=5, sticky=tk.W)

        self.search_button2 = tk.Button(self.userframe, text="Search By Name", command=self.search_user_name)
        self.search_button2.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

        self.update_button1 = tk.Button(self.userframe, text="Update name", command=self.update_name)
        self.update_button1.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)
        
        self.update_button2 = tk.Button(self.userframe, text="Update email", command=self.update_email)
        self.update_button2.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.detailsframe = tk.Frame(self.root)
        self.detailsframe.grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)

        
        label = tk.Label(self.detailsframe, text="Enter a post:")
        label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)  
        self.post_entry = tk.Entry(self.detailsframe, width=20)  
        self.post_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)  

        
        self.post_button = tk.Button(self.detailsframe, text="Add Post", command=self.add_post)
        self.post_button.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)  



        label = tk.Label(self.detailsframe, text="Enter an interest:")
        label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)  
        self.interest_entry = tk.Entry(self.detailsframe, width=20)  
        self.interest_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)  

        
        self.interest_button = tk.Button(self.detailsframe, text="Add Interest", command=self.add_interest)
        self.interest_button.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W) 

        self.recommendation_button = tk.Button(self.detailsframe, text="View Recommendations", command=self.recommendation)
        self.recommendation_button.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W) 

         

        self.friendsframe = tk.Frame(self.root)
        self.friendsframe.grid(row=5, column=0, padx=20, pady=10, sticky=tk.W)

        label = tk.Label(self.friendsframe, text="Enter first user:")
        label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)  
        self.user1_entry = tk.Entry(self.friendsframe, width=20)  
        self.user1_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)  

        label = tk.Label(self.friendsframe, text="Enter second user:")
        label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)  
        self.user2_entry = tk.Entry(self.friendsframe, width=20)  
        self.user2_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)  

        label = tk.Label(self.friendsframe, text="Enter weight:")
        label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)  
        self.weight_entry = tk.Entry(self.friendsframe, width=20)  
        self.weight_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W) 

        self.addfriend_button = tk.Button(self.friendsframe, text="Add Friendship", command=self.add_friendship)
        self.addfriend_button.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W) 

        self.removefriend_button = tk.Button(self.friendsframe, text="Remove Friendship", command=self.remove_friendship)
        self.removefriend_button.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W) 

        self.stats_button = tk.Button(self.friendsframe, text="Print Stats", command=self.print_stats)
        self.stats_button.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W) 

        self.print_button = tk.Button(self.friendsframe, text="Print graph", command=self.print_graph)
        self.print_button.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W) 

        self.sort_button = tk.Button(self.friendsframe, text="Sort graph", command=self.sort)
        self.sort_button.grid(row=2, column=4, padx=10, pady=5, sticky=tk.W) 

        self.components_button = tk.Button(self.friendsframe, text="Connected Components", command=self.connected_components)
        self.components_button.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        self.addfriend_button = tk.Button(self.friendsframe, text="Dijkstra", command=self.dijkstra)
        self.addfriend_button.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W) 
  
    def notification(self,message):
        messagebox.showinfo("Notification", message)

    def add_friendship(self):
        try:
            user1=int(self.user1_entry.get())
            user2=int(self.user2_entry.get())
            weight=int(self.weight_entry.get())
            self.graph.add_friendship(user1,user2,weight)
            self.notification("Friendship created")
        except Exception as e:
            self.notification("Error Creating Bond")

    def remove_friendship(self):
        try:
            user1=int(self.user1_entry.get())
            user2=int(self.user2_entry.get())
            self.graph.remove_friend(user1,user2)
            self.notification("Friendship removed")
        except Exception as e:
            self.notification("Error Creating Bond")

    def add_user(self):
        try:
            user_id = self.user_id
            user_name = self.name_entry.get()
            user_email = self.email_entry.get()
            user=User(user_id, user_name, user_email)
            self.graph.add_user(user)
            self.notification("user added successfully")
            self.user_id+=1
        except Exception as e:
            self.notification("error occured")
    
    def dijkstra(self):
        try:
            id1=int(self.user1_entry.get())
            id2=int(self.user2_entry.get())
            user1=graph.binary_search_by_id(id1)
            user2=graph.binary_search_by_id(id2)
            distance, path = graph.dijkstra(user1, user2)
            print(f"\nShortest path distance: {distance}")
            print(f"Path: {[user.name for user in path]}")
            self.notification(f"Shortest path distance: {distance}\nPath: {[user.name for user in path]}")
        except Exception as e:
            self.notification("error occured")
    
    def connected_components(self):
        try:
            components = self.graph.connected_components()
            print("\nConnected components in the graph:")
            for component in components:
                print(component)
            self.notification("success, check terminal")
        except Exception as e:
            self.notification("error occured")
    

    def search_user_id(self):
        try:
            id = int(self.id_entry.get())
            if int(self.id_entry.get())>0:
                result=self.graph.binary_search_by_id(id)
                print(f"Account with Id {id} is {result.name} and has:\ncontact info:{result.email}\nposts: {result.posts}\nand these interests:{result.interests} ")
                self.notification("user found check terminal")
            else:
                self.notification("enter Id")
            
        except Exception as e:
            self.notification("user not found")

    def search_user_name(self):
        try:
            
            user_name = self.name_entry.get().strip()
            
            if user_name:
                user=self.graph.binary_search_by_name(user_name)
                print(user_name)
                print(f"{user_name}'s account has:\ncontact info:{user.email}\nposts: {user.posts}\nand these interests:{user.interests} ")
                self.notification("user found check terminal")
            else:
                self.notification("enter name")
            
        except Exception as e:
            self.notification("user not found")

    def update_name(self):
        try:
            user_name = self.name_entry.get().strip()
            user_id=int(self.id_entry.get())
            user=self.graph.binary_search_by_id(user_id)
            if user_name:
                user.update_name(user_name)
                self.notification("name updated")
            else:
                self.notification("enter name")
            
        except Exception as e:
            self.notification("error occured")

    def print_graph(self):
        self.graph.print_graph()
        self.notification("graph was printed")

    def sort(self):
        print(f"\nGraph after sorting by name: {graph.sort_graph_by_name()}")
        print(f"\nGraph after sorting by friends num: {graph.sort_graph_by_friends()}")
        print(f"\nGraph after sorting by id: {graph.sort_graph_by_id()}")
        self.notification("sorted lists was printed")

    def print_stats(self):
        print(f"\n display stats {graph.display_statistics()}")
        self.notification("stats were printed")
    
    def recommendation(self):
        print("\nrecommended friends for each user based on matuality:")
        print(graph.recommend_friends_by_connection())

        print("\nrecommended friends for each user based on common intersts:")
        print(graph.recommend_friends_by_interests())

    def visualize(self):
        graph.visualize_graph()
        
    
    def bfs(self):
        try:
            user_id=int(self.id_entry.get())
            user=self.graph.binary_search_by_id(user_id)
            print(f"BFS starting from {user.name}: {graph.bfs(user)}")
            self.notification(f"BFS starting from {user.name}: {graph.bfs(user)}")
        except Exception as e:
            self.notification("enter Id")
    def dfs(self):
        try:
            user_id=int(self.id_entry.get())
            user=self.graph.binary_search_by_id(user_id)
            print(f"DFS starting from {user.name}: {graph.dfs(user)}")
            self.notification(f"DFS starting from {user.name}: {graph.dfs(user)}")
        except Exception as e:
            self.notification("enter Id")

    def update_email(self):
        try:
            user_email = self.email_entry.get().strip()
            user_id=int(self.id_entry.get())
            user=self.graph.binary_search_by_id(user_id)
            if user_email:
                user.update_email(user_email)
                self.notification("email updated")
            else:
                self.notification("enter email")
            
        except Exception as e:
            self.notification("error occured")
                
        
    def add_post(self):
        try:
            user_id = int(self.id_entry.get())
            user=self.graph.binary_search_by_id(user_id)
            post = self.post_entry.get()
            user.add_post(post)
            self.notification("post added successfully")
        except Exception as e:
            self.notification("error occured")

    def add_interest(self):
        try:
            user_id = int(self.id_entry.get())
            user=self.graph.binary_search_by_id(user_id)
            interest = self.interest_entry.get()
            user.add_interest(interest)
            self.notification("interest added successfully")
        except Exception as e:
            self.notification("error occured")

if __name__ == "__main__":
    root = tk.Tk()
    graph=Graph()
    app = GUI(root,graph)
    root.mainloop()
    
