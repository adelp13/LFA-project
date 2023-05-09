class DFA:
    def __init__(self):
        self.finalStates = []
        self.transitions = {}
        self.initialState = 'q0'
        self.statesNo = 0
        self.alphabet = []
        self.automatStates = []
        self.partition = [] #stocheaza partitia din care face parte fiecare stare la o anumita etapa a partitionarii
        self.partitionElements = [] #multimea partitiilor
        self.minimalDFA = {}
        self.initialStateMinDFA = ''
        self.finalStatesMinDFA = []

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
                self.transitions[line[i][0]] = {line[i][1]: []}
                self.transitions[line[i][0]][line[i][1]].append(line[i][2])
            elif line[i][1] not in self.transitions[line[i][0]]:
                self.transitions[line[i][0]][line[i][1]] = []
                self.transitions[line[i][0]][line[i][1]].append(line[i][2])
            else:
                self.transitions[line[i][0]][line[i][1]].append(line[i][2])

        self.finalStates = [x for x in line[len(line) - 1].split()]
        self.automatStates.sort()

        f.close()

    def eliminateUnreachableStates(self): #dupa citirea auomatului, eliminam starile inaccesibile
        accesibleStates = [self.initialState] # aici stocam starile in care se ajunge din starea initiala
        i = 0
        while i < len(accesibleStates):
            for letter in self.alphabet:
                if self.transitions[accesibleStates[i]][letter][0] not in accesibleStates:
                    accesibleStates.append(self.transitions[accesibleStates[i]][letter][0])
            i += 1

        while i < len(self.automatStates):
            if self.automatStates[i] not in accesibleStates: #daca este inaccesibila, o stergem din dictionar
                del self.transitions[self.automatStates[i]]
                self.automatStates.pop(i)
                self.statesNo -= 1
            else:
                i += 1

        self.partitionElements = [[] for i in range(2)]  # aici vom stoca partitiile la fiecare etapa de partitionare
        # momentan avem 2 partitii, separand starile finale de cele nefinale
        self.partition = [0] * self.statesNo
        for i in range(self.statesNo):
            if 'q' + str(i) in self.finalStates:
                self.partition[i] = 1
                self.partitionElements[1].append(i)
            else:
                self.partitionElements[0].append(i)


    def equivalentStates(self, a, b): #functia verifica daca 2 stari din aceeasi partitie sunt in continutare echivalente
        for letter in self.alphabet:
            first = self.transitions['q' + str(a)][letter][0]
            first = int(first[1:])
            second = self.transitions['q' + str(b)][letter][0]
            second = int(second[1:])
            if self.partition[first] != self.partition[second]:
                return False
        return True

    def partitioning(self): #calculeaza care sunt starile echivalente
        partitionat = False
        while not partitionat: # partitionam pana cand in toate partitiile raman stari echivalente
            partitionat = True
            partitionsNumber = len(self.partitionElements)
            for i in range(partitionsNumber): #pentru fiecare partitie verificam daca starile sale raman in continuare echivalente
                semiPartitions = [] # aici stocam subpartitiile generate
                # comparam fiecare stare din partitie cu prima stare din fiecare subpartitie, pana gasim o stare echivalenta
                # daca nu gasim, cream o noua subpartitie
                for j in range(len(self.partitionElements[0])):
                    same = 0
                    for k in range(len(semiPartitions)):
                        if self.equivalentStates(self.partitionElements[0][j], semiPartitions[k][0]):
                            same = 1
                            semiPartitions[k].append(self.partitionElements[0][j])
                            break
                    if same == 0: # nu s a gasit o subpartitie echivalenta cu starea curenta din partitie
                        semiPartitions.append([self.partitionElements[0][j]])

                self.partitionElements.pop(0) #partitia s-a spart in mai multe subpartitii, deci o stergem din multimea partitiilor
                if len(semiPartitions) > 1:
                    partitionat = False

                #adaugam semipartitiile in multimea de partitii
                for j in range(len(semiPartitions)):
                    self.partitionElements.append(semiPartitions[j])
                    for k in range(len(semiPartitions[j])):
                        self.partition[semiPartitions[j][k]] = partitionsNumber + j

    def calculateMinimalDFA(self):
        # starile care se afla in aceeasi partitie vor face parte din aceeasi stare
        statesList = ['q'] * len(self.partitionElements)  # transformam partitiile in stari
        for i in range(len(self.partitionElements)):
            initialState = finalState = False
            for j in range(len(self.partitionElements[i])):
                statesList[i] += str(self.partitionElements[i][j]) + '+'
                if 'q' + str(self.partitionElements[i][j]) == self.initialState:
                    #daca una dintre starile compnente este initiala, starea compusa din elem partitiei va fi de asemena initiala
                    initialState = True
                elif 'q' + str(self.partitionElements[i][j]) in self.finalStates:
                    finalState = True
            statesList[i] = statesList[i][:len(statesList[i]) - 1]
            if initialState:
                self.initialStateMinDFA = statesList[i]
            if finalState and statesList[i] not in self.finalStatesMinDFA:
                self.finalStatesMinDFA.append(statesList[i])

        for i in range(len(self.partitionElements)):
            for letter in self.alphabet:
                destination = self.transitions['q' + str(self.partitionElements[i][0])][letter][0]
                for j in range(len(self.partitionElements)):
                    if int(destination[1:]) in self.partitionElements[j]:
                        if statesList[i] not in self.minimalDFA.keys():
                            self.minimalDFA[statesList[i]] = {letter: statesList[j]}
                        else:
                            self.minimalDFA[statesList[i]][letter] = statesList[j]
                        break

        #acum aflam starile din care nu putem ajunge in vreo stare finala
        statesToFinal = self.finalStatesMinDFA.copy() # aici stocam starile din care se ajunge intr-o starea finala
        for i in range(len(statesList)): #analizam pe rand fiecare stare
            accesibleStates = [statesList[i]] #starile in care se poate ajunge plecand din ea
            j = 0
            finalRoute = False
            while j < len(accesibleStates) and not finalRoute: #se opreste cand am parcurs toate starile in care puteam ajunge
                #sau cand ajungem intr-o stare din multimea statesToFinal
                if statesList[i] in self.finalStatesMinDFA:
                    break
                for letter in self.alphabet:
                    if self.minimalDFA[accesibleStates[j]][letter] not in accesibleStates:
                        accesibleStates.append(self.minimalDFA[accesibleStates[j]][letter])
                        if self.minimalDFA[accesibleStates[j]][letter] in statesToFinal:
                            finalRoute = True #am ajuns din starea curenta intr o stare din care stim ca putem ajunge in ceva final
                            statesToFinal.append(statesList[i])
                            break
                j += 1

        i = 0
        while i < len(statesList): #parcurgem din nou toate starile
            if statesList[i] not in statesToFinal: #daca nu se poate ajunge intr-o stare finala, eliminam starea curenta
                for state in statesList:
                    for letter in self.alphabet:
                        if self.minimalDFA[state][letter] == statesList[i]: #stergem toate legaturile
                            del self.minimalDFA[state][letter]
                del self.minimalDFA[statesList[i]]
                statesList.pop(i)
                i -= 1
            i += 1

    def printMinimalDFA(self):
        for state in self.minimalDFA:
            for letter in self.minimalDFA[state]:
                print(state, letter, self.minimalDFA[state][letter])
        print("Initial state: ", self.initialStateMinDFA)
        print("Final states: ", *self.finalStatesMinDFA)


dfa = DFA()
dfa.readAutomat("minimal3.in")
dfa.eliminateUnreachableStates()
dfa.partitioning()
dfa.calculateMinimalDFA()
dfa.printMinimalDFA()