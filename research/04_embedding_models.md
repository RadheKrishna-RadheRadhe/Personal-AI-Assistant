# Embedding Models for Retrieval-Augmented Generation (RAG)

## Introduction

Embedding models are responsible for converting text into numerical vector representations that capture semantic meaning.

These vectors are stored inside a vector database and later used to retrieve relevant information when users ask questions.

The quality of retrieval in a RAG system depends heavily on the quality of the embedding model.

---

# What Does an Embedding Model Do?

Input:

A deadlock occurs when multiple processes wait indefinitely for resources.

Output:

[0.134, -0.542, 0.881, ...]

The output is a vector that represents the semantic meaning of the text.

The model attempts to place semantically similar text close together in vector space.

Example:

Text A:

Process scheduling determines which process executes next.

Text B:

CPU scheduling decides the execution order of processes.

Although the wording is different, both texts have similar meaning.

A good embedding model places these vectors close together.

---

# Embedding Generation Pipeline

Document

↓

Text Extraction

↓

Chunking

↓

Embedding Model

↓

Vector Representation

↓

FAISS Storage

Every chunk receives its own embedding.

When a user submits a question, the same embedding model converts the question into a vector.

FAISS then compares the query vector with stored vectors to identify the most relevant chunks.

---

# Why Not Use an LLM Directly?

Large Language Models are designed for generation.

Embedding models are designed for retrieval.

LLM Responsibilities:

* Text generation
* Summarization
* Question answering
* Reasoning

Embedding Model Responsibilities:

* Semantic representation
* Similarity comparison
* Information retrieval

Separating these responsibilities improves performance and reduces computational requirements.

---

# Popular Embedding Models

## OpenAI Embeddings

Examples:

* text-embedding-3-small
* text-embedding-3-large

Advantages:

* Excellent retrieval quality
* Easy integration

Disadvantages:

* Requires API calls
* Cost per request
* Privacy concerns

Not suitable for a fully local system.

---

## Sentence Transformers

Popular open-source option.

Examples:

* all-MiniLM-L6-v2
* all-mpnet-base-v2

Advantages:

* Local execution
* Easy deployment
* Lightweight

Widely used in production systems.

---

## BGE Embedding Models

Developed by the organization:

Beijing Academy of Artificial Intelligence

Examples:

* bge-small-en-v1.5
* bge-base-en-v1.5
* bge-large-en-v1.5

Advantages:

* Excellent retrieval performance
* Open source
* Strong benchmark results
* Efficient local execution

These models are among the most popular choices for modern RAG systems.

---

# Why We Are Choosing BAAI/bge-small-en-v1.5

Project Constraints:

* Intel i5 10th Gen
* 12 GB RAM
* CPU-only execution

Requirements:

* Fast embedding generation
* Low memory consumption
* Good retrieval quality

Selected Model:

BAAI/bge-small-en-v1.5

Reasons:

* Lightweight
* Fast on CPU
* Strong retrieval accuracy
* Suitable for laptops
* Production-proven

This model provides an excellent balance between performance and resource consumption.

---

# Understanding Embedding Dimensions

Every embedding model produces vectors with a specific number of dimensions.

Example:

384 Dimensions

[0.12, 0.44, -0.78, ...]

Example:

768 Dimensions

[0.18, -0.22, 0.91, ...]

Higher dimensions generally allow richer representations but require more storage and computation.

---

# Trade-Off Between Dimensions and Performance

Lower Dimensions:

Advantages:

* Faster search
* Lower memory usage
* Smaller vector database

Disadvantages:

* Slightly less expressive

Higher Dimensions:

Advantages:

* Richer semantic representation

Disadvantages:

* Larger storage requirements
* Increased search time

For personal knowledge assistants, moderate-sized embeddings are typically sufficient.

---

# Storage Requirements

Assume:

10,000 chunks

Embedding Size:

384 dimensions

Approximate Storage:

10,000 × 384 values

This remains manageable on a typical laptop.

Even collections containing hundreds of documents can be stored efficiently.

This makes local RAG systems practical without requiring cloud infrastructure.

---

# Query Embedding Process

User Question:

What is process scheduling?

The system performs:

Question

↓

Embedding Model

↓

Query Vector

↓

FAISS Search

↓

Relevant Chunks

↓

LLM

↓

Final Answer

The same embedding model must be used for both:

* Document embeddings
* Query embeddings

Using different models may reduce retrieval accuracy.

---

# Similarity Search Example

Stored Chunk:

Process scheduling determines which process executes next.

User Query:

How does the operating system choose the next process?

Although the wording differs, the semantic meaning is similar.

The embedding vectors will be close together.

FAISS retrieves the chunk.

The language model then uses that context to generate the answer.

---

# Embedding Model Selection Criteria

When evaluating embedding models, consider:

Retrieval Quality

* Accuracy of semantic search

Latency

* Speed of embedding generation

Memory Usage

* RAM consumption

Storage Requirements

* Vector database size

Privacy

* Local execution capability

For this project, local execution and privacy are major priorities.

---

# Embedding Workflow in Our Project

PDF

↓

Text Extraction

↓

Recursive Chunking

↓

BAAI/bge-small-en-v1.5

↓

Embeddings

↓

FAISS

↓

Retriever

↓

Qwen 2.5 3B

↓

Cited Response

This architecture balances performance, privacy, and hardware limitations.

---

# Future Improvements

Potential upgrades include:

* bge-base-en-v1.5
* bge-large-en-v1.5
* multilingual embedding models
* domain-specific embeddings
* hybrid retrieval systems

These improvements can be explored after the initial system is functional.

---

# Key Takeaways

* Embedding models convert text into semantic vectors.
* Embeddings enable semantic search.
* Retrieval quality depends heavily on embedding quality.
* Open-source embedding models allow local execution.
* BAAI/bge-small-en-v1.5 is a strong choice for CPU-based systems.
* The same embedding model must be used for documents and queries.
* Embeddings are stored in FAISS and retrieved during question answering.
* Embedding models form the retrieval foundation of a RAG system.
