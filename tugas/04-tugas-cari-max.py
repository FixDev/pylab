def search_max_number(seq):
    imax = 0
    max = 0
    for i in range(0, len(seq)):
        if(seq[i] > max):
            imax = i
            max = seq[i]

    print(f"imax => {imax}")
    print(f"max => {max}")


search_max_number([100, 20, 40, 10, 90])
