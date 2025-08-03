import os

def learn_from_trade(symbol, decision, result):
    os.makedirs("logs", exist_ok=True)
    with open("logs/trades.log", "a") as f:
        f.write(f"{symbol} | {decision['action']} | Result: {str(result)}\n")
