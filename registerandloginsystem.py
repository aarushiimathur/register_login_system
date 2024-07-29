import csv

class LoginSystem:
    def __init__(self, filename='users.csv'):
        self.users = {}
        self.logged_users = set()
        self.filename = filename
        self.mapping = {
            "a": "i", "b": "l", "c": "q", "d": "f", "e": "z", "f": "s",
            "g": "a", "h": "g", "i": "e", "j": "p", "k": "w", "l": "o",
            "m": "v", "n": "u", "o": "b", "p": "j", "q": "k", "r": "n",
            "s": "x", "t": "d", "u": "h", "v": "y", "w": "t", "x": "m",
            "y": "r", "z": "c"
        }
        self.load_users()

    def encrypt(self, password):
        return ''.join(self.mapping.get(char, char) for char in password)

    def register(self, username, password):
        if username in self.users:
            print("User already exists")
        else:
            encrypted_password = self.encrypt(password)
            self.users[username] = encrypted_password
            self.save_users()
            print("User registered successfully")

    def login(self, username, password):
        if username not in self.users:
            print("User isn't in the system")
        else:
            encrypted_password = self.encrypt(password)
            if self.users[username] != encrypted_password:
                print("Password doesn't match")
            else:
                self.logged_users.add(username)
                print("User logged in successfully")

    def sign_out(self, username):
        if username not in self.users:
            print("User is not in the system")
        elif username not in self.logged_users:
            print("User is not logged in")
        else:
            self.logged_users.remove(username)
            print("User signed out successfully")

    def save_users(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for username, password in self.users.items():
                writer.writerow([username, password])

    def load_users(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                self.users = {rows[0]: rows[1] for rows in reader}
        except FileNotFoundError:
            self.users = {}

if __name__ == "__main__":
    system = LoginSystem()
    
    while True:
        action = input("Choose an action: register, login, sign_out, or quit: ").strip().lower()
        if action == "quit":
            break
        elif action == "register":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            system.register(username, password)
        elif action == "login":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            system.login(username, password)
        elif action == "sign_out":
            username = input("Enter username: ").strip()
            system.sign_out(username)
        else:
            print("Invalid action. Please choose again.")
