
# '''
# Basic hash table key/value pair
# '''


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = (hash * 33) + ord(char)
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_pair = Pair(key, value)
    hashed_key = hash(new_pair.key, hash_table.capacity)
    if hash_table.storage[hashed_key]:
        print(
            f"Warning: Storage already contains this {value}")
    hash_table.storage[hashed_key] = new_pair.value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)
    if not hash_table.storage[hashed_key]:
        print(f"Warning: {key} does not exist")
    else:
        hash_table.storage[hashed_key] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)
    if not hash_table.storage[hashed_key]:
        return None
    else:
        return hash_table.storage[hashed_key]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
