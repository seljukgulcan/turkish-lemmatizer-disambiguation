## Turkish TreeBank

[Main Page](index.html)

*06.12.2018*

Authors explains the process of building a Turkish syntactic corpus known as Turkish Treebank. Main points of the chapter are issues encountered during the development of the corpus, design choices such as how the information should be represented and the evolution of Turkish TreeBank.

#### Morphological Information Representation

They decided to use the following form:

`root+Infl_1 ˆDB+Infl_2 ˆDB+. . . ˆDB+Infl_n`

`Infl_i` is the inflectional features of morpheme `i` and `ˆDB` denotes the derivational boundaries. The paper gives representation of the word `evimdekiler` as an example:

`ev+Noun+A3sg+P1sg+LocˆDB+Adj+RelˆDB+Noun+Zero+A3pl+Pnon+Nom`

The number of inflectional groups per word is about 2. Although there is no limit to the number of inflection a word can have in theory, common words have less number of morphemes. That’s why the average number is 2.

#### The CoNLL Format

To be able to use Turkish Treebank in inter-language competitions, the format is adjusted to cover generally accepted format, namely The CoNLL format. In CoNLL format, the sentences are stored in a grid where each row represents a word. Columns of the grid shows different properties of words. Although this format is more human readable than original Turkish TreeBank format, it is not very expressive. Therefore, some of the information related to morphological structure is lost.

Author also mentions an annotation tool to generate such datasets. A review about this tool will be done at the later stages of the project.

------

Eryiğit, Oflazer, et al. 2018, “The Turkish Treebank” pp 273-289 in: Turkish Natural Language Processing. Springer, Cham.