start = '''
How today goes is all up to you! Just make the right decisions :)
'''
def function_game():
    socialPoints = 0
    minLate = 0
    print(start)
    Player = input("What is your name?")

    print('Good morning', Player)


    print("Your alarm goes off. Do you snooze it or wake up on time?")
    user_input = input()
    if user_input == "snooze it":

        print("Well, now you are 10 minutes late for school.")
        minLate+=10

        print("Will you take a shower?")
        shower_choice = input()
        if shower_choice == "yes":
            socialPoints+=5
            minLate+=10

            print("Well, now you are 20 minutes late and you missed your bus! Will you walk or run to school?")
            walk_choice = input()
            if walk_choice == "walk":
                minLate+=20


                print("While you are walking, you see a live concert! Do you stop to snapchat and story it?")
                snap_choice = input()
                if snap_choice == "yes":
                    socialPoints +=10
                    minLate += 20


                    print("You arrive to school SUPER late. The principal calls you into her office and gives you the option of your punishment.")


                    print("Detention or call home?")
                    pun_choice = input()
                    if pun_choice == "detention":
                        socialPoints += -10


                        print("You lose all of your friends. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

                    elif pun_choice == "call home":
                        socialPoints += -10


                        print("You are grounded. Your mom sends you off to boarding school. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

                elif snap_choice == "no":
                    socialPoints += -5


                    print("You are only 45 minutes late to school. Do you pretend you were sick? Yes or no?")
                    sick_choice = input()
                    if sick_choice == "yes":
                        socialPoints += -5


                        print("You have to spend the rest of the day in the infirmary room. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)
                    elif sick_choice == "no":


                        print ("You get one morning detention. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

            elif walk_choice == "run":
                minLate+=10


                print("Well, now you smell really bad! Guess that shower wasn't a good choice.")
                socialPoints += -5


                print("Your day is going horribly. Your boyfriend cheats on you with your best friend")
                socialPoints += -5


                print("Do you cheat on him with his best friend, yes or no?")
                cheat_choice = input()
                if cheat_choice == "yes":
                    socialPoints += -5


                    print("You are compared to Taylor Swift for the rest of your life.Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

                elif cheat_choice == "no":
                    socialPoints +=5


                    print("You cry and move on. In the end, you marry a really great guy! Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

        elif shower_choice == "no":
            socialPoints += -5


            print("Now you smell really bad, but at least you made the bus!")


            print("An elderly woman walks on the bus. Do you offer your seat to her?")
            seat_choice = input()

            if seat_choice == "yes":
                socialPoints +=5


                print("Now you feel great about yourself!")


                print("You arrive at school and the person you like asks you out! Do you say yes or no?")
                date_choice = input()
                if date_choice == "yes":


                    print("You live happily ever after with them. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

                elif date_choice == "no":


                    print("You will be forever alone. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)


            elif seat_choice == "no":
                socialPoints += -5


                print("Someone on the bus yells at you. They try to pick a fight with you.")


                print("Will you fight them?")
                fight_choice = input()


                if fight_choice == "yes":


                    print("You get beat up. Guess what? Someone records the fight and posts it online!!")
                    socialPoints += -10


                    print("Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)


                elif fight_choice == "no":


                    print("They jump you anyway :) ")
                    socialPoints += -5


                    print("Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)

    elif user_input == "wake up on time":


        print("Will you take a shower?")
        choice_shower1 = input()
        if choice_shower1 == "yes":
            socialPoints += 5


            print("You barely made the bus.")


            print("You have a test first period. Do you skip or take it?")
            choice_test = input()
            if choice_test == "skip it":


                print("Will you hide in the bathroom or go home?")
                hide_choice = input()
                if hide_choice == "hide in the bathroom":
                    socialPoints += -10


                    print("A teacher finds you and gives you a detention. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)
                elif hide_choice == "go home":
                    socialPoints += -5


                    print("Your parents ground you Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)
            elif choice_test == "take it":


                print("Did you study for the test? Yes or no?")
                study_choice = input()
                if study_choice == "yes":
                    socialPoints += 10


                    print("You got an A on the test! Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)
                elif study_choice == "no":
                    socialPoints += -5


                    print("You have to go to summer school. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)


        elif choice_shower1 == "no":
            socialPoints += -10


            print("Now your mom has to drive you to school and is going to be late to her job.")


            print("Would you rather have your mom lose her job or you wake up an hour earlier for school everyday? Option 1 or 2?")
            option_choice = input()
            if option_choice == "option 1":


                print("You are forced to move. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)
            elif option_choice == "option 2":

                print("Your grades go down because you are constantly tired. Story Over. Social Points: " , socialPoints , "Minutes Late: ", minLate)


function_game()
