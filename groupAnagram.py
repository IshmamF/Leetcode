# Problem: https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
        
        answer = anagram_map.values()
        return answer
# one way to improve memory complexity is by using a fixed size array of length 26 for each word
# time complexity is O(N * K * log(K)), where N is number of words, K is biggest length of a word
# space complexity is O(N * K)
