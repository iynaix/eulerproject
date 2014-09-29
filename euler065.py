from collections import defaultdict, Counter
import itertools


def gen_combi_tuples(N):
    combi_sums = defaultdict(list)
    for combi in itertools.combinations(range(1, 2 * N + 1), 3):
        combi_sums[sum(combi)].append(combi)

    for s, combis in combi_sums.iteritems():
        if len(combis) < N:
            continue
        for s in itertools.combinations(combis, N):
            yield s


def largest_ngon_repr(ngon, first_digit):
    ngon = list(list(a) for a in ngon)
    num_cnts = Counter(itertools.chain(*ngon))

    def pop_arm(digit):
        #gets and removes the arm with the given digit
        for a in ngon:
            if digit in a:
                break
        ngon.remove(a)
        return a

    ret = []
    first_arm = pop_arm(first_digit)
    first_arm.remove(first_digit)
    ret.append([first_digit] + sorted(first_arm, reverse=True))

    while ngon:
        d = ret[-1][2]
        next_arm = pop_arm(d)
        next_arm.remove(d)
        if num_cnts[next_arm[0]] == 1:
            ret.append([next_arm[0], d, next_arm[1]])
        else:
            ret.append([next_arm[1], d, next_arm[0]])

    return int(''.join(str(x) for x in itertools.chain(*ret)))


def euler65():
    N = 5
    viable_ngons = defaultdict(list)
    first_digit = 0

    for s in gen_combi_tuples(N):
        num_cnts = Counter(itertools.chain(*s))
        if len(num_cnts) != 2 * N:
            continue
        if Counter(num_cnts.values()).values() != [N, N]:
            continue
        #calculate first digit of n-gon
        first_digit = min([d for d, cnt in num_cnts.most_common() if cnt == 1])
        viable_ngons[first_digit].append(s)

    first_digit, ngons = sorted(viable_ngons.items())[-1]
    return max(largest_ngon_repr(ngon, first_digit) for ngon in ngons)
