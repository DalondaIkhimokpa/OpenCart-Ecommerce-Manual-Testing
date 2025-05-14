# 🧪 Test Strategy - OpenCart E-commerce 


- **Project:** OpenCart E-commerce
- **Test Plan ID:** OPEN-CART-TP-001
- **Author:** Dalonda Ikhimokpa
- **Report Date:** March 5, 2025
- **Version:** 1.0

## 1. Objective

Define the overall approach to testing the OpenCart platform, covering types, levels, tools, environments, and responsibilities.

---

## 2. Testing Scope

- ✅ Functional Testing (Login, Cart, Checkout, Orders)
- ✅ Cross-browser & Compatibility
- ✅ Performance Testing (JMeter)
- ✅ Security Testing (SSL, data protection)
- ✅ Regression Testing

---

## 3. Test Types & Levels

| Test Level     | Description                                 |
| -------------- | ------------------------------------------- |
| Unit Testing   | Handled by devs (not in scope)              |
| Integration    | API interactions between cart & payment     |
| System Testing | Full platform validation                    |
| Acceptance     | Final verification vs business requirements |

---

## 4. Test Design Techniques

- Equivalence Partitioning
- Boundary Value Analysis
- Decision Tables (for payment flows)
- Error Guessing (for cart/session issues)

---

## 5. Test Environments

| Component   | Configuration                        |
| ----------- | ------------------------------------ |
| Web Server  | Apache, Nginx                        |
| DB          | PostgreSQL                           |
| Frontend    | React 18.2, jQuery                   |
| OS/Browsers | Windows/macOS, Chrome/Firefox/Safari |

---

## 6. Tools Used

| Tool     | Purpose                        |
| -------- | ------------------------------ |
| JIRA     | Bug tracking                   |
| TestRail | Test case & execution mgmt     |
| JMeter   | Load & performance testing     |
| Excel    | Manual test logs and reporting |

---

## 7. Entry/Exit Criteria

**Entry**:

- Environment ready
- Requirements approved
- Test cases designed

**Exit**:

- 100% test execution
- No Critical/High bugs open
- Final test report submitted

---

## Author: Dalonda Ikhimokpa

**Date:** March 5, 2024
**Version:** 1.0
