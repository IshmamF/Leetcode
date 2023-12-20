# Problem: https://leetcode.com/problems/split-strings-by-separator/description/

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for strings in words:
            temp = strings.split(separator)
            for word in temp:
                if word:
                    output.append(word)

        return output

  # Python split operator takes care of finding the separators and splitting the word into lists
  # The overall time complexity would be O(k * n) where k is the number of strings in words list
  # and n is the number of words in each string 
