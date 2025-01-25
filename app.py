import streamlit as st
import openai

# 设置 API 密钥
openai.api_key = "your_openai_api_key"

# Streamlit 应用界面
st.title("AI 文案生成器")
st.subheader("为你的创意快速生成文案")

# 用户输入需求
user_input = st.text_input("请输入你的文案需求：", "为环保水瓶写一段吸引人的广告文案")

# 用户选择文案风格
style = st.selectbox("选择文案风格：", ["正式", "幽默", "简洁"])

# 文案生成函数
def generate_copy(prompt, style):
    style_prompts = {
        "正式": "写一个正式的广告文案：",
        "幽默": "写一个幽默的广告文案：",
        "简洁": "写一个简洁的广告文案："
    }

    full_prompt = style_prompts.get(style, "") + prompt

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=full_prompt,
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()

    except Exception as e:
        st.error(f"发生错误：{str(e)}")
        return ""
        
# 用户点击生成按钮
if st.button("生成文案"):
    if user_input:
        result = generate_copy(user_input, style)
        st.write("生成的文案：")
        st.write(result)
    else:
        st.write("请先输入文案需求！")
