import nltk
from datetime import datetime
import random

nltk.download('punkt')

def Bollywood_dialogues():
    bollywood_dialogues = [
        "Har team main bas ek hi gunda ho sakta hai aur iss team ka gunda main hoon!",
        "Tension lene ka nahi, sirf dene ka.",
        "Main udna chahta hoon, daudna chahta hoon, girna bhi chahta hoon ... bus rukna nahi chahta."
    ]
    return random.choice(bollywood_dialogues)

tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added to your list."

def list_tasks():
    if tasks:
        return "Your tasks are:\n" + "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))
    else:
        return "Your task list is empty."

def chatbot():
    print("Hello! I am your innovative chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        
        if "bollywood dialogues" in user_input:
            dialogue = Bollywood_dialogues()
            print(f"Chatbot: {dialogue}")
        elif "add task" in user_input:
            print("Chatbot: What task would you like to add?")
            task = input("Task: ")
            task_response = add_task(task)
            print(f"Chatbot: {task_response}")
        elif "list tasks" in user_input:
            tasks_info = list_tasks()
            print(f"Chatbot: {tasks_info}")
        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

chatbot()
