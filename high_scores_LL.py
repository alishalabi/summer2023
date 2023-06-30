"""
Design a data structure to store high scores of a video game.
Constraints:
- We want to keep a record of only the last X number of high scores (ex: capactiy = 10)
- If we want to add a high score when our data struct is at capacity, override the oldest entry
- We want to be have access to Y number of ALL TIME top scores (ex: top_scores = 3)
- High scores should be accessible even if the score has been overridden from the data sctruct
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ScoreBoard:
    def __init__(self, capacity=5, top_scores=3):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0
        self.high_scores = [0] * top_scores

    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        elif self.size < self.capacity:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.head = self.head.next
            self.tail.next = new_node
            self.tail = new_node

        if new_node.data > self.high_scores[-1]:
            self.high_scores[-1] = new_node.data
            self.high_scores = sorted(self.high_scores, reverse=True)

    def print_all(self):
        current_node = self.head
        # print(current_node)
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)

    def print_highscores(self):
        print(self.high_scores)


my_scoreboard = ScoreBoard()
my_scoreboard.add_node(1)
my_scoreboard.add_node(2)
my_scoreboard.add_node(5)
my_scoreboard.add_node(6)
my_scoreboard.add_node(9)
my_scoreboard.print_all()
my_scoreboard.print_highscores()

my_scoreboard.add_node(12)
my_scoreboard.add_node(8)
my_scoreboard.print_all()
my_scoreboard.print_highscores()
