"""
 This is a graph problem and the shortest path we find with bfs approcah . the time complexity will
 be O(N^2 * M )
"""

from collections import defaultdict, deque


def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    if endWord not in wordList:
        return 0
    neighbor = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            neighbor[pattern].append(word)

    visited = set([beginWord])
    queue = deque([beginWord])
    level = 1
    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return level
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for nei in neighbor[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

        level += 1

    return 0


print(ladderLength("hit", 'cog',  ["hot", "dot", "dog", "lot", "log", "cog"]))
