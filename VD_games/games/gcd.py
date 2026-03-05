import random
import math

DESCRIPTION = "Найдите наибольший общий делитель заданных чисел."

def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(answer)
