pokemon = {'Bulbasaur', 'Squirtle', 'Charmander'}

print(pokemon, type(pokemon))

pokemon.add("Pikachu")
print(pokemon)

# Sets are mutable and unordered

pokemon.discard('Bulbasaur')
print(pokemon)

pokemon.add('Bulbasaur')
pokemon.add('Bulbasaur')
print(pokemon)

#sets can only have one of each thing

l = [1, 2, 3, 4, 5, 6, 3, 34, 5, 2, 4, 5, 3, 1, 2, 2]
print(l)
print(set(l))

# Frozen Set

x = frozenset(['let', 'it', 'go'])
print(x)

# frozen sets are immutable
