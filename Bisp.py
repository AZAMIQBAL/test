# import streamlit as st
# import matplotlib.pyplot as plt
# import datetime as dt
# import pandas as pd
# import numpy as np
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report
# uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
# data = pd.read_csv(uploaded_data)
# # create the pandas profiling report
# pr = data.profile_report()
# st_profile_report(pr)
# # optional, save to file
# pr.to_file('pandas_prof.html')


import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv(
    "https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)


# def load_data():
#     # df=load_data.clear()
#     # loading online csv
#     data = "https://kobo.humanitarianresponse.info/api/v2/assets/a5n7ThvXYrgR4QsQQmAJPN/export-settings/esLUM5TFwKdqbzRnsZLf2Qj/data.csv"  # ,";")
#     # s = requests.get(url).content
#     data = pd.read_csv(data, on_bad_lines='skip', sep=";")
#     df = pd.DataFrame(data)

#     return df


# if st.button("Click Me To Get Refresh Data"):
#     # Clears all singleton caches:
#     #     st.experimental_singleton.clear()
#     load_data.clear()
# df = load_data()

# pr = df.profile_report()
# st_profile_report(pr)
# # df.head()
# # profile = ProfileReport(df, title="Pandas Profiling Report")
# # profile.to_file("Anylsis")
