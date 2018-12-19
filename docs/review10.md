## BRAT: a web-based tool for NLP-assisted text annotation

[Main Page](index.html)

*13.12.2018*

Dataset annotation can be considered as an inevitable step in supervised machine learning tasks. The quality of labeled dataset is directly related to the end result of supervised learning but annotation is also most time consuming and and costly step as it requires domain experts’ time. Many annotation tools are developed to help annotaters in this process. Authors proposes such annotation tool called BRAT which is specially designed for NLP data.

The authors state that the tool is highly configurable so it can be used in any text annotation task. Most annotation tasks can be summarized as selecting a group of letters and assigning a type. POS-tagging can be given as an example of span-assign task. Other areas that the tool is used includes semantic role labeling, chunking and dependency annotation.

The tool can also be used for validation purposes. It support common NLP corpora formats. Therefore, automatically labeled datasets can be imported and validated by human annotators. Statistical systems can be integrated into the annotation system to show options for the annotator on the fly. They used machine learning based semantic class disambiguation system to test this feature. The machine learning model was capable of offering multiple outputs with probabilities. According to the experiments mentioned in the paper, BRAT reduces the annotation time by 15.4%.

Download and Github links (https://github.com/nlplab/brat) for the software are given in the paper. It is nice to see that the tool is still used and maintained. We had planned to review another paper about the annotation tool that is mentioned in Oflazer’s Turkish Language Processing book but we couldn’t access the tool from the links on the book. Therefore, we decided to review this paper instead.

------

Stenetorp, Pontus, et al. "BRAT: a web-based tool for NLP-assisted text annotation." Proceedings of the Demonstrations at the 13th Conference of the European Chapter of the Association for Computational Linguistics. Association for Computational Linguistics, 2012.