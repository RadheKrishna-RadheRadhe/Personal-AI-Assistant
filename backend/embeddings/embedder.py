from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def generate_embeddings(self, chunks):
        """
        Generate embeddings from chunk metadata objects.

        Expected format:

        [
            {
                "text": "...",
                "source": "sample.pdf",
                "page": 1,
                "chunk_id": 0
            }
        ]
        """

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings

    def generate_query_embedding(
        self,
        query: str
    ):
        """
        Generate embedding for user query.
        """

        return self.model.encode(
            query
        )