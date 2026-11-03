# Workshop 2 — Chapter 1

แบบฝึกหัดเรื่อง **Class และ Object** ใน Python  
แต่ละไฟล์สร้าง class แล้วนำไปสร้าง object เพื่อเก็บข้อมูลและแสดงผล

รันไฟล์ด้วย:

```bash
python work1.py
python work2.py
python work3.py
```

---

## work1.py — Class พื้นฐาน (`Car`)

สร้าง class `Car` ที่มี attribute สองตัว คือ `model` และ `year`

- `__init__` รับค่าตอนสร้าง object
- สร้าง `car1` เป็นรถรุ่น `Lead125` ปี `2025`
- ใช้ `print` แสดงค่า `car1.model` และ `car1.year` โดยตรง

**สิ่งที่ฝึก:** การประกาศ class, constructor, และการเข้าถึง attribute ของ object

**ผลลัพธ์ที่คาดไว้:**

```
Lead125
2025
```

---

## work2.py — Method ของ object (`Person`)

สร้าง class `Person` ที่มี `name` และ `age`

- มี method `greeting()` ที่พิมพ์ข้อความทักทายจากข้อมูลของ object นั้น
- สร้าง `p1` เป็นคนชื่อ `Pond` อายุ `18`
- เรียก `p1.greeting()` เพื่อให้ object พิมพ์ข้อความเอง

**สิ่งที่ฝึก:** การเขียน method ใน class และการเรียก method ผ่าน object

**ผลลัพธ์ที่คาดไว้:**

```
Hello, my name is Pond
I am 18 years old
```

---

## work3.py — หลาย object จาก class เดียวกัน (`Product`)

สร้าง class `Product` ที่มี `product_name` และ `price`

- มี method `show_details()` สำหรับแสดงชื่อสินค้าและราคา
- สร้าง object สองตัวจาก class เดียวกัน:
  - `product1` — E-Book ราคา 199
  - `product2` — Online Course ราคา 1490
- เรียก `show_details()` ของทั้งสอง object

**สิ่งที่ฝึก:** class หนึ่งตัวใช้สร้าง object ได้หลายตัว แต่ละตัวมีข้อมูลของตัวเอง

**ผลลัพธ์ที่คาดไว้:**

```
E-Book
199
Online Course
1490
```
