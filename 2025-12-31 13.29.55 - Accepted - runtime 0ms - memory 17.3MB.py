class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captured = 0
        i = 0
        
        while i < len(forts):
            if forts[i] == 1:
                # Start from your fort, look for empty (move to -1)
                j = i + 1
                while j < len(forts) and forts[j] == 0:
                    j += 1
                if j < len(forts) and forts[j] == -1:
                    max_captured = max(max_captured, j - i - 1)
            elif forts[i] == -1:
                # Start from empty, look for enemy (move to 1)
                j = i + 1
                while j < len(forts) and forts[j] == 0:
                    j += 1
                if j < len(forts) and forts[j] == 1:
                    max_captured = max(max_captured, j - i - 1)
            i += 1
        
        return max_captured