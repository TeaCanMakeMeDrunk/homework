import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by lynn on 2018/7/20.
  *
  * 练习题1：
  * 定义一个天气温度列表，写出里面每一天的温度
  * 打印一周的天气，遇到周三就加上温度，周三+温度
  *
  */
object test {
  def main(args: Array[String]) {

    val tempLsit = List("15℃", "18℃", "17℃", "25℃", "18℃", "19℃", "11℃")
    var j = 1
    for (i <- tempLsit) {
      println("第" + j + "天温度是%s".format(i))
      j = j + 1
    }
    val map = Map(("星期一", List("温度", "31℃", "天气情况", "热")),
      ("星期二", List("温度", "31℃", "天气情况", "热")),
      ("星期三", "温度, 31℃,天气情况, 炎热"),
      ("星期四", List("温度", "31℃", "天气情况", "热")),
      ("星期五", List("温度", "31℃", "天气情况", "热")),
      ("星期六", List("温度", "31℃", "天气情况", "热")),
      ("星期六", List("温度", "31℃", "天气情况", "热")))

    print("星期三天气情况：" + map("星期三"))
  }
}

object test2 {
  def main(args: Array[String]): Unit = {
    //  使用函数式思想
    //map 映射
    1.to(10).map(i => i * 10).foreach(i => println(i))
  }
}


object ScalaFun2 {
  def main(args: Array[String]) {
    //1到10 每个数*10 打印每个数
    //    for(i<-Range(1,11)){
    //      val j=i*10
    //      println(j)
    //    }
    //使用函数式编写的思想写出以上的要求,, ,,,闭包lambda+函数作为参数
    //    def m(i:Int)=i*10
    1.to(10).map(i => i * 10).foreach(i => println(i)) //lambda函数作为了第一等公民(参数) 传递
  }
}

object findCityId {
  def main(args: Array[String]) {
    val xml = <ul class="clearfix">
      <li data-val="北京" data-id="2" onclick="$.setVar('claimCity', 11)">北京</li>
      <li data-val="天津" data-id="2" onclick="$.setVar('claimCity', 12)">天津</li>
      <li data-val="河北" data-id="2" onclick="$.setVar('claimCity', 13)">河北</li>
      <li data-val="山西" data-id="2" onclick="$.setVar('claimCity', 14)">山西</li>
      <li data-val="内蒙古" data-id="2" onclick="$.setVar('claimCity', 15)">内蒙古</li>
      <li data-val="辽宁" data-id="2" onclick="$.setVar('claimCity', 21)">辽宁</li>
      <li data-val="吉林" data-id="2" onclick="$.setVar('claimCity', 22)">吉林</li>
      <li data-val="黑龙江" data-id="2" onclick="$.setVar('claimCity', 23)">黑龙江</li>
      <li data-val="上海" data-id="2" onclick="$.setVar('claimCity', 31)">上海</li>
      <li data-val="江苏" data-id="2" onclick="$.setVar('claimCity', 32)">江苏</li>
      <li data-val="浙江" data-id="2" onclick="$.setVar('claimCity', 33)">浙江</li>
      <li data-val="安徽" data-id="2" onclick="$.setVar('claimCity', 34)">安徽</li>
      <li data-val="福建" data-id="2" onclick="$.setVar('claimCity', 35)">福建</li>
      <li data-val="江西" data-id="2" onclick="$.setVar('claimCity', 36)">江西</li>
      <li data-val="山东" data-id="2" onclick="$.setVar('claimCity', 37)">山东</li>
      <li data-val="河南" data-id="2" onclick="$.setVar('claimCity', 41)">河南</li>
      <li data-val="湖北" data-id="2" onclick="$.setVar('claimCity', 42)">湖北</li>
      <li data-val="湖南" data-id="2" onclick="$.setVar('claimCity', 43)">湖南</li>
      <li data-val="广东" data-id="2" onclick="$.setVar('claimCity', 44)">广东</li>
      <li data-val="广西" data-id="2" onclick="$.setVar('claimCity', 45)">广西</li>
      <li data-val="海南" data-id="2" onclick="$.setVar('claimCity', 46)">海南</li>
      <li data-val="重庆" data-id="2" onclick="$.setVar('claimCity', 50)">重庆</li>
      <li data-val="四川" data-id="2" onclick="$.setVar('claimCity', 51)">四川</li>
      <li data-val="贵州" data-id="2" onclick="$.setVar('claimCity', 52)">贵州</li>
      <li data-val="云南" data-id="2" onclick="$.setVar('claimCity', 53)">云南</li>
      <li data-val="西藏" data-id="2" onclick="$.setVar('claimCity', 54)">西藏</li>
      <li data-val="陕西" data-id="2" onclick="$.setVar('claimCity', 61)">陕西</li>
      <li data-val="甘肃" data-id="2" onclick="$.setVar('claimCity', 62)">甘肃</li>
      <li data-val="青海" data-id="2" onclick="$.setVar('claimCity', 63)">青海</li>
      <li data-val="宁夏" data-id="2" onclick="$.setVar('claimCity', 64)">宁夏</li>
      <li data-val="新疆" data-id="2" onclick="$.setVar('claimCity', 65)">新疆</li>
    </ul>

    xml.child.foreach(node => {
      val cityList = node.attribute("data-val")
      val idList = node.attribute("onclick")
      if (cityList != None && idList != None) {
        val city = cityList.get.toString()
        val id = idList.get.toString().split(", ")(1).substring(0, 2)
        println(city + "的ID是:" + id + "\t")
      }
    })
  }
}

object tes {
  def main(args: Array[String]) {
    println("$.setVar('claimCity', 11)".split(", ")(1))
    val a = "$.setVar('claimCity', 11)".split(", ")(1).substring(0, 2)
    println(a)
  }
}