import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px


engine=create_engine('sqlite:///hr_data.db')

st.set_page_config(page_title='HR Analysis Dashboard',layout='wide')

st.markdown("""
<style>
    div.stbutton> button{
            width: 100%;
            border-radius: 0px;
            height: 4em;
            background-color: transparent;
            border: none;
            text-align: left;
            border-bottom: 1px;
            }

    div.stButton> button:hover{
            background-color: #333333
            }
</style>
        """,unsafe_allow_html=True)

if 'choice' not in st.session_state:
    st.session_state.choice="All Departments"

with st.sidebar:
    st.title("Navigation Bar")
    st.markdown("---")

    if st.button("Dashboard",key="nav_dash"):
        st.session_state.page="Dashboard"
        st.rerun()
    if st.button("Add New Employee ",key="nav_add"):
        st.session_state.page="Add"
        st.rerun()

    if st.session_state.get('page','Dashboard')=="Dashboard":
        st.header("Filters")
        df_all=pd.read_sql("SELECT DISTINCT Department FROM employees",con=engine)
        all_dept=["All Departments"]+df_all['Department'].tolist()

    
        for dept in all_dept:
            if st.button(dept,key=dept):
                st.session_state.choice=dept 
                st.rerun()

    current_selection=st.session_state.choice


    st.markdown("---")
    st.caption("Developed by Jana ")

if 'page' not in st.session_state:
    st.session_state.page="Dashboard"



if st.session_state.page=="Dashboard":

    st.title('HR Analysis Dashboard')
    st.markdown('Analysis for Employee Data')
    st.divider()

    if current_selection=="All Departments":
        chart_title="Employee Distirbution Across Departments:"
        q_total="SELECT COUNT(*) AS total FROM employees"
        q_departments="SELECT Department AS Label, COUNT(*) AS Employee_Count FROM employees GROUP BY Department"
    else:
        chart_title="Job Roles Across The Department:"
        q_total=f"SELECT COUNT(*) AS total FROM employees WHERE Department ='{current_selection}'"
        q_departments=f"""SELECT JobRole AS Label, COUNT(*) AS Employee_Count FROM employees WHERE Department= '{current_selection}'
        GROUP BY JobRole"""

    total=pd.read_sql(q_total,con=engine)['total'][0]
    departments=pd.read_sql(q_departments,con=engine)

    col1, col2= st.columns([1,2])
    with col1:
        st.subheader("Total Employee Count:")
        st.markdown(f"""
                <div style="text-algin: center;">
                    <h1 style="font-size: 80px;"> {total}</h1>
                    </div>
                    """,unsafe_allow_html=True)

        
    with col2:
        st.subheader(chart_title)
        fig_pieChart=px.pie(
            departments, values='Employee_Count',
            names='Label',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_pieChart.update_layout(height=300, margin=dict(t=0,b=0,l=0,r=0))
        st.plotly_chart(fig_pieChart,use_container_width=True)

    st.divider()

    st.subheader("Job Satisfaction: ")

    if current_selection=="All Departments":
        q_bar=f"""SELECT Department, AVG(JobSatisfaction) AS job_sat FROM employees
        GROUP BY Department
        """
        df_bar=pd.read_sql(q_bar,con=engine)

        fig_bar=px.bar(
            df_bar,
            x='Department',
            y='job_sat',
            color='Department',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig_bar.update_layout(
            xaxis_title="Department",
            yaxis_title="Job Satisfaction",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )

    else:
        q_bar=f"""SELECT JobRole, AVG(JobSatisfaction) AS job_sat FROM employees
        WHERE Department ='{current_selection}'
        GROUP BY JobRole
        """
        df_bar=pd.read_sql(q_bar,con=engine)

        fig_bar=px.bar(
            df_bar,
            x='JobRole',
            y='job_sat',
            color='' \
            'JobRole',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig_bar.update_layout(
            xaxis_title="Job Role",
            yaxis_title="Job Satisfaction",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )

    st.plotly_chart(fig_bar,use_container_width=True)

elif st.session_state.page=="Add":
    st.title("Add New Employee ")
    st.markdown("Fill in the Employees details")

    with st.form("add_form",clear_on_submit=True):
        q_departments=pd.read_sql("SELECT DISTINCT Department FROM employees",con=engine)
        dept=st.selectbox("Department",options=q_departments['Department'].tolist())
        role=st.text_input("Job Role")
        submit=st.form_submit_button("Save to Database")

        if submit:
            new_data= pd.DataFrame({
                'Department': [dept],
                'JobRole': [role]
            })

            new_data.to_sql('employees',con=engine,if_exists='append',index=False)