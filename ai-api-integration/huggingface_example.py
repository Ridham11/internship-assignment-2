# huggingface_example.py
import os
import requests

# --- API Configuration ---
API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {os.environ['HUGGINGFACE_API_KEY']}",
    "Content-Type": "application/json"
}

# --- Query Function ---
def query_huggingface(prompt):
    """Query the Hugging Face Inference API with a prompt"""
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "MiniMaxAI/MiniMax-M2.5:novita",
        "max_tokens": 500,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e} | Response: {response.text}"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect. Check your internet connection."
    except KeyError:
        return f"Unexpected response format: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# --- Main Execution ---
if __name__ == "__main__":
    print("=== Hugging Face API Query ===")
    print("Model: MiniMaxAI/MiniMax-M2.5\n")

    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Hugging Face API...")

    response_text = query_huggingface(user_prompt)

    print("\n--- Response ---")
    print(response_text)