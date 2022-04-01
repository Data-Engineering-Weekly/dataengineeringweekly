# Shipyard Founder Story

Hey everyone! I’m [Blake Burch](https://www.linkedin.com/in/blakeburch/), the data co-founder at [Shipyard](http://www.shipyardapp.com). We’re a modern data orchestration platform that serves as the quickest way for data teams to launch, monitor, and share data workflows. With fully-hosted infrastructure, built-in security, dynamic scalability, and optional low-code templates, we’re breaking down the barriers of entry so anyone on a data team can deploy resilient data pipelines in a matter of minutes.

This is the story of how our journey began.

## The Beginnings

I started my journey in data by not touching data at all. In 2014, I was your everyday account manager at [PMG](https://www.pmg.com/), a digital advertising agency. We were a small crew of roughly 30 individuals serving high-profile brands like Travelocity, Sephora, OpenTable, and J.Crew. My days consisted of researching new keywords, creating new ads, and adjusting bids and budgets to maximize performance. All the work was Excel based and, as someone passionate about automation, I eventually started getting fed up with the manual work.

I knew there had to be a way to take those repetitive daily tasks and cut myself out of the picture. I worked with the development team to automate data ingestion from advertising APIs to a database (Redshift at the time). Once in the database, I taught myself SQL (thanks [SQL Zoo](https://sqlzoo.net/wiki/SQL_Tutorial)) so I could replicate the data I was manually pulling into Excel every day.

Once I had that logic in place, I needed to figure out how to execute that SQL programmatically and push updates directly to each advertising platform. It was time to learn Python. With my budding programming skills, I started creating scripts to perform my daily account management work and quickly realized I couldn't keep running things on my local machine. I needed a way to automate and monitor their performance.

That’s where [Eric Elsken](https://www.linkedin.com/in/eric-elsken-80095998/), my co-founder comes in.

## Joint Efforts

Eric was one of our best engineers and a frequent go-to when anyone needed something automated at the company. At the time, he was building out a solution that helped our analytics team automate Tableau extracts for our client dashboards. Soon after, he was tasked with automating web scraping for our client’s websites. And then he had me pestering him with my solutions. It was in that moment he thought, “What if instead of building these one-off use cases and being the company cron manager, I build a UI that lets anyone at the agency automate, monitor, and share any script they want?”. So he did just that.

With the birth of a new platform, my scripts were automated for one client and started driving crazy growth. I’m talking 300%+ more conversions on million dollar budgets. That growth, of course, spurred the need for every client to run these scripts with slight tweaks. That use case led us to building templates directly in the platform.

Through this growth cycle, I had the opportunity to build the Data Engineering, Data Innovation, and Data Activation teams from the ground up. Our main goal was to mix 1st party data with 3rd party advertising platform data to scale omni-channel digital marketing efforts like crazy using algorithms and automation. We pushed our new internal platform to the limits, systematically building out the same data sets for every client so we could rapidly experiment and implement winning solutions across clients with minimal effort. These solutions included:

- Reacting to Social Influencer Trends in Real Time
- Hourly Forecasting for Holidays
- Using Live Stores Visits + User Location Modifiers to influence Store Traffic
- Dynamic Ad Creation from Promotional Calendars
- QA Notification Bots for Account Best Practices
- Scoring Inventory Based on Competitive Pricing

## The Problems We Identified

As we continued to expand our use cases across the organization, we realized there were three big gaps across our clients.

### **1) Too Much Engineering Time Gets Wasted on Repetitive Code.**

From my experience, most data work is ubiquitous, no matter the tool or the industry. Despite this, hundreds of engineering hours gets wasted writing the same basic scripts to perform tasks like downloading and uploading data from common services in an efficient manner. I’ve seen a few ways to get around this issue:

- Some teams manage their repetitive code by sharing snippets that can be copied and pasted around the organization. This makes the code easy to implement, but even easier to get out of sync when updates need to be made.
- More advanced teams build out internal packages that can be imported into other scripts and updated from a central location. While this makes management easier, it’s still difficult to verify where the package is being used and what impact an update will have.

In the end, most teams don’t have a solution in place, so everyone codes from scratch every time.

### **2) Getting Data Workflows into Production is really Hard.**

In many ways, the existing data orchestration technology is prohibitively technical for the average data practitioner.

To get started, you have to sift through hours of documentation to learn how to either create a proprietary DAG file or how to mix proprietary platform logic with the business logic in your code.

After building proof-of-concept workflows, these tools can take weeks of DevOps knowledge to get a production environment set up. Once servers are live, you’ll inevitably run into scalability issues in a few months due to increased memory usage, unplanned query volume, or general package version conflicts. While the latter issue can be solved by teaching the data team Docker, that just adds one more layer of complexity.

As a result of this difficulty, I saw many data teams spending a majority of their time gathering, cleaning, and troubleshooting data rather than **actually acting** on it. That’s why you see articles where [73% of company data goes unused](https://www.inc.com/jeff-barrett/misusing-data-could-be-costing-your-business-heres-how.html) or [87% of data projects never make it to production](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/).

### **3) Data Teams Lack Visibility of End-to-End Impact**

A lot of data teams operate a black box where few people are aware of every data touchpoint and how the data gets used. Teams rely on fragmented tools to run data ingestion, transformation, report delivery, model deployment, and reverse ETL at very specific scheduled times without regard for the steps that need to occur before and after.

This results in three common issues:

- Someone changes the underlying definition of a dataset which negatively impacts other data team member’s models, dashboards, or automated scripts. This is isn’t malicious - it’s just the nature of not knowing what end products each data set is supporting.
- One process fails, resulting in bad data that nobody notices until a business user finds it days or weeks later. At that point, there’s a mad scramble to try and pinpoint when and where the issue occurred, all while business users loses trust in the data.
- Data pipelines are artificially slow due to self-imposed bottlenecks of running fragmented systems one after the other at specific times.

## Next Steps

After seeing the value that the technology was able to create for our internal data team and our clients, we decided to spin off PMG’s internal orchestration technology into its own separate entity - what today we call Shipyard. When we spun off, PMG was around 250 people with even bigger clients (Apple, Gap Inc., TikTok). These clients all relied on 98 solution templates and 1.8k unique data workflows that ran on an hourly or daily basis to power marketing campaigns.

While we knew our technology was battle tested by some of the largest brands, we still had to overcome the hurdle of turning an internal technology into something that anyone could pick up and use. After 6 months of interviews, testing, and redesigns, we had our first iteration of the product in 2020 that directly addressed the problems we saw in the market.

## Building the Solution

### **1) Eliminate Repetitive Code with Low-Code Templates + Custom Template Builder**

Out of the gate, we built 60+ low-code templates to perform simple actions like downloading data, uploading data, executing queries, or sending messages against all of the major tools a data team might use (BigQuery, Snowflake, S3, GCS, Slack, Email, Fivetran, dbt, etc.). All you need to do is provide your credentials and fill out a form to get started. Since we know that the data ecosystem values transparency, we designed our templates as [open source Python CLIs](https://github.com/shipyardapp?q=blueprint) so teams can see what’s happening under the hood and make adjustments where needed.

Since we were in the weeds ourselves, we know that our templates that will only get you 80% of the way there. Once you inevitably have a proprietary process that needs to be repeated, you can build your own template in Shipyard for others to use. Code can be synced directly with a Github repository and branch of your choice to keep everything up-to-date. Our advantage over creating an importable package is that you gain visibility into every time a template is added to a workflow, helping you track performance and usage at a high level.  Plus, the interface makes it easy for anyone to run your code with slight tweaks without needing to code themselves.

### **2) Make deploying Data Workflows ridiculously easy.**

To combat the complexity we noticed, we designed Shipyard with the goal of helping data practitioners build and deploy new data workflows in 10 minutes or less. We accomplish this by making the actual build process as flexible as possible:

- We’re a fully-hosted and serverless, scaling dynamically as you automate more workflows.
- You can build workflows with a drag-and-drop visual editor or with a YAML editor.
- Workflows can be as simple or complex as needed with options for branching, converging, and conditional logic.
- Workflows can be a mix of our low-code templates, proprietary low-code templates that you build, or your own custom code written in Python, Node, or Bash.
- Every task in a workflow is containerized so language and package conflicts will never occur.
- Workflows can be triggered manually, on a schedule, or with event-driven webhooks.
- In the event of errors, we’ll handle automatic retries and send notifications to the appropriate team.

All of these efforts combined let us help data professionals focus on what they’re best at - building solutions with data.

### **3) Enhance Observability by enabling Collaboration**

By breaking down the barriers to entry, everyone from the Data Analyst to the Data Engineer can build data workflows together in a single unified platform. Every interaction can be connected together, giving your team the full end-to-end picture of how data is used.

With detailed notifications, metadata, and logging, you gain visibility into the specific location of any error for further investigation. Plus, with the visual overview of how your data workflow is designed, you’ll know exactly what downstream actions your changes might affect and who built them. This gives teams the confidence to make updates without fear of unknown breakages.

For example, let’s say that your dbt transformation steps break for finance data tables. Shipyard can automatically send proactive alerts to both the data team and the finance team so everyone is aware of the issue. Since every touchpoint is connected, downstream financial forecast models, reports, and dashboards will be halted in place so the bad data never gets delivered. 

## Today

Today, we’re expanding our templates to cover more tools in the modern data stack while simultaneously improving the developer experience. We service high-growth data teams at companies in almost every industry. This year, we’re planning on doubling our team size with key hires to invest in our product development and marketing.

Want to build data workflows like a 10x engineer? You can [get started for free](https://app.shipyardapp.com/auth/signup) and try out everything that Shipyard has to offer.
