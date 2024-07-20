class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.friends=[]
        self.interests=[]
        self.posts=[]
        
    def add_post(self,post):
        self.posts.append(post)

    def add_interest(self,interest):
        self.posts.append(interest)