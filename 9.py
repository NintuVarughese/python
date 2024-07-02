def set_union(set1, set2):
    return set1.union(set2)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

def main():
    set1 = set(input("Enter elements of the first set (separated by spaces): ").split())
    set2 = set(input("Enter elements of the second set (separated by spaces): ").split())

    print("\nSet Operations:")
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")

    union_result = set_union(set1, set2)
    print(f"Union: {union_result}")

    intersection_result = set_intersection(set1, set2)
    print(f"Intersection: {intersection_result}")

    difference_result = set_difference(set1, set2)
    print(f"Difference (Set1 - Set2): {difference_result}")

if __name__ == "__main__":
    main()
