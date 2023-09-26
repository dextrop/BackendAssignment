from api.models import User
from api.lib.helperfns import hash_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class UserController:
    """
    Controller for handling user related operations.
    """

    def get_user(self, email):
        """
        Get a user object by the given email.

        Args:
            email (str): The email of the user.

        Returns:
            Users: A user object if found. None otherwise.
        """
        try:
            return User.objects.get(email=email)
        except ObjectDoesNotExist:
            return None

    def add_user(self, userInfo):
        """
        Create a new user with the given email, password and salt.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
            salt (str): The salt for hashing the password.

        Returns:
            Users: The created user object.
        """
        password = userInfo.get("password")
        hashed_password, salt = hash_password(password)
        userInfo["password"], userInfo["salt"] = hashed_password, salt
        return User.objects.create(**userInfo)

    def login(self, email, password):
        """
        Validate the login information provided by the user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            dict: Dictionary containing refresh and access tokens if user validation is successful. None otherwise.
        """
        user = self.get_user(email)
        if user is None:
            raise ValidationError("user does not exits")

        hashed_password, salt = hash_password(password, user.salt)
        if hashed_password != user.password:
            raise ValidationError("invalid password")

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def signup(self, userInfo):
        """
        Sign up a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            str: A success message if user signup is successful. None otherwise.
        """
        required_keys = ["name", "email", "password"]
        for key in required_keys:
            if not userInfo.get(key):
                raise ValidationError("Missing {} in signup request".format(key))


        if self.get_user(userInfo.get("email")) is not None:
            raise ValidationError("User Already Exits")

        self.add_user(userInfo)
        return "Signup successful, kindly login to start posting!"
