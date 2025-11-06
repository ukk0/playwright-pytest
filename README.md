# SauceDemo E2E Tests with Playwright + pytest

This project demonstrates **end-to-end UI testing** of the [SauceDemo](https://www.saucedemo.com/) web application using **Playwright + pytest**.  
A [separate project of mine](https://github.com/ukk0/saucedemo-playwright-behave) utilizes instead **Playwright + Behave** to explore **BDD workflows** for the same web app. 
Both serve as a comparison of different frameworks and approaches to test design.

---

## Project overview
The goal of this project is to provide not 100% thorough, but high **functional test coverage** of the SauceDemo site using a **scalable, modular, and reusable framework** built with pytest.

It emphasizes:
- The use of **fixtures** and **parametrization** for reusability and maintainability  
- Clean separation of concerns using the **Page Object Model (POM)**  
- Consistent code quality enforced through **pre-commit hooks**

---

## Project structure

├── pages/              # Page Object Models (POMs)  
├── tests/              # Test files  
├── conftest.py         # Shared fixtures and test setup  
├── requirements.txt  
├── pytest.ini  
└── .pre-commit-config.yaml  

---

## Setup

This project was developed using **Python 3.13**.  
It’s recommended to use the same version to ensure compatibility.

Install dependencies and Playwright browsers:
```bash
pip install -r requirements.txt
playwright install
```

Enabling pre-commit hooks:

```bash
pre-commit install
```

---

## Running tests

Run all tests:

```bash
pytest
```

Run specific tests:

```
pytest <path_to_test_file>
```

Run tests in parallel with the help of pytest-xdist:

```bash
pytest -n auto
```
(the 'auto' option will automatically distribute test execution across all available CPUs, you can also
replace it with a specific number you would like to utilize, f.e. ```pytest -n 4```)

Additional test configuration options (browser, headless mode, slow motion, etc.) will be added later.

---

## Code quality

Pre-commit hooks automatically ensure clean and consistent code using:
- ruff — linting and formatting
- isort — import sorting

Hooks will automatically run during commits for changed files.  
They can also be run manually for all files with:
```bash
pre-commit run --all-files
```

---

## Test reporting

(Coming soon. Framework and format TBD)

---

## CI/CD Integration

(Coming soon. GitHub Actions pipeline will be added together with reporting)
