# McDonald's India Interactive Macro Calculator

An interactive web application built with Python and Streamlit that allows users to build a custom meal from the McDonald's India menu and instantly track its nutritional information.

<img width="1735" height="941" alt="image" src="https://github.com/user-attachments/assets/e9d44617-d749-4134-8fd1-264e857ea531" />


## Features

-   **Dynamic Meal Builder**: Add or remove items and adjust quantities on the fly.
-   **Real-Time Macro Calculation**: Your meal's totals for calories, protein, carbs, fat, sugar, and sodium are updated instantly.
-   **Interactive Calorie Chart**: A visual breakdown of the percentage of calories derived from protein, carbohydrates, and fat.
-   **Daily Goal Tracking**: Set personal calorie and protein targets and see your progress with intuitive progress bars.
-   **Live Search & Filtering**: Quickly find any menu item by name, filter by multiple categories (e.g., Burgers, Drinks), and sort by any nutritional value.

## Tech Stack

-   **Language:** Python
-   **Framework:** Streamlit
-   **Data Manipulation:** Pandas

## Local Setup and Installation

Follow these steps to run the project on your local machine.

### 1. Prerequisites

-   Python 3.8 or newer installed and added to your system's PATH.

### 2. Clone the Repository

Clone this project to your local machine.
```bash
git clone https://github.com/Lemnistatic/McD-Macro-Calculator-Streamlit-
```

### 3. Create a `requirements.txt` file

Create a file named `requirements.txt` in your project folder and add the following lines to it:
```
streamlit
pandas
```

### 4. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### 5. Install Dependencies

Install the necessary libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit App

Launch the application using the following command:
```bash
streamlit run app.py
```

The application will automatically open in a new tab in your web browser.
