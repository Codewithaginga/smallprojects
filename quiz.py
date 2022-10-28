
quiz = {

    "Question 1": {
        "Question":"What is the capital city of France: ",
        "answer": "Paris"
    },
    "Question 2":{
        "Question": "What is the capital city of Germany: ",
        "answer": "Berlin"

    },
    "Question 3":{
        "Question": "What is the capital city of spain: ",
        "answer": "Madrid"
    },
    "Question 4":{
        "Question": "What is the capital city of Kenya: ",
        "answer": "Nairobi"

    },
    "Question 5":{
        "Question": "What is the capital city of Senegal: ",
        "answer": "Dakar"
    },
    "Question 6":{
        "Question": "What is the capital city of South Africa: ",
        "answer": "Pretoria"
    },
    "Question 7":{
        "Question": "What is the capital city of America: ",
        "answer": "Washington DC"
    }
}

score = 0

for k, value in quiz.items():
    print(value['Question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('correct')

        score += 1
        print(f'your score is {score}')

    else:
        print("you can do better")
        print("The answer is: ", value['answer'])
        print(f'your score is {score}')


