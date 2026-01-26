import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# 1. DB Connection
engine = create_engine('sqlite:///hr_data.db')

st.set_page_config(page_title='HR Analysis Dashboard', layout='wide')

# --- Page Navigation ---

def set_page(page_name):
    st.session_state.page = page_name

def set_dept(dept_name):
    st.session_state.choice = dept_name
    st.session_state.page = "Dashboard"

# --- CSS Styling ---
def load_css(path="style.css"):
    with open(path,"r",encoding="utf-8") as f:     
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# --- Load Data ---
def init_data():
    try:
        df_test = pd.read_sql("SELECT count(*) as cnt FROM employees", con=engine)
        if df_test['cnt'][0] > 0:
            return 
    except:
        pass

init_data()

# --------------
purple_theme = ['#d1c4e9', '#b39ddb', '#9575cd', '#7e57c2', '#673ab7', '#5e35b1', '#4527a0']

if 'choice' not in st.session_state:
    st.session_state.choice = "All Departments"

if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# --- Sidebar ---
with st.sidebar:
    st.title("Navigation Bar")
    st.markdown("---")
    
    st.button("View Employee List", key="nav_list", on_click=set_page, args=("List",))
    st.button("Add New Employee", key="nav_add", on_click=set_page, args=("Add",))

    st.markdown("---")
    st.header("Filters")
    
    try:
        df_all = pd.read_sql("SELECT DISTINCT Department FROM employees", con=engine)
        all_dept = ["All Departments"] + df_all['Department'].tolist()
    except:
        all_dept = ["All Departments"] 

    for dept in all_dept:
        st.button(dept, key=dept, on_click=set_dept, args=(dept,))
                
    current_selection = st.session_state.choice
    st.markdown("---")
    st.caption("Developed by Jana 👩‍💻")


