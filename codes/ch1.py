import sqlite3
import pandas as od
conn=sqlite3.connect("ch1.db")
orders_data = {
    "order_id": [
        1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
        1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020,
        1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030,
        1031, 1032, 1033, 1034, 1035
    ],
    "customer_name": [
        "Ahmed Ali", "Sara Mahmoud", "Omar Hassan", "Mona Adel", "Youssef Tarek",
        "Nourhan Samy", "Ahmed Ali", "Khaled Walid", "Hana Mostafa", "Tarek Ziad",
        "Salma Amr", "Mahmoud Essam", "Dina Ashraf", "Karim Nabil", "Aya Mohamed",
        "Mostafa Galal", "Rana Hisham", "Ziad Sherif", "Menna Allah", "Ali Reda",
        "Nadia Kamal", "Hassan Fathy", "Sara Mahmoud", "Eman Sayed", "Wael Gomaa",
        "Laila Magdy", "Amr Diab", "Yara Adel", "Hossam Ghaly", "Mai Ezz",
        "Sherif Ekramy", "Noha Nabil", "Bassem Morsi", "Ramy Sabry", "Donia Samir"
    ],
    "category": [
        "Electronics", "clothing", "Electronics", "Home & Kitchen", "Electronics",
        "Clothing", "Electronics", "Books", "Electronics", "Home & Kitchen",
        "CLOTHING", "Electronics", "Books", "Home & Kitchen", "Electronics",
        "Clothing", "Books", "Electronics", "Home & Kitchen", "Electronics",
        "Clothing", "Books", "clothing", "Electronics", "Home & Kitchen",
        "Clothing", "Electronics", "Books", "Electronics", "Home & Kitchen",
        "Clothing", "Electronics", "Books", "Home & Kitchen", "Electronics"
    ],
    "price": [
        15000, 450, 22000, 1200, 18500,
        600, 15000, 150, 9500000, None,
        800, 12000, 200, 3500, 19000,
        550, 180, 16500, 2800, 14000,
        700, None, 450, 21000, 4200,
        950, 17500, 220, 13500, None,
        500, 25000, 120, 3100, 16000
    ],
    "quantity": [
        1, 2, 1, 1, 1,
        -2, 1, 3, 1, 2,
        1, 1, 2, 1, 1,
        2, 1, 0, 1, 1,
        1, 4, 2, 1, 1,
        2, 1, 2, 1, 1,
        3, 1, 2, 1, 1
    ],
    "discount_pct": [
        10, 0, 15, 5, 10,
        0, 10, 0, 5, 10,
        120, 5, 0, 15, 10,
        0, 0, 5, 10, 10,
        -10, 0, 0, 15, 5,
        10, 10, 0, 5, 0,
        5, 20, 0, 10, 10
    ],
    "order_date": [
        "2026-10-01", "2026-10-01", "2026-10-02", "2026-10-02", "2026-10-03",
        "2026-10-03", "2026-10-01", "2026-10-04", "2026-10-04", "2026-10-05",
        "2026-10-05", "2026-10-06", "2026/10/06", "2026-10-07", "2026-10-07",
        "2026-10-08", "2026-10-08", "2026-10-09", "2026-10-09", "2026-10-10",
        "2026-10-10", "2026-10-11", "2026-10-01", "2026-10-12", "2026-10-12",
        "2026-10-13", "2026-10-13", "2026-10-14", "2026-10-14", "2026-10-15",
        "2026-10-15", "2026-10-16", "2026-10-16", "2026-10-17", "2026-10-17"
    ],
    "city": [
        "Cairo", "Giza", "alex", "Cairo", "Giza",
        "Cairo", "Cairo", "Alexandria", "Cairo", "Giza",
        "Cairo", "Alexandria", "Giza", "cairo", None,
        "Giza", "Cairo", "Alexandria", "Giza", "Cairo",
        "Alexandria", "Cairo", "Giza", "Giza", "Cairo",
        "Alexandria", "Cairo", "Giza", "Alexandria", "Cairo",
        "Giza", "Cairo", "Alexandria", "Giza", "Cairo"
    ],
    "payment_method": [
        "Credit Card", "Cash", "Credit Card", "Wallet", "Credit Card",
        "Cash", "Credit Card", "cash", "Credit Card", "Wallet",
        "Credit Card", "Credit Card", "Cash", "Credit Card", "Wallet",
        "Cash", "Credit Card", "Credit Card", "Wallet", "Credit Card",
        "Cash", "Wallet", "Cash", "Credit Card", "CREDIT CARD",
        "Cash", "Wallet", "Cash", "Credit Card", "Wallet",
        "Cash", "Credit Card", "Cash", "Wallet", "Credit Card"
    ]
}
od.DataFrame(orders_data).to_sql("tb1",conn,index=False,if_exists="replace")
conn.close()