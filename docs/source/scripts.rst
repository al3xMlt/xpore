.. _scripts:

Scripts
==========

We provide 2 main scripts to run the analysis of differential RNA modifications as the following.

1. ``xpore-dataprep``

Input
-------

Usage example
--------------

=================  ==========  =============== =============
Argument name(s)    Required    Default value   Description
=================  ==========  =============== =============
--eventalign=FILE       Yes         NA              Eventalign filepath, the output from nanopolish.         
--summary=FILE          Yes         NA              Eventalign summary filepath, the output from nanopolish.
--out_dir=DIR           Yes         NA              Output directory.
--ensembl=NUM           No          91              Ensembl version for gene-transcript mapping.
--species=STR           No          homo_sapiens    Species for ensembl gene-transcript mapping.
--genome                No          False           To run on Genomic coordinates. Without this argument, the program will run on transcriptomic coordinates.
--n_processes=NUM       No          1               Number of processes to run.
--readcount_max=NUM     No          1000            Maximum read counts per gene.
--resume                No          False           With this argument, the program will resume from the previous run.
=================  ==========  =============== =============

Output
--------

2. ``xpore-diffmod``

Input
--------

Usage example
--------------

=================  ==========  =============== =============
Argument name(s)    Required    Default value   Description
=================  ==========  =============== =============
--config=FILE           Yes         NA              Yaml configuraion filepath.
--n_processes=NUM       No          1               Number of processes to run.
--save_models           No          False           With this argument, the program will save the model parameters for each id.
--resume                No          False           With this argument, the program will resume from the previous run.
--ids=LIST              No          []              Gene / Transcript ids to model.
=================  ==========  =============== =============

Output
--------
   
