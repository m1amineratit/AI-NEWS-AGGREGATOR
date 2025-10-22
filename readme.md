# AI-Powered News Aggregator

A Python script that fetches top technology news articles, extracts their content, and generates AI-powered summaries.

## Features

- Fetches latest technology news using NewsAPI
- Extracts full article content using Jina Reader API
- Generates concise summaries using Mistral AI model via OpenRouter
- Handles API errors gracefully with informative messages

## Prerequisites

- Python 3.6+
- `requests` library
- Active API keys for:
  - NewsAPI
  - Jina Reader
  - OpenRouter

## Installation

1. Clone this repository
2. Install required package:
```sh
pip install uv
uv venv venv
venv\scripts\activate
uv pip install -r requirements.txt
```

## Configuration

Create the following API keys and replace them in `main.py`:

- `NEWS_API_KEY`: Get from [NewsAPI](https://newsapi.org)
- `JINA_KEY`: Get from [Jina AI](https://jina.ai)
- `OPENROUTER_KEY`: Get from [OpenRouter](https://openrouter.ai)

## Usage

Run the script:
```sh
python main.py
```

The script will:
1. Fetch the top 5 technology news articles
2. Extract the full content of each article
3. Generate an AI-powered summary
4. Display results in the console with emoji indicators

## Output Format

- 🔹 Article title
- 🧠 AI-generated summary
- ⚠️ Warning messages (if any)
- ❌ Error messages (if any)

## Error Handling

The script includes error handling for:
- Failed API requests
- Invalid API responses
- JSON parsing errors
- Network timeouts

## Rate Limits

- NewsAPI: Depends on your plan
- Jina Reader: Check your subscription limits
- OpenRouter: Based on your account tier