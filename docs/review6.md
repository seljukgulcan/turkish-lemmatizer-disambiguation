## Profile Hidden Markov Models

[Main Page](index.html)

[Go to presentation](presentations/Profile%20Hidden%20Markov%20Models.pdf)

*15.11.2018*

In this paper author reviews the literature on application of profile hidden Markov models (HMM) on biological sequence maching problems. This paper has been very impactful in many other bioinformatics applications in tha past two decades. We choose to review this paper to investigate feasibility of character level labeling techniques in our project. Although this paper is from bioinformatics domain, it is still of interest due to the nature of textual data is being similar to the morphological analysis task.

#### Profile HMMs

The profile HMMs are used to model known protein sequences for being able to recognize patterns in a larger query text. The profiles are being constructed from the set of sequences which represent amino-acids as they occur in the known protein coding genes. There are many families of proteins that are known to show very similar structure within of their members. Such sequences are aligned by their edit distance to represent a consensus. 

From this multi-sequence alignment profile, a first-order Markov chain learned to calculate the emission probabilites for _deletion_, _insertion_ and _match_ for each structural position of the sequence in the HMM.

The authors describe that the Viterbi algorithm is commonly used in order to generate sequence alignments. This methods was preferred in many applications because it is able to generate global or local alignment of a query text with respect to a family of sequences at once. These results are statistically meaningful because state transition and emission probabilities can directly be associated with the edit distances in the given multiple alignment scheme. 

#### Softwares and libraries

In this chapter, the authors describe the prominent software and model libraries. Authors have compare their profile HMM analysis toolkit HMMER for the first time in this chapter and briefly describe the HMM model design of the HMMER and compare respect to the other implementations.


#### Conclusions

The profile HMM models give an another perspective of us to look at our textual features. We have learned a way that hints to a model that can recognize morphological features at the letter level. Thus, we can further investigate a way to train a model that can recognize without depending on an external feature extraction to enumerate possible tags for each word in a sentence.

------

#### References

Eddy, S. R. (1998). Profile hidden Markov models. _Bioinformatics (Oxford, England)_, 14(9), 755-763.
