import os
import re



def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def save_to_file(file_name, content):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"File saved: {file_name}")

def extract_themes(content):
    match = re.search(r"\[\s*(.*?)\s*\]", content, re.DOTALL)
    return f"[{match.group(1)}]" if match else content


def generate_response(client, prompt, max_tokens, model="gpt-4o-mini", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You're an assistant who specialises in summarising meetings."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

def format_time(hour, minute):
    if (minute < 60):
        return f"{hour:02d}:{minute:02d}"
    else:
        return f"{hour+1:02d}:{minute-60:02d}"
