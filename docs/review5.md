## Morphological Disambiguation for Turkish

[Main Page](index.html)

*08.11.2018*

This is a chapter of Turkish Natural Language Processing book, It presents a summary studies in the field of morphological disambiguation for Turkish language for past 25 years. Morphological ambiguity is having more than one morphological parse candidates for a word. An example from the paper shows 3 possible morphological interpretations for word 'evin':

ev+Noun+A3sg+P2sg+Nom -> (your) house

ev+Noun+A3sg+Pnon+Gen -> of the house

evin+Noun+A3sg+Pnon+Nom -> wheat grain

Methods for disambiguation can be divided into rules based methods and statistic methods.

#### Rule Based Methods

This approach uses a set of hand written rules for expression recognition and morphological disambiguation. Oflazer and Kuruoz's (1) study is reported to be first work on the field.

#### Statistical Methods

Below are some machine learning based methods that utilized labeled datasets.

##### Hidden Markov Models

Hidden Markov Models (HMM) try to find a sequence of morphological parse such that it maximazes posterior probability of the sequence given the sentence. To make calculations easier, they utilize some markov assumptions.

##### Discriminative Methods

Here, authors mention *Morphological Disambiguation of Turkish Text with Perceptron Algorithm* (2) paper that we have [reviewed](review1.html) earlier. What they propose is basically a perceptron model with 23 hand-crafted features. This work can regarded as one of the first neural network related studies in this field.

------

#### References

1 - Oflazer K, Kuruöz İ (1994) Tagging and morphological disambiguation of Turkish text. In:Proceedings of ANLP, Stuttgart, pp 144–149

2 - Sak, Haşim, Tunga Güngör, and Murat Saraçlar. "Morphological disambiguation of Turkish text with perceptron algorithm." International Conference on Intelligent Text Processing and Computational Linguistics. Springer, Berlin, Heidelberg, 2007. 

------

Hakkani-Tür, Dilek Zeynep, et al. 2018, "Morphological Disambiguation for Turkish." pp 53-67 in: Turkish Natural Language Processing. Springer, Cham.



