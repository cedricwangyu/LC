class Solution:
    def makeStringSorted(self, s: str) -> int:
        cnt, ans, tot, comb_tot = [0]*26, 0, 0, 1           # cnt - counter of the letters, tot - number of letters onward, comb_tot - see in the explanation 
        for cur_letter in s[::-1]:                          # Loop over all the letters from the end
            num = ord(cur_letter) - ord('a')                # Convert letter to number
            cnt[num] += 1                                   # Increment the counter for the current letter
            tot += 1                                        # Increment the number of letters from the current one onward
            comb_tot = (comb_tot * tot) // cnt[num]         # Iteratively update comb_tot
            ans = ans + (comb_tot * sum(cnt[:num]))//tot    # Add the number of combinations for all letters that are smaller than the current one
        return ans % 1_000_000_007