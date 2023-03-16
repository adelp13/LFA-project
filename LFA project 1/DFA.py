class DFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {}
        self.currentState = []
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

dfa = DFA()
dfa.readAutomaton("test.in")