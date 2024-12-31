from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23272158"))
API_HASH = getenv("API_HASH", "9c6b7311bf4b00c649674db048c52cbf")

BOT_TOKEN = getenv("BOT_TOKEN","6508386922:AAFLNzk3fMLRIUjcFGXtewk8QEJ9o0KSBfM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID","7575713445"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AgFjGt4AAzWubewyrf2i82Z-y92Kcr5bIxRf7J6BkyvlQB2qG0Rbg9XHQhJo48aLSKmjSsZaHUNZNSKLs-hwDSweyz992hqt0ou-_6JHj57c2ENBxcFZvbu0cL7jHntLkRpy16WVffBDUuLZUtQELuYeo8YEJcjlf1Z4BKFlWVVAIJJELcIp0XFTnLqyCHpEfeCEKIFOyOV-FULnz9B8M6oD7qJsdRgdfg3ylPttn6zFTlgfY8YzG7sZQXZxLLfkXV6NkVbz8EcnCyWiWq4kdg4eDFkvGAyuHqjzsOKmGCqTpDQg6-mTzgdz82FSP_A4dtaObMHNRWfLtADJzgqFoDGaU4DNIwAAAAHDjDalAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7575713445").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
