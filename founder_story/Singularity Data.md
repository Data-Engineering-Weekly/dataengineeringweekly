#  Singularity Data

Hey everyone! I'm [Yingjun Wu](https://twitter.com/YingjunWu?s=20&t=_Imy0cpwOWg3sK6NYiWz4A), the founder of [Singularity Data](https://singularity-data.com) — an early-stage startup innovating next-generation database systems. Our product is [RisingWave](https://github.com/singularity-data/risingwave), a cloud-native SQL streaming database for modern real-time applications. With RisingWave, users can easily extract knowledge from streaming data by issuing powerful and efficient queries using standard SQL language.

This is the story of how our journey began.

## The Beginnings, the Encounters, and the Realization...

*"There's a way to do it better – find it." – Thomas A. Edison*

You can't tackle new problems with old solutions; therefore, you must always look for fresh ways to innovate. And that is what a Ph.D. degree entails: a voyage of discovery and invention. I began working on database systems during my Ph.D. at the National University of Singapore. Those were the formative years that shaped my journey of entrepreneurship.

I've always tried to do things differently since I was a child. Getting a Ph.D. was all about honing that ability of creativity — coming up with new ideas and putting them into action. However, I quickly realized that academia has its own set of constraints. All of these unique concepts don't always reach the light of day. They aren't implemented in real time. Simply put, new ideas emerge, but breakthroughs don't happen in terms of application / reaching users.

Hence, I joined IBM research, a wonderful blend of academic research and industry, to put my ideas into action and see changes in real time. IBM Research provided me with access to amazing brains, a wealth of valuable resources, and, above all, DB2. DB2 is a world-class database system that was developed about 40 years ago. I collaborated closely with the product development team. During brainstorming sessions, breakthrough ideas would emerge, but the execution would be limited because the focus had to be on the product. Following IBM, I joined AWS and worked on developing Redshift, one of their most important products. AWS is the world's most frequently used cloud platform, and Redshift is the most widely used cloud data warehouse. I had a great time working there — a great learning experience.

But, alas, innovation proved to be a difficult task once again. All were attempting to repair or improve various issues by employing tried-and-tested technology. I wanted to do something new. I knew one hundred percent that real-time data was becoming increasingly important to users. And something new could have revolutionized the field and genuinely benefit users. I firmly believe that we must continue to innovate. We won't be able to sell things if we continue to rely on outdated technology. So, I wanted to combine my findings and create something useful for today's generation: a next-gen model.

Look, you can have brilliant ideas, but you won't put them into action unless there's a genuine demand. People increasingly demand real-time analytics and want to shift their streaming database to the cloud to save money and improve efficiency. Based on these two reasons, I decided to create something new: a streaming database that is not just streaming but also cloud-based. I came up with the concept, and it was time to implement it. With this notion in mind, I talked to some prominent personalities and startup founders in the Bay Area. We talked about it, and I asked them for their thoughts. I was hoping to get feedback on whether or not my ideas were feasible.

Long story short, I received assistance from several startup founders (whom I will not name). Those multi-hour chats have been invaluable to me. Singularity Data was formed in early 2021, after much deliberation, planning, and execution. RisingWave was developed by a collaboration of professional database researchers and practitioners from businesses including AWS Redshift, Microsoft Azure, Snowflake, LinkedIn, and Uber.

## The Problem

Stream processing has a huge demand. An increasing number of firms are looking into modern streaming systems to see how they may revolutionize their operations. But unfortunately, many stop along the way, blaming the exorbitant expense of implementing streaming technology. There are two critical reasons for this:

### Steep learning curve:

Unlike traditional databases (such as MySQL and PostgreSQL), which utilize SQL as their interactive interface, most, if not all, streaming systems require users to master a set of platform-specific programming interfaces (most likely in Java) to modify the data. For non-tech people, learning streaming technologies becomes a near-impossible task. Data is represented differently in streaming systems than it is in databases. Users must create sophisticated data extraction logic to transfer data between streaming systems and databases. 

### Expensive operation:

Several prominent streaming systems use open-source software. Docker images and comprehensive deployment scripts are readily available. But, open-source does not imply that something is free or inexpensive. Streaming workloads can change dramatically depending on demand. Businesses must purchase a big cluster of computers to withstand worst-case scenarios. The cost of setting up and maintaining a streaming system is sometimes substantially more than buying devices. In fact, putting together a team of engineers to work late to run the system can be a genuine pain.

## Our Solution

We put all of our efforts into democratizing stream processing at Singularity Data. RisingWave is a cloud-native streaming database that makes stream processing simple, affordable, and accessible to everybody.

### Simple

RisingWave is a distributed streaming database with an interactive interface based on ordinary SQL. It uses the PostgreSQL dialect and can be integrated into the PostgreSQL environment without requiring any code changes. RisingWave treats streams like tables, allowing users to declaratively and elegantly create complicated queries over streaming and historical data. Users can also focus solely on their analytical query logics with RisingWave, rather than learning Java or system-specific low-level APIs.

### Affordable

RisingWave is a cloud-based application. RisingWave can fully utilize cloud platforms' elastic resources, thanks to its cloud-native architecture. RisingWave, as a fully managed service, deploys, manages, and scales in the cloud on its own, without human intervention. RisingWave automatically assembles multiple tiers of compute and storage resources in the cloud to accomplish the performance target at a minimal cost once users establish their service-level agreement (SLA). RisingWave is a serverless platform, meaning that users only pay for what they use and don't have to pay unless they use it. We're continually improving the service to keep RisingWave inexpensive for small businesses.

### Accessible

A great product originates from the pooled wisdom of a vibrant and open community. Instead of depending on the expertise of a limited number of professionals to produce RisingWave, we collaborate with the open-source community to design and implement it. We chose to release RisingWave kernel under the Apache License 2.0, a permissive free software license. The [RisingWave community](https://github.com/singularity-data/risingwave) is open to all. Here's how you can get involved:

* Participate in the development of the project roadmap.
* Deploy the distributed streaming database in your cloud service.
* Contribute and provide feedback to the community.

## Today's Scene

The RisingWave community is collaborative, and we're excited to work with other communities to construct the new real-time data infrastructure stack. RisingWave is in the early stages of development, but we're growing rapidly. We have over 70 contributors worldwide, and we examine and integrate more than 100 Pull Requests every week. We still have a long way to go to get recognized as a "fully-fledged" system. But, hey, we've covered quite a lot in the last few months. Check out our recently launched [roadmap](https://singularity-data.com/blog/on-the-way-to-democratized-stream-processing-risingwaves-roadmap) (our first roadmap).

*This is our story. And to know more, check the RisingWave *[*GitHub repository*](https://github.com/singularity-data/risingwave/)*, join our *[*Slack*](https://join.slack.com/t/risingwave-community/shared_invite/zt-120rft0mr-d8uGk3d~NZiZAQWPnElOfw)* community, follow us on *[*Twitter*](https://twitter.com/SingularityData)*, and stay tuned with RisingWave!*
