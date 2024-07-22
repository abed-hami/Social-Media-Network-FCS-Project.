class User:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
        self.interests=[]
        self.posts=[]
        self.friends=[]
        
    def add_post(self,post):
        self.posts.append(post)

    def add_interest(self,interest):
        self.posts.append(interest)

    def update_profile(self,name=None,email=None):
        if name:
            self.name = name
        if email:
            self.email=email

    