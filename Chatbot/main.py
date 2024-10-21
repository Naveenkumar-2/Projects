import openai

openai.api_key="YOUR-API-KEY"
def chat_with_gpt(prompt):
    respose = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return respose.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","end","exit"]:
            break
        response =chat_with_gpt(user_input)
        print("BOT: ",response)