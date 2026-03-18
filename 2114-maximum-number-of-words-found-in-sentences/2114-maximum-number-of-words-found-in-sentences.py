class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
      max_words=0
      for sentence in sentences:
        word=sentence.split()
        maxs=len(word)
        max_words=max(max_words,maxs)
      return max_words 