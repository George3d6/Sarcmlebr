from random import choice


def scramble(text):
    phrases = text.split('\n')
    for x in range(0,len(phrases)):
        ignore_chars = set(['.',',','?','!',':',';','\'','"','\t'])
        words = phrases[x].split(' ')
        for i in range(0,len(words)):
            word = words[i]
            lw = len(word)
            if lw > 3:
                letters = list(word)

                begin = []
                start = 0
                for letter in letters:
                    begin.append(letter)
                    start +=1
                    if letter not in ignore_chars:
                        break

                end = []
                stop = lw
                for letter in reversed(letters):
                    end.append(letter)
                    stop -=1
                    if letter not in ignore_chars:
                        break
                end = list(reversed(end))

                try:
                    print(word)
                    print(end)
                except:
                    pass

                to_scramble = letters[start:stop]
                new_letters = []
                while len(to_scramble) > 0:
                    letter = choice(to_scramble)
                    to_scramble.remove(letter)
                    new_letters.append(letter)
                words[i] = ''.join([*begin,*new_letters,*end])
        phrases[x] = ' '.join(words)
    return '\n'.join(phrases)
