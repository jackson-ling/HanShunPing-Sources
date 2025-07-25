#!/bin/bash
#案例1："ok"是否等于"ok"
#判断语句：使用 =
if [ "ok" = "ok" ]
then
	echo "equal"
fi
#案例2：23是否大于等于22
#判断语句：使用 -ge
if [ 23 -ge 22 ]
then 
	echo "大于"
fi
#案例3：/root/shcode/aaa.txt 目录中的文件是否存在
#判断语句： 使用 -f 
if [ -f /root/shcode/aaa.txt ]
then 
	echo "存在"
fi
#看几个案例
if [ hspedu ]
then 
	echo "hello,hspedu"
fi
