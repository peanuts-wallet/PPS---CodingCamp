class Solution:
    def countPrimes(self, n: int) -> int:
        # 2보다 작으면 소수가 존재하지 않음
        if n <= 2:
            return 0

        # is_prime[i]는 i가 소수인지 나타냄
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # i의 배수들은 소수가 아님
                for multiple in range(i * i, n, i):
                    is_prime[multiple] = False

        return sum(is_prime)