import logging
import requests
from models import Contact
import config

logger = logging.getLogger(__name__)

_BASE_URL = "https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"

def send_message(contact: Contact) -> bool:
    url = _BASE_URL.format(instance_id=config.ZAPI_INSTANCE_ID, token=config.ZAPI_TOKEN)
    headers = {
        "Content-Type": "application/json",
        "Client-Token": config.ZAPI_CLIENT_TOKEN,
    }
    payload = {
        "phone": contact.phone,
        "message": f"Olá, {contact.name} tudo bem com voce?",
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        logger.info(f"Mensagem enviada -> {contact.name} ({contact.phone})")
        return True
    except requests.HTTPError as e:
        logger.error(f"Erro HTTP [{e.response.status_code}] para {contact.name}: {e.response.text}")
        return False
    except requests.RequestException as e:
        logger.error(f"Erro de conexao para {contact.name}: {e}")
        return False
