from models.User import User
from repository.UserRepository import UserRepository


repository = UserRepository()

user = User("Sakir","Quliyev","625439","salam.babagmail.com","Kartnan","Admin")
repository.add_user(user)
print(repository.read_all_users())