# import
import google.generativeai as genai

#select API Key
genai.configure(api_key="AIzaSyDUcsqMXXxc053uX8E1huVE9wN5SUk3YX8")


# select modal
model=genai.GenerativeModel("gemini-2.5-flash-lite")

print("Chat started (Type 'exit' or 'bye' or 'quit')")
# apply while loop
while True:
    user_input=input("you!")
    if user_input in ['exit','bye','quit']:
        print("Goodbye! see you tomorrow!")
        break
    # user input passing
    response=model.generate_content(user_input)
    print("Agent:", response.text)