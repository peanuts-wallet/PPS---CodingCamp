
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def count_primes(n):
            cnt = 0
            for i in range(2, n + 1):
                prime = True
                j = 2
                while j * j <= i:
                    if i % j == 0:
                        prime = False
                        break
                    j += 1
                if prime:
                    cnt += 1
            return cnt

        def fact(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res

        p = count_primes(n)
        return (fact(p) * fact(n - p)) % MOD