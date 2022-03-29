# I Founded Spectacles With Someone I'd Only Met Once
By [Josh Temple](https://twitter.com/joshptemple)

![Dylan and I at Looker's 2019 JOIN conference](https://miro.medium.com/max/700/1*pkm_HqVE1Y3NrzzKo7kghA.jpeg)

*This is the story of how [Dylan Baker](https://twitter.com/_dylan_baker) and I founded and bootstrapped [Spectacles](https://www.spectacles.dev), a continuous integration and DevOps suite for Looker developers and admins. 45% of Looker changes have unseen errors, so the best data teams rely on Spectacles to check their work (over 10k Pull Requests worth of work!) and ship bug-free code, faster.*

## The first date

They say that choosing a co-founder is the most important decision you'll make when starting a business. Choosing a co-founder is kind of like getting married. There's a legally binding contract, hundreds of high-stakes decisions, and sometimes you get texts from them in the middle of the night. So why did I decide to start a company with someone I'd only spoken with for 30 minutes at a bar? Sounds like the start of the Tinder Swindler, right?

Let's rewind to the spring of 2019, when "Co-vid" sounded more like a bad Netflix competitor than a world-altering pandemic.

I was sitting in the audience for a panel discussion at a Looker meetup in NYC. Dylan Baker, a highly regarded Looker consultant, was on stage, lamenting, "I would pay someone to build this, my *clients* would pay someone to build this. *Please*, somebody build this!"

This got my attention. If you'd like to start a company someday, here's a hint: if someone tells you they'll pay for you to solve their problem, listen up! And if they'll pay you now to build it later, even better.

Dylan was venting about a frustrating experience that developers in Looker encounter every day: the drudgery of manually testing dimensions and measures from the Explore page to make sure they don’t have SQL errors. As a data analytics lead and Looker developer, I'd been doing a lot of this. And I had an idea for how we might automate away this tedious task.

I nervously approached Dylan at the happy hour after the meetup. I said, "I think we could build that tool you described!" We talked about how automated testing, or *continuous integration*, was taking off in the software engineering community, but hadn't been adopted much by data teams. We talked about how Looker was investing more and more in their API and platform strategy.

Soon, the genesis of an idea emerged: a continuous integration tool for Looker that automatically tests LookML for SQL errors and content validation issues.

We agreed we'd submit an abstract to Looker's upcoming JOIN conference. Would continuous integration for Looker be compelling to anyone else?

## Remote work before it was cool

We were thrilled when Looker accepted our abstract a few months later. But then reality set in: we actually needed to build this tool. Unlike the founder fable where two college kids sit across from each other in a dorm room, coding for 36 hours straight with nothing but cold pizza and Mountain Dew to sustain them, Dylan and I lived nearly 3,500 miles apart—me in NYC, and Dylan in London.

Today, most of us are familiar with the barriers and blessings of remote work. But in those dreamy, pre-pandemic days, working remotely on nights and weekends to develop a product across GitHub Pull Requests and Slack messages felt exciting and futuristic. This was true remote, globalized work! Technology without borders! 

Between code reviews and pairing sessions, Dylan and I began to get to know each other better. We compared fantasy football draft algorithms, we debated the correct spelling of "organisation," we reviewed the Hamilton soundtrack. I learned that Dylan has no self control when it comes to buying website domains. And slowly but surely, we became less like LinkedIn connections and more like friends.

We came up with the name Spectacles after browsing unclaimed names for Python packages. As humongous nerds, we liked the pun that Spectacles could help you "Look" (see: Looker) better. Naming things is the hardest problem in engineering, and we found this to be true. All of our other ideas didn't pass muster ("Looker Lawyer" being a particularly egregious example).

![The title slide from our JOIN 2019 presentation](https://files.slack.com/files-pri/T0VLPD22H-FNVU0RU9J/screenshot_2019-09-30_at_13.33.40.png?pub_secret=6020f0d8c4)
*The title slide from our JOIN 2019 presentation.*

## Who cares about testing anyway?

That fall, we flew to San Francisco for Looker's annual conference with nothing but a dream and a CLI in our pocket. At each networking event and happy hour, we pitched people on Spectacles. I couldn't stop smiling after one of Looker's first engineers said to me, "I've been *telling* people we should do this in Looker for years!"

But my heart sank as I walked to our designated spot for the presentation—a small room with about 30 seats, tucked away in a far-flung corner of the convention center. I remember thinking to myself, "I guess our abstract title, 'Develop LookML Like a Software Engineer: Continuous Integration for Looker' didn't exactly *dazzle* the conference organizers." (A few years later, I can only hope I've gotten better at marketing and headline writing).

Despite our best efforts to prematurely bomb our talk attendance with a boring title, people turned out in droves to listen. As our start time neared, there was standing room only, and there were rows of people lining up outside the door to listen in. I turned to Dylan and said, "Okay, this is clearly a topic people care about. There might be something here..."

Afterwards, we collected a list of emails of people who were interested in testing Spectacles. Many of these teams became alpha customers, and are still loyal customers today. We agreed we needed to make Spectacles a reality, not as a command-line utility, but as a fully-fledged software product.

## Putting on our Spectacles

Over the past three years, Dylan, myself, and Tom (our 3rd co-founder), built on the original Spectacles CLI to create an easy-to-setup SaaS application that integrates with Looker to validate LookML and squash bugs before they can escape to production.

Today, Spectacles gives hundreds of Looker developers at 50+ companies peace of mind as they ship high-quality LookML. We've worked with teams of two and teams of 100 to solve countless LookML issues.

Looking back, it's been a wild ride. Dylan moved to Toronto, then back to London, Tom moved to Stockholm. Even though there's an Atlantic Ocean between us, I'm lucky to have them as partners. Spectacles is a testament to the power of remote entrepreneurship. Should you be cautious about starting a company with an Internet friend? Certainly! But the data space is growing faster than ever and is filled with wonderful people with brilliant ideas. The term "modern data stack" already feels passé—what a time to be alive!

*Don't take it from us! You can try Spectacles for free, no-strings-attached, for 14 days. [Sign up on our website](https://www.spectacles.dev). Or check out this [2-minute video](https://youtu.be/tM1AqHtIHTo) on how Spectacles works.*
