import csv
import matplotlib.pyplot as plt


def generate_population_dictionary_from_csv(filename):
  """Generates a dictionary of population per continent from CSV file in format"""
  output = {}

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])

      if continent not in output:
        output[continent] = {'populations': [], 'years': []}

      output[continent]['populations'].append(population)
      output[continent]['years'].append(year)

  return output


def generate_population_plots_from_dictionary(population_dictionary):
  """Generates a plot for each continent in the population dictionary."""
  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    populations = population_dictionary[continent]['populations']
    plt.plot(years, populations, label=continent, marker='o', alpha=0.5)

  plt.title('Global Netizens (Internet Users per Continent)')
  plt.xlabel('Year')
  plt.ylabel('Internet Users (Billions)')
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()


filename = 'data.csv'

population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)
