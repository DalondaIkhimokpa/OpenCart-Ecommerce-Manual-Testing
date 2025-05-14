# Test Log 002 – OpenCart Checkout Testing

| Date       | Tester            | Module   | Test Case ID       | Result | Notes                                   |
| ---------- | ----------------- | -------- | ------------------ | ------ | --------------------------------------- |
| 2024-03-17 | Dalonda Ikhimokpa | Checkout | TC-OC-CHECKOUT-001 | Pass   | Guest checkout completed                |
| 2024-03-17 | Dalonda Ikhimokpa | Checkout | TC-OC-CHECKOUT-002 | Fail   | Shipping cost not updating with address |
| 2024-03-18 | Dalonda Ikhimokpa | Checkout | TC-OC-CHECKOUT-003 | Pass   | Credit card payment processed           |
| 2024-03-18 | Dalonda Ikhimokpa | Checkout | TC-OC-CHECKOUT-004 | Fail   | Order confirmation email not sent       |

**Environment:**

- OpenCart v4.0.2.1
- Safari 17, Edge 121
- Test Payment Gateway: Sandbox Mode

**Defects Logged:**

- BUG-OC-103: Shipping calculation error
- BUG-OC-104: Email delivery failure

**Tester:** Dalonda Ikhimokpa
**Version:** 1.0
**Log Date:** 2024-03-18
