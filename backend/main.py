import os
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    PORT = os.getenv('PORT', 8000)
    print(f"localhost working on port: {PORT}")