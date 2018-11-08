## Morphological Disambiguation for Turkish

[Main Page](index.html)

*08.11.2018*

This is a chapter of Turkish Natural Language Processing book, it presents a summary of studies in the field of morphological disambiguation for Turkish language in past 25 years. Morphological ambiguity is defined as having more than one morphological parse candidates for a word. An example from the paper shows 3 possible morphological interpretations for word 'evin':

ev+Noun+A3sg+P2sg+Nom -> (your) house

ev+Noun+A3sg+Pnon+Gen -> of the house

evin+Noun+A3sg+Pnon+Nom -> wheat grain

Methods for disambiguation can be divided into rule based methods and statistical methods.

#### Rule Based Methods

This approach uses a set of hand written rules for expression recognition and morphological disambiguation. Oflazer and Kuruoz's (1) study is reported to be first work on the field. Authors state that they formed about 250 rules and the method halved the ambiguity a lexical functional grammar parser.

#### Statistical Methods

Below are some machine learning based methods that utilize labeled datasets.

##### Hidden Markov Models

Hidden Markov Models try to find a sequence of morphological parse such that it maximizes posterior probability of the sequence given the sentence. To make calculations easier, they utilize some markov assumptions such as morphological parse of a word depends on only parses of previous two words.

##### Discriminative Methods

Here, authors mention *Morphological Disambiguation of Turkish Text with Perceptron Algorithm* (2) paper that we have [reviewed](review1.html) earlier. What they propose is basically a perceptron model with 23 hand-crafted features. This work can regarded as one of the first neural network related studies in this field.

Lastly, the chapter mentions popular datasets used in the literature.

------

#### References

1 - Oflazer K, Kuruöz İ (1994) Tagging and morphological disambiguation of Turkish text. In:Proceedings of ANLP, Stuttgart, pp 144–149

2 - Sak, Haşim, Tunga Güngör, and Murat Saraçlar. "Morphological disambiguation of Turkish text with perceptron algorithm." International Conference on Intelligent Text Processing and Computational Linguistics. Springer, Berlin, Heidelberg, 2007. 

------

Hakkani-Tür, Dilek Zeynep, et al. 2018, "Morphological Disambiguation for Turkish." pp 53-67 in: Turkish Natural Language Processing. Springer, Cham.



