def rock_paper_scissors():

  import random

  choices = ["rock", "paper", "scissors"]

  print("Rock, Paper, Scissors Game ✊✋✌️")

  while True:
      user = input("Choose rock, paper or scissors (or 'quit' to stop): ").lower()
      if user == 'quit':
          print("Thanks for playing!")
          break
      if user not in choices:
          print("Invalid choice. Try again!")
          continue

      computer = random.choice(choices)
      print("Computer chose:", computer)

      if user == computer:
          print("It's a tie!")
      elif (user == "rock" and computer == "scissors") or \
          (user == "paper" and computer == "rock") or \
          (user == "scissors" and computer == "paper"):
          print("You win!")
      else:
          print("You lose!")

def Dice_Rolling_Simulator ():
  import random

  def roll_dice():
      return random.randint(1, 6)

  print("Dice Rolling Simulator 🎲")

  while True:
      roll = input("Roll the dice? (yes/no): ").lower()
      if roll == "yes":
          print("You rolled:", roll_dice())
      elif roll == "no":
          print("Thanks for playing!")
          break
      else:
          print("Please type 'yes' or 'no'")

def Random_Password_Generator():
  import random
  import string

  def generate_password(length):
      characters = string.ascii_letters + string.digits + string.punctuation
      password = ''.join(random.choice(characters) for _ in range(length))
      return password

  print("Random Password Generator 🔐")
  try:
      length = int(input("Enter desired password length: "))
      if length < 4:
          print("Password should be at least 4 characters long.")
      else:
          print("Generated Password:", generate_password(length))
  except ValueError:
      print("Please enter a valid number.")

def To_Do_List_App():
  todo_list = []

  def show_menu():
      print("\nTo-Do List Menu:")
      print("1. View Tasks")
      print("2. Add Task")
      print("3. Delete Task")
      print("4. Exit")

  while True:
      show_menu()
      choice = input("Enter your choice (1-4): ")

      if choice == '1':
          if not todo_list:
              print("No tasks yet.")
          else:
              for i, task in enumerate(todo_list, 1):
                  print(f"{i}. {task}")
      elif choice == '2':
          task = input("Enter new task: ")
          todo_list.append(task)
          print("Task added!")
      elif choice == '3':
          task_no = int(input("Enter task number to delete: "))
          if 0 < task_no <= len(todo_list):
              removed = todo_list.pop(task_no - 1)
              print(f"Removed: {removed}")
          else:
              print("Invalid task number!")
      elif choice == '4':
          print("Goodbye!")
          break
      else:
          print("Invalid choice. Try again.")

def calculator():
    print("Simple Calculator")
    
    num1 = float(input("Enter first number: "))
    op = input("Choose operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation!")

def Number_Guessing_Game():
  import random

  number_to_guess = random.randint(1, 100)
  guess = None
  attempts = 0

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  while guess != number_to_guess:
      guess = int(input("Enter your guess: "))
      attempts += 1

      if guess < number_to_guess:
          print("Too low! Try again.")
      elif guess > number_to_guess:
          print("Too high! Try again.")
      else:
          print(f"Congratulations! You guessed it in {attempts} tries.")

def Web_scraping():
  import requests
  from bs4 import BeautifulSoup
  print("Welcome to web scraping\n")
  print("The link used here is: http://quotes.toscrape.com\n")
  print("Lets see the Quotes from the above link:\n")
  url = 'http://quotes.toscrape.com'
  response = requests.get(url)
  data = response.text
  soup = BeautifulSoup(data, 'lxml')
  posts = soup.find_all('div', class_='quote')
  for quote in posts:
    text=quote.find('span', class_="text").text
    author=quote.find('small',class_='author').text
    print(f"{text}-{author}")
    print("\n")

