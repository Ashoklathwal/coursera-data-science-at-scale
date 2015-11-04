import sys
import json

def main():
    sent_file = open(sys.argv[1])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    unknown_words = {}
    with open(sys.argv[2]) as f:
        content = f.read().splitlines()
        for row in content:
            data = json.loads(row)
            #print data

            text = data.get('text', None)
            lang = data.get('lang', None)

            tweets_unknown_words = []
            if text and lang and lang == 'en':
                words = text.split(' ')
                tweet_score = 0
                for word in words:
                    if word in scores:
                        tweet_score += scores[word]
                    else:
                        tweets_unknown_words.append(word)

            for unknown_word in tweets_unknown_words:
                if unknown_word in unknown_words:
                    unknown_words[unknown_word] += tweet_score
                else:
                    unknown_words[unknown_word] = tweet_score

    for word, score in unknown_words.iteritems():
        print word, score


if __name__ == '__main__':
    main()
