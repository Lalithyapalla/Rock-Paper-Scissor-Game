import random
options=['Rock','Paper','Scissor']
print("--------ROCK PAPER SCISSOR GAME--------")
print('\nWelcome to Rock, Paper, Scissors!')
start=input("\nAre you ready to play?  (Yes/No):")

while((start.lower()=="yes") or (start.capitalize()=="Yes") or (start.upper()=="YES")):

    Player_turn=input("\nEnter one choice:\n\nRock\nPaper\nScissor\n")
    Computer_turn=random.choice(options)
    print("\nYou chose:",Player_turn)
    print("\nComputer chose:",Computer_turn)

    if  ( Computer_turn==Player_turn.capitalize() ) :
        print("\nWell done!! , Match is Tie")

    elif  ( (Computer_turn=="Scissor") and (Player_turn.capitalize()=="Rock") ) :
        print("\nCongratulations!!! , you won the match")

    elif  ( (Computer_turn=="Paper") and (Player_turn.capitalize()=="Rock") ) :
        print("\nYou lost!! , Better luck next time")

    elif  ( (Computer_turn=="Rock") and (Player_turn.capitalize()=="Paper") ) :
        print("\nCongratulations, you won the match")

    elif  ( (Computer_turn=="Scissor") and (Player_turn.capitalize()=="Paper") ) :
        print("\nYou lost!! , Better luck next time")

    elif  ( (Computer_turn=="Rock") and (Player_turn.capitalize()=="Scissor") ) :
        print("\nYou lost!! , Better luck next time")

    elif ( (Computer_turn=="Paper") and (Player_turn.capitalize()=="Scissor") ) :
        print("\nCongratulations!!! , you won the match")

    start=input("\nDo you want to play again? (Yes/No):")

    if ( (start.lower()=="no") or (start.upper()=="NO") or (start.capitalize()=="No") ) :
        print("\nThanks for playing!!")
