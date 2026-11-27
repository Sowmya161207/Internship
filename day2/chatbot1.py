replies = {
    "hi": "Hello!",
    "hello": "Hi! How are you?",
    "python": "Python is easy to learn!",
    "how are you": "I am fine!"
}
conversation=[]
while True:
    user=input("You: ").lower().strip()
    conversation.append({"role":"user","content":user})
    if user=="bye":
        print("BOT:goodbye!")
        conversation.append({"role":"bot","content":"Goodbye"})
        break
    reply="SORRY! I did not understand!"
    for key in replies:
        if key in user:
            reply=replies[key]
            break
    print("Bot:",reply)
    conversation.append({"role":"bot","content":reply})
print("\nChat History:")
print(conversation)
