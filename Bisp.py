# # import streamlit as st
# # import matplotlib.pyplot as plt
# # import datetime as dt
# # import pandas as pd
# # import numpy as np
# # import pandas_profiling
# # from streamlit_pandas_profiling import st_profile_report
# # uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
# # data = pd.read_csv(uploaded_data)
# # # create the pandas profiling report
# # pr = data.profile_report()
# # st_profile_report(pr)
# # # optional, save to file
# # pr.to_file('pandas_prof.html')


# import pandas as pd
# import pandas_profiling
# import streamlit as st

# from streamlit_pandas_profiling import st_profile_report

# df = pd.read_csv(
#     "https://storage.googleapis.com/tf-datasets/titanic/train.csv")
# pr = df.profile_report()

# st_profile_report(pr)


# # def load_data():
# #     # df=load_data.clear()
# #     # loading online csv
# #     data = "https://kobo.humanitarianresponse.info/api/v2/assets/a5n7ThvXYrgR4QsQQmAJPN/export-settings/esLUM5TFwKdqbzRnsZLf2Qj/data.csv"  # ,";")
# #     # s = requests.get(url).content
# #     data = pd.read_csv(data, on_bad_lines='skip', sep=";")
# #     df = pd.DataFrame(data)

# #     return df


# # if st.button("Click Me To Get Refresh Data"):
# #     # Clears all singleton caches:
# #     #     st.experimental_singleton.clear()
# #     load_data.clear()
# # df = load_data()

# # pr = df.profile_report()
# # st_profile_report(pr)
# # # df.head()
# # # profile = ProfileReport(df, title="Pandas Profiling Report")
# # # profile.to_file("Anylsis")


from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from PIL import Image

st.set_page_config(layout='wide')  # Choose wide mode as the default setting

# Add a logo (optional) in the sidebar
# logo = Image.open(r'C:\Users\13525\Desktop\Insights_Bees_logo.png')
# st.sidebar.image(logo,  width=120)

# Add the expander to provide some information about the app
with st.sidebar.expander("About the App"):
    st.write("""
        This data profiling App was built by My Data Talk using Streamlit and pandas_profiling package. You can use the app to quickly generate a comprehensive data profiling and EDA report without the need to write any python code. \n\nThe app has the minimum mode (recommended) and the complete code. The complete code includes more sophisticated analysis such as correlation analysis or interactions between variables which may requires expensive computations. )
     """)

# Add an app title. Use css to style the title
st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Import your data and generate a Pandas data profiling report easily...</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your csv file:", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    option1 = st.sidebar.radio(
        'What variables do you want to include in the report?',
        ('All variables', 'A subset of variables'))

    if option1 == 'All Variables':
        df = df

    elif option1 == 'A subset of variables':
        var_list = list(df.columns)
        option3 = st.sidebar.multiselect(
            'Select variable(s) you want to include in the report.',
            var_list)
        df = df[option3]

    option2 = st.sidebar.selectbox(
        'Choose Minimal Mode or Complete Mode',
        ('Minimal Mode', 'Complete Mode'))

    if option2 == 'Complete Mode':
        mode = 'complete'
        st.sidebar.warning('The default minimal mode disables expensive computations such as correlations and duplicate row detection. Switching to complete mode may cause the app to run overtime or fail for large datasets due to computational limit.')
    elif option2 == 'Minimal Mode':
        mode = 'minimal'
        grid_response = AgGrid(
            df,
            editable=True,
            height=300,
            width='100%',
        )

    updated = grid_response['data']
    df1 = pd.DataFrame(updated)
if st.button('Generate Report'):
    if mode == 'complete':
        profile = ProfileReport(df,
                                title="User uploaded table",
                                progress_bar=True,
                                dataset={
                                    "description": 'This profiling report was generated by Insights Bees',
                                    "copyright_holder": 'Insights Bees',
                                    "copyright_year": '2022'
                                })
        st_profile_report(profile)
    elif mode == 'minimal':
        profile = ProfileReport(df1,
                                minimal=True,
                                title="User uploaded table",
                                progress_bar=True,
                                dataset={
                                    "description": 'This profiling report was generated by Insights Bees',
                                    "copyright_holder": 'Insights Bees',
                                    "copyright_year": '2022'
                                })
        st_profile_report(profile)
