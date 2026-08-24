class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        #cleaned = [ word for word in words if word.strip() ]
        return len(words[-1])