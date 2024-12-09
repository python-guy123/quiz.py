
iy = input("This is a quiz. For every right answer, you will obtain 5 points. Are you okay with this? If yes, type y. If not, type n.")
if iy == "y":
    score = int(0)
    q1 = input("What is the capital of the United arab Emirates?\nA) Abu Dhabi\nB)Dubai\nC)Bangalore")
    if q1 == "A":
        score+= 5
    q2 = input("Where is the Musée du Louvre?\nA) Paris, France\nB)Orly, France\nC)Abu Dhabi, UAE")
    if q2 == "A":
        score+= 5
    q3 = input("Where is the Museum Of The Future?\nA) Paris, France\nB)Dubai, UAE\nC)Abu Dhabi, UAE")
    if q2 == "A":
        score+= 5
    print("Congratulations! You have succesfully completed the quiz with a score of", score)
else:
    print("This program has been terminated.")
