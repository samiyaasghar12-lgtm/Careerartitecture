import google.generativeai as genai

# Aapki API Key (Jo screenshot mein thi)
genai.configure(api_key="AIzaSyDUcsqMXXxc053uX8E1huVE9wN5SUk3YX8")

# Madam wala model version
model=genai.GenerativeModel("gemini-2.5-flash-lite")

print("Chat started (Type 'exit' or 'bye' or 'quit')")

while True:
    user_input=input("you!")
    if user_input in ['exit','bye','quit']:
        print("Goodbye! see you tomorrow!")
        break
    
    response=model.generate_content(user_input)
    print("Agent:", response.text)