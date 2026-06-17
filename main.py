import logging
import config
from services import fetch_contacts, send_message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

def main():
    try:
        config.validate()
    except EnvironmentError as e:
        logger.error(e)
        raise SystemExit(1)

    logger.info("Buscando contatos no Supabase...")
    contacts = fetch_contacts()

    if not contacts:
        logger.warning("Nenhum contato encontrado na tabela.")
        return

    logger.info(f"{len(contacts)} contato(s) encontrado(s). Iniciando envio...")
    success = sum(send_message(contact) for contact in contacts)
    logger.info(f"Concluido: {success}/{len(contacts)} mensagens enviadas.")

if __name__ == "__main__":
    main()
