class User:
    # Define the fields and methods for your object here.

    def __init__(self, user_name,real_name):
        # variable SCOPE: parameter variables only exist inside their function
        self.username = user_name
        self.realname = real_name
        self.connections = [] #ready to connect with users

class Network:
    def __init__(self):
        self.userlist = [] #is ready to recieve new users

    def add_user(self, requested_name, real_name):
# this function will check if the username you chose has already been used
        for person in self.userlist: # check every user in the network
            if person.username == requested_name: #check if existing users already have this name
            # person.username refers to an existing object of type User
                print("This username is already taken")
                new_name = input("Please enter a new username")

        # create a new object of type User with the given credentials
        new_user = User(requested_name, real_name)
        self.userlist.append(new_user)

    def add_connection(self, user1, user2):
        #link between user1 and user2
        user1.connections.append(user2)
        user2.connections.append(user1)

    def print_users(self):
        # print every existing user
        for person in self.userlist:
            print(person)

    def print_connections(self, username):
        # print every connection for a specific user
        for connection in username.connections:
            print(connection)

def main():
    # Define the program flow for your user interface here.
    snap_cat = Network()

    megan = User("megan1", "Megan Kuo")

    snap_cat.print_connections(megan)


# Runs your program.
if __name__ == '__main__':
    main()
