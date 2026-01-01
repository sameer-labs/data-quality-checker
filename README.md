# CSV Data Cleaning Automation

## Overview

This project automates the **cleaning and validation of CSV datasets** using Python.
It focuses on detecting **missing and dirty data**, safely cleaning numeric fields,
and producing both a **cleaned output file** and a **data quality summary**.

The script is designed to handle **messy real-world data**, making it suitable for
beginner portfolios, freelancing tasks, and data preprocessing pipelines.

---

## Features

* Detects missing or dirty values (`null`, empty fields, extra spaces)
* Cleans and standardises numeric data (removes units such as `kmpl`, `CC`, `bhp`)
* Converts missing values to `NaN` for analysis readiness
* Generates a column-wise data quality summary
* Preserves valid text fields safely
* Works with real-world, inconsistent CSV data

---

## Input

* CSV file containing **used car listings**, including:

  * Mileage, Engine size, Power, Seats, and Price
  * Mixed text and numeric values
  * Missing or inconsistent entries

Example input fields:

```
Name, Location, Year, Mileage, Engine, Power, Seats, New_Price
```

---

## Output

* **Cleaned CSV file** (`used_cars_cleaned.csv`)
* **Console summary report** showing the number of detected issues per column

Example summary:

```
Power: 1 issue detected
New_Price: 4 issues detected
```

---

## How to Run

```bash
python src/clean_csv.py
```

Ensure the input CSV file is in the same directory or update the file path in the script.

---

## Use Cases

* Data cleaning for analytics or machine learning
* Freelance CSV cleanup tasks
* Data quality validation before reporting
* Beginner-friendly automation project

---

## Technologies Used

* Python
* csv module
* NumPy
