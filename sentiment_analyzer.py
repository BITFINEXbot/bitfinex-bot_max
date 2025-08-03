from newsapi import NewsApiClient
from textblob import TextBlob
from config import NEWS_API_KEY

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def update_sentiment(symbol):
    symbol_map = {
        "tBTCUSD": "Bitcoin",
        "tETHUSD": "Ethereum",
        "tLTCUSD": "Litecoin",
        "tXRPUSD": "Ripple"
    }

    query = symbol_map.get(symbol, "crypto")

    try:
        articles = newsapi.get_everything(q=query, language='en', sort_by='publishedAt', page_size=5)
        sentiments = []

        for article in articles["articles"]:
            title = article.get("title", "")
            description = article.get("description", "")
            content = f"{title}. {description}"

            polarity = TextBlob(content).sentiment.polarity
            sentiments.append(polarity)

        if sentiments:
            avg_sentiment = sum(sentiments) / len(sentiments)
            return avg_sentiment
        else:
            return 0.0

    except Exception as e:
        print(f"[❌] Грешка при sentiment анализа: {e}")
        return 0.0
