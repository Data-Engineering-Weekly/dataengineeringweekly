# From Splunk Eventgen pain to Eventum

Hi, I'm [Nikita Reznikov](https://github.com/rnv812), author of [Eventum](https://github.com/eventum-generator/eventum).

Eventum is an open-source platform for generating realistic synthetic data. You describe events in YAML and get a stream of them: logs, metrics, security events, transactions etc. Typical uses are testing pipelines and detection rules, live demos, seeding databases, and load testing.

## Where the pain came from

I work on a data analytics platform similar to Splunk. A big part of shipping and selling such a platform is customer demos, and every demo needs a believable case: dashboards, searches and alerts running on data that looks alive. Real customer data is rarely an option, so we built demo cases on generated data.

For years the standard tool for that was Splunk Eventgen. It did the job, but for our workflow it never felt convenient: developing event samples was awkward, debugging them took time, and running everything required extra effort. Every new demo case turned into a small engineering project of its own.

## Building my own

Around 2023 I decided to try a different approach and started building Eventum. The design goals came straight from that experience: configuration is plain YAML, a generator is a pipeline of three swappable stages (when events happen, what they contain, where they go), and there is a web UI, Eventum Studio, where you preview and debug events before anything goes live - the part I missed the most.

At work it took off. Today our SIEM team and data engineers use it to build demo cases, test detection rules, and feed data pipelines.

What started as a replacement for one internal tool has grown into a platform: a server that runs many generators in parallel, a REST API and an MCP server alongside the web UI, a plugin system for every pipeline stage, and ready-to-use content packs that generate realistic data out of the box.

## What Eventum looks like today

- Pipeline of three swappable stages: when events happen, what they contain, where they go
- Scheduling from cron and fixed intervals to statistical time patterns
- Jinja templates with an extended API (Faker and Mimesis data generators, weighted random helpers, CSV/JSON samples, and more), or Python scripts when templates aren't enough
- Stateful generation: three scopes of state plus a finite state machine mode for multi-step scenarios
- Parallel fan-out: stdout, files, ClickHouse, OpenSearch, Kafka, any HTTP endpoint
- Live mode (events fire at their timestamps) or sample mode (everything at once)
- Eventum Studio web UI, REST API, and an MCP server for AI agents

Eventum is Apache-2.0 and ships as a pip package or Docker image. If you generate test or demo data, give it a try: [eventum.run](https://eventum.run).
