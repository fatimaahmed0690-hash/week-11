from database_manager import DatabaseManager
import hashlib
import pandas as pd

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, db: DatabaseManager) -> bool:
        if not db.get_user(self.username):
            db.add_user(self.username, self.password_hash)
            return True
        return False

    def authenticate(self, db: DatabaseManager) -> bool:
        user = db.get_user(self.username)
        return user and user['password_hash'] == self.password_hash


class SecurityIncident:
    def __init__(self, category, severity, status, description, incident_date):
        self.category = category
        self.severity = severity
        self.status = status
        self.description = description
        self.incident_date = incident_date

    @staticmethod
    def fetch_all(db: DatabaseManager):
        return db.fetch_incidents()


class Dataset:
    def __init__(self, data: list):
        self.data = pd.DataFrame(data)

    def to_csv(self, filename="dataset.csv"):
        self.data.to_csv(filename, index=False)

    def filter_by(self, column, value):
        return self.data[self.data[column] == value]


class ITTicket:
    def __init__(self, title, description, priority="Medium", status="Open"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }
