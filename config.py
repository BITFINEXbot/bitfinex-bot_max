
import os
import sys

API_KEY = os.getenv("44ae4009463e22aeb1ff314117c9141e74601ac57e0")
API_SECRET = os.getenv("2bfeff8dcfe81cb993d498aa8b7685fcecb6ff23da6")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "1d4f3fff3f074e4b8009ed96d45439d7")

STOP_LOSS_PERCENT = 0.02
TAKE_PROFIT_PERCENT = 0.04

# Проверка дали ключовете са налични
if not API_KEY or not API_SECRET:
    print("❌ Липсва BITFINEX_API_KEY или BITFINEX_API_SECRET. Провери ENV променливите в Render.")
    sys.exit(1)
