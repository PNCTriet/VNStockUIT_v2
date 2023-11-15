import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import main

authentication = False
# Cài đặt Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("vnstockuit-9d3a2d1b7569.json")
    default_app = firebase_admin.initialize_app(cred)
   
# Bắt đầu Streamlit app
def main_acc():
    st.title("VNSTOCK")
    login()

def login():
    authentication = False
    
    st.title("#Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Signin"):
            if email and password:
                try:
                    user = auth.get_user_by_email(email)
                    st.success(f"Xin chào {user.email}!")
                    st.balloons()
                    authentication = True
                except:
                    st.error("Mật khẩu không chính xác.")   
                    authentication = False    
            else:
                st.warning("Vui lòng nhập đầy đủ thông tin đăng nhập.")
            if authentication : 
                main.page_main()
        else:
            if st.button("Signup"):
                signup()
                
        
def signup():
    
    st.title("#Signup")
    email = st.text_input("Email:")
    password = st.text_input("Mật khẩu:", type="password")
        
    if st.button("Đăng ký"):
        try:
            user = auth.create_user(email=email, password=password)
            st.success(f"Đăng ký thành công! ID người dùng mới: {user.email}")
            st.markdown('pls login using your email and password')
            st.balloons()
        except:
            st.error(f"Faild to signup")
  

if __name__ == "__main__":
    # The main app
    main_acc()
   
    
   