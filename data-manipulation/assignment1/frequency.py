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

            text = data.get('text', None)
            lang = data.get('lang', None)

            tweets_unknown_words = []
            if text and lang and lang == 'en':
                words = text.split(' ')

                for word in words:
                    num_terms += 1
                    if word in term_frequencies:
                        term_frequencies[word] += 1
                    else:
                        term_frequencies[word] = 0

    for word, freq in term_frequencies.iteritems():
        print word, freq / num_terms


if __name__ == '__main__':
    main()
