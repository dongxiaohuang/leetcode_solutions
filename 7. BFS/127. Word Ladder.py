from collections import deque


class Solution:

    def build_map(self, wordList):
        memory = {}
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + '*' + word[i+1:]
                memory[tmp] = memory.get(tmp, []) + [word]
        return memory

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        memory = self.build_map(wordList)
        queue = deque()
        queue.append(beginWord)
        steps = 1
        used = set([beginWord])
        while queue:
            count = len(queue)
            steps += 1
            # print(queue, steps)
            while count:
                top_word = queue.popleft()
                trs_words = []
                for i in range(len(top_word)):
                    tmp = top_word[:i] + '*' + top_word[i+1:]
                    if tmp in memory:
                        trs_words.extend(memory[tmp])
                count -= 1
                for word in trs_words:
                    if word not in used:
                        used.add(word)
                        if word == endWord:
                            return steps
                        queue.append(word)
        return 0
