# LFA-project
DETERMINSTIC FINITE AUTOMATA AND NOT-DETERMINISTIC FINITE AUTOMATA:

This is a program written in Python which verifies if a word given is accepted by a NFA or a DFA
The user is asked to enter 0 if the automata is determinstic and 1 for a non-determinstic automata.
After that, the automata will be read from a specified file.<br/>

Exemple of input file:<br/>
	q0 b q0<br/>
 	q0 a q1<br/>
  	q1 a q1  <br />
  	q1 b q2<br />
  	q2 a q1<br/>
	q2 b q3 <br/>
	q3 b q1<br/>
	q3 a q4<br/>
	q4 a q4<br/>
 	q4 b q4<br/>
	q4<br/>

Explanation: q0, q1, q2, q3 and q4 are the states of the automata and on every line is written the connection between two states.<br/>
ex: on the second line, "q0 a q1" means we can get from state q0 to state q1 using letter 'a'.<br/>
On the last line we have the final states (in this case only q4)<br/>
If the user pressed '0' but the automata is non-deterministic, the program will specify that and it will stop.<br/>
Otherwise, the user will have to enter a word to be verified and if it is accepted by the DFA it will display the path.<br/>
For the word lambda, the user will press enter.
<br/>
In the NFA case, if the word is accepted, all the paths will be displayed.<br/>
If the program expects a NFA but the automata is a DFA, it will display "This is a DFA, not a NFA, but the word can still be verified:", because the function that calculates the paths for a NFA can aslo be used for a DFA, but vice-versa is not possible. <br/>

Using the input above, these are the outputs for the next cases:<br/>

  -user pressed 0, word = bbabbabba:<br/>
          Path: q0 q0 q0 q1 q2 q3 q4 q4 q4 q4<br/>
	  
  -user pressed 1, word = bbbbbbaaaaabbbabbaaaaaaab:<br/>
         This is a DFA, not a NFA, but the word can still be verified:<br/>
        Number of paths: 1<br/>
        q0 q0 q0 q0 q0 q0 q0 q1 q1 q1 q1 q1 q2 q3 q1 q1 q2 q3 q4 q4 q4 q4 q4 q4 q4 q4<br/>
	
 -user pressed 0, word = ababababababaaaaaba:<br/>
        Word not accepted<br/>
        
       
        
Another exemple of input file:<br/>
q0 0 q0<br/>
q0 1 q0<br/>
q0 1 q1<br/>
q0 1 q0<br/>
q1 0 q1<br/>
q1 1 q2<br/>
q2 0 q2<br/>
q0 1 q2<br/>
q2 0 q3<br/>
q3 1 q0<br/>
q2 q1<br/>

Outputs:<br/>

-user pressed 0:<br/>
      This is a NFA, not a DFA<br/>
      
-user pressed 1, word = 101010<br/>
      Number of paths: <br/>
      q0 q0 q0 q0 q0 q1 q1<br/>
      q0 q0 q0 q0 q0 q2 q2<br/>
      q0 q0 q0 q1 q1 q2 q2<br/>
      q0 q2 q3 q0 q0 q1 q1<br/>
      q0 q2 q3 q0 q0 q2 q2<br/>







