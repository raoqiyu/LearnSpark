from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

spark = SparkSession.builder.appName('structured network word count').getOrCreate()


# Structured Streaming: new data is appended after the table
# lines is a table(DataFrame)
lines = spark.readStream.format('socket').option('host','localhost').option('port',9999).load()

# DataFrame cannot use flatMap
# In Streaming, we cap flatMap every line recived
# words = lines.flatMap(lambda line: line.split(" "))

#
words = lines.select(
            explode(
                split(lines.value," ")
            ).alias('word')
        )

wordCounts = words.groupBy('word').count()

results = wordCounts.writeStream.outputMode('complete').format('console').start()


results.awaitTermination()
