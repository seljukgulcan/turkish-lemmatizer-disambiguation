## A Quick Tour of Word Sense Disambiguation, Induction and Related Approaches

[Main Page](index.html)

*27.11.2018*

Word Sense Disambiguation (WSD) is the task of finding the correct sense of a word in a given sentence context. Consider the following two sentences:

I can hear bass sounds.
They like grilled bass.

bass in the first sentence means low-frequency sound whereas it is a type of fish in the second sentence. WSD is the identification of correct meaning. A WSD system produces results like “They like/`ENJOY` grilled/`COOKED` bass/`FISH`” where each word is tagged with its meaning. To be able to tag words, an inventory of sense tokens is needed.

There are supervised and unsupervised approaches to this problem. Supervised methods utilizes an annotated training set. However, it is difficult to find a dataset that everybody agrees on labels. Unsupervised methods try to discover senses from unlabeled corpora. The main unsupervised methods:

Context Clustering: Assumption is that two word are semantically related if they are in the same context. The approach is similar to word2vec.
Word Clustering: Uses a similarity metric to calculate similarity between each pair of word in corpara. The aim is to put semantically similar words into the same group.
Co-occurrence Graph: Builds an analyses graph of words. Semantic relation between words are represented as graph edges.

There is also inter-language aspect of the problem. Cross-lingual WSD is a subproblem of WSD, the goal of Cross-lingual WSD is to find senses in a target language given input sentence in a source language. It it a popular problem in machine translation field.

------

Navigli, Roberto. "A quick tour of word sense disambiguation, induction and related approaches." International Conference on Current Trends in Theory and Practice of Computer Science. Springer, Berlin, Heidelberg, 2012.