# Generative AI and LLMs — Comprehensive Study Notes

**Audience:** Python learners building a practical portfolio. **Data:** all records are synthetic; results are illustrative.

## Learning objectives

### 1. Tokens and context windows

### 2. Embeddings and vector similarity

### 3. Chunking and retrieval

### 4. Retrieval augmented generation (RAG)

### 5. Prompt design and structured outputs

### 6. Hallucinations, grounding and citations

### 7. Evaluation and failure analysis

### 8. Privacy, cost and safety

A token is a model text unit. Context windows limit how much evidence can be supplied at once.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Embeddings map text to numerical vectors; similarity ranks semantically related passages. TF-IDF is a useful transparent local retrieval baseline.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Chunk documents into coherent passages with stable source identifiers; overlapping chunks can improve recall but increase duplicates.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

RAG retrieves relevant evidence before generating an answer. A retrieval result is not proof that the answer is supported.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Use clear instructions: answer only from sources, cite document IDs, and abstain when evidence is missing. Parse and validate any structured outputs.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Model-generated citations may be fabricated. Verify quoted evidence against retrieved documents and avoid sending secrets to third-party APIs.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Create a small labeled set of questions and expected source IDs. Evaluate retrieval hit rate, answer correctness, and abstention behavior.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Protect sensitive data, consider prompt injection in documents, track latency and cost, and define human escalation for uncertain answers.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

## Workflow checklist
1. Define the question and the unit of analysis.
2. Inspect schema, missingness, duplicates, and target leakage.
3. Build a simple baseline and keep an independent test set where relevant.
4. Create interpretable charts and explain uncertainty.
5. Record assumptions, limitations, and next actions.

## Suggested references
- pandas documentation: https://pandas.pydata.org/docs/
- scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Matplotlib documentation: https://matplotlib.org/stable/
