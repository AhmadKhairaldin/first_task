class Person:
    def __init__(self, name):
        self.name = name

    def print(self):
        return f"Person {self.name}"

class Player(Person):
    def __init__(self, name, number, position,moved):
        super().__init__(name)
        self.number = number
        self.position = position
        self.__moved = moved
    def display(self):
        print(f"Player name is: {self.name} , number is : {self.number}, position: {self.position}")

    def get__moved(self):
            return  (self.__moved)

    def set__moved(self,new_moved):
        self.__moved = new_moved
class Team():
    def __init__(self,name,player):
        self.name = name
        self.player = player

    def dispaly(self):
        print(f"the team is :{self.name}, and the player name:{self.player}")

class Fan(Person):
    def __init__(self,name,player,team):
        super().__init__(name)
        self.player = player
        self.team = team

    def display(self):
        print(f"the fan name is :{self.name}, and encourages the player name:{self.player}, he/she play in team name is : {self.team}")

    def add(self,team):
        print(f"the name of new team is :{self.team}")
class Stadium():
    def __init__(self,name,capacity,team):
        self.name = name
        self.capacity = capacity
        self.team = team

    def display(self):
        print(f"the stad name is :{self.name}, the capacity is :{self.capacity},team name is play in stad is : {self.team}")




player1 = Player("Messi", 10, "forward","no")
player2 = Player("Xavi", 6, "midfielders","yes")

team1 = Team("Inter-miami",[player1.name])
team2 = Team("Barcelona",[player2.name])

fan =Fan("Ahmad",[player2.name],[team2.name])
fan2 = Fan("Iyad",[player1.name],[team1.name])

stad = Stadium("Camp-Nou",35000,[team2.name])
stad2 = Stadium("Lockhart",15000,[team1.name])

string_x = input("Please chosse the Stadium to know the palyer and fans : Camp-Nou or Lockhart\n")

if(string_x == "campnou"):
    stad.display()
    fan.display()
    player2.display()
    string_moved = input("this for research you with moved the player in other team :\n")
    if(string_moved == "yes"):
        player2.set__moved("yes")
        print("ohh the player is moved in next seasion !!",player2.get__moved())
    else:
        player2.set__moved("no")
        print("an sha' allah is not moved in the team !!",player2.get__moved())
    add2=input("enter your new team : ")
    # team.name = add
    fan.team.append(add2)
    fan.add(set(team2.name))

else:
    stad2.display()
    fan2.display()
    player1.display()
    string_moved = input("this for research you with moved the player in other team :\n")
    if (string_moved == "yes"):
        player2.set__moved("yes")
        print("ohh the player is moved in next season !!", player2.get__moved())
    else:
        player2.set__moved("no")
        print("an sha' allah is not moved in the team !!", player2.get__moved())
    add = input("enter your new team : ")
    # team.name = add
    fan2.team.append(add)
    fan2.add(team1.name)




