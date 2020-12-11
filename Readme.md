##PPIs-XGBoost

Prediction of protein-protein interaction sites through eXtreme gradient boosting with kernel principal component analysis

###PPIs-XGBoost uses the following dependencies:

 * Python 3.6
 * numpy
 * scipy
 * scikit-learn
 * pandas

###Guiding principles: 

**The dataset file contains three datasets, among which dset72_fasta, dset164_fasta, dset186_fasta

**Feature extraction：
 * PseAAC.py is the implementation of PseAAC.
 * PsePSSM.m is the implementation of PsePSSM.
 * pssm_example.example, pssm_slide.m and PSSM_creat.m are the implementation of PsePSSM.
 * ASA_example.spd33 is the implementation of ASA.
 * Hy_index_exampie.index is the implementation of hydrophilic index.

**Feature_selection:
 * FA_selection is the implementation of FA.
 * ICA_selection is the implementation of ICA.
 * KPCA_selection is the implementation of KPCA.
 * LASSO_selection is the implementation of LASSO.
 * LR_selection is the implementation of LR.
 * MI_selection is the implementation of MI.
 * PCA_selection is the implementation of PCA.
 * SE_selection is the implementation of SE.

 
**SMOTE:
 * SMOTE.R is the implementation of SMOTE.
 
**Classifier:
 * AdaBoost_classifier.py is the implementation of Adaboost.
 * DT_classifier.py is the implementation of DT.
 * GBDT_classifier.py is the implementation of GBDT.
 * KNN_classifier.py is the implementation of KNN.
 * RF_classifier.py is the implementation of RF.
 * SVM_classifier.py is the implementation of SVM.
 * XGBoost_classifier.py is the implementation of XGBoost.
 * MLP_classifier.py is the implementation of MLP.
 * NB_classifier.py is the implementation of NB.


