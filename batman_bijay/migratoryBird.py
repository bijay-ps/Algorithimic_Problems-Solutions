# Approach I
def migratoryBird(arr):
    arr_dict = {}
    for item in arr:
        arr_dict.update({item: arr.count(item)})
    max_val = max(arr_dict.values())
    keys = []
    for key, val in arr_dict.items():
        if max_val == val:
            keys.append(key)
    return min(keys)

# Approach II


def migratoryBirdII(arr):
    count_dict = {
        1: arr.count(1),
        2: arr.count(2),
        3: arr.count(3),
        4: arr.count(4),
        5: arr.count(5)
    }
    print(count_dict)
    max_val = max(count_dict.values())
    keys = []
    for key, val in count_dict.items():
        if max_val == val:
            keys.append(key)
    return min(keys)


birds_arr = [1, 1, 1, 2, 3, 1, 5, 5, 4, 4, 4, 4, 4, 4, 3, 2, 5, 4, 4, 1, 1, 1, 1, 1, 4,
             1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 3, 3, 3, 2, 1, 4, 4, 4, 1, 3, 5, 2]

print(f"birds_arr length is {len(birds_arr)}")

# res = migratoryBird(birds_arr)
# print(f"res: {res}")

res = migratoryBirdII(birds_arr)
print(f"res: {res}")
