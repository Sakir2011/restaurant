import json
from pathlib import Path

from models.User import User
class UserRepository:
    def __init__(self, db_path="db/users.json"):
        self.file = Path(db_path)
        self.file.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.exists():
            self.file.write_text("[]")


    def read_all_users(self):
        with self.file.open("r") as f:
            data = json.load(f)
            return [User.from_dict(u) for u in data]

    def write_all_users(self, user_list):
        data = [u.to_dict() for u in user_list]
        print("Writing data:", data)
        with self.file.open("w") as f:
            json.dump(data, f, indent=4)


    def add_user(self, user):
        users = self.read_all_users()
        users.append(user)
        self.write_all_users(users)


    def find_by_email(self, email):
        users = self.read_all_users()
        for user in users:
            if user.email == email:
                return user
        print("User not found")
        return None

    def delete_user(self, user):
        users = self.read_all_users()
        users = [u for u in users if u.email != user.email]
        self.write_all_users(users)