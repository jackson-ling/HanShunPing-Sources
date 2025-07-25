package com.hspedu.regexp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author 韩顺平
 * @version 1.0
 */
public class RegTheory {

    public static void main(String[] args) {
        String content = "1998年12月8日，第二代Java平台的企业版J2EE发布。1999年6月，Sun公司发布" +
                "了第二代Java平台（简称为Java2）的3个版本：J2ME（Java2 Micro Edition，Java2平台" +
                "的微型版），应用于移动、无线及有限资源的环境；J2SE（Java 2 Standard Edition，Java 2平台" +
                "的标准版），应用于桌面环境；J2EE（Java 2Enterprise Edition，Java 2平台的企业版），" +
                "应用3443于基于Java的应用服务器。Java 2平台的发布，是Java发展过程中最重要的一个里程碑，" +
                "标志着Java的应用开始普及9889 \n";

        //
        String patternStr = "(\\d\\d)(\\d\\d)";
        Pattern pattern = Pattern.compile(patternStr);
        Matcher matcher = pattern.matcher(content);

        /**
         * matcher.find() 方法完成的任务
         *
         * 1. 根据 pattern 的规则, 定位满足规则的字符串(比如:1999) 在content的开始索引位置(0)和结束索引位置+1(4)
         * 2. 将索引位置记录到 属性 int[] groups; 的下标 groups[0] = 0 groups[1] = 4
         *     特别说明: 当在正则表达式中有() ， 则表示分组 (\d\d)(\d\d) ，第1个() 表示第一组
         *     第2个() 表示第2组
         *     2.1如果分组的话 groups[0] groups[1] 记录匹配到的完整结果比如 1999
         *     2.2groups[2] groups[3] 记录匹配到的结果的第一个()的内容的开始索引和结束索引+1 即0和2
         *     2.3groups[4] groups[5] 记录匹配到的结果的第2个()的内容的开始索引和结束索引+1 即2和4
         * 3. 并且oldLast 属性也设置为 35, 表示下一次匹配从35开始
         *
         * 4. 什么时候返回false.
         *
         *
         * matcher.group(0) 方法完成的任务
         *     public String group(int group) {
         *         if (first < 0)
         *             throw new IllegalStateException("No match found");
         *         if (group < 0 || group > groupCount())
         *             throw new IndexOutOfBoundsException("No group " + group);
         *         if ((groups[group*2] == -1) || (groups[group*2+1] == -1))
         *             return null;
         *         return getSubSequence(groups[group * 2], groups[group * 2 + 1]).toString();
         *     }
         * 1. 根据int[] groups 记录的位置，从content字符串，截取 groups[0]到 groups[1]-1 的子字符串
         * 2. 如果matcher.group(1) groups[2]0到groups[3]2 对应索引的子字符串
         * 2. 如果matcher.group(2) groups[4]2到groups[5]4 对应索引的子字符串
         * 然后循环的执行find和group的方法
         *
         *
         * 看看分组的情况..
         */
        while (matcher.find()) {
            System.out.println("找到: " +matcher.group(0));
            System.out.println("第一个()[第一组]: " +matcher.group(1));
            System.out.println("第2个()[第2组]: " +matcher.group(2));
        }


        System.out.println("ok");
    }
}
