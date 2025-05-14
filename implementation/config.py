import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL")
DB_NAME = os.getenv("DB_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-key-if-not-using-env")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
