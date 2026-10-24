# From database permissions to text-to-SQL: why I built schemagate

Hey there, I'm Ashish Sinha, a database engineer and the author of [schemagate](https://github.com/ashishsinha1602/schemagate), an open-source layer that decides which tables an AI model may see before it writes any SQL.

## The problem I kept running into

I've spent my career on the database side: grants, roles, row-level security, the slow work of making sure the right people see the right data. When text-to-SQL agents arrived, I noticed they skip all of it. A typical agent reads the whole schema into the prompt, writes a query, and runs it with one service account. Every user's question is answered with everyone's access.

The usual fix is a line in the prompt: "don't use the salary table". That isn't a control. A SIGMOD '27 benchmark measured it: even when restricted columns are hidden, models still "answer" about a quarter of the questions they should refuse, by improvising from what's left.

## What schemagate does

schemagate sits between the question and the model:

1. It reads the database's own grants and policies, so permissions come from the place they already live.
2. For each question, it picks the tables needed **from the ones this caller may read**. The model never sees the rest.
3. It checks every generated query against the same permissions before it runs, and fails closed.

It works with PostgreSQL, Oracle, SQL Server, MySQL and SQLite, and runs as an MCP server, a LangChain retriever or a CLI.

## Measuring it on benchmarks I didn't write

I decided early that every claim would be checked by someone else's evaluator, with the predictions published:

- **RBAC Text-to-SQL** (SIGMOD '27): AC-F1 90.1, against 88.1 for the paper's best setup
- **Spider-ACL**: refusal F1 0.984, with 0 queries reading ungranted data out of 8,128
- **BIRD dev**: 77.1% execution accuracy on all 1,534 questions, with one model call per question
- **Spider 2.0-lite** SQLite questions: 71.9%
- **Oracle (UniQL)**: 64.5% on the first try, against a best published 49.6

The most useful part wasn't the scores. Twice the benchmarks found real bugs in my access check, including one where recursive queries were wrongly refused for every user. Benchmarks you didn't write are very good at that.

## Where it is now

schemagate first shipped in September 2026. It has passed 30,000 downloads on PyPI, sits in several curated MCP and AI-security lists, and every benchmark result is reproducible from the repository.

If you're putting an LLM in front of a warehouse, I'd love to hear how you handle permissions today.

- GitHub: https://github.com/ashishsinha1602/schemagate
- Benchmarks and every caveat: https://ashishsinha1602.github.io/schemagate/benchmarks/
- `pip install schemagate`
