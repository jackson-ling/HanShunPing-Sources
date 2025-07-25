#!/bin/bash
#案例1 ：从1加到100的值输出显示, 如何把 100做成一个变量
#定义一个变量 SUM
SUM=0
for(( i=1; i<=$1; i++))
do
#写上你的业务代码
	SUM=$[$SUM+$i]
done
echo "总和SUM=$SUM"
