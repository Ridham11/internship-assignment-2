# ollama_example.py
import requests
import os

# --- API Configuration ---

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

# --- Query Function ---
def query_ollama(prompt):
    """Query the local Ollama model with a prompt"""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        return result["response"]

    except requests.exceptions.ConnectionError:
        return "Error: Ollama is not running. Please start Ollama first."
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e} | Response: {response.text}"
    except KeyError:
        return f"Unexpected response format: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# --- Main Execution ---
if __name__ == "__main__":
    print("=== Ollama Local API Query ===")
    print(f"Model: {MODEL_NAME}\n")

    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Ollama API...")

    result = query_ollama(user_prompt)

    print("\n--- Response ---")
    print(result)