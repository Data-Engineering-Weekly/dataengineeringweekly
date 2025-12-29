# From India to London: A Data Engineer's Journey from Student to Production at Scale

## The 3 AM Alert That Changed Everything

It was 3 AM on a Saturday when my phone buzzed. Our production pipeline had processed the same day's data 47 times over the weekend. The analytics team would arrive Monday morning to dashboards showing impossible metrics—customer transactions that looked like they'd grown 4,700% overnight.

This wasn't my first production incident, but it was the one that crystallized three years of lessons across three countries into a single truth: reliable data engineering isn't about the tools you use—it's about understanding what can go wrong and building systems that survive it.

## The Beginning: From India to Rome

I grew up in India, where my fascination with technology started early. After completing my schooling, I made a bold decision in September 2020: moving to Rome, Italy, to pursue a Bachelor's degree in Internet and Communication Technology at Tor Vergata University.

Moving to a new continent during a global pandemic wasn't easy, but it opened doors I never imagined. While my peers were focused purely on academics, I was hungry to apply what I was learning. I spent nights reading about distributed systems, data pipelines, and the emerging field of data engineering.

The theoretical knowledge was valuable, but I knew I needed real-world experience.

## First Steps: Barcelona and Real Data

In May 2022, while still completing my degree, I landed my first data engineering role at Dpoint Group in Barcelona, Spain. This was my introduction to production data systems—and to the gap between academic projects and business-critical pipelines.

My first project involved building ETL processes using SSIS to extract data from SAP BW. I remember the excitement of seeing my first pipeline successfully load data into the warehouse. I also remember the panic when that same pipeline failed on a Monday morning, blocking critical business reports.

**Lesson 1: Data pipelines don't care about your clever code—they care about reliability.**

At Dpoint, I learned the fundamentals:
- How to structure ETL workflows for maintainability
- Why data quality checks aren't optional
- The importance of clear error messages (your future self will thank you)
- How business intelligence depends on trustworthy data

But I was still building relatively small-scale systems. I wanted to work on data platforms that processed millions of records, supported hundreds of users, and where downtime meant real business impact.

## Scaling Up: Enterprise Data at Accenture

In July 2023, I joined Accenture as a Data Engineer, working on large-scale cloud data platforms for enterprise clients. This is where I learned what "production at scale" really means.

I worked across both Azure and AWS, building platforms that handled:
- Terabytes of data flowing through Azure Databricks and Snowflake
- Complex ETL/ELT pipelines serving multiple business units
- Data transformations using dbt for consistent business logic
- Real-time and batch processing requirements

**Lesson 2: At scale, every design decision has consequences.**

One client project involved migrating their on-premises data warehouse to Azure. The migration went smoothly in our dev environment. But in production, a query that took 2 minutes in the old system was now taking 45 minutes. After days of investigation, we discovered the root cause: we hadn't properly configured partition pruning in our new data lake structure.

That incident taught me that cloud data platforms offer incredible power and flexibility—but you need to understand how they work under the hood. Reading documentation isn't enough; you need to test with production-like data volumes and patterns.

I also learned the value of automation and Infrastructure as Code. We used Terraform and GitHub Actions to deploy our data platforms, which meant:
- Consistent environments across dev, test, and production
- Auditable changes through Git history
- Faster recovery when things went wrong (and they always do)

## Production at Scale: Banking Data in London

In September 2025, I joined NatWest Bank as a Data Engineer. This is where everything I'd learned came together—and where I faced my biggest challenges yet.

Banking data is different. It's not just about scale (though we process millions of transactions daily). It's about:
- **Regulatory requirements**: Every data flow must be auditable and compliant
- **Zero tolerance for data loss**: Financial data cannot be approximated or estimated
- **Real-time requirements**: Fraud detection and risk analysis need fresh data
- **Data quality**: A single incorrect transaction can cascade into major issues

Our tech stack includes Kafka for real-time ingestion, PySpark for distributed processing, Snowflake for our data warehouse, and Airflow for orchestration. On paper, it's a modern, scalable architecture. In reality, every component introduces complexity and potential failure points.

## The Lessons Production Taught Me

### 1. Test with Weekend Data

Remember that 3 AM incident I mentioned? Our analytics code assumed certain transaction patterns that held true on weekdays but broke on weekends when volumes dropped. We had tested thoroughly—but only with weekday data.

