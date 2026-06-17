import os
from dotenv import load_dotenv

load_dotenv()

_REQUIRED = [
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "ZAPI_INSTANCE_ID",
    "ZAPI_TOKEN",
    "ZAPI_CLIENT_TOKEN",
]

def validate():
    missing = [key for key in _REQUIRED if not os.getenv(key)]
    if missing:
        raise EnvironmentError(f"Variaveis de ambiente ausentes: {', '.join(missing)}")

SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
ZAPI_INSTANCE_ID: str = os.getenv("ZAPI_INSTANCE_ID", "")
ZAPI_TOKEN: str = os.getenv("ZAPI_TOKEN", "")
ZAPI_CLIENT_TOKEN: str = os.getenv("ZAPI_CLIENT_TOKEN", "")

MAX_CONTACTS: int = 3
