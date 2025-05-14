# 🧪 Test Log - OpenCart E-commerce Project

## Test ID: TL-002

### Test Case ID: TC-CHECKOUT-001

### Date: Mar 19, 2024

### Executed By: Dalonda Ikhimokpa

---

## Test Objective:

Verify that the checkout process works correctly with a valid payment method.

---

## Test Steps:

1. Add products to the cart.
2. Proceed to checkout.
3. Enter valid shipping details.
4. Choose Stripe as the payment method.
5. Complete the payment by clicking on the "Pay Now" button.

---

## Test Data:

- **Product:** 2 x Widget A
- **Shipping Address:** 123 Test St, Lakewood 98439
- **Payment Method:** Stripe (valid credit card)

---

## Expected Result:

The checkout should complete successfully, and the user should receive an order confirmation.

---

## Actual Result:

Test Failed: Payment processed but the amount for the order was incorrect; user did receive a confirmation.

---

## Status: Fail

---

- ## Test Execution Notes:
- The issue is intermittent, with payment amount updating failures occurring 20% of the time during checkout.
- Bug ID: BUG-002 has been logged for further investigation.
- Test marked as "Blocked" pending resolution of BUG-002.

---

## Attached Files:

- [Attached: Screenshot of error message during payment]
  [screenshot.1](/assets/screenshots/Screenshot%202025-05-13%20at%2012.45.47 PM.png)
  [screenshot.2](/assets/screenshots/Screenshot%202025-05-13%20at%201.41.44 PM.png)
  [screenshot.3](/assets/screenshots/Screenshot%202025-05-13%20at%201.51.41 PM.png)
  [screenshot.4](/assets/screenshots/Screenshot%202025-05-13%20at%201.52.05 PM.png)

**Tester:** Dalonda Ikhimokpa
**Version:** 1.0
**Log Date:** 2024-03-19
