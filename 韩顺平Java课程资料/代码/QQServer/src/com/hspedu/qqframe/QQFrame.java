package com.hspedu.qqframe;

import com.hspedu.qqserver.service.QQServer;

/**
 * @author 韩顺平
 * @version 1.0
 * 该类创建QQServer ,启动后台的服务
 */
public class QQFrame {
    public static void main(String[] args)  {
        new QQServer();
    }
}
