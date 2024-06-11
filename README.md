# DFA Input and String Validation in Python
This Python script allows users to define a Deterministic Finite Automaton (DFA) and validate input strings against it. The DFA is defined using a 5-tuple, and the script interacts with the user to collect necessary information and validate strings.

## Features
- User Input for DFA Definition: The script prompts the user to input the states, alphabet, final states, and transition function.
- String Validation: Users can input strings to check if they are accepted by the DFA based on the defined transitions and final states.

## Getting Started
## Prerequisites
- Python 3.x

## Running the Script
- Clone the repository:
```bash
git clone https://github.com/Abdallah2A/DFA-Validation
```

- Run the script:
```bash
python dfa_validation.py
```
## Code Overview
- DFA Definition
The DFA is defined using user inputs for states, alphabet, final states, and transition functions.

- States Definition
The script prompts the user to input the number of states and their names.

- Alphabet Definition
The user is prompted to input the number of alphabets and the alphabets themselves.

- Final States
The user specifies the final states from the defined states.

- Transition Function
The user defines the transition function for each state and alphabet combination.

- String Validation
The spot function is used to check the transitions, and the main loop checks if the input string is accepted or rejected by the DFA.
