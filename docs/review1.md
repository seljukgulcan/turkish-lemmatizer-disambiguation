## Morphological Disambiguation of Turkish Text with Perceptron Algorithm

[Main Page](index.html)

10.10.2018

The paper proposes an algorithm for finding the best fitting morphological parsing of a given word. In languages with complex morphological structure, a word can map to multiple morphemes sequences. Example in the paper:

 - alın (forehead)
 - al-ın (take it)

The paper tries to solve this ambiguity. Problem definition can be stated as finding a morphological parse (t) that maximize the probability of the parse given words (w_i) in the sentence. It is argmax_t P(t | w_1, w_2, ..., w_n) in mathematical terms.

The reason we chose this paper as first review is that our problem is similar with authors' and the method in the paper is proposed for Turkish language.

The paper compares their method with a trigram-based model. Trigram-based model is a simply 2-order markov chain. Firstly, it produces candidate morphological parses of given word. For each parse, it calculates the probability of that parse in the training set given previous 2 words. Then, morphological parse with the highest probability selected. Probability calculations are done on an already parsed set of words, which is known as training set.

The paper's approach is as follows: They generated 23 features manually. Some of them are syntactic (e.g. whether or not word occurring as last word of the sentence), morphological (e.g. number of inflectional groups) and depends on other words in the sentence (e.g. root of previous word). Then they use a single perceptron (or single layered neural network) to calculate likelihood of each parse. The paper argues that their method is superior than the baseline trigram-based model.

------

Sak, Haşim, Tunga Güngör, and Murat Saraçlar. "Morphological disambiguation of Turkish text with perceptron algorithm." International Conference on Intelligent Text Processing and Computational Linguistics. Springer, Berlin, Heidelberg, 2007. 