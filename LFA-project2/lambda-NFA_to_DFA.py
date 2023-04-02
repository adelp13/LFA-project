class lambdaNFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {}
        self.lambdaTrans = []
        self.initialState = 'q0'
        self.statesNo = 0
        self.alphabet = []
        self.automatStates = []
        self.NFA = {}
        self.finalStatesNFA = []
        self.DFA = {}
        self.finalStatesDFA = []
        self.initialStateDFA = 'q0'
    def readAutomat(self, fileName):
        f = open(fileName)
        line = f.readlines()
        for i in range(len(line) - 1):
            line[i] = [x for x in line[i].split()]
            if line[i][1] not in self.alphabet:
                self.alphabet.append(line[i][1])
            if line[i][0] not in self.automatStates:
                self.statesNo += 1
                self.automatStates.append(line[i][0])
            if line[i][2] not in self.automatStates:
                self.statesNo += 1
                self.automatStates.append(line[i][2])
            if line[i][0] not in self.transitions.keys():
                 self.transitions[line[i][0]] = {line[i][1] : []}
                 self.transitions[line[i][0]][line[i][1]].append(line[i][2])
            elif line[i][1] not in self.transitions[line[i][0]]:
                 self.transitions[line[i][0]][line[i][1]] = []
                 self.transitions[line[i][0]][line[i][1]].append(line[i][2])
            else:
                self.transitions[line[i][0]][line[i][1]].append(line[i][2])

        self.finalStates = [x for x in line[len(line) - 1].split()]
        f.close()
    def lambdaTransitions(self, state, currentState):
        if currentState not in self.lambdaTrans[int(state[1:])]:
            self.lambdaTrans[int(state[1:])].append(currentState)
        if currentState in self.transitions:
            if 'lambda' in self.transitions[currentState]:
                states = tuple(self.transitions[currentState]['lambda'])
                for x in states:
                    if x not in self.lambdaTrans[int(state[1:])]:
                        self.lambdaTransitions(state, x)

    def calculateLambdaTransitions(self):
        self.lambdaTrans = [[] for i in range(self.statesNo)]
        for state in self.automatStates:
            self.lambdaTransitions(state, state)

    def calculateNFA(self):
        self.alphabet.sort()
        for state in self.transitions:
            #final state check:
            if state not in self.finalStatesNFA:
                finalState = False
                for q in self.lambdaTrans[int(state[1:])]:
                    if q in self.finalStates:
                        finalState = True
                        break
                if finalState:
                    self.finalStatesNFA.append(state)
            # lambda:
            st = self.lambdaTrans[int(state[1:])]
            for letter in self.alphabet:
                if letter == 'lambda':
                    continue
                st2 = []
                #letter:
                for x in st:
                    if x in self.transitions:
                        if letter in self.transitions[x]:
                            y = tuple(self.transitions[x][letter])
                            for z in y:
                                if z not in st2:
                                    st2.append(z)
                #lambda:
                st3 = []
                for x in st2:
                    for y in self.lambdaTrans[int(x[1:])]:
                        if y not in st3:
                            st3.append(y)
                #update NFA:
                st3.sort()
                if state not in self.NFA.keys():
                    self.NFA[state] = {letter: st3}
                else:
                    self.NFA[state][letter] = st3

    def calculateDFA(self):
        states = []
        states.append(tuple(sorted(self.lambdaTrans[int(self.initialState[1:])])))
        i = 0

        while i < len(states):
            finalFormKey = 'q'
            finalState = False
            for q in states[i]:
                finalFormKey += q[1:] + '+'
                # final state check:
                if q in self.finalStatesNFA:
                    finalState = True
            finalFormKey = finalFormKey[:len(finalFormKey) - 1]
            if finalState and finalFormKey not in self.finalStatesDFA:
                self.finalStatesDFA.append(finalFormKey)
            if i == 0:
                self.initialStateDFA = finalFormKey
            for letter in self.alphabet:
                if letter == 'lambda':
                    continue
                newState = []
                for q in states[i]:
                    if q in self.NFA.keys():
                        if letter in self.NFA[q]:
                            y = tuple(self.NFA[q][letter])
                            for z in y:
                                if z not in newState:
                                    newState.append(z)
                newState = tuple(newState)
                if len(newState) > 0:
                    newState = sorted(newState)
                    if newState not in states:
                        states.append(newState)
                    finalFormValue = 'q'
                    for q in newState:
                         finalFormValue += q[1:] + '+'
                    finalFormValue = finalFormValue[:len(finalFormValue) - 1]

                    #update DFA dictionary:
                    if finalFormKey not in self.DFA.keys():
                        self.DFA[finalFormKey] = {letter: finalFormValue}
                    else:
                        self.DFA[finalFormKey][letter] = finalFormValue
            i += 1

    def printDFA(self):
        for state in self.DFA:
            for letter in self.DFA[state]:
                print(state, letter, self.DFA[state][letter])
        print("Initial state: ", self.initialStateDFA)
        print("Final states: ", *self.finalStatesDFA)



automat = lambdaNFA()
command = input("Calculate: 0-NFA   1-DFA\n")
automat.readAutomat("lambda_nfa.in")
automat.calculateLambdaTransitions()
automat.calculateNFA()
if command == '0':
    for state in automat.NFA:
        print(state + ':', automat.NFA[state])
    print("Final states: ", *automat.finalStatesNFA)
else:
    automat.calculateDFA()
    automat.printDFA()
    # for state in automat.DFA:
    #     print(state + ':', automat.DFA[state])
    # print("Final states: ", *automat.finalStatesDFA)
