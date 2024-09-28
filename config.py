import os

API_ID = API_ID =  23713783

API_HASH = os.environ.get("API_HASH", "2daa157943cb2d76d149c4de0b036a99")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7106709057:AAEDzg7JSl0lTC-Nc5kcyKen6gYWLiywMdM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5487643307))

LOG = -1002169361625,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [5219193259,1327415906]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5487643307").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


