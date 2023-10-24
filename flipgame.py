# problem: https://xiaoguan.gitbooks.io/leetcode/content/LeetCode/293-flip-game-easy.html

def flipGame(str: s): 
    moves = []
    map = {"+":"-", "-":"+"}
    i  = 0
    while i+1 < len(s):
    	if s[i] == s[i+1]:
    		if i+2 < len(s):
    			word = s[:i] + map[s[i]]*2 + s[i+2:]
    		else:
    			word = s[:i] + map[s[i]]*2
    		moves.append(word)
    	i += 1
    return moves
# intuition is to have two pointers, one at current index and the next at index after it
# Concatinate the signs before the value at the index, the flipped sign at that index and values after the index and index after it. 
# Time complexity = O(n) Space Complexity = O(n)
