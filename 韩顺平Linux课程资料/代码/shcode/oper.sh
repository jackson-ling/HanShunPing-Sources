#!/bin/bash
#案例1：计算（2+3）X4的值
#使用第一种方式
RES1=$(((2+3)*4))
echo "res1=$RES1"
#使用第二种方式, 推荐使用
RES2=$[(2+3)*4]
echo "res2=$RES2"
#使用第三种方式 expr
TEMP=`expr 2 + 3`
RES4=`expr $TEMP \* 4` 
echo "temp=$TEMP"
echo "res4=$RES4" 
#案例2：请求出命令行的两个参数[整数]的和 20 50
SUM=$[$1+$2]
echo "sum=$SUM"
