
age = int(input("How old are you?"))
film_rating = input("What film rating do you want to watch?")
if age >= 18:
    print("You can watch any movie, please proceed")
elif (age >= 15 and age < 18) and film_rating == 18 :
    print("You cannot watch this film, please choose from U, PG, 12A or 15")
elif (12 <= age < 15) and (film_rating == 18 or film_rating == 15) :
    print("You cannot watch this film, please choose from U, PG or 12A")
elif age >= 8 and age < 12 and film_rating == 18 or film_rating == 15 or film_rating == "12A" :
    print("You cannot watch this film, please choose from U or PG")
elif age < 8 and film_rating == 18 or film_rating == 15 or film_rating == "12A" or film_rating == "PG" :
    print("You cannot watch this film, please choose U rated film")

else: print("Please enter a valid input")

def additi12
 on (a,b):
    return (a + b)
print(addition(3,5))
print(addition(165,194))
