# from jose import jwt, JWTError, ExpiredSignatureError
# from dotenv import load_dotenv
# import os
# from datetime import datetime, timedelta, timezone

# load_dotenv()

# secret_key = os.getenv("SECRET_KEY")
# algorithm = os.getenv("ALGORITHM")

# if not secret_key:
#     raise ValueError("Secret key not found!")

# if not algorithm:
#     raise ValueError("Algorithm not found!")

# def create_token(user_data: dict, expiry_time: timedelta=timedelta(minutes=30)):
#     payload = user_data.copy()
#     payload["exp"] = datetime.now(timezone.utc) + expiry_time
#     payload["sub"] = str(user_data["id"])
    
#     token = jwt.encode(payload, secret_key, algorithm=algorithm)
#     return token

# def verify_token(token):
#     try:
#         check_token = jwt.decode(token, secret_key, algorithms=[algorithm])
#     except JWTError:
#         raise ValueError("JWT token error!")
#     except ExpiredSignatureError:
#         raise ValueError("token expired!")
    
#     return check_token


