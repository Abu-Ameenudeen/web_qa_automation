
# 🧪 Web QA Automation Suite

Automated UI testing framework built using **Python**, **Selenium**, and **Pytest**.  
Test target: [SauceDemo.com](https://www.saucedemo.com) — a dummy e-commerce site for QA practice.

---

## 🚀 Features

- ✅ Login test (valid and invalid)
- ✅ Add to cart test
- ✅ Logout test
- ✅ HTML test reports with `pytest-html`
- ✅ Pytest markers: `smoke`, `regression`, `negative`
- ✅ Page Object Model (POM) structure
- ✅ Config-based setup (URL, credentials)

---

## 🗂️ Project Structure

```bash
web_qa_automation/
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_invalid_login.py
│   └── test_add_to_cart.py
│
├── utils/
│   ├── driver_factory.py
│   └── config.py
│
├── drivers/       # ChromeDriver here
├── reports/       # HTML reports output
├── conftest.py    # Browser fixture
├── pytest.ini     # Pytest marker config
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/web_qa_automation.git
cd web_qa_automation
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate  # For Windows with Git Bash
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Setup ChromeDriver

- Download ChromeDriver from the official source:  
  [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

- Make sure the version matches your installed Chrome browser.

- Extract `chromedriver.exe` and place it in the `drivers/` directory of this project:

```bash
web_qa_automation/
└── drivers/
    └── chromedriver.exe
```

---

## ▶️ Running Tests

### Run all tests:
```bash
pytest
```

### Run only smoke tests:
```bash
pytest -m "smoke"
```

### Run only regression tests:
```bash
pytest -m "regression"
```

### Run only negative tests:
```bash
pytest -m "negative"
```

### Generate an HTML report:
```bash
pytest --html=reports/test_report.html
```

> The HTML report will be saved in the `reports/` folder. Open it in your browser to view detailed test results.

---

## 🧪 Example Test Case

```python
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_item_to_cart()

    cart_count = products_page.get_cart_count()
    assert cart_count == "1"
```

---

## 👨‍💻 Author

**Abu Ameenudeen**  
GitHub: [Abu-Ameenudeen](https://github.com/Abu-Ameenudeen)

---

## ✅ License

This project is for educational and demonstration purposes.
