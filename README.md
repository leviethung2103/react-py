## ReactPy

ReactPy is a library for building user interfaces in Python without Javascript. 

These interfaces are built from small elements of functionality like buttons text and images.

ReactPy allows you to combine these elements into reusable “components”. 

ReactPy interfaces are made from components which look and behave similarly to those found in ReactJS. 
Designed with simplicity in mind, ReactPy can be used by those without web development experience while also being powerful enough to grow with your ambitions.


```bash
# create environment using miniconda
conda create -n py38 python=3.8
# activate virtual environment
conda activate py38
# install libraries
pip install -r requirements.txt
```


## Usage
```bash
python example_1.py
uvicorn example_7:app
```

## Ưu điểm
- Cú pháp đơn giản, dễ học
- Handle được những components cơ bản như button, events, images, item lists.
- Tạo layout đơn giản dễ dàng kết hợp giữa python và html.
- Chạy khởi tạo server rất là nhanh

## Nhược điểm
- Thư viện còn khá mới, nên tài liệu chưa được nhiều
- Cộng đồng sử dụng thư viện còn ít 
- Khi chạy thì rất khó mà debug lỗi, hầu như không báo lỗi, khó maintain.