def Quiz_App():
    questions = {
        "What is the output of print(2 ** 3)?": "c",
        "Which of the following is a Python data type?": "b",
        "What is the correct file extension for Python files?": "a",
        "Which keyword is used for function in Python?": "c",
        "What is the correct way to create a function in Python?": "a",
        "Which of the following is not a Python data structure?": "c",
        "How do you start a for loop in Python?": "b",
        "What is the keyword to check if a value exists in a list?": "b",
        "Which operator is used for floor division?": "a",
        "Which of these is used to define a block of code in Python?": "c",
        "What is the output of type([])?": "a",
        "Which statement is used to handle exceptions?": "a",
        "Which of these is a dictionary?": "c",
        "What is the keyword used to define a class?": "a",
        "What is the output of type([])?": "a",
        "What is the use of 'pass' in Python?": "c",
        "Which keyword is used to start a loop in Python?": "b",
        "What does 'continue' do in Python loops?": "b",
        "How do you define a function named 'fun'?": "c",
        "Which module is used for regex in Python?": "a",
        "How to inherit a class in Python?": "b",
        "What is the output of type(5)?": "a",
        "Which data structure is immutable?": "a",
        "What does IDE stand for?": "b",
        "What is pip in Python?": "c",
        "Which method is used to add an element in list?": "b",
        "What is the result of len('Python')?": "b",
        "Why is indentation required in Python?": "c",
        "Which of these is a Python module?": "b",
        "Which symbol is used for decorators?": "a",
        "What is the output of print(10//3)?": "c",
        "What is the output of print(bool('False'))?": "c",
        "How do you write an if statement in Python?": "c",
        "How to declare a constant in Python?": "b",
        "What is recursion?": "a",
        "How is a lambda function written?": "a",
        "Which of these is immutable?": "b",
        "Which method returns the highest number?": "a",
        "Which function gives ASCII of a character?": "c",
        "What type of language is Python?": "a",
        "How to create an empty set?": "a",
        "Which function returns number of elements?": "c",
        "Are tuples mutable?": "a",
        "Which of these is not a list method?": "c",
        "What is the output of 'a'*3?": "c"
    }

    options = [
        ["a) 6", "b) 5", "c) 8"],
        ["a) HTML", "b) List", "c) HTTP"],
        ["a) .py", "b) .pyt", "c) .pt"],
        ["a) fun", "b) func", "c) def"],
        ["a) def myfunc():", "b) function myfunc()", "c) create myfunc()"],
        ["a) List", "b) Dictionary", "c) Folder"],
        ["a) for i in 5", "b) for i in range(5):", "c) foreach i in range(5)"],
        ["a) include", "b) in", "c) has"],
        ["a) //", "b) /", "c) %"],
        ["a) Curly braces", "b) Semicolon", "c) Indentation"],
        ["a) <class 'list'>", "b) <class 'tuple'>", "c) <class 'dict'>"],
        ["a) try", "b) catch", "c) except"],
        ["a) [1: 'a']", "b) ['key': 'value']", "c) {'key': 'value'}"],
        ["a) class", "b) define", "c) defclass"],
        ["a) <class 'list'>", "b) <class 'tuple'>", "c) <class 'dict'>"],
        ["a) Stops program", "b) Breaks from function", "c) Placeholder"],
        ["a) for", "b) while", "c) switch"],
        ["a) Exits loop", "b) Skips to next iteration", "c) Stops program"],
        ["a) function()", "b) create()", "c) def function():"],
        ["a) re", "b) regex", "c) expression"],
        ["a) inherit", "b) class Derived(Base)", "c) base"],
        ["a) <class 'int'>", "b) <class 'char'>", "c) <class 'str'>"],
        ["a) tuple", "b) list", "c) set"],
        ["a) Integrated Developer Editor", "b) Integrated Development Environment", "c) Internal Dev Environment"],
        ["a) Python Index Package", "b) Python Integrated Platform", "c) Preferred Installer Program"],
        ["a) push()", "b) append()", "c) add()"],
        ["a) 6", "b) 6", "c) 5"],
        ["a) To confuse compiler", "b) To shorten code", "c) Define blocks"],
        ["a) class", "b) module", "c) dictionary"],
        ["a) @", "b) module", "c) def"],
        ["a) 10", "b) 14", "c) 3"],
        ["a) False", "b) Error", "c) True"],
        ["a) if (condition)", "b) if condition", "c) if condition:"],
        ["a) const", "b) No fixed way", "c) static"],
        ["a) Function calling itself", "b) Loop inside loop", "c) Calling external lib"],
        ["a) lambda args: expression", "b) lambda =>", "c) lambda x: x+2"],
        ["a) list", "b) tuple", "c) integer"],
        ["a) max()", "b) highest()", "c) max_value()"],
        ["a) char()", "b) ascii()", "c) ord()"],
        ["a) Interpreted & dynamic", "b) Interpreted", "c) Compiled"],
        ["a) set()", "b) {}", "c) []"],
        ["a) size()", "b) count()", "c) len()"],
        ["a) Yes", "b) Sometimes", "c) No"],
        ["a) array", "b) str", "c) set"],
        ["a) aaa", "b) a3", "c) aaa"]
    ]

    questions_list = list(questions.items())
    score = 0
    for i, (question, correct_answer) in enumerate(questions_list):
        print(f"\n{question}")
        for option in options[i]:
            print(option)
        answer = input("Enter your answer (a/b/c): ").lower()
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        a=input("Enter Yes To Continue(Y/N): ")
        if a.lower()=="n":
          print("Closing Quiz App")
          break
    print(f"\nYour final score is: {score}/{len(questions_list)}")
    print("Closing Quiz App")

