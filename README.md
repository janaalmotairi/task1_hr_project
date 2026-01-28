# 📊 HR Analysis Dashboard

## 📝 Project Overview
This project is a comprehensive HR data analysis focused on understanding employee attrition cycles. It combines exploratory data analysis (EDA) conducted in a Jupyter Notebook with an interactive web dashboard built using Streamlit to visualize key insights and trends in employee demographics and turnover.

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
* `hr_analysis.ipynb`:Jupyter Notebook containing Exploratory Data Analysis,Data cleaning.
* `WA_Fn-UseC_-HR-Employee-Attrition.cvc`: the dataset source used for analysis and dashboard visualizaion.
* `hr_data.db`: SQLite database file that stores all employee records and data.

## 📷 Screenshots
**Dashboard**:
  <img width="2158" height="1182" alt="Screenshot 2026-01-26 152754" src="https://github.com/user-attachments/assets/e03f86fb-7309-4e02-90d0-a15f9d1e9cb9" /><img width="1616" height="829" alt="Screenshot 2026-01-26 152821" src="https://github.com/user-attachments/assets/573000fb-88da-469e-a2b2-33dcd2a0debb" /><img width="1650" height="904" alt="Screenshot 2026-01-26 152829" src="https://github.com/user-attachments/assets/15106015-67b3-4168-8b48-737e3ffa8936" />
The main dashboard provides a comprehensive view of HR metrics. It begins with high-level **KPI Cards** (Total Employees, Attrition Rate, Avg Income) for quick insights, followed by detailed interactive visualizations analyzing **Income by Job Role**, **Department Distribution**, **Attrition** and **Hourly Rate** statistics, additionally on the sidebar you are able to filter insights by Department.

**View Employee List**:
<img width="2130" height="1149" alt="Screenshot 2026-01-26 152850" src="https://github.com/user-attachments/assets/cefaad8d-6af4-44e2-bbeb-a9b8d69cdff8" />
A filterable database view to browse employee records.

**Add Employee**:
<img width="2146" height="1179" alt="Screenshot 2026-01-26 152919" src="https://github.com/user-attachments/assets/a4b56ba0-e28f-4aab-9967-cf9842c3a925" />
A user-friendly form to Add employees and save details to the database.

**Update Income**:
<img width="2142" height="1160" alt="Screenshot 2026-01-26 152937" src="https://github.com/user-attachments/assets/f4fabfed-2ec3-4bb9-8985-97ce15bcaab2" />
A tool to update employee income by ID.

  

