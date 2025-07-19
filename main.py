from agents.rl_agent import train_rl_agent
from agents.sentiment_agent import get_sentiment_from_news
from backtester.backtest import run_backtest

def run_pipeline():
    model = train_rl_agent()
    sentiment = get_sentiment_from_news(["Apple stock sees strong demand..."])
    print(f"Sentiment: {sentiment}")

    run_backtest(model, sentiment)

if __name__ == "__main__":
    run_pipeline()
