import os

API_ID = API_ID = 23455230

API_HASH = os.environ.get("API_HASH", "1740e4541ec18b9cdd3e5ff6f3687d46")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6823140439:AAEn8drCNncmt0UV8O8ojld6r3gbN7hWk3A")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6332321765))

LOG = -1002143990914

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6332321765").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


