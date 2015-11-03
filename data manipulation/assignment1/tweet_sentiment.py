import sys
import json

def main():
    sent_file = open(sys.argv[1])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    with open(sys.argv[2]) as f:
        content = f.read().splitlines()
        for row in content:
            data = json.loads(row)
            if 'text' in data:
                text = data['text']
                words = text.split(' ')
                tweet_score = 0
                for word in words:
                    if word in scores:
                        tweet_score += scores[word]

                print tweet_score

if __name__ == '__main__':
    main()
