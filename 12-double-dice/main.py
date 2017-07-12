import pygal
from die import Die

# Create a pair of d6
die_1 = Die()
die_2 = Die()

# Roll, store results in list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze frequencies
frequencies = []
max_result = die_1.sides + die_2.sides
for val in range(2, max_result+1):
    frequency = results.count(val)
    frequencies.append(frequency)

# Visualize results
hist = pygal.Bar()

hist.title = "Results of rolling two d6 1000 times"
hist.x_labels = [str(n) for n in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 + D6', frequencies)
hist.render_to_file('roll_results.svg')
