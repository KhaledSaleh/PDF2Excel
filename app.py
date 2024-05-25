import streamlit as st
import pdfplumber
import pandas as pd




def main():
    """Streamlit app testing camelot.py"""

    st.write("# PDF2Excel Parser!")

    uploaded_file = st.file_uploader(label="Upload PDF with tables", type="pdf")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as file:

            all_pages = file.pages
            tbl = all_pages[0].extract_table()
            original_df = pd.DataFrame(tbl)
            st.dataframe(original_df)  # Same as st.write(df)

    else:
        st.write("Upload a PDF file with some tables in it.")


if __name__ == "__main__":
    main()
