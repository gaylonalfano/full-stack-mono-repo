import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

SECRET_FROM_SETTINGS = os.getenv("SECRET_FROM_DOTENV")
# print(SECRET_FROM_SETTINGS)  # works!
