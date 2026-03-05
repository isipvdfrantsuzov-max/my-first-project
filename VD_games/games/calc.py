"""
Логика игры "Калькулятор".
"""

import random

# Описание игры - ЭТА СТРОКА ОБЯЗАТЕЛЬНО ДОЛЖНА БЫТЬ!
DESCRIPTION = "What is the result of the expression?"


"""
Логика игры "Калькулятор".
"""
import random

DESCRIPTION = "What is the result of the expression?"

def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])
    
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    question = f"{num1} {operator} {num2}"
    return question, str(answer)
