# First, let's define the functions as described by the user for generating the list of sequences.
# Since we want to find the best path for the sequence of observations 'Red, Green, Red',
# we'll use the Viterbi algorithm to find the most probable sequence of states.

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[obs[0] + '|' + y]
        path[y] = [y]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t - 1][y0] * trans_p[y0 + '|' + y] * emit_p[obs[t] + '|' + y], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Don't need to remember the old paths
        path = newpath

    # Return the most probable sequence and its probability
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])


# Given parameters
states = ['A', 'B']
obs = ['Red', 'Green', 'Red']
start_p = {'A': 1.0, 'B': 0.0}
trans_p = {'A|A': 0, 'A|B': 1, 'B|A': 1, 'B|B': 0}
emit_p = {'Red|A': 1, 'Green|A': 0, 'Red|B': 0.25, 'Green|B': 0.75}

# Apply Viterbi algorithm
prob, path = viterbi(obs, states, start_p, trans_p, emit_p)
print(prob, path)
