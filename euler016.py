def euler16():
    def num_to_english(num):
        names = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred",
            1000: "thousand",
        }
        vals = sorted(names.keys())[::-1]
        n = num
        ret = []
        while n > 0:
            for v in vals:
                quot, rem = divmod(n, v)
                if quot > 0:
                    if (quot == 1 and v >= 100) or quot > 1:
                        ret.append(names[quot])

                    ret.append(names[v])
                    if v == 100 and rem > 0:
                        ret.append("and")
                    n -= v * quot

        return " ".join(ret)

    return sum(len(num_to_english(i).replace(" ", "")) for i in range(1, 1001))
