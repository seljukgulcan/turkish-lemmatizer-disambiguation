## Morphological Disambiguation of Turkish Text with Perceptron Algorithm

[Main Page](index.html)

*17.10.2018*

The paper proposes a lemmatization method for Turkish words. Most common Turkish lemmatizers use either a huge database of suffixes or complicated syntax rules. The proposed method however relies on only a word corpus.

They try to model a bayesian graph to capture infection relationship of words. To give more detail, all words are represented as nodes in the graph. Directed edges show the similarity between words. That's, if a node A has an edge to node B it means word B is infected from word A. Therefore, if we start from a word (node) and follow its edges backward, the path leads us the lemma of the word.

The only inputs of this method are a set of words and corresponding lemma flags specifying whether the word is lemma or nonlemma. How they build this graph is as follows:
The similarity of each word pair is calculated. If similarity is larger than a threshold, an edge is created between them. The value of similarity determines the weight of the edge. They even proposed a similarity function specialized for Turkish language, which is similar to hamming distance but can handle consonant voicing change and syllable drop.

One another thing to note is that since a word may be linked with more than one neighbor, words can have multiple lemmas. To solve this ambiguity, it compares product of weights on candidate paths. Lemma having larger similarity product is selected. The paper argues that their method has over 91% correct lemmatization ratio.

------

Arslan, Enis, and Umut Orhan. "Graph-based lemmatization of Turkish words by using morphological similarity." INnovations in Intelligent SysTems and Applications (INISTA), 2016 International Symposium on. IEEE, 2016.