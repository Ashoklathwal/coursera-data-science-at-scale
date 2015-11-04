import sys
import json
import string

def main():
    hashtag_counts = {}

    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
        for row in content:
            data = json.loads(row)
            if not 'entities' in data: continue
            entities = data[u'entities']
            hashtags = entities[u'hashtags']
            for hashtag in hashtags:
                hashtag_text = hashtag[u'text'].encode('utf8')
                print hashtag_text
                hashtag_text = hashtag_text
                if hashtag_text in hashtag_counts:
                    hashtag_counts[hashtag_text] += 1
                else:
                    print hashtag_text
                    hashtag_counts[hashtag_text] = 0

    sorted_hashtags = list(sorted(hashtag_counts, key=hashtag_counts.__getitem__, reverse=True))
    for x in xrange(0, 10):
        print sorted_hashtags[x]

if __name__ == '__main__':
    main()
