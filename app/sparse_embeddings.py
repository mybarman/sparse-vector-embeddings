from pinecone import SparseValues
from splade.models.transformer_rep import Splade
from transformers import AutoTokenizer, AutoModelForMaskedLM
from typing import List
from pydantic import BaseModel
import torch


SPLADE_MODEL = "naver/splade-cocondenser-ensembledistil"

tokenizer = AutoTokenizer.from_pretrained(SPLADE_MODEL)
model = AutoModelForMaskedLM.from_pretrained(SPLADE_MODEL)

model = Splade(SPLADE_MODEL, agg="max")
model.eval()
tokenizer = AutoTokenizer.from_pretrained(SPLADE_MODEL)
reverse_voc = {v: k for k, v in tokenizer.vocab.items()}

# SparseEmbedding = SparseValues


class SparseEmbedding(BaseModel):
    indices: List[int]
    values: List[float]

    def to_sparse_values(self) -> SparseValues:
        return SparseValues(
            indices=self.indices,
            values=self.values,
        )


def get_sparse_embedding(text: str) -> SparseEmbedding:
    """
    Get the sparse vector representation of a text
    """
    input_ids = tokenizer(text, return_tensors='pt',  truncation=True, max_length=512)

    # now compute the document representation
    with torch.no_grad():
        # (sparse) doc rep in vocabulary space
        sparse_vec = model(d_kwargs=input_ids)["d_rep"].squeeze()

    indices = sparse_vec.nonzero().squeeze().cpu().tolist()
    weights = sparse_vec[indices].cpu().tolist()
    sparse_embedding = SparseEmbedding(indices=indices, values=weights)
    return sparse_embedding
