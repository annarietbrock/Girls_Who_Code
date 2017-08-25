import sys
class User:
    # Define the fields and methods for your object here.

    def __init__(self,name):
        self.name = name




class Network:
    def __init__(self):
        self.users = []


    # Define the fields and methods for your object here.



def main():
    print("Welcome to whatever we want to call this!")
    myNet = Network()
    callStatements = False

    def reCall():
         print('''Press u to add a user,
         press p to print users,
         press c to add a connection,
         press pc to print connections, and press q to quit''')
         user_input = input()
         callStatements = False
         while callStatements == False:
             if user_input == "u":
                print("What is your name?")
                print("")
                name = input()
                for i in myNet.users:
                    if name == myNet.users[i]:
                        print("Username taken son, please try again")
                        reCall()
                    else:
                        myNet.users.extend([name])
                        reCall()

             if user_input == "p":
                for all in myNet.users:
                    print(all)
                    print("")
                reCall()
             if user_input == "q":
                sys.exit("Goodbye! Hope to see you soon")
                print()
                callStatements = True

    if callStatements == False:
        reCall()





    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
    main()
