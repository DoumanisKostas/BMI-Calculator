# BMI Calculator

A simple desktop application for calculating the Body Mass Index (BMI). This application allows users to input their height and weight to determine their BMI and corresponding weight category.

## Features

- Input height (in meters) and weight (in kilograms).
- Calculates BMI and determines the weight category (Underweight, Normal weight, Overweight, Obese).
- Displays the result in a message box.
- Option to save the result to a text file.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bmi-calculator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd bmi-calculator
    ```

3. Ensure you have Python 3 installed. Tkinter should be included by default. If not, install it using:
    ```bash
    pip install tk
    ```

## Usage

1. Run the application:
    ```bash
    python bmi_calculator.py
    ```

2. Enter your first name, last name, age, height (in meters), and weight (in kilograms).

3. Click "Calculate BMI" to compute your BMI and see the result.

4. The result will be displayed in a message box.

5. Click "Save" to save the result to a text file.

## Code Explanation

- **calculate_bmi()**: This function retrieves the user's height and weight, calculates the BMI, determines the weight category, displays the result, and saves it to a file.
- **save_result(result)**: This function prompts the user to choose a file location to save the BMI result.
- **center_window(window, width, height)**: This function centers the application window on the screen.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For bug reports or feature requests, please use the GitHub issues page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by common BMI calculation methods and user feedback.
