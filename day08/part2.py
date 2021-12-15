from collections import Counter

segments = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

seg_counts = {s: len(v) for s,v in segments.items()}
freqs = Counter(seg_counts.values())

segments = {s: set(v) for s,v in segments.items()}

m = {}
uniq_lens = {len(segments[n]): n for n in [1,4,7,8]}

ans = 0

def pm():
    mm = {k: "".join(sorted(v)) for k,v in m.items()}
    print(mm)

def update_if(dig, prop, comp):
    global m

    if comp not in m or (prop in m and m[prop] == set(dig)):
        return True
    if prop in m:
        return False

    if len(m[comp].union(dig)) == 7:
        if prop in m:
            print(dig, prop, comp, m[comp])
            print(m[prop])
        assert prop not in m
        m[prop] = set(dig)

        return True
    return False



with open("input.txt") as f:
    for line in f:
        m = {}

        inp, out = line.strip().split(" | ")
        inp_digits = inp.split()
        output_digits = out.split()

        for dig in inp_digits:
            if len(dig) in uniq_lens: # 1,4,7,8
                m[uniq_lens[len(dig)]] = set(dig)

        while len(m) < 10:
            for dig in inp_digits:
                if len(dig) == 6:
                    if not update_if(dig, 6, 1): # 6
                        if not update_if(dig, 0, 4): # 0
                            assert 9 not in m or m[9] == dig
                            m[9] = dig

                elif len(dig) == 5:
                    if not update_if(dig, 2, 4): # 2
                        if not update_if(dig, 3, 6): # 3
                            assert 5 not in m or m[5] == dig
                            m[5] = dig

        for i in range(10):
            assert i in m

        mm = {"".join(sorted(v)):k for k,v in m.items()}
        ans += int("".join(str(mm["".join(sorted(o))]) for o in output_digits))

print(ans)