# --- Page 1: Dashboard ---
if st.session_state.page == "Dashboard":

    st.title('HR Analysis Dashboard')
    st.markdown(f'Overview for: **{current_selection}**')
    st.markdown("---") 

    if current_selection == "All Departments":
        where = ""
    else:
        where = f"WHERE Department = '{current_selection}'"

    try:
        q_insights = f"""
            SELECT 
                COUNT(*) as Total,
                SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as AttritionCount,
                AVG(MonthlyIncome) as AvgIncome,
                AVG(HourlyRate) as AvgHourly
            FROM employees {where}
        """
        metrics = pd.read_sql(q_insights, con=engine)
        
        total_emp = metrics['Total'][0]
        if total_emp and total_emp > 0:
            att_count = metrics['AttritionCount'][0] if metrics['AttritionCount'][0] else 0
            att_rate = round((att_count / total_emp * 100), 1)
            avg_income = int(metrics['AvgIncome'][0]) if metrics['AvgIncome'][0] else 0
            avg_hourly = int(metrics['AvgHourly'][0]) if metrics['AvgHourly'][0] else 0

            # Cards Row
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f'<div class="metric-card"><h3>Total Employees</h3><h1>{total_emp}</h1></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="metric-card"><h3>Attrition Rate</h3><h1>{att_rate}%</h1></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="metric-card"><h3>Avg Monthly Income</h3><h1>${avg_income:,}</h1></div>', unsafe_allow_html=True)
            with c4:
                st.markdown(f'<div class="metric-card"><h3>Avg Hourly Rate</h3><h1>${avg_hourly}</h1></div>', unsafe_allow_html=True)

            st.markdown("---")

            # Charts Row 1
            r1_c1, r1_c2 = st.columns(2)
            with r1_c1:
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.subheader("Income by Job Role")
                q_income = f"SELECT JobRole, AVG(MonthlyIncome) as Income FROM employees {where} GROUP BY JobRole"
                df_inc = pd.read_sql(q_income, con=engine)
                fig_inc = px.bar(df_inc, x='JobRole', y='Income', color='Income', color_continuous_scale=px.colors.sequential.Purples)
                fig_inc.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#4527a0'))
                st.plotly_chart(fig_inc, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with r1_c2:
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.subheader("Department Distribution")
                if current_selection == "All Departments":
                    q_dept = "SELECT Department as Label, COUNT(*) as Count FROM employees GROUP BY Department"
                else:
                    q_dept = f"SELECT JobRole as Label, COUNT(*) as Count FROM employees {where} GROUP BY JobRole"
                df_pie = pd.read_sql(q_dept, con=engine)
                fig_pie = px.pie(df_pie, values='Count', names='Label', color_discrete_sequence=purple_theme, hole=0.4)
                fig_pie.update_layout(height=350, margin=dict(t=30,b=0,l=0,r=0), paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_pie, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # Charts Row 2
            st.subheader("Attrition & Hourly Analysis")
            r2_c1, r2_c2 = st.columns(2)

            with r2_c1:
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.caption("Attrition by Status")
                q_att = f"SELECT Attrition, COUNT(*) as Count FROM employees {where} GROUP BY Attrition"
                df_att = pd.read_sql(q_att, con=engine)
                fig_att = px.bar(df_att, x='Attrition', y='Count', color='Attrition', color_discrete_map={'Yes': '#4527a0', 'No': '#b39ddb'})
                fig_att.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#4527a0'))
                st.plotly_chart(fig_att, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with r2_c2:
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.caption("Avg Hourly Rate by Role")
                q_rate = f"SELECT JobRole, AVG(HourlyRate) as Rate FROM employees {where} GROUP BY JobRole"
                df_rate = pd.read_sql(q_rate, con=engine)
                fig_rate = px.bar(df_rate, x='JobRole', y='Rate', color='Rate', color_continuous_scale=px.colors.sequential.Purples)
                fig_rate.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#4527a0'))
                st.plotly_chart(fig_rate, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("No data found. Please check your database.")
    except Exception as e:
         st.error(f"Error: {e}")

# --- Page 2: Employee List ---
elif st.session_state.page == "List":
    st.title("Full Employee List")
    try:
        df_options = pd.read_sql("SELECT DISTINCT Department FROM employees", con=engine)
        list_opts = ["All Departments"] + df_options['Department'].tolist()
    except:
        list_opts = ["All Departments"]

    try:
        curr_index = list_opts.index(current_selection)
    except:
        curr_index = 0

    new_selection = st.selectbox("Filter Table by Department:", options=list_opts, index=curr_index)
    
    if new_selection != current_selection:
        st.session_state.choice = new_selection
        st.rerun()

    st.markdown(f"Currently showing: **{new_selection}**")
    
    if new_selection == "All Departments":
        list_query = "SELECT * FROM employees"
    else:
        list_query = f"SELECT * FROM employees WHERE Department = '{new_selection}'"

    try:
        df_all = pd.read_sql(list_query, con=engine)
        st.dataframe(df_all, use_container_width=True)
    except:
        st.error("No data found.")

# --- Page 3: Add Employee ---
elif st.session_state.page == "Add":
    st.title("Add New Employee")
    st.markdown("Fill in the Employees details")
    
    st.markdown('<div class="metric-card" style="text-align: left;">', unsafe_allow_html=True)
    with st.form("add_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        try:
            q_departments = pd.read_sql("SELECT DISTINCT Department FROM employees", con=engine)
            dept_opts = q_departments['Department'].tolist()
        except:
            dept_opts = ["Sales", "HR", "IT"]

        with c1:
            dept = st.selectbox("Department", options=dept_opts)
            role = st.text_input("Job Role")
            age = st.number_input("Age", 18, 80, 25)
            edu = st.text_input("Education Field", "Life Sciences")
        
        with c2:
            income = st.number_input("Monthly Income ($)", 1000, 50000, 5000)
            rate = st.number_input("Hourly Rate ($)", 10, 200, 50)
            sat = st.slider("Job Satisfaction", 1, 4, 3)
            attrition = st.selectbox("Attrition", ["No", "Yes"])

        submit = st.form_submit_button("Save to Database")
        if submit:
            new_data = pd.DataFrame({
                'Department': [dept], 'JobRole': [role], 'Age': [age], 'EducationField': [edu],
                'MonthlyIncome': [income], 'HourlyRate': [rate], 'Attrition': [attrition], 'JobSatisfaction': [sat]
            })
            new_data.to_sql('employees', con=engine, if_exists='append', index=False)
            st.success("Employee added successfully!")
    st.markdown('</div>', unsafe_allow_html=True)