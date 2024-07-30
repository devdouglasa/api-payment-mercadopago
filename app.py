import os
from dotenv import load_dotenv


load_dotenv()


print(os.getenv("ACCESS_TOKEN_MERCADOPAGO"))

