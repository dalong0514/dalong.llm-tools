import json

finename = '/Users/Daglas/dalong.backup/api-key.json'

# get the api_key from config.json
def openai_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['openai_key']

def claude_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['claude_key']

def gemini_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['gemini_key']

def ai302_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['ai302_key']

def fireworks_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['fireworks_key']

def deepseek_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['deepseek_key']

def zhipu_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['zhipu_key']

def qwen_api_key():
    with open(finename) as f:
        config = json.load(f)
    return config['qwen_key']

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

if __name__ == "__main__":
    openai_api_key()