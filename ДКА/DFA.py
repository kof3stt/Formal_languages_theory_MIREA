def bfs(new_states, stf):
    if not (len(temp_states)):
        return
    initial = temp_states[0]
    if initial in new_states:
        return
    new_states.append(initial)
    for alpha in alphabet:
        string = set()
        for inst in initial:
            for trans in stf:
                if trans[1] == alpha and inst == trans[0] and trans[2] not in string:
                    string.add(trans[2])
        string = ''.join(sorted(string))
        new_stf.append([initial, alpha, string])
        if (string not in new_states + temp_states) and len(string):
            temp_states.append(string)
    temp_states.pop(0)
    bfs(new_states, stf)


with open("nfa.txt") as file:
    info = [i.rstrip() for i in file.readlines()]
    states, alphabet, stf, finish = [], [], [], []
    new_stf, new_states = [], []
    for line in info:
        if line in ('Set of states:', 'The input alphabet:', 'State-transitions function (current state, input character, next state):',
                    'A set of initial states:', 'A set of final states:'):
            status = line
        else:
            match status:
                case 'Set of states:':
                    states.append(line)
                case 'The input alphabet:':
                    alphabet.append(line)
                case 'State-transitions function (current state, input character, next state):':
                    stf.append(line.split())
                case 'A set of initial states:':
                    start = line
                case 'A set of final states:':
                    finish.append(line)
    temp_states = [start]
    bfs(new_states, stf)
    print("DFA:")
    print(f'Set of new states: {new_states}')
    print('State-transitions function: ')
    for state in new_stf:
        print(f'D({state[0]}, {state[1]}) = {state[2]}')
    print('Final states:')
    for i in new_states:
        for j in finish:
            if j in i:
                print(i)
