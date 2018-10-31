from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

spark = SparkSession.builder.appName('network word count').getOrCreate()

sc = spark.sparkContext
ssc = StreamingContext(sc,1)

lines = ssc.socketTextStream("localhost",9999)

words = lines.flatMap(lambda line: line.split(" "))

pairs = words.map(lambda word: (word,1))
wordCounts =  pairs.reduceByKey(lambda x,y:x+y)
wordCounts.pprint()

ssc.start()
ssc.awaitTermination()
