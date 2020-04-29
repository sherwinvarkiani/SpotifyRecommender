from os import getenv

from dotenv import load_dotenv

load_dotenv()
ID = getenv ('ID',None)
SECRET = getenv('SECRET',None)

assert ID
assert SECRET
