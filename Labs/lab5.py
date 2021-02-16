print("Howdy dog lets do some maths and stuff")

print("I am 1 year old. Please tell me how many years old you are ")
birthYear = int(input("year: "))

print("Please tell me what month you were born, as a number. I am a dumb robot and do not understand the text month SO DO NOT DO THAT")
birthMonth = int(input("Month: "))

print("Now for the special day. You guessed it what is the day of you birthday? and do not think about doing anything but a number ._.")
birthDay = int(input("day: "))

print("Now for the current date, we're almost there :)")


seconds = birthYear * 24 * 60 * 60 * 365 + birthMonth * 30 * 60 + birthDay * 60 

print("Aloha you are" , seconds , "seconds old give or take a couple thousands of seconds")