#git init
#git remote add origin https://github.com/gabrielyuske/streamlit.git
#git add .
#git commit -m"1st commit"
#git push origin master
#
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import time

#titulo
st.title("Streamlit")

st.write("Dataframe")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40],
})

st.write(df)

#　serve pra qunado vc quiser selecionar o tamanho
st.dataframe(df,width=100,height=100)

#axis= 0 列,　1=行
st.dataframe(df.style.highlight_max(axis=0))

# serve pra quando quiser mostrar somente uma tabela
st.table(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ["a","b","c"]
)

#grafico de linha
st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

df= pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=["lat","lon"]
)

st.map(df)

st.write("Display Image")

#True or False
if st.checkbox("Show image"):

    img = Image.open("py2.png")
    # use_column_width serve pa ajustar de acordo com o tamnho da tela
    st.image(img , caption="Python is BEST" ,use_column_width=True)

option = st.selectbox(
    "あなたの好きな数字",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です"

# st.write("テキストビュー")
# text = st.text_input("あなたの趣味は?")
# "あなたの趣味は",text,"です"
#
# condition = st.slider("あなたの調子は?",0,100,50)
# "調子",condition

st.sidebar.write("Interactive Widgets")
text2 = st.sidebar.text_input("あなたの趣味は?")
condition2 = st.sidebar.slider("あなたの調子は?",0,100,50)

"調子",condition2
"あなたの趣味は",text2,"です"

# aparece algo quando apertar o botao
left_column,right_column = st.beta_columns(2)
button = left_column.button("右に表示")
if button:
    right_column.write("右カラム")

st.write("プログレスバー")
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(99):
    latest_iteration.text(f"Iteration {i+2}")#mudando o numero do texto
    bar.progress(i+1)#adcionando 1 no bar
    time.sleep(0.1)
"Done!!!!"

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く２")

expander2 = st.beta_expander("問い合わせ")
expander2.write("問い合わせ内容を書く")
# aparece algo quando apertar o botao
left_column2,right_column2 = st.beta_columns(2)
button2 = left_column2.button("右に表示２")
if button2:
    right_column2.write("右カラム")
