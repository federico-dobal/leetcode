class Solution(object):

    def buildWordsDictionary(self, w):
        words_dict = {}
        ix = 0
        last_break = 0

        while ix < len(w) - 1:
            if w[ix] != w[1 + ix]:
                #print(w[last_break:ix + 1])

                if w[ix] not in words_dict.keys():
                    words_dict[w[ix]] = [[last_break, ix + 1]]
                else:
                    words_dict[w[ix]].append([last_break, ix + 1])
                last_break = 1 + ix
            ix += 1

        if w[ix] not in words_dict.keys():
            words_dict[w[ix]] = [[last_break, ix + 1]]
        else:
            words_dict[w[ix]].append([last_break, ix + 1])

        return words_dict

    def isStretchy(self, target_dict, word):
        #print(target)
        #print(word)


        ix_word = 0
        last_break = 0

        word_dict = self.buildWordsDictionary(word)

        if set(word_dict.keys()) != set(target_dict.keys()):
            return False


        print(target_dict)
        print(word_dict)

        for c in word_dict.keys():
            c_in_target = target_dict.get(c)
            if c_in_target:
                c_in_word = word_dict.get(c)
                current_target_limits = c_in_target[0]
                current_word_limits = c_in_word[0]
                print(current_target_limits, current_word_limits)
                tl, tr = current_target_limits[0], current_target_limits[1]
                wl, wr = current_word_limits[0], current_word_limits[1]
                #print(tl, tr)
                #print(wr, wl)
                if tr-tl < wr-wl:
                    return False

                if tr-tl == wr-wl or tr-tl>=3:
                    pass
                else:
                    return False
                target_dict[c] = c_in_target[1:]
                word_dict[c] = c_in_word[1:]
            else:
                return False

        return all([not v for v in target_dict.values()]) and all([not v for v in word_dict.values()])

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        #for w in words:
        #    print(self.isStretchy(S, w))
        if S:
            target_dict = self.buildWordsDictionary(S)
            return sum([1 if self.isStretchy(target_dict, w) else 0 for w in words])
        else:
            return 0



s = Solution()
print(s.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
#print(s.expressiveWords("sass", ["sa"]))
#print(s.expressiveWords("", ["abc"]))
#""
#["hello", "hi", "helo"]
