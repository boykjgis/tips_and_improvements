from dotenv import load_dotenv
import os

load_dotenv()
USER_PW = os.getenv("user_pw")

username = input('Username')
password = input('Password')

print(f'Logging in as {username}')