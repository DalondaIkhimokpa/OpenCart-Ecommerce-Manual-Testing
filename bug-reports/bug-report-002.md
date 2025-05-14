🐞 Bug Report - OpenCart E-commerce Project

## Bug ID: BUG-004

### Title: Incorrect Order Total Calculation for Cash on Delivery (COD)

### Reported By: Dalonda Ikhimokpa

### Date Reported: March 23, 2024

### Severity: High (Financial Impact)

### Priority: Urgent

### Status: Open

---

## Description:

When selecting Cash on Delivery (COD) as the payment method, the final checkout amount incorrectly reduces the total price instead of displaying the correct sum (product price + shipping fee).

Example Scenario:

- Product Price: $122
- Shipping Fee: $5
- Expected Checkout Total: $127
- Actual Checkout Total: $105 (Incorrect)

---

## Steps to Reproduce:

1. Add a product to cart (e.g., $122)
2. Proceed to checkout
3. Select Cash on Delivery (COD) as payment
4. Observe the final amount displayed before order confirmation
5. Expected: $127 (Product + Shipping)
6. Actual: $105 (Wrong Calculation)

---

## Expected Result:

- Correct total ($122 + $5 shipping = $127) is displayed and charged

## Actual Result:

- Incorrect total ($105) is shown at checkout

---

## Environment:

- OpenCart Version: 3.0.3.8
- Payment Method: Cash on Delivery (COD)
- Browser: Chrome, Firefox, Safari (All affected)
- OS: Windows, macOS, Android, iOS

---

## Evidence:

Screenshots:

1. [Cart Page] - Shows correct subtotal ($122 + $5 shipping)
2. [Checkout Page] - Displays incorrect COD total ($105)

Logs:
[Error] Order #10030: Cart Total = $127, COD Checkout = $105

## Screenshots/Logs:

 [Attached: Screenshot of checkout page showing incorrect total]

- [screenshot.1](/assets/screenshots/Screenshot%202025-05-13%20at%201.51.41 PM.png)

---

## Root Cause (Suspected):

- Possible bug in shipping fee exclusion during COD calculation
- Tax or discount misapplication in checkout flow

---

## Assigned To: Payment & Checkout Team

### Fix Deadline: April 3, 2024

---

## Notes:

- Critical Issue - Affects all COD transactions
- Suggested Fix:
  1. Audit the COD payment module for calculation errors
  2. Test with multiple product combinations to verify correct totals

**Tester:** Dalonda Ikhimokpa
**Version:** 1.0
**Log Date:** 2024-03-23
