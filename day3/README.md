# 🤖  Internship – Day 3
### Building a Smart ChatBot with Python

> Turning Python concepts into a practical chatbot experience!

## 🌟 Project Overview

Day 3 focuses on exploring Python's Object-Oriented Programming, file handling, exception handling, and environment configuration.

As part of this task, I developed a simple interactive chatbot that remembers conversations, responds to user messages, and displays student performance statistics using CSV data.

## 🚀 Features

| Feature | Description |
|---|---|
| 🤖 Interactive ChatBot | Responds to user messages using predefined keywords |
| 🧩 OOP Concepts | Uses classes, objects, constructors, and methods |
| 💬 Chat History | Saves and loads conversations using JSON |
| 🛡️ Error Handling | Handles missing files using exception handling |
| 📊 Student Analytics | Calculates average, highest, and lowest marks |
| ⚙️ Environment Setup | Uses `.env` to configure the chatbot name |

## 🛠️ Built With

- **Python** – Core programming language
- **JSON** – Conversation storage
- **CSV** – Student data management
- **python-dotenv** – Environment variable management
- **OOP** – Classes and objects

## 📂 Project Structure

```text
day3/
│
├── main.py             # Main chatbot application
├── students.csv        # Student records
├── chat_history.json   # Saved conversations
├── .env                # Bot configuration
└── README.md           # Project documentation
```

## ▶️ Getting Started

**1. Install the dependency**

```bash
python -m pip install python-dotenv
```

**2. Configure the chatbot**

Create a `.env` file:

```env
BOT_NAME=MyBot
```

**3. Run the application**

```bash
python main.py
```

## 💻 Sample Interaction

```text
Welcome to MyBot
Type 'bye' to exit.

You: hi
MyBot: Hello!

You: how are you?
MyBot: I am fine!

You: bye
MyBot: Goodbye!
```

## 📚 Key Learnings

- Implementing Object-Oriented Programming in Python.
- Creating reusable class methods.
- Reading and writing JSON files.
- Processing CSV datasets.
- Handling file-related exceptions.
- Managing application settings using environment variables.

## 🎯 Outcome

Successfully built a Python-based chatbot with persistent conversation history and a student performance summary.

**Day 3: From learning Python concepts to building a practical application! 🚀**

---

*Python Internship | Day 3 | Keep Learning, Keep Building.*