# How to export a full Ethereum history into S3, efficiently

Blockchain technologies are not a geeky thing anymore and many companies run their business around crypto assets. A popular scenario is to **build a Data Platform operating blockchain data** and launch analytical and realtime services on top of it. This is what I have done recently, and want to share my experience with you.

Hi 👋 I am Anton Bryzgalov (aka [@bryzgaloff](https://www.linkedin.com/in/bryzgaloff/)), an Expert Data Engineer and Architect in Cloud & Blockchain.

The solution I have built is described in detail in [my blogpost on Medium](https://medium.com/@tony.bryzgaloff/how-to-dump-full-ethereum-history-to-s3-296fb3ad175). **This email is a short summary** exclusively for Data Engineering Weekly 😊

## Which node to use?

I have exported the data using a number of [public node providers](https://ethereumnodes.com/). This is ok for an MVP. However, in a long term, I strongly **advise you to run your own node**. Such a node will take several weeks to sync and extra cost for hosting, but the further data extraction speed will be significantly higher than when using a public node.

Also, using free public nodes require a solid fallback mechanism due to rate and other limits. **With an owned node the rate is limited only by your VM resources**.

Using a paid provider like Alchemy or QuickNode is completely not an option: the full history is too big and **will result in $10Ks**.

## Alternatives?

For a quick launch, I have used **public BigQuery datasets with Ethereum data**. They are populated using an [open source Ethereum ETL](https://github.com/blockchain-etl/) tool. Exporting data from BigQuery into S3 is a cheap option.

A set of optimizations described in the article, allowed me to **export the data in 24 hours and ≈$100** (BigQuery -> S3).

However, relying on BigQuery leads to a data structure loss, so to operate on raw JSONs I have had to switch back to the public nodes.

## How do we use the data now?

🔥 As an outcome, I have ingested the full history of Ethereum to S3. The data is hosted a raw JSON format as responded by the nodes. This allows me to **easily rerun any calculations on the full history without touching faulty public nodes**.

The querying is performed using AWS Athena. It supports JSON brilliantly. But the full dataset is of 4.5TB now and Athena is paid for a volume of scanned data. Reading the full history in raw costs ≈$25. So, to reduce the costs I convert the data from a raw JSON into a cost-efficient Parquet format (with Snappy compression). For specific purposes, this has **reduced querying costs by 97%!**

## Realtime data ingestion

Our product-level goal was to build a cryptowallets balances API: given a wallet address, it should respond with a list of _all_ tokens contained by the wallet with _100% accurate_ balances. The latency should be _minimal_ from the latest mined block.

Following a KISS ("keep it simple, stupid!") principle, I have implemented **a polling script which "listens" to new blocks** on top of the Ethereum and once a new block appears, updates a DynamoDB table containing aggregated balances for each wallet.

Calculating balances using Athena and uploading the data into DynamoDB was quite a challenge:

* firstly, because of a high volume (≈30GB of uncompressed aggregated data);
* and secondly, because of `uint256`-based calculations in Athena (which's the biggest number type is 128-bit Decimal).

⚡️ As a result we are able to **recalculate the full balances history and upload it to DynamoDB in ≤3 hours** (and <$1). The API's latency is **<1s from the latest block**. Dive deeper into the details [in the article](https://betterprogramming.pub/how-to-dump-full-ethereum-history-to-s3-296fb3ad175).

# Thank you for reading!

Working on something similar? I am happy to have a further discussion with you, let's [get in touch on LinkedIn](https://www.linkedin.com/in/bryzgaloff/)! 🤝
