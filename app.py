import streamlit as st
import tensorflow as tf

from object_detection.utils import label_map_util

def main() :
    
    st.sidebar.header('Menu')
    menu = ['Home', 'Data']

    choice = st.sidebar.selectbox('메뉴를 선택하세요 : ', menu)

    if choice == 'Home' :
        st.title('Object Detection')
        st.subheader('파일 업로드하면 오브젝트 디텍션 결과가 나옵니다.')
        st.header(' ')

        uploaded_file = st.file_uploader("파일을 선택하세요.")
        if uploaded_file is not None:
            pass



    elif choice == 'Data' :
        pass

if __name__ == '__main__' :
    main()
