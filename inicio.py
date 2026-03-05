def player_name(name):
    return f"hello {name_player}"
name_player = input("enter your name: ")


print("what is your level? \n1 = easy \n2 = midlle or \n3 = difcult?")
print("you can only enter a number")

 
def level_dif(level):
    return f"your level is: {lev}"

lv = True

while(lv):
    lev = str(input("enter your level(only numbers): "))
    if lev == "1":
        lev = "easy"
        lv = False
    elif lev == "2":
        lev = "medio"
        lv = False
    elif lev == "3":
        lev = "hard"
        lv = False
    else:
        print("invalid, please try again")



if lev == "easy":
    print(f"{player_name(name_player)} \n{level_dif(lev)}")
    server = 70
    temperature = 50
    custumer = 35
    
elif lev == "medio":
    print(f"{player_name(name_player)} \n{level_dif(lev)}")
    server = 40
    temperature = 60
    custumer = 20

elif lev == "hard":
    print(f"{player_name(name_player)} \n{level_dif(lev)}")
    server = 40
    temperature = 75
    custumer = 15


