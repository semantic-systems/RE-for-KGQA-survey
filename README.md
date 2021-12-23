# Relation Extraction

Relation Extraction (RE) is the procedure used to detect the relations between various entities in (unstructured/unlabelled) texts. RE is a very actively researched field and there have been a lot of very interesting papers and promising algorithms proposed in the recent years along with a multitude of high quality datasets. 

This repositories goal is to provide an overview of the current research challenges and how they are adressed. 

If some links appear broken, you can feel free to update that link and issue a pull request. (Or you can just notify me, that's fine too.)

## Surveys:

1. [(Bach and Badaskar, 2007) A Review of Relation Extraction](https://www.cs.cmu.edu/~nbach/papers/A-survey-on-Relation-Extraction.pdf)
2. [(de Abreu et al., 2013) A review on Relation Extraction with an eye on Portuguese](https://link.springer.com/article/10.1007/s13173-013-0116-8)
3. [(Konstantinova, 2014) Review of Relation Extraction Methods: What is New Out There?](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.727.1005&rep=rep1&type=pdf)
4. [(Asghar, 2016) Automatic Extraction of Causal Relations from Natural Language Texts: A Comprehensive Survey](https://arxiv.org/pdf/1605.07895.pdf)
5. [(Kumar, 2017) A Survey of Deep Learning Methods for Relation Extraction](https://arxiv.org/pdf/1705.03645)
6. [(Pawar et al., 2017) Relation extraction: A survey](https://arxiv.org/abs/1712.05191)
7. [(Cui et al., 2017) A Survey on Relation Extraction](https://books.google.de/books?hl=en&lr=&id=o-FHDwAAQBAJ&oi=fnd&pg=PA50&ots=fzj45p0LGl&sig=4jszWDQYxbhRU2y5kqUubk2l8Kc&redir_esc=y#v=onepage&q&f=false)
8. [(Chakraborty et al., 2019) Introduction to Neural Network based Approaches for Question Answering over Knowledge Graphs](https://arxiv.org/pdf/2007.13069.pdf)
9. [(Han et al., 2020) More Data, More Relations, More Context and More Openness: A Review and Outlook for Relation Extraction](https://arxiv.org/pdf/2004.03186.pdf)
10. [(Fu et al., 2020) A Survey on Complex Question Answering over Knowledge Base: Recent Advances and Challenges](https://arxiv.org/pdf/2007.13069.pdf)
11. [(Yang et al., 2021) A Survey on Extraction of Causal Relations from Natural Language Text](https://arxiv.org/pdf/2101.06426)
12. [(Nayak et al., 2021) Deep Neural Approaches to Relation Triplets Extraction: A Comprehensive Survey](https://arxiv.org/pdf/2103.16929)
13. [(Wang et al., 2021) Deep Neural Network Based Relation Extraction: An Overview](https://arxiv.org/pdf/2101.01907)
14. [(Aydar et al., 2021) Neural Relation Extraction: A Review](https://journals.tubitak.gov.tr/elektrik/issues/elk-21-29-2/elk-29-2-35-2005-119.pdf)
15. [(Pawar et al., 2021) Techniques for Jointly Extracting Entities and Relations A Survey](https://arxiv.org/pdf/2103.06118)
16. [(Lan et al., 2021) A Survey on Complex Knowledge Base Question Answering: Methods, Challenges and Solutions](https://arxiv.org/pdf/2105.11644.pdf)

## Knowledge Graphs / Knowledge Bases
1. DBpedia [Website](https://www.dbpedia.org) / [GitHub](https://github.com/dbpedia/) / [Paper](http://svn.aksw.org/papers/2013/SWJ_DBpedia/public.pdf)
2. Freebase [Website](https://developers.google.com/freebase) / DEPRECATED / [Paper](https://dl.acm.org/doi/10.1145/1376616.1376746)
3. YAGO [Website](https://yago-knowledge.org) / [Latest Release](https://yago-knowledge.org/downloads/yago-4) / [Paper](https://suchanek.name/work/publications/eswc-2020-yago.pdf)
4. Wikidata [Website](https://www.wikidata.org/wiki/Wikidata:Main_Page) / [Paper](https://dl.acm.org/doi/pdf/10.1145/2629489)

## Datasets:

Here is a distribution of some of the most used datasets showing their usage frequency in over 550 papers.

<p align="center">
   <img src="./figures/research_distribution.png" alt="drawing" width="600"/>
</p>

If you created a new dataset or found something missing, please don't hesitate to create a pull request to add it here.

1. Datasets for Semantic Parsing
   1. LC-QuAD [Paper](http://lc-quad.sda.tech/static/ISWC2017_paper_152.pdf) / [Website](http://lc-quad.sda.tech) / [Repository](https://github.com/AskNowQA/LC-QuAD) 
   1. LC-QuAD 2.0 [Paper](http://jens-lehmann.org/files/2019/iswc_lcquad2.pdf) / [Website](http://lc-quad.sda.tech)
   1. ComplexWebQuestions [Paper](https://arxiv.org/pdf/1803.06643.pdf) / [Website](https://www.tau-nlp.org/compwebq) 
   1. WebQuestionsSP [Paper](https://aclanthology.org/P16-2033.pdf) / [Download](https://www.microsoft.com/en-us/download/details.aspx?id=52763)
   1. QALD Series [Website](http://qald.aksw.org/)
   1. CompositionalFreebaseQuestions (CFQ) [Paper](https://arxiv.org/pdf/1912.09713.pdf) / [Repository](https://github.com/google-research/google-research/tree/master/cfq) 

1. Datasets for Information Retrieval
   1. SimpleQuestions [Paper](https://arxiv.org/pdf/1506.02075v1.pdf) / [Repository](https://github.com/davidgolub/SimpleQA/tree/master/datasets/SimpleQuestions)
   1. WebQuestions [Paper](https://aclanthology.org/D13-1160.pdf) / [Website](https://nlp.stanford.edu/software/sempre/)
   1. ComplexQuestions (unfortunately, there are 2 datasets with the same name <i>ComplexQuestions</i>)
      1. ComplexQuestions (a.k.a. <i>CompQ</i>) [Paper](https://aclanthology.org/C16-1236.pdf) / [Repository](https://github.com/JunweiBao/MulCQA/tree/ComplexQuestions)
      1. ComplexQuestions [Paper](https://dl.acm.org/doi/10.1145/3038912.3052583) / [Website](https://worksheets.codalab.org/worksheets/0x91d77db37e0a4bbbaeb37b8972f4784f) – Note that the dataset was provided by a different author
   1. MetaQA [Paper](https://arxiv.org/abs/1709.04071) / [Repository](https://github.com/yuyuz/MetaQA)

1. Datasets for Reinforcement Learning
   1. UMLS [Paper](https://dl.acm.org/doi/10.1145/1273496.1273551) / [Repository](https://github.com/shehzaadzd/MINERVA/tree/master/datasets/data_preprocessed/umls) ([MINERVA](https://arxiv.org/abs/1711.05851) Repository)
   1. NELL-995 [Paper](https://arxiv.org/abs/1707.06690) / [Repository](https://github.com/shehzaadzd/MINERVA/tree/master/datasets/data_preprocessed/nell-995)([MINERVA](https://arxiv.org/abs/1711.05851) Repository)


1. Datasets for Hybrid KGQA
   1. CommonSenseQA [Paper](https://arxiv.org/abs/1811.00937) / [Website](https://www.tau-nlp.org/commonsenseqa)
   1. OpenBookQA [Paper](https://arxiv.org/abs/1809.02789) / [Website](https://allenai.org/data/open-book-qa)

## Research Challenges:

