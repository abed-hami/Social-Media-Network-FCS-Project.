from user import User
from graph import Graph

user1 = User(1, "Alice","alice@gmail.com")
user2 = User(2, "Bob","bob@gmail.com")
user3 = User(3, "Charlie","charlie@gmail.com")

graph = Graph()

graph.add_user(user1)
graph.add_user(user2)
graph.add_user(user3)

graph.add_friend(user1, user2)
graph.add_friend(user2, user3)

user1.add_interest("Reading")
user1.add_post("Hello World!")


