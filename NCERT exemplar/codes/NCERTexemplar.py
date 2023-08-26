from scipy.stats import bernoulli

total_eggs = 400
bad_eggs = 14

prob_bad = bad_eggs/total_eggs

# Calculate the combined probability of selecting an envelope with no cash prize (X = 0)
probability_X_equals_0 = bernoulli(prob_bad).pmf(1) 
print("Probability of selecting bad egg (X = 0):", probability_X_equals_0)
print("The number of bad eggs:", bad_eggs)
