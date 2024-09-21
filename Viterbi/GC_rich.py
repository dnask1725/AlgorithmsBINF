# In order to determine if a given sequence is likely from a GC-rich region or the background,
# we can calculate the likelihood of the sequence under each model (Background and GC-rich)
# by multiplying the emission probabilities of each observed nucleotide.

def calculate_likelihood(sequence, emit_p, state):
    # Start with a likelihood of 1, then multiply by each nucleotide's emission probability
    likelihood = 1.0
    for nucleotide in sequence:
        likelihood *= emit_p[nucleotide][state]
    return likelihood

# Given parameters from the HMM architecture
emit_p = {
    'A': {'Background': 0.25, 'GC-rich': 0.10},
    'T': {'Background': 0.25, 'GC-rich': 0.10},
    'C': {'Background': 0.25, 'GC-rich': 0.40},
    'G': {'Background': 0.25, 'GC-rich': 0.40}
}

# Hypothetical DNA sequence
sequence = 'TCGCAGCGCGCGCGCGCTTAAC'

# Calculate likelihoods for both Background and GC-rich states





likelihood_background = calculate_likelihood(sequence, emit_p, 'Background')
likelihood_gc_rich = calculate_likelihood(sequence, emit_p, 'GC-rich')

# Compare likelihoods to determine if the sequence is GC-rich or not
is_gc_rich = likelihood_gc_rich > likelihood_background

print(likelihood_background, likelihood_gc_rich, is_gc_rich)



