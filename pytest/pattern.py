# Define the two lists
lista1 = ["a", "a", "a", "b", "b", "c", "d", "e"]
lista2 = ["pato", "pato", "pato", "mano", "mano", "perro", "gato", "jirafa"]

# Check if the lengths of the two lists are the same
if len(lista1) != len(lista2):
    print("Las listas no coinciden")
    exit(1)

# Define the two dictionaries (equivalent to associative arrays in Bash)
map1 = {}
map2 = {}

# Iterate over the indices and compare/match elements
for i in range(len(lista1)):
    key_list1 = lista1[i]
    key_list2 = lista2[i]
    print(key_list1)

    if key_list1 in map1:
        if map1[key_list1] != key_list2:
            print(f"las listas no coinciden, {key_list1} ya existe y vale {map1[key_list1]}, no {key_list2}")
            exit(1)
    else:
        if key_list2 in map2:
            print(f"las listas no coinciden, {key_list2} ya existe y vale {map2[key_list2]}, no {key_list1}")
            exit(1)
        map1[key_list1] = key_list2
        map2[key_list2] = key_list1

print("las listas coinciden")
