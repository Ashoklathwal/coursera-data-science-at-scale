import sys
import json

def main():
    num_terms = 0.0
    term_frequencies = {}

    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
        for row in content:
            data = json.loads(row)
            #print data

            if not 'lang' in data: continue
            if not 'text' in data: continue

            lang = data[u'lang']
            text = data[u'text']

            tweets_unknown_words = []
            words = text.split(' ')

            for word in words:
                #print words
                word = word.encode('utf-8')
                word = word.strip()
                if len(word) == 0: continue

                num_terms += 1
                if word in term_frequencies:
                    term_frequencies[word] += 1
                else:
                    term_frequencies[word] = 0

    for word, freq in term_frequencies.iteritems():
        print word, freq / num_terms

if __name__ == '__main__':
    main()
