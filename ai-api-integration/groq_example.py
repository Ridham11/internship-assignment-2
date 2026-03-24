import os
from groq import Groq

# Configure API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=api_key)


def query_groq(prompt):
    """Query the Groq API with a prompt"""
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying Groq API (LLaMA 3.1 model)...")

    result = query_groq(user_prompt)

    print("\nGroq Response:\n")
    print(result)