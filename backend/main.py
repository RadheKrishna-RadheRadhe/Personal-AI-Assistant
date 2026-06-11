from ingestion.pdf_loader import (
    extract_pages
)

from ingestion.document_processor import (
    DocumentProcessor
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


PDF_PATH = "Operating Systems.pdf"


# Extract pages from PDF
pages = extract_pages(
    PDF_PATH
)

print(
    f"Total Pages: {len(pages)}"
)


# Process pages into chunks with metadata
processor = DocumentProcessor()

chunks = processor.process_pages(
    pages,
    PDF_PATH
)

print(
    f"Total Chunks: {len(chunks)}"
)

# Generate embeddings
embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(
    chunks
)


# Create FAISS index
dimension = len(
    embeddings[0]
)

vector_store = FAISSStore(
    dimension
)

vector_store.add_embeddings(
    embeddings
)


# Create retriever
retriever = Retriever(
    vector_store,
    chunks,
    embedder
)


# Interactive query loop
while True:

    query = input(
        "\nAsk Question: "
    ).strip()

    if not query:
        continue

    if query.lower() == "exit":
        break

    results = retriever.retrieve(
        query
    )

    print("\nRetrieved Chunks:\n")

    for i, result in enumerate(results):

        print(f"\nResult {i+1}")
        print("-" * 50)

        print(
            f"Source: {result['source']}"
        )

        print(
            f"Page: {result['page']}"
        )

        print(
            f"Chunk ID: {result['chunk_id']}"
        )

        print("\nText:\n")

        print(
            f"Score: {result['score']:.4f}"
        )

        print("\nText:\n")

        print(
            result["text"]
        )