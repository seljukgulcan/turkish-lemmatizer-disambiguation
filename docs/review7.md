## A Perspective on Word Sense Disambiguation Methods and Their Evaluation 

[Main Page](index.html)

*27.11.2018*

Word sense disambiguation (WSD) is identifying correct sense of a word in a sentence, when the word has more than one meanings. The paper starts with an observation: Evaluation of WSD systems is not standardized. Studies use different corpora and different evaluation metrics. It leads to a situation that every researcher has to set up their own test environment and the difference between test environments makes comparing different models difficult.

Generally accepted evaluation criteria is accuracy. Accuracy for WSD is defined as the ratio of the number of exactly matched sense tags to the number assigned sense tags. The paper gives an example to show drawback of this criteria:

Word `interest` has 4 senses: `monetary`, `share`, `benefit` and `intellectual curiosity`. Let’s assume that meaning `share` is the correct one in a context. The following table shows probabilities returned by 4 imaginary systems:

| sense                  | 1   | 2   | 3   | 4    |
|------------------------|-----|-----|-----|------|
| monetary               | .47 | .85 | .28 | 1.00 |
| stake (correct)        | .42 | .05 | .24 | .00  |
| benefit                | .06 | .05 | .24 | .00  |
| intellectual curiosity | .05 | .05 | .24 | .00  |

It is a misclassification for all systems. Although system 1 gives a reasonable probability to correct sense and others are clearly worse than system 1. Accuracy criteria gives equal penalty to all systems. The author proposes a evaluation function that gives partial credit to avoid this problem.

`Sum of (-1/N) Pr_A(cs_i | w_i, context_i) for 0 < i < N`

where `N` is the number test cases, `Pr_A` is the probability of correct sense, `cs_i`, given word and context, assigned by system `A`. This cross entropy criteria gives better results to systems that are confident with their prediction.

------

Resni, Philip. "A perspective on word sense disambiguation methods and their evaluation." Tagging Text with Lexical Semantics: Why, What, and How? (1997).