---
title: Tutorial on Using FrameNet in NLP
---

# Tutorial: Getting the Roles Right: Using FrameNet in NLP

Time
: Afternoon.

Responsible
: Collin F. Baker, Nathan Schneider, Miriam R. L. Petruck, and Michael Ellsworth.

Course material
: See the outline below

## Abstract

The FrameNet lexical database (Fillmore & Baker 2010, Ruppenhofer et al. 2010, <http://framenet.icsi.berkeley.edu>), covers roughly 13,000 lexical units (word senses) for the core Engish lexicon, associating them with roughly 1,200 fully defined semantic frames; these frames and their roles cover the majority of event types in everyday, non-specialist text, and they are documented with 200,000 manually annotated examples. This tutorial will teach attendees what they need to know to start using the FrameNet lexical database as part of an NLP system. We will cover the basics of Frame Semantics, explain how the database was created, introduce the Python API and the state of the art in automatic frame semantic role labeling systems; and we will discuss FrameNet collaboration with commercial partners. Time permitting, we will present new research on frames and annotation of locative relations, as well as corresponding metaphorical uses, along with information about how frame semantic roles can aid the interpretation of metaphors.

## Outline

- Introduction [[*PDF slides*](tutorial-framenet-data/TutorialIntroCFBRev.pdf)]:

  * FrameNet and its relevance to NLP
  * Crucial differences from other resources
      * WordNet
      * PropBank
      * AMR
  * FrameNets in other languages
      * Spanish FN
      * Swedish FN++
      * Japanese FN
      * Multilingual FrameNet

- The Components of Berkeley FrameNet [[*PDF slides*](tutorial-framenet-data/FNComponentsMRLP.pdf)]:

  * Frames
  * Frame Elements (roles)
  * Frame-to-frame relations
  * Lexicographic annotation
  * Full-text annotation

- Demo of the FrameNet website [[*PDF slides*](tutorial-framenet-data/FNWebsiteDemoNAACL2015.pdf)]

- Using the Python API and NLTK integration [[*PDF slides*](tutorial-framenet-data/FrameNetAPI.pdf)]

- How FrameNet annotation works [[*PDF slides*](tutorial-framenet-data/FNDataCreationNAACL2015.pdf)]:

  * Vanguarding, subcorporation, and annotation
  * Frame creation
  * Current research on procedural improvements (crowdsourcing, etc.).

- Overview of ASRL research (including SEMAFOR) [[*PDF slides*](tutorial-framenet-data/SEMAFORslides.pdf)]

- Applications of FrameNet/ASRL [[*PDF slides*](tutorial-framenet-data/FNAppsFull.pdf)]:

  * FN Brasil: World Cup, Olympics
  * DAC collaboration

- Q&A / Discussion

## Instructors

Collin Baker
: (International Computer Science Institute, <collinb@icsi.berkeley.edu>), has been Project Manager of the FrameNet Project since 2000. His research interests include FrameNets in other languages (Loenneker-Rodman & Baker 2009), aligning FrameNet to other lexical resources (Fellbaum & Baker 2013, Ferrandez et al 2010), linking to ontologies and reasoning (Scheffczyk et al. 2010), and the frame semantics of metaphor.

Nathan Schneider
: (University of Edinburgh, <nschneid@inf.ed.ac.uk>, <http://nathan.cl>) has worked on a coarse-grained representation for lexical semantics (2014 dissertation at Carnegie Mellon University) and the design of the Abstract Meaning Representation (AMR; Banarescu et al. 2014). Nathan helped develop the leading open-source frame-semantic parser for English, SEMAFOR (Das et al. 2010, 2014) (<http://demo.ark.cs.cmu.edu/parse>), as well as a Python interface to the FrameNet lexicon (with Chuck Wooters) that is part of the NLTK suite.

Miriam R. L. Petruck
: (International Computer Science Institute, <miriamp@icsi.berkeley.edu>) received her PhD in Linguistics from the University of California, Berkeley. A key member of the team developing FrameNet almost since the project’s founding, her research interests include semantics, knowledge base development, grammar and lexis, lexical semantics, Frame Semantics and Construction Grammar.

Michael Ellsworth
: (International Computer Science Institute, <infinity@icsi.berkeley.edu>) has been involved with FrameNet for well over a decade. His chief focus is on semantic relations in FrameNet (Ruppenhofer et al. 2010), how they can be used for paraphrase (Ellsworth & Janin 2007), and mapping to other resources (Scheffczyk et al 2006, Ferrandez et al. 2010). Increasingly, he has examined the connection of FrameNet to syntax and the Constructicon (Torrent & Ellsworth 2013, Ziem & Ellsworth 2015), including in his pending dissertation on the constructions and frame semantics of emotion.

## References

Atkins,  B.T.S., Klavens,  J., and B. Levin. 1988. Anatomy of a verb entry: from linguistic theory to lexicographic practice. *International Journal of Lexicography* 1(2): 84--126

Baker, C., Ellsworth, M., & Erk, K. 2007. *SemEval-2007 Task 19: Frame Semantic Structure Extraction*. SemEval.

Banarescu, L., Bonial  C., Cai S., Georgescu,  M.,  Griffitt, K. Hermjakob,  M., Knight,  K. Koehn,  P. , Palmer, M., and Schneider. 2013. Abstract Meaning Representation for Sembanking. *Proceedings of LAW and Interoperability with Discourse*. 178--186.

Chang, N., Paritosh, P.  Huynh, D. and Baker, C. 2015. Scaling Semantic Frame Annotation. *Proceedings of The 9th Linguistic Annotation Workshop*. 1--10.

Das, D., Chen, D., Martins, A. F. T., Schneider, N., & Smith, N. A. 2014. Frame-semantic parsing. *Computational Linguistics* 40(1), 9-–56.

Das, D., Martins, A. F. T., and Smith, N. A. 2012. An exact dual decomposition algorithm for shallow semantic parsing with constraints. *\*SEM*.

Das, D., Schneider, N., Chen, D., & Smith, N. A. 2010. Probabilistic frame-semantic parsing. *NAACL-HLT*.

Das, D., and Smith, N. A. 2011. Semi-supervised frame-semantic parsing for unknown predicates. *ACL*.

Das, D., and  Smith, N. A. 2012. Graph-based lexicon expansion with sparsity-inducing penalties. *NAACL-HLT*.

Erk, K. and Padó, S. 2006. Shalmaneser - a toolchain for shallow semantic parsing. *LREC*.

Fillmore, C.  J. 1975. An  alternative  to  checklist theories of meaning. *Proceedings of  the    First Annual Meeting of the Berkeley Linguistics Society*, 123--131.

Fillmore, C. J.  1977. The case for case reopened. In Cole, P. and Sadock, J. (Eds.) *Syntax and Semantics: Grammatical Relations. Academic Press*. 8, 59--81.

Fillmore,    C. J.  1985. Frames and the semantics of understanding. *Quaderni di Semantica*, 6(2): 222--254.

Fillmore, C. J. 2012. Encounters with Language. *Computational  Linguistics*  38(4): 701--718.

Fillmore, C.J.  and  Atkins, B.T.S.. 1992. Towards a Frame-based organization of the lexicon: the semantics of RISK and its neighbors. In Lehrer, A. and E. Kitay (eds.) *Frames, Fields, and Contrasts: New Essays in Semantics and  Lexical Organization*. Hillsdale: Lawrence Erlbaum, 75--102.

Fillmore, C.  J. and  C. Baker. 2010.  A Frames Approach to Semantic Analysis. In Heine, B. and H. Narrog  (eds.), *The Oxford  Handbook of Linguistic Analysis*. Oxford: Oxford University Press, 791--816.

Fillmore, C. J., Johnson C. R., and Petruck,  M.R.L. 2003. Background to FrameNet. *International Journal of Lexicography*, 16(3):235--250.

Fontenelle, T. (ed.)  2003.  Special Issue on FrameNet and Frame Semantics. *International Journal of Lexicography* 16(3):231--385.

Fleischman, M., Kwon, N., and Hovy, E. 2003. Maximum entropy models for FrameNet classification. *EMNLP*.

Fürstenau, H., and Lapata, M. 2009. Semi-supervised semantic role labeling. *EACL*.

Gildea, D., and Jurafsky, D. 2002. Automatic labeling of semantic roles. *Computational Linguistics*, 28(3), 245--288.

Hermann, K. M., Das, D., Weston, J., and Ganchev, K. 2014. Semantic frame identification with distributed word representations. *ACL*.

Johansson, R., and Nugues, P. 2007. LTH: semantic structure extraction using nonprojective  dependency trees. *SemEval*.

Kwon, N., Fleischman, M., and Hovy, E. 2004. FrameNet-based semantic parsing using maximum entropy models. *Coling*.

Matsubayashi, Y., Okazaki, N., and Tsujii, J. 2009. A comparative study on generalization of semantic roles in FrameNet. *ACL-IJCNLP*.

Padó, S., and  Lapata, M. 2005. Cross-linguistic projection of role-semantic information. *HLT/EMNLP*.

Palmer, M., D. Gildea, and P. Kingsbury. 2005. The Proposition Bank: An Annotated Corpus of Semantic Roles. *Computational Linguistics*. 31:71--106.

Petruck,  M. R. L.  1996. Frame Semantics. *Handbook of Pragmatics*.

Petruck, M.R.L. and de Melo, G. 2012. Precedes: A Semantic relation in FrameNet. In Proceedings of the Workshop on Language Resources for Public Security Applications,  *Eighth   LREC Conference*, Istanbul,  45--49.

Ruppenhofer,J., Ellsworth, M., Petruck, M.R.L., Johnson, C.R., and Scheffczyk, J. 2010. FrameNet II: Extended  Theory and Practice. Web Publication.

Täckström, O., Ganchev, K., and Das, D. 2015. Efficient inference and structured learning for semantic role labeling. *TACL*, 3:29--41.

Thompson, C. A., Levy, R., and  Manning, C. D. 2003. A generative model for semantic role labeling. *ECML*.

Valverde-Albacete, F. J. 2008. Extracting Frame-Semantics Knowledge using Lattice Theory. *Journal of Logic and Computation*. 18:361--384.

Fellbaum, C. (Ed.) *WordNet: An Electronic Lexical Database*. MIT Press, 1998.
