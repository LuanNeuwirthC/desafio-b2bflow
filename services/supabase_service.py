import logging
from supabase import create_client
from models import Contact
import config

logger = logging.getLogger(__name__)

def fetch_contacts() -> list[Contact]:
    client = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
    response = (
        client.table("contacts")
        .select("name, phone")
        .limit(config.MAX_CONTACTS)
        .execute()
    )
    contacts = []
    for row in response.data:
        try:
            contacts.append(Contact.from_dict(row))
        except ValueError as e:
            logger.warning(e)
    return contacts
