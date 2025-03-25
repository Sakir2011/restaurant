import uuid
class User:
    def __init__(self, first_name, last_name, phone_number, email, payment_method, user_type):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.payment_method = payment_method
        self.user_type = user_type
    def to_dict(self):
        return {
            "id": self.id,
            "first_name":  self.first_name,
            "last_name": self.last_name,
            "phone_number":self.phone_number,
            "email":self.email,
            "payment_method":self.payment_method,
            "user_type":self.user_type,
        }
    @staticmethod
    def from_dict(data):
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone_number=data["phone_number"],
            email=data["email"],
            payment_method=data["payment_method"],
            user_type=data["user_type"]
        )
        user.id=data["id"]
        return user
