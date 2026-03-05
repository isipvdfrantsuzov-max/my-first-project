import prompt

ROUNDS_TO_WIN = 3


def run_game(game_module):
    """
    Запускает игру.
    
    Args:
        game_module: модуль с логикой конкретной игры
    """
    print("Welcome to the VD games!")
    
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    print(game_module.DESCRIPTION)
    
    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = game_module.generate_round()
        
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
