# import nltk
# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import subjectivity
# from nltk.sentiment import SentimentAnalyzer
# from nltk.sentiment.util import *

# nltk.download('subjectivity')
# n_instances = 100
# subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
# obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

# train_subj_docs = subj_docs[:80]
# test_subj_docs = subj_docs[80:100]
# train_obj_docs = obj_docs[:80]
# test_obj_docs = obj_docs[80:100]
# training_docs = train_subj_docs+train_obj_docs
# testing_docs = test_subj_docs+test_obj_docs

# sentim_analyzer = SentimentAnalyzer()
# all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

# unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

# sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

# training_set = sentim_analyzer.apply_features(training_docs)
# test_set = sentim_analyzer.apply_features(testing_docs)

# trainer = NaiveBayesClassifier.train
# classifier = sentim_analyzer.train(trainer, training_set)
# for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
#     print('{0}: {1}'.format(key, value))

# classifier.show_most_informative_features()

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentences = ["VADER is smart, handsome, and funny.", # positive sentence example
    "VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
    "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
    "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
    "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
    "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
    "The book was good.",         # positive sentence
    "The book was kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
    "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
    "A really bad, horrible book.",       # negative sentence with booster words
    "At least it isn't a horrible book.", # negated negative sentence with contraction
    ":) and :D",     # emoticons handled
    "",              # an empty string is correctly handled
    "Today sux",     #  negative slang handled
    "Today sux!",    #  negative slang with punctuation emphasis handled
    "Today SUX!",    #  negative slang with capitalization emphasis
    "Today kinda sux! But I'll get by, lol" # mixed sentiment example with slang and constrastive conjunction "but"
    ]
paragraph = "It was one of the worst movies I've seen, despite good reviews. \
Unbelievably bad acting!! Poor direction. VERY poor production. \
The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"

import nltk
from nltk import tokenize
nltk.download('punkt')
lines_list = tokenize.sent_tokenize(paragraph)
sentences.extend(lines_list)

tricky_sentences = [
   "Shout out to WSB, if I didn't see everyone mentioning TSLA puts I wouldn't have known to buy calls"
]
sentences.extend(tricky_sentences)
for sentence in sentences:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()

