from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=10
)

def create_hash_password(password: str):
    if password is None:
        raise ValueError("Password is None!")
    password_hashing = pwd_context.hash(password)
    print(password_hashing)
    return password_hashing


def verify_hash_password(plain_password: str, hash_password: str):
    if plain_password is None or hash_password is None:
        raise ValueError("plain password or hash password is None")
    password_verify = pwd_context.verify(plain_password, hash_password)
    return password_verify

