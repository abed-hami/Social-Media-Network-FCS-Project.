class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_user(self,user):
        #check for existance of the user in the graph
        if user not in self.graph:
            #adds the user as a key and the value is an empty list to add friends in
            self.graph[user]=[]
    
    def remove_user(self,user):
        #check for existance of the user in the graph
        if user in self.graph:
            #deletes the user from the graph
            del self.graph[user]
            #loops over the values aka friens list
            for friends in self.graph.values():
                #if the user is one of the friends it is removed
                if user in friends:
                    friends.remove(user)

    def add_friend(self,user1,user2):
        if user1 in self.graph and user2 in self.graph:
            #adds the user2 to the user1 friends list
            self.graph[user1].append(user2)
            #adds the user1 to the user2 friends list
            self.graph[user2].append(user1)
    
    def remove_friend(self,user1,user2):
        #check for existance of the users in the graph
        if user1 in self.graph and user2 in self.graph:
            #if the user2 is in the user1 friends list it is removed
            if user1 in self.graph[user2]:
                self.graph[user2].remove(user1)
            #if the user1 is in the user2 friends list it is removed
            if user2 in self.graph[user1]:
                self.graph[user1].remove(user2)