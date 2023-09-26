import hashlib, binascii, os

def hash_password(password, salt=None):
    """
    Create a hashed password using provided password and salt.

    Args:
        password (str): The password string to be hashed.
        salt (str): The salt to be used for hashing the password.

    Returns:
        str: The hashed password.
        salt: the salt used for hashing password.
    """
    if not salt:
        salt = binascii.hexlify(os.urandom(8)).decode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('ascii'), 100000)
    return binascii.hexlify(pwdhash).decode('ascii'), salt