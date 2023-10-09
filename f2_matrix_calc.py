import streamlit as st
import numpy as np
import pandas as pd

from matrix import F2Matrix

# タイトルと説明を表示
st.title('F2空間での行列の積計算')

# 行列のサイズを入力
st.sidebar.title('行列の計上 (m×n)(n×l)')
m = st.sidebar.slider('行列の行数 (m):', 0, 10, 3)
n = st.sidebar.slider('行列の列数 (n):', 0, 10, 3)
l = st.sidebar.slider('行列の行数 (l):', 0, 10, 3)

matrix1_input, matrix1_display = st.columns(2)
with matrix1_input:
    left_matrix = F2Matrix(st.data_editor(pd.DataFrame(np.zeros((m, n)).astype(bool), columns=[str(i) for i in range(n)]),
                        key="matrix1"))
with matrix1_display:
    st.write(left_matrix.content.astype(int))

matrix2_input, matrix2_display = st.columns(2)
with matrix2_input:
    right_matrix = F2Matrix(st.data_editor(pd.DataFrame(np.zeros((n, l)).astype(bool), columns=[str(i) for i in range(l)]),
                        key="matrix2"))
with matrix2_display:
    st.write(right_matrix.content.astype(int))

if st.button('計算する'):
    st.write(left_matrix*right_matrix)
