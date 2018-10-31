# LearnSpark
Learning spark


#### 0 安装  
下载hadoop和spark，解压在/opt/目录下   
**配置hadoop**
```xml
./etc/hadoop/core-site.xml
 <configuration>
       <property>
              <name>hadoop.tmp.dir</name>            
              <value>file:/opt/hadoop/tmp</value>
              <description>Abase for other temporary directories.</description>
        </property>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://0.0.0.0:9000</value>
        </property>
</configuration>

./etc/hadoop/hdfs-site.xml
<configuration>
         <property>
              <name>dfs.replication</name>
              <value>1</value>
         </property>
         <property>
              <name>dfs.namenode.name.dir</name>
              <value>file:/opt/hadoop/tmp/dfs/name</value>
         </property>
         <property>
              <name>dfs.datanode.data.dir</name>
              <value>file:/opt/hadoop/tmp/dfs/data</value>
         </property>
</configuration>

在./etc/hadoop/hadoop-env.sh中配置JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
**配置spark**  
在台式机上安装单机spark
```
#./conf/spark-default.conf, spark-submit默认参数
#这个配置在笔记本上也需要进行同样的操作
spark.master                     spark://wahahr:7077
spark.pyspark.python            /home/xh/anaconda3/bin/python3.6
spark.psspark.dirver.python     python3.6

#./conf/spark-env.sh, SPARK_MASTER_HOST允许外部IP访问
SPARK_LOCAL_IP=10.19.138.99
SPARK_MASTER_HOST=0.0.0.0

#./conf/log4j.properties, 消息输出等级为WARN
#这个配置在笔记本上也需要进行同样的操作
log4j.rootCategory=WARN, console
```

**配置环境变量**   
在台式机上进行配置
```shell
export PYSPARK_PYTHON=/home/xh/anaconda3/bin/python3.6                         
export PYSPARK_DRIVER_PYTHON=python3.6

export HADOOP_HOME=/opt/hadoop/
# pyspark会报WARN找不到hadoop native，需要进行配置
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native

export SPARK_HOME=/opt/spark-hadoop/  
# 将下载的spark中的pyspark加入到PYTHONPATH后，运行pyspark会报错:auth_token,
# 需要安装py4j: pip install py4j
export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python

export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$SPARK_HOME/sbin/
```
在笔记本上进行配置，访问台式机的spark
```shell
# 将hadoop和spark也下载安装在/opt目录下
export HADOOP_HOME=/opt/hadoop/
export SPARK_HOME=/opt/spark-hadoop/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python

# 这里配置的PYSPARK环境对应的是台式机上的，笔记本提交任务到台式机需要下面的配置
export PYSPARK_DRIVER_PYTHON=python3.6
export PYSPARK_PYTHON=/home/xh/anaconda3/bin/python3.6

# 配置hadoop的用户，否则笔记本访问台式机的hadoop时会报错“没有权限”，这里配置为台式机的用户名
export HADOOP_USER_NAME=xh

```

#### 1 运行
**运行hadoop**
```shell
hdfs namenode -format
start-dfs.sh
```
**运行spark**
```shell
start-all.sh
```

