import streamlit as st
from Bank import Bank

bank = Bank()
st.set_page_config(page_title="Bank Management System", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.radio("Select Action", [
    "Create Account", "Deposit", "Withdraw", "View Details", "Update Details", "Delete Account"
])

if menu == "Create Account":
    st.header("Create a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("E-mail")
    pin = st.number_input("PIN (min 4 digits)", min_value=0, step=1)

    if st.button("Create Account"):
        success, result = bank.create_account(name, age, email, pin)
        if success:
            st.success("Account created successfully!")
            st.json(result)
        else:
            st.error(result)

elif menu == "Deposit":
    st.header("Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=0, step=1)
    amount = st.number_input("Amount", min_value=0, step=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc_no, pin, amount)
        st.success(msg) if success else st.error(msg)

elif menu == "Withdraw":
    st.header("Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=0, step=1)
    amount = st.number_input("Amount", min_value=0, step=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc_no, pin, amount)
        st.success(msg) if success else st.error(msg)

elif menu == "View Details":
    st.header("Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=0, step=1)

    if st.button("Get Details"):
        success, result = bank.get_details(acc_no, pin)
        st.json(result) if success else st.error(result)

elif menu == "Update Details":
    st.header("Update Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=0, step=1)
    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.number_input("New PIN (optional)", min_value=0, step=1)

    if st.button("Update"):
        success, msg = bank.update_details(acc_no, pin, new_name or None, new_email or None, new_pin or None)
        st.success(msg) if success else st.error(msg)

elif menu == "Delete Account":
    st.header("Delete Account")
    acc_no = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=0, step=1)

    if st.button("Delete"):
        success, msg = bank.delete_account(acc_no, pin)
        st.success(msg) if success else st.error(msg)
