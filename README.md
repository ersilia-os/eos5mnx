# SAND Shape-Aware Descriptor

SAND (Shape Aware Neural Descriptor) turns a molecules 2D structure into a compact fixed-length embedding that captures its 3D shape without generating any conformers. The resulting vector enables rapid retrieval of shape-similar molecules for ligand-based virtual screening, and serves as a general-purpose descriptor for downstream similarity search and property-prediction tasks. Trained by Pfizer (ICML 2026); GINE graph encoder producing a 512-dimensional embedding whose cosine similarity approximates 3D shape overlap.

This model was incorporated on 2026-08-03.Last packaged on 2026-08-03.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5mnx`
- **Slug:** `sand-shape-descriptor`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Embedding`, `Similarity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `512`
- **Output Consistency:** `Fixed`
- **Interpretation:** 512-dimensional shape-aware embedding whose cosine similarity approximates 3D molecular shape overlap

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | SAND shape-aware embedding dimension 0 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_001 | float |  | SAND shape-aware embedding dimension 1 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_002 | float |  | SAND shape-aware embedding dimension 2 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_003 | float |  | SAND shape-aware embedding dimension 3 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_004 | float |  | SAND shape-aware embedding dimension 4 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_005 | float |  | SAND shape-aware embedding dimension 5 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_006 | float |  | SAND shape-aware embedding dimension 6 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_007 | float |  | SAND shape-aware embedding dimension 7 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_008 | float |  | SAND shape-aware embedding dimension 8 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |
| feat_009 | float |  | SAND shape-aware embedding dimension 9 (L2-normalized; cosine similarity approximates 3D molecular shape overlap) |

_10 of 512 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5mnx](https://hub.docker.com/r/ersiliaos/eos5mnx)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5mnx.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5mnx.zip)

### Resource Consumption
- **Model Size (Mb):** `321`
- **Environment Size (Mb):** `1408`
- **Image Size (Mb):** `2039.84`

**Computational Performance (seconds):**
- 10 inputs: `30.45`
- 100 inputs: `21.23`
- 10000 inputs: `245.22`

### References
- **Source Code**: [https://github.com/pfizer-opensource/SAND](https://github.com/pfizer-opensource/SAND)
- **Publication**: [https://openreview.net/forum?id=pB6WAdnRDR](https://openreview.net/forum?id=pB6WAdnRDR)
- **Publication Type:** `Preprint`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [TiagoJanela](https://github.com/TiagoJanela)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5mnx
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5mnx
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
