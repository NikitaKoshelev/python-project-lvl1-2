from random import randrange
from brain_games.templates import flow_game, greet_user


def generate_random():
    random_item = randrange(1, 60, 2)
    return random_item


def get_expression_result(num):
    index = num
    count = 0
    while index > 0:
        if num % index == 0:
            count += 1
        index -= 1
    return "yes" if count == 2 else "no"


def get_result():
    random_num = generate_random()
    result = get_expression_result(random_num)
    print("Question: ", random_num)
    return result


def run_game():
    case = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = greet_user(case)
    flow_game(get_result, name)