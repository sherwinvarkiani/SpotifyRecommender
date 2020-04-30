from os import getenv

from dotenv import load_dotenv

load_dotenv()
ID = getenv ('ID',None)
SECRET = getenv('SECRET',None)
REDIRECTURI= getenv('REDIRECTURI', None)

assert ID
assert SECRET
assert REDIRECTURI
