from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 and str2 share the same repeating pattern
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute gcd of lengths
        length = gcd(len(str1), len(str2))
        
        # Return the substring of length gcd
        return str1[:length]


# -------------------------------
# Test locally
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(sol.gcdOfStrings("ABCABC", "ABC"))        # Expected: "ABC"
    print(sol.gcdOfStrings("ABABAB", "ABAB"))       # Expected: "AB"
    print(sol.gcdOfStrings("LEET", "CODE"))         # Expected: ""
