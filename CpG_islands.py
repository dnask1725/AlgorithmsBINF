def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    calculations = []  # To store detailed calculations for each step

    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
        calculations.append(f"Start {y}: {V[0][y]}")  # Record start probabilities

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
        step_details = []

        for cur_state in states:
            max_prob = -1
            chosen_state = None

            for prev_state in states:
                prob = V[t - 1][prev_state] * trans_p[prev_state][cur_state] * emit_p[cur_state][obs[t]]
                if prob > max_prob:
                    max_prob = prob
                    chosen_state = prev_state

            V[t][cur_state] = max_prob
            newpath[cur_state] = path[chosen_state] + [cur_state]
            step_details.append(f"Prob({obs[t]} in {cur_state} from {prev_state}): {prob}")

        path = newpath
        highest_prob_state = max(V[t], key=V[t].get)
        calculations.append(f"Step {t}: " + " | ".join(step_details))
        calculations.append(f"Highest probability at step {t} is {V[t][highest_prob_state]:.6f} for state {highest_prob_state}")

    # Return the most likely sequence and detailed calculations
    n = len(obs) - 1
    final_prob, final_state = max((V[n][y], y) for y in states)
    return (final_prob, path[final_state], calculations)


# Define the parameters
states = ('CpG+', 'CpG-')
observations = ('TCGCAGCTTAAC')
start_probability = {'CpG+': 0.5, 'CpG-': 0.5}
transition_probability = {
    'CpG+': {'CpG+': 0.6, 'CpG-': 0.4},
    'CpG-': {'CpG+': 0.4, 'CpG-': 0.6}
}
emission_probability = {
    'CpG+': {'A': 0.15, 'C': 0.35, 'G': 0.35, 'T': 0.15},
    'CpG-': {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}
}

# Apply the Viterbi algorithm and print detailed output
prob, path, detailed_calculations = viterbi(observations, states, start_probability, transition_probability, emission_probability)
print("Probability of the path:", prob)
print("Path through the states:", path)
print("\nDetailed Calculations:")
for calc in detailed_calculations:
    print(calc)

