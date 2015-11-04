import sys
import json

def main():
    sent_file = open(sys.argv[1])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    state_score = {}
    state_counts = {}
    num_valid_tweets = 0
    with open(sys.argv[2]) as f:
        content = f.read().splitlines()
        for row in content:
            data = json.loads(row)

            text = data.get('text', None)
            lang = data.get('lang', None)
            place = data.get('place', None)

            if not text: continue
            if not lang: continue
            if lang != 'en': continue
            if not place: continue
            if not place['country_code'] == 'US': continue
            state = place['full_name'].split(',')[1].strip()
            #print place
            #print state

            num_valid_tweets += 1

            text = data['text']
            words = text.split(' ')
            tweet_score = 0
            for word in words:
                if word in scores:
                    tweet_score += scores[word]

            if state in state_score:
                state_score[state] += tweet_score
                state_counts[state] += 1
            else:
                state_score[state] = 0
                state_counts[state] = 1.0

            #print tweet_score

    max_score = 0
    max_state = 'AK'
    for state, score in state_score.iteritems():
            this_score = state_score[state] / state_counts[state]
            if state_score > max_score:
                max_score = this_score
                max_state = state

    print max_state

if __name__ == '__main__':
    main()
