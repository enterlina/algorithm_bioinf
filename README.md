# Algorithmic Bioinformatics

Python coursework exploring computational methods for biological sequences, RNA structure, phylogenetic trees, and probabilistic sequence models. Completed as part of my bioinformatics studies.

## Repository guide

| Topic | Directory and examples |
| --- | --- |
| Pairwise sequence alignment and scoring matrices | [HW1 Alignments](HW1%20Alignments/), including Alignment.py, Alignment_CustomMatrix.py, and HW1_AlignmentSW.py under venv/ |
| Alignment with affine gap penalties | [HW2_Algoritms](HW2_Algoritms/), including venv/HW2_AffineGaps.py |
| Nussinov-style RNA secondary-structure dynamic programming | [HW3_Nussin/Alg_Nussin.py](HW3_Nussin/Alg_Nussin.py) |
| Distance-based phylogenetic reconstruction: UPGMA/WPGMA exercises and neighbor joining | [HW4_WPGMA_UPGMA](HW4_WPGMA_UPGMA/) |
| Hidden Markov models: Viterbi and forward/backward exercises | [HW5_HMM/Viterbi.py](HW5_HMM/Viterbi.py) |

## Approach

The scripts implement algorithmic steps directly, using Python and NumPy to build scoring matrices, reconstruct paths, update distances, or calculate state probabilities. Many examples define their inputs within the script.

## Using this archive

Browse the source files above to follow individual exercises. Some original source files sit inside directories named venv alongside old environment artifacts. Use a fresh environment and review each script's imports and inputs before execution. This is historical coursework without a unified test suite or a pinned dependency environment; the algorithms have not been revalidated as part of the documentation update.

## Author

Elena Dalboni da Rocha · [Portfolio and current work](https://buildnxt.app) · [GitHub](https://github.com/enterlina)
