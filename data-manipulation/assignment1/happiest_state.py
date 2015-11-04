import sys
import json

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

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

    print state

if __name__ == '__main__':
    main()
