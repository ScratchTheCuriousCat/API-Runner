import os
from openai import OpenAI

version = "0.1"

# api essentials
api_key = "sk-unsloth-example-api"
base_url = "http://localhost:8888/v1"
ai_model = "unsloth/LFM2-350M-GGUF:F16"

os.system("title Setup")
os.system("cls")

def deco():
    print("----------------------")

def essentials():
    print(f"API Key: {api_key}")
    print("")
    print(f"Base URL: {base_url}")
    print("")
    print(f"AI Model: {ai_model}")
    print("")

print("Those are the API Essentials: ")
deco()
essentials()
print("Press '1' to change, else press '0' to mantain.")
inp = input("> ")
if inp == "1":
    api_key = input("API Key: ")
    base_url = input("Base URL: ")
    ai_model = input("AI Model: ")
elif inp == "0":
    print("No changes made, starting..")
    print("")

os.system("color 6")
os.system("title API Runner")
os.system("cls")

print(f"API Runner {version}")
print("Type /help to get a list of commands.")

client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

# commands

instruct = "You're a helpful assistant"
ts = "1"

def command(user_input):
    if user_input == "/help":
        print("----- List of Commands -----")
        print("/help -- Get a list of commands")
        print("/get -- Get the API, Base URL and Model.")
        print("/clear -- Clear the terminal")
    elif user_input == "/get":
        essentials()
    elif user_input == "/clear":
        os.system("cls")
        print(f"API Runner {version}")


while ts == "1":
    user_input = input("> ")
    user2 = f"SYSTEM PROMPT: {instruct} | User Input: {user_input}"
    if user_input.startswith("/"):
        command(user_input)
    else:
        print("Working...")
        response = client.chat.completions.create(
            model=ai_model,
            messages=[{"role": "user", "content": user2}],
            stream=True,
            )
    
        for chunk in response:
            print(chunk.choices[0].delta.content or "", end="")
        print("")
