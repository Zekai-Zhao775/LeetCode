class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        bina = bin(a)[2:]
        binb = bin(b)[2:]
        binc = bin(c)[2:]
        print(bina)
        print(binb)
        print(binc)
        biggest_len = max(len(bina), len(binb), len(binc))
        bina = "0" * (biggest_len - len(bina)) + bina
        binb = "0" * (biggest_len - len(binb)) + binb
        binc = "0" * (biggest_len - len(binc)) + binc
        print(bina)
        print(binb)
        print(binc)
        for i in range(biggest_len):
            if bina[i] == "0" and binb[i] == "0" and binc[i] == "1":
                count += 1
            elif bina[i] == "1" and binb[i] == "0" and binc[i] == "0":
                count += 1
            elif bina[i] == "0" and binb[i] == "1" and binc[i] == "0":
                count += 1
            elif bina[i] == "1" and binb[i] == "1" and binc[i] == "0":
                count += 2
        return count