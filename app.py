import streamlit as st
import pdfplumber
import pandas as pd




def main():
    """Streamlit app testing camelot.py"""

    st.write("# PDF2Excel Parser!")

    st.sidebar.title("PDF2Excel 🧾")
    st.sidebar.caption("Parse your PDF tables and convert it to excel/csv file.")
    st.sidebar.markdown("Made by [Khaled Saleh](https://www.linkedin.com/in/khaled-saleh-5881a924)")

    st.sidebar.markdown("---")
    st.sidebar.header("Settings")

    all_pages = []
    
    uploaded_file = st.file_uploader(label="Upload PDF with tables", type="pdf")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as file:
            all_pages = file.pages
    else:
        st.write("Upload a PDF file with some tables in it.")
    
    total_pages = len(all_pages)
    page_num = st.sidebar.selectbox("PDF Table Page", [i+1 for i in range(total_pages)], help="Specify the number of the PDF page that contains the table you would like to display/export.")
    click = st.button("Display/Download Table", disabled=False)

    if click:
        tbl = all_pages[page_num-1].extract_table()
        original_df = pd.DataFrame(tbl)
        st.dataframe(original_df)



if __name__ == "__main__":
    main()
