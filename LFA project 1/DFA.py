class DFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {}
        self.path = ['0']
        self.currentState = '0'
    def readAutomaton(self, fileName):
        f = open(fileName)

        line = f.readlines()
        for i in range(len(line) - 1):
            line[i] = [x for x in line[i].split()]
            if line[i][0] not in self.transitions.keys():
                 self.transitions[line[i][0]] = {line[i][1]: line[i][2]}
            else:
                 self.transitions[line[i][0]][line[i][1]] = line[i][2]

        self.finalStates = [x for x in line[len(line) - 1].split()]
        #print(self.finalStates)
        #print(self.transitions)
        f.close()

    def calculatePath(self, word):
        if len(word) == 0:
            if self.currentState in self.finalStates:
                print("Path:", *self.path)
            else:
                print("Word not accepted")
            return
        elif word[0] in self.transitions[self.currentState]:
            self.path.append(self.transitions[self.currentState][word[0]])
            self.currentState = self.path[len(self.path) - 1]
            self.calculatePath(word[1:])
        else:
            print("Word not accepted")

class NFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {}
        self.path = ['0']
        self.currentState = '0'
    def readAutomaton(self, fileName):
        f = open(fileName)

        line = f.readlines()
        for i in range(len(line) - 1):
            line[i] = [x for x in line[i].split()]
            if line[i][0] not in self.transitions.keys():
                 self.transitions[line[i][0]] = {line[i][1] : []}
                 self.transitions[line[i][0]][line[i][1]].append(line[i][2])
            elif line[i][1] not in self.transitions[line[i][0]]:
                 self.transitions[line[i][0]][line[i][1]] = []
                 self.transitions[line[i][0]][line[i][1]].append(line[i][2])
            else:
                self.transitions[line[i][0]][line[i][1]].append(line[i][2])
                
        self.finalStates = [x for x in line[len(line) - 1].split()]
        print(self.finalStates)
        print(self.transitions)
        f.close()

    def calculatePath(self, word):
        if len(word) == 0:
            if self.currentState in self.finalStates:
                print("Path:", *self.path)
            else:
                print("Word not accepted")
            return
        elif word[0] in self.transitions[self.currentState]:
            self.path.append(self.transitions[self.currentState][word[0]])
            self.currentState = self.path[len(self.path) - 1]
            self.calculatePath(word[1:])
        else:
            print("Word not accepted")

nfa = NFA()
nfa.readAutomaton("nfa.in")
# command = int(input("Type 0 for DFA and 1 for NFA:"))
# if command == 0:
# dfa = DFA()
# dfa.readAutomaton("exempleOfInput.in")
# word = input("Word = ")
# word = [x for x in word]
# dfa.calculatePath(word)
# else:
#     nfa = NFA()
#     nfa.readAutomaton("exempleOfInput.in")
#     word = input("Word = ")
#     word = [x for x in word]
#     nfa.calculatePaths(word)