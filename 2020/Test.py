from pyspark import SparkContext

logFile = 'file:///home/mesos/spark_test/spark-2.4.0-bin-hadoop2.7/README.md'
#logFile = 'README.md'
sc = SparkContext('local', 'Simple App')
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print(numAs)
print(numBs)
#print('Lines with a: %d, lines with b: %d' %{numAs, numBs})
