# Embeddings and Semantic Search

## Introduction

Retrieval-Augmented Generation (RAG) systems rely on embeddings and semantic search to retrieve relevant information from a knowledge base. Understanding these concepts is essential before building any AI-powered retrieval system.

---

# What Are Embeddings?

Embeddings are numerical vector representations of text that capture semantic meaning.

Computers cannot directly understand natural language. Therefore, text must be converted into numbers before machine learning models can process it.

Example:

Text:

The dog is running.

Embedding:

[0.22, -0.13, 0.88, 0.04, ...]

An embedding model converts words, sentences, or paragraphs into high-dimensional vectors.

The key property of embeddings is that texts with similar meanings are represented by vectors that are close to each other in vector space.

---

# Why Embeddings Are Important

Consider the following sentences:

Sentence A:

The dog is running.

Sentence B:

A puppy is playing outside.

Although the words are different, the meanings are similar.

A good embedding model places these sentences close together in vector space.

Now consider:

Sentence C:

Quantum mechanics describes subatomic particles.

This sentence has a very different meaning and will be placed far away from the previous sentences.

This ability to capture meaning enables semantic search.

---

# Traditional Search vs Semantic Search

## Traditional Keyword Search

Keyword search relies on exact word matching.

Example:

Document:

Deadlocks occur when processes wait indefinitely for resources.

Query:

Why can processes become permanently blocked?

The document may not be retrieved because the query does not contain the word "deadlock".

### Limitations

* Requires exact keywords
* Misses context
* Cannot understand meaning
* Produces lower quality retrieval

---

## Semantic Search

Semantic search compares meaning instead of words.

Process:

1. Convert query into an embedding
2. Convert documents into embeddings
3. Compare embeddings
4. Retrieve the most similar results

Even if the query and document use different vocabulary, semantic search can still retrieve relevant information.

### Advantages

* Understands context
* Handles synonyms
* Finds conceptually related information
* Produces more accurate retrieval

---

# Vector Space Representation

Embeddings exist in a mathematical space called vector space.

Example:

Dog → Close
Puppy → Close
Cat → Moderately Close
Physics → Far Away

The distance between vectors represents semantic similarity.

Smaller distance generally indicates higher similarity.

---

# Cosine Similarity

Cosine similarity is the most common metric used to compare embeddings.

Instead of measuring physical distance, it measures the angle between vectors.

### Interpretation

Cosine Similarity = 1.0

Vectors are extremely similar.

Cosine Similarity = 0.0

Vectors are unrelated.

Cosine Similarity = -1.0

Vectors are completely opposite.

Most vector databases use cosine similarity to find relevant documents.

---

# Why Chunking Is Required

Large documents should not be embedded as a single vector.

Example:

A 500-page Operating Systems textbook contains many topics:

* Process Scheduling
* Memory Management
* Deadlocks
* File Systems
* Synchronization

If the entire book is converted into a single embedding, retrieval becomes inaccurate because the vector represents the entire document rather than specific concepts.

---

## Document Chunking

Instead of embedding the whole document:

Book

↓

Chunk 1

Chunk 2

Chunk 3

Chunk 4

...

Chunk N

Each chunk receives its own embedding.

Benefits:

* Improved retrieval precision
* Faster search
* Better contextual relevance
* Higher quality RAG responses

---

# What Is FAISS?

FAISS stands for Facebook AI Similarity Search.

It is a library developed by Meta for efficient similarity search over large collections of vectors.

Purpose:

* Store embeddings
* Index vectors efficiently
* Perform fast similarity searches
* Retrieve relevant chunks for RAG systems

Without FAISS, every query would require comparing against every stored vector, which becomes slow as the knowledge base grows.

FAISS uses optimized indexing techniques to perform retrieval much faster.

---

# Role of Embeddings in RAG

RAG stands for Retrieval-Augmented Generation.

The workflow is:

Document

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

FAISS Vector Database

↓

User Query

↓

Query Embedding

↓

Similarity Search

↓

Relevant Chunks

↓

Large Language Model

↓

Generated Answer

---

# Example RAG Workflow

User uploads:

Operating_Systems.pdf

The system:

1. Extracts text from the PDF
2. Splits text into chunks
3. Generates embeddings
4. Stores embeddings in FAISS

Later the user asks:

Explain deadlocks.

The system:

1. Converts the query into an embedding
2. Searches FAISS for similar vectors
3. Retrieves relevant chunks
4. Sends retrieved context to the LLM
5. Generates a cited response

The language model does not read the entire document. It only receives the retrieved chunks.

This approach improves accuracy, reduces hallucinations, and allows the model to answer questions about private documents.

---

# Key Takeaways

* Embeddings convert text into numerical representations.
* Similar meanings produce similar vectors.
* Semantic search retrieves information based on meaning rather than keywords.
* Cosine similarity measures the similarity between embeddings.
* Chunking improves retrieval quality.
* FAISS enables efficient vector search.
* Embeddings and semantic search form the foundation of RAG systems.
