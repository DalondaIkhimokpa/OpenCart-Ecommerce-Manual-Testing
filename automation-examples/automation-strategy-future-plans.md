## 🛒 **OpenCart E-commerce Manual Testing**

### 🔧 Automation Strategy & Future Plans

This repository currently includes a **SQL-based automation example** that demonstrates how to validate order records in a backend PostgreSQL database. The script can be used after test execution to verify order creation, total values, and customer information.

### ✅ Current Automation Included:

* `order_verification_query.sql` in `/automation-examples/`
  * Confirms that specific orders exist
  * Validates customer linkage and transaction totals

### 🧩 Future Automation Plans:

* Integrate **Selenium WebDriver** to test end-to-end shopping flow
* Automate **user registration and login tests**
* Add **data integrity checks** post-checkout using SQL scripts
* Incorporate **API testing** for endpoints (if exposed)

### 📌 Note for Contributors:

If you're working with a local PostgreSQL instance of OpenCart, run the SQL script using:

psql -U <user> -d <opencart_db> -f automation-examples/order_verification_query.sql


Adjust values as needed. These scripts offer a backend validation layer for database-driven verification.
