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

    