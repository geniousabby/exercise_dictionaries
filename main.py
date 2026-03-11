"""
Dictionary exercises
"""

# PETS:
# Make 3 dictionaries where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner's name.

pets = [

    {"Type": "dog", "owner": "Saanvi"},

    {"Type": "cat", "owner": "Saanvii"},

    {"Type": "fish", "owner": "Saanviii"}
]

# Store these dictionaries in a list called "pets".

# Next, loop through your list and as you do, print everything you know about each pet.

for pet in pets:
    print(f"\nPet kind: {pet['Type']}, owner: {pet['owner']}")

# Make sure the final output is nicely formatted and neat.


# PEOPLE:
# Make 3 dictionaries representing different people (their firstname, lastname, and phone number)
# and store all three dictionaries in a list called "people".

people = [

    {"Name": "Saanvi", "Last Name": "Ivnaas", "Phone number": "123456"},

    {"Name": "Saanvii", "Last Name": "Iivnaas", "Phone number": "234567"},

    {"Name": "Saanviii", "Last Name": "Iiivnaas", "Phone number": "345678"}
]

# Loop through your list of people, printing everything you know about each person.

for person in people:
    print(f"\nName: {person['Name']}, last name: {person['Last Name']}, phone number: {person['Phone number']}")

# Make sure the final output is nicely formatted and neat.


# CITIES
# Make a dictionary called "cities".
# Use the names of three cities as keys in your dictionary.

cities = [

    {"City": "Vancouver", "Country": "Canada", "Population": "662.25K", "Fun fact": "BC Place, the soccer stadium, has the largest retractable roof in the world with 7500 sq. meters of sky."},

    {"City": "Paris", "Country": "France", "Population": "2.05 million", "Fun fact": "Emperor Napoléon is buried in Les Invalides."},

    {"City": "Berlin", "Country": "Germany", "Population": "3.69 million", "Fun fact": "Berlin has 1,700 bridges, and more canals than Amsterdam and Venice combined!"}

]

for city in cities:
    print(f"\nName: {city['City']}, Country: {city['Country']}, Population: {city['Population']}, Fun fact: {city['Fun fact']}")

# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city.
# The keys for each city's dictionary should be something like "country, population, and fact".
# Print the name of each city and all of the information you have stored about it.
# Make sure the final output is nicely formatted and neat.
