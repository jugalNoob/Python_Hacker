tab1, tab2 = st.tabs(['one' , 'two'])

with tab1:
    # if st.button("Check CSV"):
        df = pd.read_csv("earth.csv")
        st.write(df)

with tab2:
    st.write("This is tab 1")
    st.write("This is tab 2")



    
# Read the CSV file /// import row class In
# df = pd.read_csv("earth.csv")

# # Display the DataFrame
# st.write(df)


# row_number = st.text_input("Enter the row number", value="0")
# row_number = int(row_number)
# if row_number >= 0 and row_number < len(df):
#     selected_row = df.iloc[row_number]
#     st.write(selected_row)
# else:
#     st.write("Please enter a valid row number")




# num_rows_input = st.text_input('Enter the number of rows to display', value='40')
# num_rows = int(num_rows_input)
# one = df.head(num_rows)
# st.write(one)