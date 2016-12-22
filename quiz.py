# Program 1
# Daily Quiz
# data-file: data.txt
import random

w = open("data.txt", "rb+")
data = {}

def main():
    print "1 - start asking"
    print "2 - feed questions/answers"
    print "3 - prepare a test"
    print "4 - exit"

def check(choice):
    while True:
        if choice == "1":
            start_asking()
        elif choice == "2":
            feed_data()
        elif choice == "3":
            random.shuffle(data)
        else:
            print 'EXITING DATA' 
            exit()


def init():
    global w
    global data
    w.seek(0)
    l = []

    for i in w:
        l.append(i.split("-"))

    
    for i in l:
        data[i[0]] = i[1]



def start_asking():
    init()
    score = 0

    for i in data:
        print "QUESTION: " + i
        answer = raw_input("Answer: ")

        if answer == data.get(i):
            score+=1
            print "Corrrect!"
        else:
            if score != 0:
                score-=1
            print "WRONG!"
    else:
        print "TOTAL SCORE: " + str(score)




def feed_data():
    n = int(raw_input("How many questions you want to add? "))
    i = 1
    while(i <= n):
        question = raw_input("Enter question: ")
        answer = raw_input("Enter answer: ")

        t = question+"-"+answer+"\n"
        w.write(t)
        print "WROTE QUESTION #%d" % i
        i+=1

    init() # init the data
            
    
        
main()
choice = raw_input("CHOICE: ")
print "\n"
check(choice)



