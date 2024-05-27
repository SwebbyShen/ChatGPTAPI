from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "ft:gpt-3.5-turbo-1106:personal::8g7blAeY"

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "寺岡精工ビジネスサービス部の部長は誰ですか。",
        }
    ],
    max_tokens=50
)

print(response.choices[0].message.content)
