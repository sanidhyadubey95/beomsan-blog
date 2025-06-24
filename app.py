import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import json
from streamlit.components.v1 import html
import utils

# ---------------- Main App ---------------- #
st.set_page_config(page_title="Beomsan's Blog", page_icon="📝", layout="wide")
utils.inject_css("images/bg.jpg")

# Load posts and setup navigation
posts = utils.load_posts()
utils.icon_text("images/whale.svg", "Sanidhya Dubey", size=28, sidebar=True)

# Tag filtering
all_tags = sorted({tag for post in posts for tag in post.get("tags", [])})
selected_tag = st.sidebar.selectbox("", all_tags, index=None, placeholder="Filter by tag")

# Navigation state
if "current_page" not in st.session_state:
    qp = st.query_params
    if "current_page" in qp:
        st.session_state.current_page = qp["current_page"]
    else:
        st.session_state.current_page = "Home"

def set_page(page):
    st.session_state.current_page = page
    st.query_params["current_page"] = page

# Sidebar navigation
if st.session_state.current_page == "About":
    st.sidebar.markdown('<div class="active-btn"><button disabled>About</button></div>', unsafe_allow_html=True)
else:
    if st.sidebar.button("About", key="btn_about"):
        set_page("About")
        st.rerun()

if st.session_state.current_page == "Home":
    st.sidebar.markdown('<div class="active-btn"><button disabled>Home</button></div>', unsafe_allow_html=True)
else:
    if st.sidebar.button("Home", key="btn_home"):
        set_page("Home")
        st.rerun()

for post in posts:
    if post["title"] != "About This Blog":  # Exclude About post from button list
        post_key = f"[{post['title']}]"
        if st.session_state.current_page == post_key:
            st.sidebar.markdown(
                f'<div class="active-btn"><button disabled>{post["title"]}</button></div>',
                unsafe_allow_html=True
            )
        else:
            if st.sidebar.button(post["title"], key=f"btn_{post['filename']}"):
                set_page(post_key)
                st.rerun()

# Main content area
choice = st.session_state.current_page

if choice == "About":
    about_post = next((p for p in posts if p["title"] == "About This Blog"), None)
    if about_post:
        st.title(about_post["title"])
        utils.render_markdown(about_post["body"])

elif choice == "Home":
    # Welcome header with animation
    html(f"""
    <div style="display: flex; align-items: center; gap: 85px;">
        <div style="width: 20px;">
            <lottie-player src="https://lottie.host/98719d10-84d0-4ecf-b0ec-2faecb3bca9f/sMMjoYjB3t.json" 
                          background="transparent" speed="1" style="width: 150px; height: 150px;" loop autoplay>
            </lottie-player>
        </div>
        <h1 style="margin: 0; font-size: 2.4rem;">Welcome to Beomsan's Blog!</h1>
    </div>
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=120)

    st.write("Browse the latest posts below:")
    st.markdown('---')

    # Display filtered posts
    filtered_posts = [post for post in posts if selected_tag is None or selected_tag in post.get("tags", [])]
    # Exclude About post from home page display
    filtered_posts = [post for post in filtered_posts if post["title"] != "About This Blog"]

    for post in filtered_posts:
        st.subheader(post["title"])
        st.caption(f"{post.get('date', '')} | Tags: {', '.join(post.get('tags', []))}")
        excerpt = post["body"].strip().split("\n\n")[0][:200]
        st.write(excerpt + ("..." if len(post["body"]) > 200 else ""))

        # Read more button → set current_page and rerun
        if st.button(f"Read more", key=post["filename"]):
            set_page(f"[{post['title']}]")
            st.rerun()

        st.markdown('---')

elif choice.startswith("[") and choice.endswith("]"):
    # Display individual post
    selected_title = choice.strip("[]")
    post = next((p for p in posts if p["title"] == selected_title), None)
    if post:
        st.title(post["title"])
        st.caption(f"{post.get('date', '')} | Tags: {', '.join(post.get('tags', []))}")
        utils.render_markdown(post["body"])
        st.markdown("---")
