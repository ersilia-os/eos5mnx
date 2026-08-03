"""Vendored subset of the SAND package (https://github.com/pfizer-opensource/SAND, Apache-2.0).

Trimmed for inference-only use inside the Ersilia model:
- the FAISS-backed ``SANDIndex`` retrieval path (``sand.index``) and the
  training data pipeline (``sand.data``) are removed;
- only ``SANDModel`` is exposed, which is all the featurizer needs
  (SMILES -> 512-d embedding).
"""
import os

# numexpr (imported transitively) caps its thread count at NUMEXPR_MAX_THREADS
# (default 64); raise it before import to silence the warning on many-core hosts.
if "NUMEXPR_MAX_THREADS" not in os.environ:
    os.environ["NUMEXPR_MAX_THREADS"] = str(os.cpu_count() or 64)

try:
    from sand._version import __version__
except ImportError:
    __version__ = "1.0.0-vendored"

from sand.model import SANDModel

# Convenient alias
Model = SANDModel

__all__ = ["__version__", "SANDModel", "Model"]
