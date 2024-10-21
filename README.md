# awesome\-mave


List of software packages (and the people developing these methods) for multiplexed assays of variant effects.
[Contributions welcome](https://github.com/Constantiam-Biosciences-Inc/awesome-mave/blob/master/CONTRIBUTING.md)...


## Contents



* [awesome\-mave](#awesome-mave)
	+ [Contents](#contents)
	+ [Software Packages](#software-packages)
		- [Analysis Tools](#analysis-tools)
		- [In Silico Tools](#in-silico-tools)
		- [Visualization Tools](#visualization-tools)
	+ [Applications](#applications)
		- [Databases](#databases)
		- [Websites / Portals](#websites-portals)
	+ [Similar Collections](#similar-collections)
		- [Similar Collections](#similar-collections_1)
	+ [Tutorials](#tutorials)
		- [Tutorials](#tutorials_1)
	+ [Assays](#assays)
		- [Assays](#assays_1)



## Software Packages


### Analysis Tools


* [Enrich2](https://enrich2.readthedocs.io/en/latest/) \- \[.] \- Enrich2 is a general software tool for processing, analyzing, and visualizing data from deep mutational scanning experiments.
* [mavetools](https://www.mavedb.org/docs/mavetools/index.html) \- \[.] \- MaveTools is a pure Python Library for bioinformatics and computational biology. It features useful tools that can be applied to MAVE data
* [OpenCRAVAT](https://opencravat.org/index.html) \- \[.] \- OpenCRAVAT is a new open source, scalable decision support system to support variant and gene prioritization
* [AnalyzeSaturationMutagenesis](https://gatk.broadinstitute.org/hc/en-us/articles/360046789232-AnalyzeSaturationMutagenesis-BETA) \- \[.] \- This tool processes reads from an experiment that systematically perturbs a mini\-gene to ascertain which amino\-acid variations are tolerable at each codon of the open reading frame.
* [MAVE\-NN](https://mavenn.readthedocs.io/en/latest/) \- \[python] \- MAVE\-NN 1 enables the rapid quantitative modeling of genotype\-phenotype (G\-P) maps from the data produced by multiplex assays of variant effect (MAVEs).
* [seqminer](https://github.com/zhanxw/seqminer) \- \[R] \- Seqminer is a highly efficient R\-package for retrieving sequence variants from biobank scale datasets of millions of individuals and billions of genetic variants.
* [dumpling](https://github.com/odcambc/dumpling) \- \[python] \- GATK\-based Snakemake pipeline for deep mutational scanning experiments
* [rosace](https://github.com/pimentellab/rosace) \- \[R] \- rosace is an R package for analyzing growth\-based deep mutational scanning screen data.
* [mutscan](https://github.com/fmicompbio/mutscan) \- \[R] \- mutscan is an R package to process, statistically analyse and visualise multiplexed assays of variant effect data.
* [TransVar](https://github.com/zwdzwd/transvar) \- \[python] \- TransVar is a multi\-way annotator for genetic elements and genetic variations.
* [SubChrom](https://github.com/MullighanLab/SubChrom) \- \[.] \- A tool for dectecting Subclonal Chromosomal aberrations and estimating tumor fraction in cell\-free DNA from next generation sequencing data.


### In Silico Tools


* [REVEL](https://sites.google.com/site/revelgenomics/) \- \[.] \- An ensemble method for predicting the pathogenicity of missense variants based on a combination of scores from 13 individual tools
* [AlphaMissense](https://alphamissense.hegelab.org/) \- \[.] \- A deep learning model that builds on the protein structure prediction tool AlphaFold2
* [CADD](https://cadd.gs.washington.edu/) \- \[.] \- CADD is a tool for scoring the deleteriousness of single nucleotide variants, multi\-nucleotide substitutions as well as insertion/deletions variants in the human genome.
* [GV\-Rep](https://github.com/bowang-lab/genomic-FM) \- \[.] \- A Large\-Scale Dataset for Genetic Variant Representation Learning
* [satmut\_utils](https://github.com/ijhoskins/satmut_utils)  \- \[python] \- satmut\_utils is a Python package for simulation and variant calling of saturation mutagenesis data. The two main subcommands are: sim and call
* [SIFT \- Sorting Intolerant From Tolerant](https://sift.bii.a-star.edu.sg/) \- \[.] \- SIFT predicts whether an amino acid substitution affects protein function based on sequence homology and the physical properties of amino acids. SIFT can be applied to naturally occurring nonsynonymous polymorphisms and laboratory\-induced missense mutations.
* [PolyPhen\-2 \- Polymorphism Phenotyping v2](http://genetics.bwh.harvard.edu/pph2/) \- \[.] \- PolyPhen\-2 (Polymorphism Phenotyping v2\) is a tool which predicts possible impact of an amino acid substitution on the structure and function of a human protein using straightforward physical and comparative considerations
* [SNPs\&GO](https://snps.biofold.org/snps-and-go/snps-and-go.html) \- \[.] \- The online predictor also provides access to PANTHER and PhD\-SNP predictions. Note that the method only handles limited variants per query, meaning full protein predictions need to be submitted in chunks.
* [DRAKES](https://github.com/ChenyuWang-Monica/DRAKES) \- \[python] \- The repository contains the code for the DRAKES method presented in the paper: Fine\-Tuning Discrete Diffusion Models via Reward Optimization with Applications to DNA and Protein design(2024\). DRAKES is a fine\-tuning method for reward optimization or alignment in discrete diffusion models, utilizing direct backpropagation with the softmax\-gumbel trick.
* [FUSE](https://github.com/TYTYBU/FUSE-pipeline) \- \[R] \- FUSE: Improving the estimation and imputation of variant impacts in functional screening


### Visualization Tools


* [gw](https://github.com/kcleal/gw/tree/master) \- \[.] \- GW is a fast browser for genomic sequencing data (.bam/.cram format) used directly from the terminal. GW also allows you to view and annotate variants from vcf/bcf files.
* [FoldMason](https://github.com/steineggerlab/foldmason) \- \[.] \- FoldMason is a software tool for constructing accurate multiple alignments from large sets of protein structures.
* [SRplot](https://www.bioinformatics.com.cn/srplot) \- \[.] \- SRplot a freely accessible easy\-to\-use web server that integrated all of the commonly used data visualization and graphing functions together. It can be run easily with all Web browsers, with a user\-friendly graphical interface, users can paste your data directly into the input box according to the defined file format


## Applications


### Databases


* [MAVERegistry](https://registry.varianteffect.org/)  \- \[.] \- MaveRegistry is a collaborative resource for sharing progress on Multiplexed Assays of Variant Effect (MAVE)
* [MaveDB](https://www.mavedb.org/) \- \[.] \- MaveDB is a public repository for datasets from Multiplexed Assays of Variant Effect (MAVEs), such as those generated by deep mutational scanning (DMS) or massively parallel reporter assay (MPRA) experiments
* [Protein Gym](https://proteingym.org/) \- \[.] \- ProteinGym is a collection of benchmarks aiming at comparing the ability of models to predict the effects of protein mutations
* [COSMIC](https://cancer.sanger.ac.uk/cosmic) \- \[.] \- the Catalogue of Somatic Mutations in Cancer – is the world's largest source of expert manually curated somatic mutation information relating to human cancers.
* [gnomAD](https://gnomad.broadinstitute.org/) \- \[.] \- The Genome Aggregation Database (gnomAD), originally launched in 2014 as the Exome Aggregation Consortium (ExAC), is the result of a coalition of investigators willing to share aggregate exome and genome sequencing data from a variety of large\-scale sequencing projects, and make summary data available for the wider scientific community.
* [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) \- \[.] \- ClinVar is a freely accessible, public archive of reports of human variations classified for diseases and drug responses, with supporting evidence.
* [OMIM](https://www.omim.org/) \- \[.] \- Online Mendelian Inheritance in Man (OMIM) is a continuously updated catalog of human genes and genetic disorders and traits, with a particular focus on the gene\-phenotype relationship.
* [dbNSFP](https://sites.google.com/site/jpopgen/dbNSFP) \- \[.] \- dbNSFP is a database developed for functional prediction and annotation of all potential non\-synonymous single\-nucleotide variants (nsSNVs) in the human genome.
* [SplicsVarDB](https://compbio.ccia.org.au/splicevardb/) \- \[.] \- SpliceVarDB, an online database consolidating over 50,000 variants assayed for their effects on splicing in over 8,000 human genes.
* [MPRAbase](https://github.com/Ahituv-lab/mprabase) \- \[.] \- MPRAbase is a comprehensive, easily accessible database whose goal is to store published MPRA datasets, process them, present them in a user\-friendly manner, provide easy to use search tools and rapidly download these datasets.
* [AACR Project GENIE](https://www.synapse.org/Synapse:syn7222066/tables/) \- \[.] \- AACR Project GENIE is a publicly accessible international cancer registry of real\-world data assembled through data sharing between 19 of the leading cancer centers in the world.
* [GDSC](https://www.cancerrxgene.org/) \- \[.] \- We have characterised 1000 human cancer cell lines and screened them with 100s of compounds. On this website, you will find drug response data and genomic markers of sensitivity.
* [KinDEL](https://github.com/insitro/kindel) \- \[python] \- KinDEL is a large DNA\-encoded library dataset containing two kinase targets (DDR1 and MAPK14\) for benchmarking machine learning models.
* [Genomics 2 Proteins portal](https://g2p.broadinstitute.org/) \- \[.] \- a resource and discovery tool for linking genetic screening outputs to protein sequences and structures


### Websites / Portals


* [MAVEvidence](https://mavevidence.com/)  \- \[.] \- MAVEvidence is the premier functional evidence resource for the clinical genetics community.
* [MAVEQuest](https://mavequest.varianteffect.org/) \- \[.] \- MaveQuest: a web resource for planning experimental tests of human variant effects
* [cBioPortal](https://www.cbioportal.org/) \- \[.] \- The cBioPortal for Cancer Genomics is an open\-access, open\-source resource for interactive exploration of multidimensional cancer genomics data sets.
* [OncoKB](https://www.oncokb.org/) \- \[.] \- MSK's Precision Oncology Knowledge Base


## Similar Collections


### Similar Collections


* [MAVE Data Analysis Tools](https://www.varianteffect.org/analysis-tools) \- \[.] \- Multiplexed assays of variant effect (MAVEs) are high\-throughput methods employed to investigate the impact of genetic variations in proteins or nucleic acids on their functionality. MAVE experiments are often referred to as deep mutational scans (DMS), and offer a comprehensive and systematic approach to examining the relationship between sequence and function.


## Tutorials


### Tutorials


* [dms\-view](https://dms-view.github.io/docs/tutorial.html) \- \[.] \- The goal of dms\_view is to facilitate the analysis of deep mutational scanning experiments through interactive visualizations. dms\_view links together three pieces of information: a site\-level summary metric, a mutation\-level metric, and the 3\-D protein structure.
* [Understanding the functional consequences of every single mutation in Your Favourite Gene](https://mdhs.unimelb.edu.au/centre-for-cancer-research/about/seminars/external-speakers/understanding-the-functional-consequences-of-every-single-mutation-in-your-favourite-gene) \- \[.] \- This talk describes Multiplexed Assays of Variant Effect (MAVEs), a family of experimental techniques that allow researchers to measure all possible variants of a gene or other functional element at once, with a focus on enabling MAVE data sharing and clinical applications.
* [Workshop report: the clinical application of data from multiplex assays of variant effect (MAVEs), 12 July 2023](https://www.nature.com/articles/s41431-024-01566-2#Sec1) \- \[.] \- ‘Clinical Application of MAVE Data’ workshop, held on 12th July 2023 at the Wellcome Connecting Science Conference Centre in between two relevant research meetings, ‘Curating the Clinical Genome 2023’ and the ‘Mutational Scanning Symposium 2023’


## Assays


### Assays


* [VAMP\-seq](https://pubmed.ncbi.nlm.nih.gov/29785012/) \- \[.] \- We describe variant abundance by massively parallel sequencing (VAMP\-seq), which measures the effects of thousands of missense variants of a protein on intracellular abundance simultaneously
* [MP3\-seq](https://www.nature.com/articles/s41589-024-01718-x) \- \[.] \- Here, we introduce massively parallel PPI measurement by sequencing (MP3\-seq), an easy\-to\-use and highly scalable yeast two\-hybrid approach for measuring PPIs.
* [LABEL\-seq](https://pubmed.ncbi.nlm.nih.gov/38659825/) \- \[.] \- Here, we developed LAbeling with Barcodes and Enrichment for biochemicaL analysis by sequencing (LABEL\-seq), a platform for the multimodal profiling of thousands of protein variants in cultured human cells.
* [STARR\-seq](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02156-3) \- \[.] \- Here, we applied STARR\-seq, a genome\-wide plasmid\-based assay, as a read\-out for the enhancer landscape in “ground\-state” (2i\+LIF; 2iL) and “metastable” (serum\+LIF; SL) mESCs.
