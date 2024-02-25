import random
from replit import clear
from module import logo_1, logo_2, ques_answer
your_score = 0


def random_question(list_question):
    new_question = random.choice(list_question)
    return new_question


def check(user_answer, question_a, question_b):
    global your_score
    if user_answer == 'a' and question_a['follower_acout'] > question_b['follower_acout']:
        your_score += 1
        print("your are right")
    elif user_answer == 'b' and question_b['follower_acout'] > question_a['follower_acout']:
        your_score += 1
        print("your are right")
    else:

        print("you are wrong")


ques_B = random_question(ques_answer)
is_continue = True

while is_continue:

    ques_A = ques_B
    ques_B = random_question(ques_answer)
    print(logo_1)
    if ques_A == ques_B:
        ques_B = random_question(ques_answer)
    print(f"Compare A: {ques_A['name']}, a {ques_A['description']}, from {ques_A['country']}")
    print(logo_2)
    print(f"Against B: {ques_B['name']}, a {ques_B['description']}, from {ques_B['country']}")
    your_answer = input("Who has more followers? Type A or B: ").lower()
    check(your_answer, ques_A, ques_B)
    clear()
    print(your_score)



