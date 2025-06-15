import requests
from config import DEEPSEEK_API_KEY, DEEPSEEK_ENDPOINT

def ask_deepseek(question, code_chunks, max_length = 30000):
    prompt = f"You are an AI assistant. Based on the following code, answer the question: '{question}'\n\n"
    total_length = len(prompt)
    for chunk in code_chunks:
        if total_length + len(chunk) > max_length:
            break
        prompt += chunk + "\n\n"
        total_length+=len(chunk)

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(DEEPSEEK_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
