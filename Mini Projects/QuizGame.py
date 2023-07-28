print("Welcome to Quiz!")
playing = input("Do you want to Play: ")
if playing.lower() != "yes":
    quit()

print("Lets Play :)")
score = 0
total = 20

print("Total Marks: 20")

answer1 = input("What does CPU stand for? ")
if answer1.lower() == "Central Processing Unit":
    print("Corrent!")
    score = score +5
else:
    print("Incorrect!")

answer2 = input("What does ROM stand for? ")
if answer2.lower() == "Read Only Memory":
    print("Corrent!")
    score = score +5
else:
    print("Incorrect!")

answer3 = input("What does GPU stand for? ")
if answer3.lower() == "Graphics Processing Unit":
    print("Corrent!")
    score = score +5
else:
    print("Incorrect!")

answer4 = input("What does RAM stand for? ")
if answer4.lower() == "Random Access Memory":
    print("Corrent!")
    score = score +5
else:
    print("Incorrect!")

print("You score: " , score)

