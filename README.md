# LFA-project
DETERMINSTIC FINITE AUTOMATA AND NOT-DETERMINISTIC FINITE AUTOMATA:

This is a program written in Python which verifies if a word given is accepted by a NFA or a DFA
The user is asked to enter 0 if the automata is determinstic and 1 for a non-determinstic automata.
After that, the automata will be read from a specified file.

Exemple of input file:
	q0 b q0
 	q0 a q1
  q1 a q1  
  q1 b q2
  q2 a q1
  q2 b q3
  q3 b q1
  q3 a q4
  q4 a q4
  q4 b q4
  q4

Explanation: q0, q1, q2, q3 and q4 are the states of the automata and on every line is written the connection between two states.
ex: on the second line, "q0 a q1" means we can get from state q0 to state q1 using letter 'a'.
On the last line we have the final states (in this case only q4)
If the user pressed '0' but the automata is non-deterministic, the program will specify that and it will stop.
Otherwise, the user will have to enter a word to be verified and if it is accepted by the DFA it will display the path.

In the NFA case, if the word is accepted, all the paths will be displayed.
If the program expects a NFA but the automata is a DFA, it will display "This is a DFA, not a NFA, but the word can still be verified:", because the function that calculates the paths for a NFA can aslo be used for a DFA, but vice-versa is not possible. 

Using the input above, these are the outputs for the next cases:
  -user pressed 0, word = bbabbabba:
          Path: q0 q0 q0 q1 q2 q3 q4 q4 q4 q4
  -user pressed 1, word = bbbbbbaaaaabbbabbaaaaaaab:
          This is a DFA, not a NFA, but the word can still be verified:
        Number of paths: 1
        q0 q0 q0 q0 q0 q0 q0 q1 q1 q1 q1 q1 q2 q3 q1 q1 q2 q3 q4 q4 q4 q4 q4 q4 q4 q4
 -user pressed 0, word = ababababababaaaaaba:
        Word not accepted
        
        
        
Another exemple of input file:
q0 0 q0
q0 1 q0
q0 1 q1
q0 1 q0
q1 0 q1
q1 1 q2
q2 0 q2
q0 1 q2
q2 0 q3
q3 1 q0
q2 q1
Outputs:
-user pressed 0:
      This is a NFA, not a DFA
-user pressed 1, word = 101010
      Number of paths: 
			q0 q0 q0 q0 q0 q1 q1
      q0 q0 q0 q0 q0 q2 q2
      q0 q0 q0 q1 q1 q2 q2
      q0 q2 q3 q0 q0 q1 q1
      q0 q2 q3 q0 q0 q2 q2







