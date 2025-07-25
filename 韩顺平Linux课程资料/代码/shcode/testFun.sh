#!/bin/bash
#案例1：计算输入两个参数的和(动态的获取)， getSum

#定义函数 getSum
function getSum() {
	
	SUM=$[$n1+$n2]
	echo "和是=$SUM"
}

#输入两个值
read -p "请输入一个数n1=" n1
read -p "请输入一个数n2=" n2
#调用自定义函数
getSum $n1 $n2
