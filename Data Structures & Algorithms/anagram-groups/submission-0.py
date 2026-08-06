class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge case: empty list
        if len(strs) == 0:
            return []

        anagrams = {} # {'act': ["act", "cat"]}
        for word in strs:
            word_sep = "".join(sorted(word))
            #print(word_sep)
            if word_sep in anagrams:
                anagrams[word_sep].append(word)
            else:
                anagrams[word_sep] = [word]
            
        return list(anagrams.values())

        