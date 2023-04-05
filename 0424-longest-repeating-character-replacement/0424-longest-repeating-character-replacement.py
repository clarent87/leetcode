class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wordmap = Counter()
        l = deque()
        r = 0
        w_size = 1
        while r < len(s):
            # count word
            wordmap[s[r]] += 1
            # add word to qeueu
            l.append(s[r])
            # get count of most common value
            most_count = wordmap.most_common(1)[0][1]
            if most_count + k >= w_size:
                r += 1
                w_size +=1
            else:
                r += 1
                wordmap[l.popleft()] -= 1

        return w_size-1