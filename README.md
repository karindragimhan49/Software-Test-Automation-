# 🧪 Software Test Automation using Python & Selenium

This project demonstrates automated testing of [SauceDemo](https://www.saucedemo.com/) using **Python 3** and **Selenium WebDriver**. It is created for **SE3010 – Software Engineering Process & Quality Management** – Assignment 02 (Part B).

---

## 📁 Folder & File Structure

```
Software-Test-Automation-/
├── chromedriver.exe           # ChromeDriver binary
├── driver_setup.py            # Common driver setup module
├── screenshots/               # Screenshots saved for each test case
│   ├── tc01_valid_login.png
│   ├── tc03_valid_checkout.png
│   └── ...
├── tc01_valid_login.py        # ✅ Valid login test
├── tc02_invalid_login.py      # ❌ Invalid login test
├── tc03_valid_checkout.py     # ✅ Valid checkout test
├── tc04_invalid_checkout.py   # ❌ Invalid checkout test
├── tc05_valid_cart.py         # ✅ Valid cart functionality test
├── tc06_invalid_cart.py       # ❌ Invalid cart interaction test
├── tc07_valid_ui_elements.py  # ✅ UI validation test
├── tc08_invalid_ui_elements.py # ❌ UI negative test
```

## ⚙️ Setup Instructions

### ✅ Prerequisites
- Python 3.12+ installed
- Google Chrome installed (latest)
- Matching version of chromedriver.exe in project root
- Selenium installed:
```bash
pip install selenium
```

## 🚀 How to Run Tests

Run individual test cases using:

```bash
python tc01_valid_login.py
python tc02_invalid_login.py
python tc03_valid_checkout.py
...
```

📸 Screenshots are saved automatically to the `screenshots/` folder.

## 🔍 Test Case Summary

| Test Case File | Description | Expected Result |
|----------------|-------------|----------------|
| `tc01_valid_login.py` | Login with valid credentials | ✅ Login success |
| `tc02_invalid_login.py` | Login with invalid credentials | ❌ Login fails |
| `tc03_valid_checkout.py` | Full checkout process | ✅ Checkout success |
| `tc04_invalid_checkout.py` | Invalid checkout flow | ❌ Checkout fails |
| `tc05_valid_cart.py` | Add/remove items in cart | ✅ Cart updates |
| `tc06_invalid_cart.py` | Invalid cart actions | ❌ Action blocked |
| `tc07_valid_ui_elements.py` | Check important UI elements | ✅ Elements exist |
| `tc08_invalid_ui_elements.py` | Check missing/wrong elements | ❌ Elements fail |

## 🖼️ Sample Screenshots

Below are screenshots from all test runs:

### ✅ Valid Login
![Login Success](screenshots/tc01_valid_login.png)

### ❌ Invalid Login
![Login Error](screenshots/tc02_invalid_login.png)

### ✅ Valid Checkout
![Checkout Success](screenshots/tc03_valid_checkout.png)

### ❌ Invalid Checkout
![Checkout Error](screenshots/tc04_invalid_checkout.png)

### ✅ Valid Cart
![Cart Test](screenshots/tc05_valid_cart.png)

### ❌ Invalid Cart
![Cart Error](screenshots/tc06_invalid_cart.png)

### ✅ UI Elements Check
![UI Elements Pass](screenshots/tc07_valid_ui_elements.png)


## 🧠 Technologies Used
* 🐍 Python 3.12
* 🌐 Selenium WebDriver
* 🧪 Automated UI Testing
* 🖥️ Chrome + ChromeDriver


## 📄 License
This project is for academic and learning purposes only.

---

### ✅ Next Steps
1. Create a new README.md in your project root.
2. Paste the content above.
3. Push to GitHub:
```bash
git add README.md
git commit -m "Add full structured README"
git push origin main
```
