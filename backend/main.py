from ingestion.pdf_loader import (
    extract_text_from_pdf
)

from ingestion.text_chunker import (
    chunk_text
)

from embeddings.embedder import (
    EmbeddingGenerator
)

from vector_store.faiss_store import (
    FAISSStore
)

from retrieval.retriever import (
    Retriever
)


PDF_PATH = "OS_Notes_Sample.pdf"


text = extract_text_from_pdf(
    PDF_PATH
)

print(
    f"Extracted Characters: {len(text)}"
)


chunks = chunk_text(text)

print(
    f"Total Chunks: {len(chunks)}"
)


embedder = EmbeddingGenerator()

embeddings = (
    embedder.generate_embeddings(
        chunks
    )
)


dimension = len(
    embeddings[0]
)

vector_store = FAISSStore(
    dimension
)

vector_store.add_embeddings(
    embeddings
)


retriever = Retriever(
    vector_store,
    chunks,
    embedder
)


while True:

    query = input(
        "\nAsk Question: "
    )

    if query.lower() == "exit":
        break

    results = retriever.retrieve(
        query
    )

    print("\nRetrieved Chunks:\n")

    for i, chunk in enumerate(results):

        print(f"\nResult {i+1}")
        print("-" * 50)
        print(chunk[:500])