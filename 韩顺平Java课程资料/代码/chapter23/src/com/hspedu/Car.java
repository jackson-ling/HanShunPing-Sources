package com.hspedu;

/**
 * @author 韩顺平
 * @version 1.0
 */
public class Car {
    public String brand = "宝马";//品牌
    public int price = 500000;
    public String color = "白色";

    @Override
    public String toString() {
        return "Car{" +
                "brand='" + brand + '\'' +
                ", price=" + price +
                ", color='" + color + '\'' +
                '}';
    }
}
