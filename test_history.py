# test_history.py
from openai import OpenAI
from datetime import datetime

DEEPSEEK_API_KEY = "sk-106446aace5344de8f57d2416d923d7d"

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def get_today_in_history():
    today = datetime.now()
    result = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是历史助手，回答简洁，每条一行，最多5条。"},
            {"role": "user", "content": f"{today.month}月{today.day}日历史上的重要事件"}
        ]
    )
    return result.choices[0].message.content

print(get_today_in_history())