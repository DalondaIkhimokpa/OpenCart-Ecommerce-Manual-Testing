# 🐞 Bug Report - OpenCart E-commerce Project

## Bug ID: BUG-001

### Title: Cart Fails to Update Quantity After Adding Product

### Reported By: Dalonda Ikhimokpa

### Date Reported: Mar 30, 2024

### Severity: High

### Priority: High

### Status: Open

---

## Description:

The shopping cart does not reflect updated quantities when a user adds or removes items after adding them to the cart. The issue occurs consistently on all tested browsers (Chrome, Firefox, Safari).

---

## Steps to Reproduce:

1. Navigate to a product page.
2. Click on the "Add to Cart" button.
3. Go to the cart page.
4. Change the quantity of the product (e.g., from 1 to 2).
5. Observe that the cart doesn't reflect the updated quantity, and the total price remains the same.

---

## Expected Result:

The cart should reflect the updated quantity and total price when the quantity of a product is changed.

---

## Actual Result:

The cart shows the same quantity and total price, even after updating the product quantity.

---

## Environment:

- **Browser:** Chrome 90.0.4430.93, Firefox 85.0.1, Safari 14.0
- **OS:** macOS Big Sur (10.16)

---

## Screenshots/Logs:

 [Attached: Screenshot of cart page showing old quantity]

- [screenshot.1](/assets/screenshots/Screenshot%202025-05-13%20at%201.25.25 PM.png)
- [screenshot.2](/assets/screenshots/Screenshot%202025-05-13%20at%201.25.05 PM.png)
- [screenshot.3](/assets/screenshots/Screenshot%202025-05-13%20at%201.23.32 PM.png)

**Error Log:** `Uncaught TypeError: Cannot read property 'updateQuantity' of undefined`

---

## Assigned To: John Doe (Frontend Developer)

### Fix Deadline: April 3, 2024

**Tester:** Dalonda Ikhimokpa
**Version:** 1.0
**Log Date:** 2024-03-30
