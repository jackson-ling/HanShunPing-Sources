package com.hspedu.exception_;

/**
 * @author 韩顺平
 * @version 1.0
 */
public class NumberFormatException_ {
    public static void main(String[] args) {
        String name = "韩顺平教育";
        //将String 转成 int
        int num = Integer.parseInt(name);//抛出NumberFormatException
        System.out.println(num);//1234
    }
}
