import pygal
from die import Die

# Create a basic d6
die = Die()

# Roll, store results in list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze frequencies
frequencies = []
for val in range(1, die.sides+1):
    frequency = results.count(val)
    frequencies.append(frequency)

# Visualize results
hist = pygal.Bar()

hist.title = "Results of rolling a d6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6', frequencies)
hist.render_to_file('roll_results.svg')
