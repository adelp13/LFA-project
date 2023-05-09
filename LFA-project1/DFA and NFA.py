class DFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {} #a double dictionary to store the automata
        self.initialState = 'q1' #q0 is supposed to be the initial state
        self.path = [self.initialState]
        self.currentState = self.initialState
        self.isDfa = True

    def readAutomaton(self, fileName):
        f = open(fileName)

        line = f.readlines()
        for i in range(len(line) - 1):
            line[i] = [x for x in line[i].split()]
            if line[i][0] not in self.transitions.keys():
                 self.transitions[line[i][0]] = {line[i][1]: line[i][2]}
            elif line[i][1] in self.transitions[line[i][0]]:
                    print("This is a NFA, not a DFA") #if the letter already has its origin in the key, this is not a DFA
                    self.isDfa = False
                    return
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
        elif self.currentState in self.transitions:
            if word[0] in self.transitions[self.currentState]:
                self.path.append(self.transitions[self.currentState][word[0]])
                self.currentState = self.path[len(self.path) - 1]
                self.calculatePath(word[1:])
        else:
            print("Word not accepted")

class NFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {}
        self.paths = []
        self.initialState = 'q0'
        self.pathsNo = 0
        self.multipleRoutes = 0 #if there aren't multiple routes in any point of the automata, it is actually a DFA
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
                self.multipleRoutes += 1

        self.finalStates = [x for x in line[len(line) - 1].split()]
        f.close()

    def calculatePaths(self, word, currentState, path):
        if len(word) == 0:
            if currentState in self.finalStates and path not in self.paths:
                self.paths.append(path)
                self.pathsNo += 1
            return
        if currentState in self.transitions:
            if word[0] in self.transitions[currentState]:
                states = tuple(self.transitions[currentState][word[0]])
                for x in states:
                        crtState = x
                        newPath = list(path)
                        newPath.append(crtState)
                        newPath = tuple(newPath)
                        self.calculatePaths(word[1:], crtState, newPath)
    def write(self):
        if self.multipleRoutes == 0:
            print("This is a DFA, not a NFA, but the word can still be verified:")
        if self.pathsNo == 0:
            print("Word not accepted")
        else:
            print(f"Number of paths: {self.pathsNo}")
            for p in self.paths:
                print(*p)

command = int(input("Type 0 for DFA and 1 for NFA: "))
if command == 0:
    dfa = DFA()
    dfa.readAutomaton("dfa.in")
    if dfa.isDfa == True:
        word = input("Word = ")
        word = [x for x in word]
        dfa.calculatePath(word)
else:
    nfa = NFA()
    nfa.readAutomaton("nfa.in")
    word = input("Word = ")
    word = [x for x in word]
    path = (nfa.initialState,)
    currentState = nfa.initialState
    nfa.calculatePaths(word, currentState, path)
    nfa.write()


    def equivalentStates(self, a,
                         b):  # functia verifica daca 2 stari din aceeasi partitie sunt in continutare echivalente
        for letter in self.alphabet:
            first = self.transitions['q' + str(a)][letter][0]
            first = int(first[1:])
            second = self.transitions['q' + str(b)][letter][0]
            second = int(second[1:])
            return self.partition[first] == self.partition[second]
        return True