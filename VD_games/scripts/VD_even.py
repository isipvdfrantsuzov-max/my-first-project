answer = prompt.string("Твой ответ: ").strip().lower()

# Отладочный вывод: покажем код символов
print("DEBUG:", [ord(c) for c in answer])

correct_answer = "yes" if is_even(number) else "no"

if answer not in ["yes", "no"]:
    print(f"'{answer}' — некорректный ввод. Введи только 'yes' или 'no'.")
    continue

if answer == correct_answer:
    print("Правильно!")
    correct_answers += 1
else:
    print(f"'{answer}' — неправильный ответ ;(. Правильный ответ был '{correct_answer}'.")
    print(f"Попробуй ещё раз, {name}!")
    return
