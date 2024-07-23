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
        print("post added!")

    def add_interest(self,interest):
        self.interests.append(interest)
        print("interest added!")

    def update_profile(self,name):
        self.name = name
        print("name updated successfully")
       

    def update_email(self,email):
        self.email = email
        print("email updated successfully")
    