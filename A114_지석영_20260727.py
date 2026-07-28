# A114 Prime Arrangements
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 1000000007
        prime_count = 0

        # 1부터 n까지 소수 개수 계산
        for number in range(2, n + 1):
            is_prime = True
            divisor = 2

            while divisor * divisor <= number:
                if number % divisor == 0:
                    is_prime = False
                    break

                divisor += 1

            if is_prime:
                prime_count += 1

        non_prime_count = n - prime_count

        def factorial(number):
            result = 1

            for value in range(2, number + 1):
                result = (result * value) % mod

            return result

        return (
            factorial(prime_count)
            * factorial(non_prime_count)
        ) % mod

