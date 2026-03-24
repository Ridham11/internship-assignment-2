# multi_api_query.py
# Multi-API Query Program with conversation history and error retry logic

import requests
import cohere
import groq
import os
import time

# --- API Configuration ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Initialize clients
groq_client = groq.Groq(api_key=GROQ_API_KEY)
cohere_client = cohere.ClientV2(COHERE_API_KEY)

# Conversation history 
conversation_history = []

#  Error Retry Logic with Backoff 
def retry_with_backoff(func, retries=3, delay=2):
    """Retry a function with exponential backoff"""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt < retries - 1:
                wait = delay * (2 ** attempt)
                print(f"  Attempt {attempt + 1} failed. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                return f"Error after {retries} attempts: {str(e)}"

# --- Individual Query Functions ---
def query_groq(prompt):
    """Query Groq API"""
    def call():
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    return retry_with_backoff(call)

def query_cohere(prompt):
    """Query Cohere API"""
    def call():
        response = cohere_client.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.message.content[0].text
    return retry_with_backoff(call)

def query_huggingface(prompt):
    """Query Hugging Face API"""
    def call():
        API_URL = "https://router.huggingface.co/v1/chat/completions"
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        payload = {
            "model": "MiniMaxAI/MiniMax-M2.5:novita",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    return retry_with_backoff(call)

def query_ollama(prompt):
    """Query local Ollama API"""
    def call():
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3.2", "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json()["response"]
    return retry_with_backoff(call)

# --- Display Menu ---
def show_menu():
    print("\n" + "="*40)
    print("       MULTI-API QUERY PROGRAM")
    print("="*40)
    print("Select an AI Provider:")
    print("  1. Groq (Llama3)")
    print("  2. Cohere (Command)")
    print("  3. Hugging Face (MiniMax)")
    print("  4. Ollama (Local)")
    print("  5. Show Conversation History")
    print("  0. Exit")
    print("="*40)

# --- Main Execution ---
if __name__ == "__main__":
    print("\nWelcome to Multi-API Query Program!")
    print("Conversation history is being tracked.\n")

    while True:
        show_menu()
        choice = input("Enter your choice (0-5): ").strip()

        if choice == "0":
            print("\nGoodbye!")
            break

        elif choice == "5":
            # Show conversation history 
            if not conversation_history:
                print("\nNo conversation history yet.")
            else:
                print("\n--- Conversation History ---")
                for i, entry in enumerate(conversation_history, 1):
                    print(f"\n[{i}] Provider : {entry['provider']}")
                    print(f"    Prompt   : {entry['prompt']}")
                    print(f"    Response : {entry['response'][:200]}...")
            continue

        elif choice in ["1", "2", "3", "4"]:
            user_prompt = input("\nEnter your prompt: ").strip()
            if not user_prompt:
                print("Prompt cannot be empty!")
                continue

            print("\nQuerying API...")

            # Call selected provider
            if choice == "1":
                provider = "Groq"
                result = query_groq(user_prompt)
            elif choice == "2":
                provider = "Cohere"
                result = query_cohere(user_prompt)
            elif choice == "3":
                provider = "Hugging Face"
                result = query_huggingface(user_prompt)
            elif choice == "4":
                provider = "Ollama"
                result = query_ollama(user_prompt)

            # Save to conversation history
            conversation_history.append({
                "provider": provider,
                "prompt": user_prompt,
                "response": result
            })

            print(f"\n--- {provider} Response ---")
            print(result)

        else:
            print("Invalid choice! Please enter 0-5.")