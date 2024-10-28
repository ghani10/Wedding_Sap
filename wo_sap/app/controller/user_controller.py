from app.model.user import User
from app import db

class UserController:
    def create_user(self, username, email, password):

        """Membuat user baru dengan username, email, dan password.

        Args:
            username (str): Nama user yang akan dibuat.
            email (str): Email user yang akan dibuat.
            password (str): Password user yang akan dibuat.

        Returns:
            User: User yang telah dibuat.
        """
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(self, id):
        """Mengambil user berdasarkan ID.

        Args:
            id (int): ID user yang ingin diambil.

        Returns:
            User: User yang telah diambil.
        """
        return User.query.get(id)

    def update_user(self, user_id: int, username: str, email: str, password: str) -> User:
        """Update user by ID.

        Args:
            user_id (int): ID of the user to be updated.
            username (str): New username.
            email (str): New email.
            password (str): New password.

        Returns:
            User: Updated user.
        """
        user = self.get_user(user_id)
        if user:
            user.username = username
            user.email = email
            user.password = password
            db.session.commit()
            return user
        return None


    def delete_user(self, id: int) -> bool:
        """Delete user by ID.

        Args:
            id (int): ID of the user to be deleted.

        Returns:
            bool: True if successfully deleted, False if not.
        """
        user = self.get_user(id)

        if user is None:
            return False

        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return True
        
