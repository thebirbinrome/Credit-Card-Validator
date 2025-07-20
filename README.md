# Credit Card Validator

This Python script validates credit card numbers using the **Luhn Algorithm**, a simple checksum formula used to validate a variety of identification numbers.

## 💻 How it works

- It strips spaces and dashes from the input number.
- It reverses the number and:
  - Doubles every second digit.
  - Sums the digits of products >=10.
- It adds all digits together and checks if the total is divisible by 10.

## 📦 Example

```python
Input:  '4111-1111-4555-1141'
Output: VALID!
