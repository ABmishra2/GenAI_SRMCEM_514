import google.generativeai as genai

# 1. Configure your API key
genai.configure(api_key="AIzaSyCySoBT56IknP79EN5noGf2a7wnP0_xkXM")

# 2. Load the Gemini model (text-only)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# 3. Function to generate a response from Gemini
def chat_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 4. User prompt input
if __name__ == "__main__":
    print("🔹 Welcome to Gemini AI Chat 🔹\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting... Bye!")
            break
        reply = chat_with_gemini(user_input)
        print(f"Gemini: {reply}\n")
