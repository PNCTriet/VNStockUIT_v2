import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import main
import time

authentication = False
edirect = 2
# Cài đặt Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("vnstockuit-9d3a2d1b7569.json")
    default_app = firebase_admin.initialize_app(cred)

if 'sbstate' not in st.session_state:
    st.session_state.sbstate = 'collapsed'

def Page01_Signup():
    st.set_page_config(page_title='page1', page_icon='📋', layout='wide', initial_sidebar_state=st.session_state.sbstate)
    st.sidebar.write("I am in the sidebar pg01")
    
    st.title("#Signup")
    email = st.text_input("Email:")
    password = st.text_input("Mật khẩu:", type="password")
        
    if st.button("Signup"):
        try:
            user = auth.create_user(email=email, password=password)
            st.success(f"Đăng ký thành công! ID người dùng mới: {user.email}")
            st.markdown('pls login using your email and password')
            st.balloons()
        except:
            st.error(f"Faild to signup")
    if st.button("Back to login"):    
        st.session_state.runpage = Page02_Login
        st.experimental_rerun()
    



def Page02_Login():
    global redirect
    st.set_page_config(page_title='page2', page_icon='📋', layout='wide', initial_sidebar_state=st.session_state.sbstate)
    st.sidebar.write("I am in the sidebar pg02")
    
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
                    st.error("Mật khẩu/tài khoản không chính xác.")   
                    authentication = False    
            else:
                st.warning("Vui lòng nhập đầy đủ thông tin đăng nhập.")
            if authentication:
                getin()
        if st.button("Signup"):
            st.session_state.runpage = Page01_Signup
            st.experimental_rerun()
            
def getin():
    with st.spinner('Wait for it...'):
        time.sleep(2)
    st.success('Done!')
    st.session_state.runpage = Page03_Main
    st.experimental_rerun()
    
def getout():
    st.session_state.runpage = Page02_Login
    st.experimental_rerun()
        

def Page03_Main():
    st.set_page_config(page_title='page3', page_icon='📋', layout='wide', initial_sidebar_state=st.session_state.sbstate)
    st.sidebar.text("Main page here")
    if st.sidebar.button("Sign out"):
        getout()
    st.title("#Main")
    main.page_main()
        

def Page_Main():
    st.set_page_config(layout='wide', initial_sidebar_state=st.session_state.sbstate)
    st.subheader('Main Page')
    
    if st.button("Login"):
        st.session_state.runpage = Page02_Login
        st.experimental_rerun()
        
    if st.button("Signup"):
        st.session_state.runpage = Page01_Signup
        st.experimental_rerun()
        
    if st.button("Main"):
        st.session_state.runpage = Page03_Main
        st.experimental_rerun()
        

if 'runpage' not in st.session_state:
    st.session_state.runpage = Page02_Login
st.session_state.runpage()