## Efficient estimation of word representations in vector space

[Main Page](index.html)

*01.11.2018*

Classical word representations ilke one-hot vectors cannot capture semantic relationships between words. word2vec method mentioned in the paper represents each word as fixed sized vectors. This representation make computing similarity between words easy and some relations can be modeled as arithmetic operations (e.g. `man + royal = king`).

Paper proposes two methods for converting words to vectors: Continuous Skip-gram Model and Continuous Bag-of-Words Model. 

Skip-gram model converts the problem into a binary classification task. It tries to find the probability that given word is a context word of given target word. Context words are word in the window of certain size, centered at target word. For example, Given sentence s and context interval 2:

`s : a + b + c + d + e`

Then `e` is context word of `c` but not `b`. If words are represented as vectors, the dot-product of two vectors gives co-occurrence probability of these words. Question is how to learn such vectors.

It turns out that it is simply a matrix factorization problem. Co-occurrence values are represented as a matrix (Let’s call as `O`). The goal is to find 2 dense matrices `W`, `C` such that `O = W x C`. Here, `W` is the word embedding matrix, `C` is context embedding matrix. By using iterative gradient methods these two matrices can be found and `W` matrix can be used as vector representation of words.

The paper shows some relationships which the model can capture. Some examples:

France-Paris, Italiy-Rome, Japan-Tokyo

Microsoft-Windows, Google-Android, IBM-Linux

------

Mikolov, Tomas, et al. "Efficient estimation of word representations in vector space." arXiv preprint arXiv:1301.3781 (2013).

