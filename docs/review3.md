## Two-level description of Turkish morphology

[Main Page](index.html)

*25.10.2018*

This paper describes a morphological analysis method for Turkish word by using two-level morphology. Although our project is about choosing the right morphological root rather than generating morphological structures of words. Morphological parsing can be considered as preprocessing step for our project.

The motivation of two level morphology is as follows: Sometimes appening a suffix causes phonome to change. Example: baby -> babies (not babys). Two level morphology can handle such problems. There are two level in this architecture: lexical and surface. Surface level is the final form of word in paper (babies). The lexical level shows the combination of root and suffixes that are combined with boundary markers (baby+s). In this framework, these two levels are connected into a single automation with some rules.

The paper is consist of a list of such rules. Here is an example:

Rule : Deletes the beginning `s`, `n` or `y` of a suffix when it gets affixed to a tem ending in a consonant.

Lexical: `ev+nHn` (H represents the set of high vowels {ı, i, u, ü})
Surface: `ev00in` (0 represents epsilon transition, not consuming any input)

There are nominal roots ending with consonant which is repeated before certain suffixes.
hakkı (means (your) right) does not fit the rule of `hak+yH`.

By using such rules, paper forms finite state machines for nominal, verbal and compound noun morphotactics. The paper also mentions some exceptions to these rules such as:

Proposed finite state machines are implemented in PC-KIMMO environment, a two level processor for morphological analyses. The paper also states that it is slow compared to other method used in author’s previous work, Turkish spell checker. However, considering that it was in 1994. we think it is no longer an issue.


------

Oflazer, Kemal. "Two-level description of Turkish morphology." Literary and linguistic computing 9.2 (1994): 137-148.