def Data_Visualization():
  import yfinance as yf
  import pandas as pd
  import matplotlib.pyplot as plt
  import seaborn as sns
  import mplfinance as mpf
  import numpy as np

  stock_data = yf.download('AAPL', start='2023-01-01', end='2024-01-01')

  stock_data['Daily Return'] = stock_data['Close'].pct_change()
  print(stock_data.columns)

  plt.figure(figsize=(12, 6))
  stock_data['Daily Return'].hist(bins=50, stacked=True, color=[ 'orange'], edgecolor='black')
  plt.title('Histogram of Daily Returns - AAPL')
  plt.xlabel('Daily Return')
  plt.ylabel('Frequency')
  plt.grid(True)
  plt.tight_layout()
  plt.show()

  stock_data['Month'] = stock_data.index.to_period('M')
  monthly_returns = stock_data.groupby('Month')['Daily Return'].sum()

  plt.figure(figsize=(12, 6))
  sns.barplot(x=monthly_returns.index.astype(str), y=monthly_returns.values, palette='plasma')
  plt.title('Monthly Aggregated Returns - AAPL')
  plt.xlabel('Month')
  plt.ylabel('Sum of Daily Returns')
  plt.xticks(rotation=75)
  plt.tight_layout()
  plt.show()

def get_weather():
    import requests
    city = input("Enter a city name 'example(Tirunelveli,IN)':")
    api_key = "bbbfdecdd4e3711b51e94a8ab0e520a4"  # Replace with your real API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or API error.")
try:
  print("Hi, Thanks For Viewing My Project\n")
  print("I have created 10 Basic Beginner Projects Inside This Mini Project\n")
  print("Check Those Projects\n")
  projects=["Simple Calculator App ➕➖✖️➗","Number Guessing Game 🎯","To-Do List App✅","Random Password Generator 🔐","Dice Rolling Simulator 🎲","Rock, Paper, Scissors ✊✋✌️","Quiz App 🧠❓","Web Scraping","Data Visualization","Weather App (Using API) ☁️☀️🌧️","Exit"]
  project_List={  "Simple Calculator App ➕➖✖️➗":calculator,
                "Number Guessing Game 🎯":Number_Guessing_Game,
                "To-Do List App✅":To_Do_List_App,
                "Random Password Generator 🔐":Random_Password_Generator,
                "Dice Rolling Simulator 🎲":Dice_Rolling_Simulator,
                "Rock, Paper, Scissors ✊✋✌️":rock_paper_scissors,
                "Quiz App 🧠❓":Quiz_App,
                "Web Scraping":Web_scraping,
                "Data Visualization":Data_Visualization,
                "Weather App (Using API) ☁️☀️🌧️":get_weather,
                }
  keyslist=list(project_List.keys())
  while True:
      print("\n")
      for i,pro in enumerate(projects,1):
          print(f"{i}.{pro}")
      print("\n")
      user=int(input("Enter a Number To choose: "))
      print("\n")
      if user > len(projects):
          print("Invalid Selection")
      elif projects[user-1]=="Exit":
          print("Closing the Mini Project. Thank You!! ")
          break
      elif projects[user-1] in keyslist:
          temp=projects[user-1]
          x=project_List[temp]
          x()
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("\nWanna Check Out Again?? Re-run it")


