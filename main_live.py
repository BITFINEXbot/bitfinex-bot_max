import threading
from symbol_scanner import scan_symbols
from logic_engine import decide_trade
from trade_executor import execute_trade
from sentiment_analyzer import update_sentiment
from ai_brain import learn_from_trade
import web_interface
import time
import os

def run_bot():
    print("🚀 ULTIMATE_AI_TRADER (REAL) стартира...")
    while True:
        symbols = scan_symbols()

        for symbol in symbols:
            sentiment_score = update_sentiment(symbol)
            decision = decide_trade(symbol, sentiment_score)

            print(f"[ℹ️] Символ: {symbol} | Sentiment: {sentiment_score} | Решение: {decision}")
            if decision['action'] != 'HOLD':
                result = execute_trade(symbol, decision['action'], 5)
                if 'error' not in result:
                    learn_from_trade(symbol, decision, result)
                    print(f"[✅] Изпълнена сделка: {symbol} -> {decision['action']}")
                else:
                    print(f"[❌] Грешка при изпълнение на сделка: {result['error']}")

            time.sleep(1)
        time.sleep(10)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    flask_thread = threading.Thread(target=lambda: web_interface.app.run(
        host="0.0.0.0", port=port, debug=False, use_reloader=False))
    flask_thread.daemon = True
    flask_thread.start()

    run_bot()
