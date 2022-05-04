import streamlit as st
import time

st.title('Streamlit 超入門')
st.header('this is a header')
st.write('プログレスバーの表示')

'Start!!'

latest_iteration= st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!'

left_column,right_column = st.columns(2)

button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander=left_column.expander('問い合わせ１')
expander.write('問い合わせ１の回答')
expander=left_column.expander('問い合わせ２')
expander.write('問い合わせ２の回答')
expander=left_column.expander('問い合わせ３')
expander.write('問い合わせ３の回答')
# if st.checkbox('Show Image'):
#     img=Image.open('LINE_ALBUM_結婚式写真候補_220206_27.jpg')
#     st.image(img, caption='maichan', use_column_width=True)

# text=st.text_input('あなたの趣味を教えてください。')
# condition=st.slider('あなたの今の調子は？',0,10,5)

# 'あなたの趣味：', text,
# 'コンディション：', condition,