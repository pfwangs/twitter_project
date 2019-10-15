
from Girrafe import Question
question_prompts = [
    "What color are apples?\n a Red\nPurple\nOrage\n\n",
    "What color are Bananas?\n a Red\nPurple\nOrage\n\n",
    "What color are strawberries?\n a Red\nPurple\nOrage\n\n"

]

questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score+1
    print("you got" + str(score))

run_test(questions)