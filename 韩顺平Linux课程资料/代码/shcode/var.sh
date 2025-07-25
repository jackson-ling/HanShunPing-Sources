#!/bin/bash
#案例1：定义变量A
A=100
#输出变量需要加上$
echo A=$A
echo "A=$A"
#案例2：撤销变量A
unset A
echo "A=$A"
#案例3：声明静态的变量B=2，不能unset
readonly B=2
echo "B=$B"
#unset B
#将指令返回的结果赋给变量
:<<!
C=`date`
D=$(date)
echo "C=$C"
echo "D=$D"
!
#使用环境变量TOMCAT_HOME
echo "tomcat_home=$TOMCAT_HOME"
