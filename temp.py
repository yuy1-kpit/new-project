import random

def return_answer(name):
    list_answer=["Just do it","Forget about it","You need relax","Be confident!","Just smile","Your heart already know the answer","You are stronger than you know"]
    number=random.randint(0,6)
    answer=list_answer[number]
    print("Hello %s, here is the answer of your question: %s " %(name,answer))

       

libarery={}
name=""
i=1
while(i<=10):
    name=input("What is your name?")
    if name.upper() in libarery.keys():
           print("%s, you have so much questions! But you have already ask a question today. Every one can only ask one time in one day" %name)
           continue
    question=input("Which question bother you now?")
    libarery[name.upper()]=question
    return_answer(name)
    answer=input("Are you satisfied with this answer?")
    if answer=="yes":
             print("I am happy with it")
    elif answer=="no":
             print("oh, man, you should accept it.That is life")
    else:
             print("good night. I run out of my energy today.")
    print(libarery)
    i+=1
    print(i)
else:
    print("I can only answer 10 questions one today. See you tomorrow guys.Enjoy today!!")