**Now I always test with:** Weekdays, weekends, holidays, month-end, and year-end data patterns.

### 2. Make Failures Visible

Early in my career, I built a pipeline that silently dropped invalid records into an error table. The pipeline showed "success" in Airflow, so nobody checked the error table for weeks. We eventually discovered we'd been losing 10% of transactions.

**Now I make failures loud:** Alert on validation failures, monitor error rates, and make data quality metrics visible to everyone.

### 3. Your Future Self is Your Most Important User

At 2 AM when a pipeline fails, you won't remember the clever optimization you made six months ago. You need:
- Clear error messages that tell you exactly what's wrong
- Comprehensive logging that shows the pipeline's state
- Documentation that explains why decisions were made
- Runbooks for common failure scenarios

### 4. Idempotency Isn't Optional

That Saturday incident happened because our retry logic had a bug. When a task failed, it would retry—but with fallback data from the previous successful run instead of reprocessing the current date.

**Now every pipeline I build is idempotent:** Running it multiple times with the same inputs produces the same output.

### 5. Data Quality is Code Quality

I used to think of data quality checks as "nice to have" validation added at the end. Now I build them into every transformation:
- Schema validation at ingestion
- Row count reconciliation between stages
- Business rule validation (e.g., transaction amounts must be positive)
- Freshness checks to catch upstream delays

## What I Wish I Knew Earlier

If I could go back and give advice to myself starting at Dpoint in Barcelona, I'd say:

**Invest time in fundamentals.** Cloud platforms and tools change constantly, but distributed systems principles, data modeling concepts, and SQL optimization techniques remain relevant. I spent time chasing the latest tools when I should have been deepening my understanding of fundamentals.

**Production is the best teacher.** You can read all the blog posts and take all the courses, but nothing teaches you like being responsible for a pipeline that processes business-critical data. Seek out production responsibility early in your career.

**Document your debugging.** Every production incident is a learning opportunity. I started keeping a "debugging journal" where I note what went wrong, how I fixed it, and what I learned. This has been invaluable—both for avoiding repeat mistakes and for mentoring junior engineers.

**Build for the next engineer.** Your code will outlive your tenure on any team. Write it for the person who will maintain it—they might be you at 3 AM, or they might be someone who's never seen this codebase before.

**Data engineering is about trust.** At the end of the day, our job is to make data trustworthy enough that business decisions can be made confidently. That means building systems that are reliable, maintainable, and transparent.

## The Journey Continues

From learning to code in India, to studying in Rome, to my first data pipeline in Barcelona, to enterprise platforms with Accenture, to banking data in London—each step taught me something new about building reliable data systems.

I'm now contributing to open-source projects like Apache Airflow and dbt-core, writing about data engineering challenges and solutions, and speaking at data community events. I've learned that the best way to solidify your knowledge is to share it with others.

The field of data engineering is evolving rapidly. Five years ago, many of the tools we use today didn't exist. Five years from now, the landscape will look different again. But the core challenge remains the same: how do we build systems that reliably transform raw data into trusted insights?

## What's Your Story?

Every data engineer has a story—the production incident that taught you humility, the optimization that made you feel like a genius, the bug that took days to find and seconds to fix.

If you're just starting out: embrace the complexity, learn from failures, and remember that everyone's first production incident is terrifying. You'll get better with each one.

If you're experienced: share what you've learned. Write about your failures (they're more valuable than your successes). Mentor someone who's where you were a few years ago. Contribute to open source projects.

The data engineering community is incredibly generous with knowledge. I've learned from countless blog posts, conference talks, and open source contributions from people I've never met. This newsletter itself is an example of that generosity—Ananth sharing knowledge with thousands of data practitioners every week.

So here's my challenge to you: What's one lesson you've learned from production that you wish someone had told you earlier? Share it—on LinkedIn, in a blog post, or simply with your team over coffee.

Because somewhere, there's a data engineer in India, or Rome, or Barcelona, or anywhere else in the world, who will learn from your experience and build better systems because of it.

---

*Pradeep Kalluri is a Data Engineer at NatWest Bank in London, building production data platforms that process millions of transactions daily. He writes about data engineering at [medium.com/@kalluripradeep99](https://medium.com/@kalluripradeep99) and contributes to open source projects including Apache Airflow and dbt-core. Connect with him on [LinkedIn](https://linkedin.com/in/pradeepkalluri).*
