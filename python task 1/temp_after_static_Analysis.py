"""file docstrings.
"""
import random
def return_answer(username):
    """return the answer from the answer book
    """
    list_answer = ["Just do it", "Forget about it", "You need relax",
                   "Be confident!", "Just smile", "Your heart already know the answer",
                   "You are stronger than you know"]
    number = random.randint(0, 6)
    answer = list_answer[number]
    print("Hello %s, here is the answer of your question: %s " %(username, answer))
LIBRARY = {}
NAME = ""
i = 1
while i <= 10:
    print("*********Welcome to the my World************")
    print("I am a book, Which has the answers of all the questions in the universe")
    print("You are the %dth person to ask my question today" %i)
    NAME = input("What is your name?")
    if NAME.upper() in LIBRARY.keys():
        print("%s, you have so much questions! But you have already ask a question today." \
              "Every one can only ask one time in one day" %NAME)
        continue
    QUESTION = input("Which question bother you now?")
    LIBRARY[NAME.upper()] = QUESTION
    return_answer(NAME)
    ANSWER = input("Are you satisfied with this answer?")
    if ANSWER.lower() == "yes":
        print("I am happy with it")
    elif ANSWER.lower() == "no":
        print("oh, man, you should accept it.That is life")
    else:
        print("good night. I run out of my energy today.")
    #print(libarery)
    i += 1
    #print(i)
else:
    print("I can only answer 10 questions one today. See you tomorrow guys.Enjoy today!!")
