import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
JINA_KEY = os.getenv("JINA_KEY")
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

# Fetch top technology news
url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    articles = response.json().get("articles", [])
    for article in articles[:5]:  # limit for testing
        link = article.get("url")
        title = article.get("title")

        if not link:
            continue

        print(f"\n🔹 Processing article: {title}\n")

        # --- Fetch full content using Jina Reader ---
        jina_url = f"https://r.jina.ai/{link}"
        headers = {"Authorization": f"Bearer {JINA_KEY}"}
        jina_response = requests.get(jina_url, headers=headers)

        if jina_response.status_code != 200:
            print("⚠️ Jina fetch failed:", jina_response.text)
            continue

        content = jina_response.text.strip()

        # --- Summarize content using OpenRouter ---
        ai_response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "mistralai/mistral-small-3.2-24b-instruct:free",
                "messages": [
                    {"role": "user", "content": f"Summarize this article:\n\n{content}"}
                ],
                "temperature": 0.2,
                "max_tokens": 300,
            },
            timeout=60,
        )

        if ai_response.status_code != 200:
            print("❌ OpenRouter error:", ai_response.text)
            continue

        try:
            ai_data = ai_response.json()
            summary = ai_data["choices"][0]["message"]["content"]
            print("🧠 Summary:\n", summary.strip())
        except Exception as e:
            print("❌ Failed to parse AI response:", e)
            print("RAW:", ai_response.text)

else:
    print("❌ NewsAPI request failed:", response.text)
