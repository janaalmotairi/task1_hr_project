# 📊 HR Analysis Dashboard

## 📝 Project Overview
An interactive HR Analytics Dashboard designed to visualize and manage employee data. This application provides insights into key performance indicators (KPIs).

## ✨ Key Features
* **Dynamic KPIs**: Real-time tracking of total employees, attrition percentage, and average income.
* **Advanced Filtering**: Ability to filter all dashboard visuals and data tables by specific departments.
* **Interactive Visualizations**: Detailed charts for Income by Job Role, Department Distribution, and Attrition Analysis using Plotly.
* **Employee Management**: Integrated forms to add new employee records or update an employee's income directly into the database.

## 🛠️ Tech Stack
* **Python**: Core programming logic.
* **Streamlit**: Web framework for the interactive UI.
* **SQLite & SQLAlchemy**: Local database management and SQL querying.
* **Plotly Express**: High-quality interactive data visualizations.
* **Pandas**: Efficient data manipulation and analysis.

## 🚀 Getting Started
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/janaalmotairi/task1_hr_project.git](https://github.com/janaalmotairi/task1_hr_project.git)

   
2. Install dependencies:
   ```bash
   pip install streamlit pandas plotly sqlalchemy

4. Run the application:
   ```bash
   streamlit run app.py

## 📂 Project Structure

* `app.py`: The main script containing the Streamlit application logic, page navigation (Dashboard, List, Add, Update), and database connections.
* `style.css`: Custom CSS file used to style the dashboard cards and enhance the purple-themed UI.
* `hr_data.db`: SQLite database file that stores all employee records and data.
