import csv
import random


# #4 functions:
# #1. load_questions:
#     #input: filename 
#     #output: is a list of questions with their answers

# def load_questions(filename):
#     #it loads the questions from the file
#     questions = []
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader) #skips the first line (header)
#         for row in reader:
#             questions.append(row)
#         return questions


# print(load_questions("quiz_questions.csv"))


def load_questions(filename):
    #it loads the questions from the file
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split(',')
            questions.append(data)
        return questions

#print(load_questions("quiz_questions.csv"))


#2. take_quiz
    #input: questions
    #it chooses 10 random questions from list of questions
    #it displays those questions
    #it asks the user for the answer
    #it checks if user's is correct
    #output: score

def take_quiz(questions):
    score = 0
    selected_questions = random.sample(questions, 10)
    index = 1

    for question in selected_questions:
        print("Question #" + str(index) + ": " + question[0])
        print("A: " + question[1])
        print("B: " + question[2])
        print("C: " + question[3])
        print("D: " + question[4])

        answer = input("You Answer: (A,B,C,D)").strip().upper()
        if answer == question[5]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is: " + question[5])

        index +=1

    return score

#3. display_result
    #inputs: score, total_questions
    #calculates a percentage
    #it gives the user a grade (80+ = A, 60-80 = B, 40-60 = C, <40 = D)

def display_result(score, total_questions):
    #calculate the percentage using the score and total questions:

    percentage = (score/total_questions)*100

    if percentage >= 80:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 40:
        print("Grade: C")
    else:
        print("Grade: D")


questions = load_questions("quiz_questions.csv")
score = take_quiz(questions)
display_result(score, 10)