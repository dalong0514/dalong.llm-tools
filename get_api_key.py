import os
import json

# get the api_key from config.json
def get_api_key():
    with open('/Users/Daglas/dalong.backup/api-key.json') as f:
        config = json.load(f)
    return config['openai_key']

if __name__ == "__main__":
    get_api_key()