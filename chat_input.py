import streamlit as st

# Create a storage for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display previous chat history 
# st.write(st.session_state.messages)
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])


prompt = st.chat_input("type here")
if prompt:
    # Add the user prompt to the chat history 
    st.session_state.messages.append({'role':'user','content':prompt})
    # Display the message 
    with st.chat_message('user'):
        st.write(prompt)

    # # for customizing the user 
    # with st.chat_message('bot', avatar='HER.png'):
    #     st.write(prompt)