
import json
import csv
import os
from dotenv import load_dotenv


load_dotenv()

bot_name = os.getenv("BOT_NAME", "MyBot")


class ChatBot:

    def __init__(self, name):
        self.name = name
        self.history = []

    # Add messages to chat history
    def add_message(self, role, message):
        self.history.append({
            "role": role,
            "content": message
        })

    # Generate chatbot reply
    def get_reply(self, message):
        replies = {
            "hi": "Hello!",
            "hello": "Hi! How are you?",
            "python": "Python is easy to learn!",
            "how are you": "I am fine!",
            "bye": "Goodbye!"
        }

        for key in replies:
            if key in message.lower():
                return replies[key]

        return "Sorry! I did not understand."

    # Save chat history
    def save_history(self):
        with open("chat_history.json", "w") as file:
            json.dump(self.history, file, indent=4)

    # Load chat history
    def load_history(self):
        try:
            with open("chat_history.json", "r") as file:
                self.history = json.load(file)

        except FileNotFoundError:
            self.history = []

        except json.JSONDecodeError:
            print("Invalid JSON file. Starting new history.")
            self.history = []


# Create chatbot object
bot = ChatBot(bot_name)

# Load previous conversation
bot.load_history()

print("Welcome to", bot.name)
print("Type 'bye' to exit.\n")


# Chatbot interaction
while True:

    user = input("You: ").strip()

    if user == "":
        print("Please enter a message.")
        continue

    bot.add_message("user", user)

    reply = bot.get_reply(user)

    print(bot.name + ":", reply)

    bot.add_message("bot", reply)

    if user.lower() == "bye":
        break


# Save conversation
bot.save_history()

print("\nChat History:")
print(bot.history)


# Read student CSV file
students = []

try:
    with open("C:\\Users\\Sowmya\\Downloads\\internship\\day3\\student.csv.txt", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    print("\nStudent Details:")

    for student in students:
        print(student)

    total = len(students)
    marks = []

    for student in students:
        marks.append(int(student["Marks"]))

    if total > 0:
        average = sum(marks) / total

        print("\nTotal Students:", total)
        print("Average Marks:", average)
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))

    else:
        print("No student records found.")

except FileNotFoundError:
    print("students.csv file not found.")

except (ValueError, KeyError):
    print("Invalid student data in CSV file.")
