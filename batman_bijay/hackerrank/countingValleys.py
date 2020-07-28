def countingValley(n, s):
    num_valleys, curr_level = 0, 0
    for step in steps:
        if curr_level == 0 and step == 'D':
            num_valleys += 1
        if step == 'U':
            curr_level += 1
        else:
            curr_level -= 1
    return num_valleys
