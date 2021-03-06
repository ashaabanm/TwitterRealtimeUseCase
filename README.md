# Introduction

The project aims at building a data platform for real time moderation and analytics of twitter data.
By ingesting tweets and make some sort of processing on data and analyze it then retweet customer based on the result of sentiment analysis model.

## Technologies used
* python : for ingesting data from twitter
* Kafka : as a staging area to store tweets which is coming from twitter
* spark 2.4.7 for streaming (DStream) and processing and write parquet files on HDFS
* Hive : to write some Sql queries on top of HDFS
* Power BI : as an analytics tool for creating some insights about data

### Usage
you can follow instruction and installation on configs_notes folder.

## Smaple of data (tweets)
[smaple of tweets in json fromat](https://github.com/ashaabanm/BigDataCaseStudy/blob/main/configs_notes/smaple_of_tweets.json)
```json
{"created_at":"Thu May 06 11:15:18 +0000 2021",
   "id":1390263903049891841,
   "id_str":"1390263903049891841",
   "text":"Random Trump https://t.co/RpULgBbz6O - #randomtrump #trump #donaldtrump #giphy #gif #gifs https://t.co/iBLJd3d1uu"}
```

## Sample of tweet after processing
![Sample of tweet](https://github.com/ashaabanm/BigDataCaseStudy/blob/main/configs_notes/smaple_of_data.png?raw=true)
## Architecture
![Architecture](https://github.com/ashaabanm/TwitterRealtimeUseCase/blob/main/configs_notes/pipline_architecture.png?raw=true)

##  [dashboard for showing some insights](https://github.com/ashaabanm/BigDataCaseStudy/blob/main/dashboard/first_dashboard.pbix)

## Requirements
* setuptools==44.1.1
* jsonpickle==2.0.0
* findspark==1.4.2
* kafka-python==2.0.2
* kafka-utils==2.3.0
* nltk==3.4.5
* textblob==0.15.3
* tweepy==3.10.0

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
