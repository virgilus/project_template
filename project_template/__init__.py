from os.path import join, dirname
from dotenv import load_dotenv

# Loading environment variables
# So all your modules have access to the same variables
env_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)
