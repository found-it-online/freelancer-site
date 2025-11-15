from openai import OpenAI
import os
import sys

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

prompt = " ".join(sys.argv[1:]) or "Say hello."

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
)

print(resp.choices[0].message.content)
