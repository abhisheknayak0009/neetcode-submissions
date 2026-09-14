class Solution:
    def isHappy(self, n: int) -> bool:
       hashset = set()
       while True:
        if n == 1:
            return True
        if n in hashset:
            return False
        hashset.add(n)
        no = 0
        while(n > 0):
            rem = n%10
            no = no + (rem * rem)
            n = n//10
        n = no