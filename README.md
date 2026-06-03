# UsefuI-T00I
This is useful tool for calculation

This repository provides a set of lightweight, local tools designed to help AI agents perform complex data analysis and mathematical calculations on local structured data.

## Features
* **Automated Data Loading**: Easily reads and parses numerical data from the `sandbox/` directory.
* **Advanced Calculator**: Provides explicit mathematical tools for calculating sums, averages, and regressions.
* **Report Generation**: Automatically exports calculation results to the `sandbox/output/` directory.

## Getting Started

### 1. Prerequisites
Ensure your agent has access to the following capabilities:
* File Read (for analyzing `sandbox/data.csv`)
* File Write (for saving reports to `sandbox/output/`)
* Tool Execution (for running functions in `tools/calculator.py`)

### 2. Usage Scenario
Ask your agent to process the sample dataset:
> "Please read the data inside `sandbox/data.csv`, calculate the average of the values, and save the final summary report to the output folder."
