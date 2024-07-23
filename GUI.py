import tkinter as tk


from graph import Graph
from user import User

class GUI:
    
    def __init__(self, root,graph):
        self.root = root
        self.root.geometry("900x500")
        self.root.title("Social Network FCS")
        self.graph = graph
        
        self.label = tk.Label(
            self.root, text="Welcome to our Social Network", font=('Arial', 18)
        )
        self.label.grid(row=0, column=0, padx=20, pady=20)  

   
        self.inputframe = tk.Frame(self.root)
        self.inputframe.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W) 

       
        label = tk.Label(self.inputframe, text="Enter your name:")
        label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name = tk.Entry(self.inputframe, width=15)
        self.name.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        label = tk.Label(self.inputframe, text="Enter your email:")
        label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.email = tk.Entry(self.inputframe, width=15)
        self.email.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    
        self.submit_button = tk.Button(self.inputframe, text="add user", command=self.submit_name)
        self.submit_button.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

    def submit_name(self):
        
        name = self.name.get()
        print(f"Name entered: {name}")

    def add_user(self):
        user_id = int(self.user_id_entry.get())
        user_name = self.user_name_entry.get()
        user_email = self.user_email_entry.get()
        user = User(user_id, user_name, user_email)
        

if __name__ == "__main__":
    root = tk.Tk()
    graph=Graph()
    app = GUI(root,graph)
    root.mainloop()
    
