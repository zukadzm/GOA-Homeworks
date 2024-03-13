#register
name = input("Please enter your name: ")
password = input("Please enter your password: ")
repeat_password = input("Please enter your password again: ")

if password == repeat_password:
        print(name, "registered succsesfully!")
else:
    print("Invalid Passwords!")
#game time
    
number= 18

level = input("You are level 1 yet , play more to get more level , lets start")

number = int(input("guess number 1 to 50: "))    # 1 question

if number == 18:
      print("correct number")

else:
      print("wrong")

level = input("You are now level 2")   # 2 question


start = int(input("whats 5 x 5 = "))

if start == 25:
      print("correct")
else:
      print("wrong")

level = input("You are now level 3")  # 3 question

play = int(input("Whats 550 : 5 = "))

if play == 110:
      print("correct")
else:
      print("wrong")

level = input("You are now level 4")  # 4 question

game4 = int(input("Whats 1250 X 15 = "))

if game4 == 18750:
      print("correct")
else:
      print("wrong")

level = input("You are now level 5")  # 5 question

game5 = int(input("Whats 2250 X 20 = "))

if game5 == 45000:
      print("correct")
else:
      print("wrong")

level = input("You are now level 6")  # 6 question

game6 = int(input("Whats 11500 X 5 = "))

if game6 == 57500:
      print("correct")
else:
      print("wrong")      

level = input("You are now level 7") # 7 question

game7 = int(input("Whats 22 500 X 3 = "))

if game7 == 67500:
      print("correct")
else:
      print("wrong")      

level = input("You are now level 8") # 8 question

game8 = int(input("Whats 35 200 X 2 = "))

if game8 == 70400:
      print("correct")
else:
      print("wrong")

level = input("You are now level 9")  # 9 question

game9 = int(input("Whats 40 500 X 3 = "))

if game9 == 121500:
      print("correct")
else:
      print("wrong") 

level = input("You are now level 10")    

hard = input("WOW, thats last level its very hard lets get it")

game10 = int(input("Whats 100 250 X 5 = ")) # 10 question last question

if game10 == 501250:
      print("correct")
else:
      print("wrong")    

done = input("its done you are genius")

thanks = input("Thanks for visit my game <3")