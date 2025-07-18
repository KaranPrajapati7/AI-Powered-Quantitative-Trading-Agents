# 📊 AI-Powered Quantitative Trading Agents

An advanced AI trading system using **Reinforcement Learning** and **LLM-powered sentiment analysis** to simulate real-time stock trading. The project combines autonomous trading agents, financial news retrieval, and market data forecasting to build a smart, explainable trading workflow.

---

## 🚀 Project Overview

This project showcases an end-to-end autonomous trading agent system that makes intelligent trading decisions based on:

- **Reinforcement Learning (RL)** for price-based strategy formulation.
- **LLMs + Retrieval-Augmented Generation (RAG)** to assess sentiment from financial news.
- **Multi-Agent Architecture** for decomposing complex trading workflows.
- **Backtesting and Simulation** to measure performance over historical data.

It simulates buy/sell decisions, integrates real-time news sentiment, and provides dashboards to visualize performance, risk, and trade reasoning.

---

## 🧠 Core Features

- 🧮 **RL-based Trading Agent**: Trained with PPO/DQN to optimize trade returns.
- 📰 **Sentiment Agent**: Uses GPT + RAG to extract bullish/bearish sentiment from financial articles.
- 🔄 **Multi-Agent Workflow**: Modular agents for forecasting, trading, risk management, and sentiment integration.
- 📉 **Backtesting Engine**: Evaluates agent performance using historical data.
- 📊 **Dashboard**: Visualizes portfolio performance, sentiment signals, and executed trades.

---

## 📚 Tech Stack

| Category        | Tools/Libraries                                         |
|----------------|---------------------------------------------------------|
| Programming     | Python                                                  |
| RL Agents       | Stable-Baselines3, Gym, PyTorch                         |
| LLM Integration | OpenAI GPT-4, LangChain, Pinecone                       |
| Data Feeds      | Alpaca API, Yahoo Finance, NewsAPI                      |
| Backtesting     | Backtrader, QuantConnect (optional), Zipline (opt)     |
| Visualization   | Streamlit, Matplotlib, Plotly                          |
| Storage         | SQLite, CSV (for logs)                                 |

---

## 🏗️ System Architecture

```text
              +---------------------------+
              |  Financial News Crawler   |
              +---------------------------+
                        |
                        v
              +---------------------------+
              |    Sentiment Agent (LLM)  |
              |  - GPT-4 + RAG + Pinecone |
              +---------------------------+
                        |
          +-------------+--------------+
          |                            |
          v                            v
+--------------------+      +------------------------+
|  Price Forecaster  |      |    RL Trading Agent    |
| (LSTM/Prophet)      |-----> Uses price + sentiment |
+--------------------+      +------------------------+
                                    |
                                    v
                         +---------------------+
                         |  Risk Management     |
                         +---------------------+
                                    |
                                    v
                         +---------------------+
                         | Trade Execution/API |
                         +---------------------+
