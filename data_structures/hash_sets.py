""" --------------------------------------------------------------------------------------------- 
SCRIPT META DATA
Name: Pawan HK 
Date: 08/29/2025 
DS: Hash Set 
Utilization: 36
Description: A HashSet is a data structure that stores unique elements and provides very fast operations for adding, removing, and checking membership. It is usually implemented using a hash table under the hood.
END DATA
--------------------------------------------------------------------------------------------- """
import collections
hash_set = collections.defaultdict(set)

hash_set[1].add("Pawan")
hash_set[2].add("Yam")

print("Pawan" in hash_set[1])
print("Yam" in hash_set[2])

hash_set[1].remove("Pawan")

print("Pawan" in hash_set[1])
print("Yam" in hash_set[2])

