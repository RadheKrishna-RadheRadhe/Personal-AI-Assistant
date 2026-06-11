from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def generate_embeddings(self, chunks):

        embeddings = self.model.encode(
            chunks,
            show_progress_bar=True
        )

        return embeddings