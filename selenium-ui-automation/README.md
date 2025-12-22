# Selenium UI Automation – Demo E-Commerce Project

A UI test automation framework built with **Python**, **Selenium**, and **Pytest**, targeting a demo e-commerce website.

This project demonstrates:
- Clean automation architecture with **Page Object Model**
- Robust **pytest fixtures** and reusable test data
- Secure **environment variables** for sensitive values
- **Allure** test reporting (local + CI)
- **Docker** execution (headless Chrome)
- **CI/CD** with GitHub Actions and automatic **GitHub Pages** publishing of the Allure HTML report

---

## 🔧 Tech Stack

- Language: Python 3.11  
- Automation: Selenium WebDriver 4  
- Test Runner: Pytest  
- Reporting: Allure Framework  
- Driver Management: webdriver-manager  
- Containerization: Docker (Headless Chrome)  
- CI/CD: GitHub Actions (Docker-based execution + GitHub Pages deploy)

---

## ✅ Key Features

### E-Commerce Flows Covered
- New user registration + delete account (cleanup)
- Login (valid & invalid)
- Logout flow
- Product search
- Category browsing (Women / Men)
- Product detail navigation
- Add / remove products from cart
- Quantity verification
- Newsletter subscription (Home & Cart)
- Test Cases page validation

### Maintainable Architecture
- Page Object Model for clean, reusable UI actions
- Improved base utilities for stability and clarity:
  - wait_for_visible(locator) – fails with clear assertion if element is not visible
  - wait_for_clickable(locator) – fails with clear assertion if element is not clickable

### Pytest Framework Quality
- Reusable fixtures:
  - home – opens BASE_URL, validates Home page, returns HomePage
  - user_data (session scoped) – loads JSON once per run
  - existing_user – provides stable user test data
- Data-driven testing via pytest.mark.parametrize
- Optional smoke suite via pytest.mark.smoke

### Allure Reporting (Minimal & Practical)
Project convention:
- allure.feature is used to group tests by system area
- allure.title is used to provide human-readable test names
- No over-tagging (story / severity only when truly needed)

### Secure Secrets Handling
- Passwords are never stored in JSON or source code
- Sensitive data is injected via environment variables:
  - os.getenv("USER_PASSWORD") for local runs
  - GitHub Secrets (USER_PASSWORD) in CI pipelines

---

## 📁 Project Structure

selenium-ui-automation/
├── pages/
├── tests/
├── data/
├── utilities/
├── screenshots/
├── conftest.py
├── requirements.txt
├── Dockerfile
└── README.md

---

## 🔐 Environment Variables (Required)

Before running the tests, define the existing user password as an environment variable.

Local (Mac / Linux):

export USER_PASSWORD="YourLocalPassword"

In CI, the same variable is injected using GitHub Secrets.

---

## ▶️ Running Tests Locally (No Docker)

1. Create and activate a virtual environment:

cd selenium-ui-automation  
python3 -m venv .venv  
source .venv/bin/activate  

2. Install dependencies:

pip install --upgrade pip  
pip install -r requirements.txt  

3. Run the test suite and generate Allure results:

pytest --alluredir=allure-results  

4. View the Allure report (Allure CLI must be installed locally):

allure serve allure-results  

5. Run smoke tests only:

pytest -m smoke --alluredir=allure-results  

---

## 🐳 Running Tests with Docker (Headless)

1. Build the Docker image:

cd selenium-ui-automation  
docker build -t selenium-tests .  

2. Run tests inside the Docker container and export Allure results:

docker run --rm \
  -e USER_PASSWORD="YourLocalPassword" \
  -v "$(pwd)/allure-results:/app/allure-results" \
  selenium-tests  

3. View the Allure report locally:

allure serve allure-results  

---

## ⚙️ CI/CD – GitHub Actions + GitHub Pages

Workflow file:

.github/workflows/tests.yml

Pipeline behavior:
- Checkout repository
- Build Docker image
- Run tests inside Docker (headless Chrome)
- Collect allure-results
- Generate Allure HTML report
- Upload report as Pages artifact
- Deploy report to GitHub Pages

After a successful run, the Allure report is available at:

https://<username>.github.io/<repository>/

Repository Settings → Pages → Source must be set to **GitHub Actions**.

---

## 🧩 Fixtures Overview (conftest.py)

- home  
  Opens BASE_URL, verifies Home page visibility, returns HomePage.

- user_data (session scope)  
  Loads test data once from JSON.

- existing_user  
  Provides stable existing user data for login and related flows.

---

## ✅ Notes
- Secrets are handled only via environment variables.
- Allure annotations are kept minimal and consistent.
- Smoke tests cover only broad, system-level functionality.
