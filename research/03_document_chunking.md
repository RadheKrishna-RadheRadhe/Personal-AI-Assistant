# Document Chunking in Retrieval-Augmented Generation (RAG)

## Introduction

Document chunking is the process of splitting large documents into smaller pieces before generating embeddings.

It is one of the most important components of a RAG system because retrieval quality depends heavily on how information is divided and stored.

Even the most advanced language models cannot compensate for poor chunking strategies.

---

# Why Chunking Is Necessary

Consider a 500-page textbook.

Embedding the entire book into a single vector creates several problems:

* Too much information is compressed into one representation.
* Retrieval becomes imprecise.
* Relevant sections become difficult to locate.
* The language model receives unnecessary context.

Example:

A book contains:

* Process Scheduling
* Deadlocks
* Memory Management
* File Systems
* Synchronization

User Question:

What is a deadlock?

If the entire book is represented by one embedding, the retrieval system cannot accurately isolate the deadlock section.

---

# The Chunking Process

Document

↓

Text Extraction

↓

Chunk Creation

↓

Embedding Generation

↓

Vector Database

Instead of storing one vector for the entire document, the system stores many vectors.

Example:

Operating_Systems.pdf

↓

Chunk 1

Chunk 2

Chunk 3

Chunk 4

...

Chunk 500

Each chunk receives its own embedding.

---

# Characteristics of a Good Chunk

A good chunk should:

* Contain a complete idea
* Preserve context
* Be small enough for accurate retrieval
* Be large enough to maintain meaning

Bad Example:

"Deadlocks occur"

This chunk is too short and loses context.

Good Example:

"A deadlock occurs when multiple processes wait indefinitely for resources held by each other."

This chunk contains a complete concept.

---

# Fixed-Size Chunking

The simplest chunking method.

Example:

Every 500 characters.

Document

↓

500 Characters

↓

500 Characters

↓

500 Characters

Advantages:

* Easy to implement
* Fast processing

Disadvantages:

* May split sentences
* May split concepts
* Lower retrieval quality

Not recommended for production systems.

---

# Recursive Chunking

A smarter approach.

The system attempts to split:

1. Paragraphs
2. Sentences
3. Words

Only when necessary.

Advantages:

* Preserves context
* Maintains readability
* Better retrieval quality

This is the approach commonly used in modern RAG systems.

---

# Chunk Overlap

One major problem occurs when important information exists at chunk boundaries.

Example:

Chunk 1:

"The operating system manages hardware resources."

Chunk 2:

"It also schedules processes and allocates memory."

The relationship between the two chunks may be lost.

To solve this problem, overlap is introduced.

---

# Overlapping Chunks

Example:

Chunk Size: 500

Overlap: 100

Chunk 1:

Characters 0–500

Chunk 2:

Characters 400–900

Chunk 3:

Characters 800–1300

Notice that information appears in multiple chunks.

Benefits:

* Better context preservation
* Improved retrieval quality
* Reduced information loss

---

# Metadata

Every chunk should store metadata.

Example:

{
"source": "Operating_Systems.pdf",
"page": 45,
"chapter": "Deadlocks"
}

Metadata enables citations.

Example Response:

Deadlocks occur when processes wait indefinitely for resources.

Source:
Operating_Systems.pdf (Page 45)

Without metadata, accurate citations become impossible.

---

# Choosing Chunk Size

There is no perfect chunk size.

The best size depends on document type.

General recommendations:

Short Notes:

200–400 characters

Articles:

500–1000 characters

Books:

800–1500 characters

Research Papers:

1000–2000 characters

For this project:

Initial Configuration:

Chunk Size = 1000

Chunk Overlap = 200

This provides a good balance between retrieval quality and efficiency.

---

# Problems Caused by Poor Chunking

## Chunk Too Small

Problems:

* Loss of context
* Incomplete ideas
* Reduced answer quality

Example:

"Deadlocks occur"

Not enough information.

---

## Chunk Too Large

Problems:

* Mixed topics
* Less precise retrieval
* Increased token usage

Example:

A chunk containing:

* Deadlocks
* Scheduling
* Memory Management
* File Systems

The retriever may struggle to determine relevance.

---

# Chunking Strategy for This Project

Phase 1:

Recursive Character Text Splitter

Configuration:

Chunk Size: 1000

Chunk Overlap: 200

Reason:

* Easy implementation
* Strong retrieval performance
* Industry-standard approach

Future Improvements:

* Semantic Chunking
* Hierarchical Chunking
* Parent-Child Retrieval
* Knowledge Graph Retrieval

---

# Example Workflow

PDF

↓

Extract Text

↓

Recursive Chunking

↓

Chunk Metadata

↓

Generate Embeddings

↓

Store in FAISS

↓

User Query

↓

Retrieve Relevant Chunks

↓

Generate Response

↓

Display Citations

---

# Key Takeaways

* Chunking is a critical component of RAG.
* Good chunking improves retrieval accuracy.
* Recursive chunking is preferred over fixed-size chunking.
* Overlap preserves context across chunks.
* Metadata enables citations and traceability.
* Chunk size significantly impacts retrieval quality.
* For this project, a chunk size of 1000 and overlap of 200 is an appropriate starting point.
