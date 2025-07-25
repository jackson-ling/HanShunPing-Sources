#!/bin/bash
#案例1：读取控制台输入一个NUM1值
read -p "请输入一个数NUM1=" NUM1
echo "你输入的NUM1=$NUM1"
#案例2：读取控制台输入一个NUM2值，在10秒内输入。
read -t 10 -p "请输入一个数NUM2=" NUM2
echo "你输入的NUM2=$NUM2"
