"""SAND inference helper: SMILES -> 512-d shape-aware embedding.

Loads the vendored SANDModel (bypassing the FAISS/Lance retrieval pipeline) and
returns the continuous, L2-normalized 512-dimensional embedding for each input
molecule. Invalid SMILES yield an all-NaN row so the output stays aligned with
the input, one row per molecule.
"""
import os

import numpy as np
import torch
from rdkit import Chem

_HERE = os.path.dirname(os.path.abspath(__file__))
# Checkpoint lives in the (eosvc-backed) checkpoints dir; config travels with the code.
_CKPT = os.path.join(_HERE, "..", "..", "checkpoints", "sand_no_comp.ckpt")
_CONFIG = os.path.join(_HERE, "sand", "config", "no_compression.yml")

EMB_DIM = 512  # SAND released model output dimension (paper Table 3)

_model = None


def _load_model():
    """Load and cache the SANDModel on CPU in eval mode."""
    global _model
    if _model is None:
        from sand.model import SANDModel

        torch.set_num_threads(max(1, os.cpu_count() or 1))
        model = SANDModel.load_from_checkpoint(
            _CKPT, _CONFIG, map_location="cpu"
        )
        model.eval()
        _model = model
    return _model


def predict(smiles_list):
    """Return an (N, 512) float32 array of SAND embeddings.

    Invalid / unparseable SMILES produce an all-NaN row at the same position.
    """
    model = _load_model()

    valid_idx, valid_smiles = [], []
    for i, smi in enumerate(smiles_list):
        if smi is not None and Chem.MolFromSmiles(smi) is not None:
            valid_idx.append(i)
            valid_smiles.append(smi)

    out = np.full((len(smiles_list), EMB_DIM), np.nan, dtype=np.float32)
    if valid_smiles:
        with torch.no_grad():
            emb = model.encode_smiles(valid_smiles, batch_size=256)
        emb = emb.detach().cpu().numpy().astype(np.float32)
        for row, i in enumerate(valid_idx):
            out[i] = emb[row]
    return out
