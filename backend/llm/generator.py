from ollama import chat


class AnswerGenerator:

    def generate_answer(
        self,
        question,
        retrieved_chunks
    ):

        context = "\n\n".join(
            [
                chunk["text"]
                for chunk in retrieved_chunks
            ]
        )

        prompt = f"""
You are a retrieval-based assistant.

Answer ONLY from the supplied context.

If the answer is not explicitly present
in the context, respond:

'I could not find sufficient information
in the provided documents.'

Context:
{context}

Question:
{question}

Answer:
"""

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content