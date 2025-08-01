import os

from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())


def get_api_key(service="default"):
    """
    Get API key for specified service.
    
    Args:
        service (str): Service name to get API key for. Options:
            - "default": API_KEY
            - "openai": OPENAI_API_KEY
            - "google": GOOGLE_API_KEY
            - "grok": GROK_API_KEY
            - "deepseek": DEEPSEEK_API_KEY
            - "fireworks": FIREWORKS_API_KEY
            - "weaviate": WCD_API_KEY
    
    Returns:
        str: API key for the specified service
    """
    load_env()
    key_mapping = {
        "default": "API_KEY",
        "local": "LOCAL_API_KEY",
        "openai": "OPENAI_API_KEY",
        "google": "GOOGLE_API_KEY",
        "grok": "GROK_API_KEY",
        "deepseek": "DEEPSEEK_API_KEY",
        "kimi": "KIMI_API_KEY",
        "zhipu": "ZHIPU_API_KEY",
        "bailian": "BAILIAN_API_KEY",
        "mistral": "MISTRAL_API_KEY",
        "fireworks": "FIREWORKS_API_KEY",
        "silicon": "SILICON_API_KEY",
        "weaviate": "WCD_API_KEY"
    }
    return os.getenv(key_mapping.get(service, "API_KEY"))

def get_base_url(service="default"):
    load_env()
    key_mapping = {
        "default": "BASE_URL",
        "local": "LOCAL_BASE_URL",
        "openai": "OPENAI_BASE_URL",
        "grok": "GROK_BASE_URL",
        "deepseek": "DEEPSEEK_BASE_URL",
        "kimi": "KIMI_BASE_URL",
        "zhipu": "ZHIPU_BASE_URL",
        "bailian": "BAILIAN_BASE_URL",
        "mistral": "MISTRAL_BASE_URL",
        "fireworks": "FIREWORKS_BASE_URL",
        "silicon": "SILICON_BASE_URL",
        "weaviate": "WCD_URL"
    }
    return os.getenv(key_mapping.get(service, "BASE_URL"))