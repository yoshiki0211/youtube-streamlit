import streamlit as st
import time
from PIL import Image

st.title('Streamlit 超入門')
st.header('this is a header')
st.write('プログレスバーの表示')
    
'Start!!'

latest_iteration= st.empty()
bar = st.progress(0)

for i in range(10):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!'

img=Image.open('LINE_ALBUM_結婚式写真候補_220206_27.jpg')
st.image(img, caption='maichan', use_column_width=True)

left_column,right_column = st.columns(2)



expander=left_column.expander('名前')
expander.write('まいちゃん')
expander=left_column.expander('おしり')
expander.write('ぷりぷり')
expander=left_column.expander('サメきち')
expander.write('かわいいね')

button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# text=st.text_input('あなたの趣味を教えてください。')
# condition=st.slider('あなたの今の調子は？',0,10,5)

# 'あなたの趣味：', text,
# 'コンディション：', condition,