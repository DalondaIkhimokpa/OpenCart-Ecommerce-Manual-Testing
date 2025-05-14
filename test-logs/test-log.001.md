# Test Log 001 – OpenCart Login Testing

| Date       | Tester            | Module | Test Case ID    | Result | Notes                                    |
| ---------- | ----------------- | ------ | --------------- | ------ | ---------------------------------------- |
| 2024-03-15 | Dalonda Ikhimokpa | Login  | TC-OC-LOGIN-001 | Pass   | Admin login successful                   |
| 2024-03-15 | Dalonda Ikhimokpa | Login  | TC-OC-LOGIN-002 | Fail   | Error message missing for wrong password |
| 2024-03-16 | Dalonda Ikhimokpa | Login  | TC-OC-LOGIN-003 | Pass   | Remember me functionality working        |
| 2024-03-16 | Dalonda Ikhimokpa | Login  | TC-OC-LOGIN-004 | Fail   | Account lockout after 3 attempts fails   |

**Environment:**

- OpenCart v4.0.2.1
- Chrome 122, Firefox 121
- PHP 8.1, MySQL 8.0

**Defects Logged:**

- BUG-OC-101: Missing password error message
- BUG-OC-102: No account lockout

**Tester:** Dalonda Ikhimokpa
**Version:** 1.0
**Log Date:** 2024-03-16
