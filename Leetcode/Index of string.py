class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h = len(haystack)
        n = len(needle)

        if n > h:
            return -1

        start = 0

        while start <= h - n:

            matched = True

            for k in range(n):
                if haystack[start + k] != needle[k]:
                    matched = False
                    break

            if matched:
                return start

            start += 1

        return -1