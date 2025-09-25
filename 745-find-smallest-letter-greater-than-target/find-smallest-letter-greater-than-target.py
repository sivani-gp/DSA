class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter = [ord(char) for char in letters]
        start = 0
        end = len(letter) - 1

        while start <= end:
            mid = (start + end) // 2
            if letter[mid] > ord(target):
                end = mid - 1
            else:
                start = mid + 1

        return letters[start % len(letters)]