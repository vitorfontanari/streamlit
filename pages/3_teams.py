import streamlit as st

st.set_page_config(
    page_title="Players",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")
st.divider()

colums = ["Photo", "Age" , "Flag", 
          "Nationality", "Overall", "Potential", 
          "Position", "Value(£)","Preferred Foot",
          "Weak Foot", "Skill Moves","Work Rate"]

st.dataframe(df_filtered[colums],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", min_value=0, max_value=100
                 ),
                 "Value(£)": st.column_config.ProgressColumn(
                     "Value(£)", format="£%f", min_value=0, max_value=df_filtered["Value(£)"].max()
                     ),
                        "Photo": st.column_config.ImageColumn(),
                        "Flag": st.column_config.ImageColumn(),
             }) 