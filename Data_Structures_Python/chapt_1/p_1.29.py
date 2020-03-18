s = ['a', 'b', 'c', 'd']

def get_perm(s, level=0):
    if len(s) == 1:
        return s
    else:
        words = []
        for i in range(len(s)):
            news = s[:i] + s[i+1:]
            print('\t'*level, 
            's[i]={0} news={1} level={2} '.format(s[i], news, level))
            new_words = get_perm(news, level+1)
            for w in new_words:
                print('\t' * (level+1), '{0} + {1}={2}'.format(s[i], w, s[i] + w))
                words.append(s[i] + w)
        return words


if __name__=='__main__':
    get_perm(s, 0)