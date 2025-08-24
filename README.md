## AKSHAY SADAMATE

This project contains an **SQLite database** (`assign.db`) 
It includes four tables: **Customer, Items, Sales, and Orders**.

---

## Database Schema

### Customer
| Column       | Type    |
|--------------|---------|
| customer_id  | INTEGER (PK) |
| age          | INTEGER |

### Items
| Column       | Type    |
|--------------|---------|
| item_id      | INTEGER (PK) |
| item_name    | TEXT |
| price        | REAL |

### Sales
| Column       | Type    |
|--------------|---------|
| sales_id     | INTEGER (PK) |
| customer_id  | INTEGER (FK → Customer.customer_id) |
| total_amount | REAL |

### Orders
| Column       | Type    |
|--------------|---------|
| order_id     | INTEGER (PK) |
| sales_id     | INTEGER (FK → Sales.sales_id) |
| item_id      | INTEGER (FK → Items.item_id) |
| quantity     | INTEGER |

---

## Data

### Customer
| customer_id | age |
|-------------|-----|
| 1 | 25 |
| 2 | 30 |
| 3 | 22 |
| 4 | 40 |

### Items
| item_id | item_name | price |
|---------|-----------|-------|
| 1 | Laptop  | 750.00 |
| 2 | Mouse   | 25.50  |
| 3 | Keyboard| 45.00  |
| 4 | Monitor | 150.00 |

### Sales
| sales_id | customer_id | total_amount |
|----------|-------------|--------------|
| 1 | 1 | 775.50 |
| 2 | 2 | 195.00 |
| 3 | 3 | 25.50 |
| 4 | 4 | 8
