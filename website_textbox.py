# save as esp32_sender.py

import streamlit as st
import socket

ESP32_IP = "192.20.10.2"  # Replace with your ESP32's IP
ESP32_PORT = 1234
SECRET_PASSWORD = "letmein"  # Change this for better security

st.title("ESP32 Text Sender")

password = st.text_input("Enter password", type="password")
message = st.text_input("Message to ESP32")

if st.button("Send"):
    if password == SECRET_PASSWORD:
        try:
            # Create socket and send message
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ESP32_IP, ESP32_PORT))
                s.sendall(message.encode())
                st.success("Message sent successfully!")
        except Exception as e:
            st.error(f"Failed to send message: {e}")
    else:
        st.warning("Incorrect password!")
