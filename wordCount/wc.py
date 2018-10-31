from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)

lines = sc.textFile('hdfs://wahahr:9000/wordCount/test.txt')

words = lines.flatMap(lambda line: line.split())

counts = words.map(lambda word: (word,1)).reduceByKey(lambda x,y: x+y)

counts.saveAsTextFile('hdfs://wahahr:9000/wordCount/testCount3')

