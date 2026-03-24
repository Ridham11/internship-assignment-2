import os
import google.generativeai as genai

# Configure API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-pro")

def query_gemini(prompt):
    """Query the Gemini API with a prompt"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
    # Main execution
if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying Gemini API...")

    result = query_gemini(user_prompt)

    print("\nResponse:\n")
    print(result)