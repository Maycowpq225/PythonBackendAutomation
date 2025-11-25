import os
from dotenv import load_dotenv

BASE_ENV_PATH = "env"

def load_environment():
    load_dotenv(os.path.join(BASE_ENV_PATH, "main.env"))

    env = os.getenv("ENV")

    env_file = f".env.{env}"
    full_path = os.path.join(BASE_ENV_PATH, env_file)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Environment file not found: {full_path}")

    load_dotenv(full_path)

    # return every variable in the file
    return dict(os.environ)

settings = load_environment()