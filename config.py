import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
AUDIO_DIR = ASSETS_DIR / "audio"
FRIENDS_CSV = ASSETS_DIR / "friends.csv"
GALI_FILE = ASSETS_DIR / "gali.txt"

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"
