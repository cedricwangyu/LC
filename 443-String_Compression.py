class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_char, curr_count, i = "", 0, 0
        while i < len(chars):
            c = chars[i]
            if c == prev_char:
                chars.pop(i)
                curr_count += 1
            if c != prev_char or i >= len(chars):
                if curr_count > 1:
                    for num_char in str(curr_count):
                        chars.insert(i, num_char)
                        i += 1
                i += 1
                prev_char, curr_count = c, 1