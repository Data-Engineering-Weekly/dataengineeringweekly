# The number that looked right and wasn't

By [Barbora Šandová](https://www.linkedin.com/in/barbora-sandova) · [Quaesitor](https://quaesitor.eu)

*This is the story of why I started [Quaesitor](https://quaesitor.eu), an independent review service that measures how often an AI assistant answers a question about your warehouse confidently, fluently, and wrongly. Not whether the assistant is accurate - whether you'd know when it isn't. Proba omnia.*

## The mistake I was always afraid of

I spent years writing SQL and Python pipelines for a living, and the mistake I feared most - and still fear - is that I wrote the query wrong, handed a wrong number to management, and nobody caught it.

I'm not talking about when the query throws an error, those you easily fix before lunch. I'm talking about the one that runs clean, returns something that looks completely reasonable, but is quietly wrong - and the risk that they don't get caught in review is quite high. You usually catch them weeks later, when somebody who knows the business squints at a slide and says "that can't be right." If you're lucky.

When data assistants showed up, text-to-SQL over the warehouse, ask-your-data in Slack, they industrialised that exact mistake. So now the confident, well-formatted, wrong number doesn't even need me to write it. All the time one of these was supposed to save me, I spent digging for where it had quietly gone off.

It took me a while to get my head around this. A model that's right nine times out of ten is more dangerous than one that's right four. Because at four you check everything, because you've learned you have to. At nine you stop, and the tenth answer walks straight into a report, a board pack, a decision. Accuracy is the number everyone quotes and on its own it's close to useless, because what hurts you is not being able to tell which answers are wrong. It gets worse as the models improve - trust grows faster than accuracy.

## Nothing measured it

I went looking for the tool that measured that, and it wasn't there. Semantic layers define what a metric means, but nobody checks that the definition matches the data, or that the model actually used it. Eval and observability tools measure consistency, latency, cost and text-level hallucination, but not whether a number is factually right. Governance tools watch how AI gets used, not whether the answer is true.

The gap between them needs data engineering, metric definitions and security at once, and almost nobody sits in all three. The honest reason it stays open is that the compute is the cheap part. Writing a verified query by hand for every question your business actually asks, and being sure it's right, takes weeks, can't be automated, and is exactly the work everyone skips.

So I built Quaesitor.

A quaesitor was the Roman examining magistrate - the one who checked the facts somebody else produced and put their name to the finding - independent, because no team can verify its own answers. It's the same reason you buy a penetration test from someone who didn't write the code.

Every question carries a query I've checked by hand next to a plausible wrong one, and the two differ in exactly one place - a fan-out join, a cohort anchored to the wrong date, a currency left unconverted. When the model misses, I can point at the cause instead of at a vibe.

So, I handed an agent the company's own schema documentation, expecting fewer wrong answers and correctness didn't move, but the failures did.

What used to come back visibly absurd, negative revenue or a figure off by three orders of magnitude, came back clean, plausible, and still wrong. The context we all reach for to make these systems safer had made the mistakes harder to see, but unfortunately not rarer.

## Where it is now

The suite is 77 questions I wrote and verified by hand, across five warehouses, three of which I didn't build. It has produced 114 runs and 5,533 classified answers across three models, with the retail pack also run in fifteen languages. Every run records a hash of the questions, the warehouse and the prompt, so any number I quote traces back to the run that produced it.

What I don't have yet is a paying client, and that part really is early.

I'm convinced this is the layer the next wave of AI-over-data needs and doesn't have: not whether your assistant is accurate, but whether you'd know when it isn't. If you're running one of these in production and that question keeps you up at night, I'd genuinely like to compare notes.

Barbora Šandová · [quaesitor.eu](https://quaesitor.eu) · [LinkedIn](https://www.linkedin.com/in/barbora-sandova)