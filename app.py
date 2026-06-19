import streamlit as st
import time
from datetime import datetime

st.set_page_config(
    page_title="Chat Bot",
    page_icon="🤖",
    layout="centered"
)

knowledge_base = {
    "python": "Python is a popular programming language used for web development, AI, data science, and automation.",

    "java": "Java is an object-oriented programming language commonly used for enterprise applications.",

    "artificial intelligence": "Artificial Intelligence (AI) enables machines to perform tasks that normally require human intelligence.",

    "machine learning": "Machine Learning is a subset of AI that allows computers to learn from data and improve over time.",

    "streamlit": "Streamlit is a Python framework used to build interactive web applications quickly and easily.",

    "chatbot": "A chatbot is a software application designed to simulate conversations with users."
}

with st.sidebar:

    st.title("🤖 Chat Bot")

    st.markdown("---")

    st.subheader("About")

    st.write(
        """
        A simple knowledge-based chatbot built using
        Python and Streamlit.
        """
    )

    st.markdown("---")

    st.subheader("Try Asking")

    st.write("""
    • What is Python?

    • What is Java?

    • What is Artificial Intelligence?

    • What is Machine Learning?

    • What is Streamlit?

    • What is a Chatbot?
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "Hello! I'm Chat Bot 🤖. Ask me a question."
            }
        ]

        st.rerun()

st.title("🤖 Chat Bot")

st.caption(
    "A Simple Knowledge-Based Chatbot Built with Streamlit"
)

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Hello! I'm Chat Bot 🤖.\n\n"
            "I can answer questions about:\n"
            "- Python\n"
            "- Java\n"
            "- Artificial Intelligence\n"
            "- Machine Learning\n"
            "- Streamlit\n"
            "- Chatbots"
        }
    ]


for message in st.session_state.messages:

    avatar = "🤖" if message["role"] == "assistant" else "👤"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):
        st.write(message["content"])


user_input = st.chat_input(
    "Type your message..."
)


if user_input:

    
    with st.chat_message(
        "user",
        avatar="👤"
    ):
        st.write(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    text = user_input.lower()

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        with st.spinner("Thinking..."):
            time.sleep(1)

        response = None

        for keyword, answer in knowledge_base.items():

            if keyword in text:

                response = answer
                break

        if response is None:

            if "hello" in text or "hi" in text:

                response = (
                    "Hello! Nice to meet you 👋"
                )

            elif "name" in text:

                response = (
                    "My name is Chat Bot 🤖"
                )

            elif "how are you" in text:

                response = (
                    "I'm doing great! 😊"
                )

            elif "time" in text:

                response = (
                    f"Current time is "
                    f"{datetime.now().strftime('%I:%M %p')}"
                )

            elif "bye" in text:

                response = (
                    "Goodbye! Have a great day 👋"
                )

            else:

                response = (
                    "Sorry, I don't know that topic yet.\n\n"
                    "Try asking about:\n"
                    "- Python\n"
                    "- Java\n"
                    "- Artificial Intelligence\n"
                    "- Machine Learning\n"
                    "- Streamlit\n"
                    "- Chatbots"
                )
        st.write(response)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

st.markdown("---")
st.caption(
    "Built with ❤️ using Python and Streamlit"
)