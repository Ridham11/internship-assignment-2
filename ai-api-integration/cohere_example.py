# cohere_example.py
import cohere
import os

# --- API Configuration ---
api_key = os.getenv("COHERE_API_KEY")
client = cohere.ClientV2(api_key)

# --- Query Function ---
def query_cohere(prompt):
    """Query the Cohere API with a prompt"""
    try:
        response = client.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.message.content[0].text

    except Exception as e:
        return f"Error: {str(e)}"

# --- Main Execution ---
if __name__ == "__main__":
    print("=== Cohere API Query ===")
    print("Model: command-a-03-2025\n")

    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Cohere API...")

    result = query_cohere(user_prompt)

    print("\n--- Response ---")
    print(result)