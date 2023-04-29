import os

class Config:
    API_ID = int(os.getenv("API_ID", 7143337))
    API_HASH = os.getenv("API_HASH", '1afa55a5f3bf7058c843d1b290f79c49')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc')
