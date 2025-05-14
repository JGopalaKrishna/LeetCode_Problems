MOD = 10**9 + 7
ALPHABET = 26

def mat_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Multiply two ALPHABET×ALPHABET matrices under MOD."""
    C = [[0] * ALPHABET for _ in range(ALPHABET)]
    for i in range(ALPHABET):
        Ai = A[i]
        Ci = C[i]
        for k in range(ALPHABET):
            aik = Ai[k]
            if aik:
                Bk = B[k]
                for j in range(ALPHABET):
                    Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
    return C

def mat_pow(M: List[List[int]], exp: int) -> List[List[int]]:
    """Fast exponentiation of a matrix M to the power exp under MOD."""
    R = [[1 if i == j else 0 for j in range(ALPHABET)] for i in range(ALPHABET)]  # Identity matrix
    while exp:
        if exp & 1:
            R = mat_mul(R, M)
        M = mat_mul(M, M)
        exp >>= 1
    return R

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Step 1: Build transition matrix T
        T = [[0] * ALPHABET for _ in range(ALPHABET)]
        for c in range(ALPHABET):
            for shift in range(1, nums[c] + 1):
                T[(c + shift) % ALPHABET][c] += 1

        # Step 2: Raise T to the power t
        Tt = mat_pow(T, t)

        # Step 3: Count the initial frequency of each character in s
        freq = Counter(s)
        result = 0

        # Step 4: Calculate the total number of characters after t transformations
        for ch, cnt in freq.items():
            col = ord(ch) - ord('a')
            col_sum = sum(Tt[row][col] for row in range(ALPHABET)) % MOD
            result = (result + cnt * col_sum) % MOD

        return result