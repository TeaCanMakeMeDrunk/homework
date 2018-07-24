import org.apache.spark.{SparkConf, SparkContext}
import org.json.JSONObject

import scala.collection.mutable.ListBuffer

/**
  * /**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  *
  */
  * object YaSpark1{
  * def main(args: Array[String]) {
  * import org.json.JSONObject//导入str转json工具包
  * import org.apache.spark.SparkConf//
  * import org.apache.spark.SparkContext
  * //sparkcontext的配置，运行在本地，名称为cala
  * val conf = new SparkConf().setAppName("cala").setMaster("local")
  * val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
  * //使用spark读取文本文件
  * sc.textFile("d:\\python\\lynn\\四川大学全国招生计划表.txt")
  * .filter(line=>line.endsWith("status\":1}"))
  * .flatMap(line=>{//line str===>List line  抚平
  * val  json = new JSONObject(line)
  * val jsonlist = json.getJSONArray("data")
  * //        jsonlist.getJSONObject(0)
  * val list = ListBuffer[JSONObject]()
  * for(i<-0 to jsonlist.length()-1){
  * list.append(jsonlist.getJSONObject(i))
  * }
  * list
  * })
  * .map(line=>(line.getString("school"),line.getString("plan").toInt))
  * .reduceByKey(_+_)
  * .foreach(line=>println(line))
  * *
  * }
  * }
  */

object spark {
  def main(args: Array[String]) {
    //    val str = "{\"data\":[{\"id\":\"152529\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"050101\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u6c49\\u8bed\\u8a00\\u6587\\u5b66(\\u57fa\\u5730\\u73ed)\",\"plan\":\"3\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"},{\"id\":\"152530\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"1202\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u5de5\\u5546\\u7ba1\\u7406\\u7c7b\",\"plan\":\"2\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"},{\"id\":\"152531\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"0503\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u65b0\\u95fb\\u4f20\\u64ad\\u5b66\\u7c7b\",\"plan\":\"2\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"},{\"id\":\"152532\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"0201\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u7ecf\\u6d4e\\u5b66\\u7c7b\",\"plan\":\"2\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"},{\"id\":\"152533\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"050204\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u6cd5\\u8bed\",\"plan\":\"2\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"},{\"id\":\"152534\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"050201\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u82f1\\u8bed\",\"plan\":\"2\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"},{\"id\":\"152535\",\"sid\":\"924\",\"school\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"city_code\":\"11\",\"city\":\"\\u5317\\u4eac\",\"subject\":\"\\u6587\\u53f2\",\"sub_type\":\"1\",\"major_code\":\"030302\",\"stu_time\":\"\",\"batch\":\"1\",\"state\":\"1\",\"type\":\"\\u975e\\u5b9a\\u5411\",\"year\":\"2016\",\"level\":\"\\u672c\\u79d1\",\"profess\":\"\\u793e\\u4f1a\\u5de5\\u4f5c\",\"plan\":\"2\",\"uniname\":\"\\u56db\\u5ddd\\u5927\\u5b66\",\"unicode\":\"4359\"}],\"info\":\"\",\"status\":1}"
    //    //    val json = JSON.parseObject(str)
    //    var json = JSON.
    //    val jsonList = JSON.parseArray(json)
    //    //    println(json.get("data"))
    //    val list = ListBuffer[JSONObject]()
    //    for (i <- 0 to jsonList.length() - 1) {
    //      list.append(jsonList.getJSONObject(i))
    //    }
  }
}

object spark1 {
  def main(args: Array[String]) {
    //sparkcontext的配置，运行在本地，名称为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc = new SparkContext(conf) //Spark运行环境,,本地电脑，集群
    //使用spark读取文本文件
    sc.textFile("D:\\python\\lynn\\全国招生计划表--四川.txt")
      .filter(line => line.endsWith("status\":1}"))
      //          .foreach(line => println(line))
      .flatMap(line => {
      val json = new JSONObject(line)
      val jsonlist = json.getJSONArray("data")
      //        jsonlist.getJSONObject(0)
      val list = ListBuffer[JSONObject]()
      for (i <- 0 to jsonlist.length() - 1) {
        list.append(jsonlist.getJSONObject(i))
      }
      list
    }).map(line => (line.getString("school"), line.getString("plan").toInt))
      .reduceByKey(_ + _) //求和
      //      .foreach(line => print("{name:'"+line._1+"',value:"+line._2+"},"))
      .foreach(line => print(line._1 + "',"))
      .foreach(line => print(line._2 + "',"))

  }
}
