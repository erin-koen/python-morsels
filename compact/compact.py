def compact(sequence):
    interim_list = [
        i
        for i in sequence
    ]

    return iter([
        j
        for i, j in enumerate(interim_list)
        if i == 0 or interim_list[i-1] is not j
    ])
