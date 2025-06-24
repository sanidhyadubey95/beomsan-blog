import os
import glob
import yaml
import re
import base64
from datetime import datetime
import mistune

# ---------------- Utilities ---------------- #
def get_base64_img(path):
    with open(path, "rb") as f:
        return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}"

def inject_css(image_path, css_path="custom.css"):
    import streamlit as st
    encoded_img = get_base64_img(image_path)
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read().replace("{{SIDEBAR_BG}}", encoded_img)
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def icon_text(svg_path, text, size=20, sidebar=False):
    import streamlit as st
    with open(svg_path, "r", encoding="utf-8") as f:
        svg = f.read()
    html_content = f"""
    <div style="display: flex; align-items: center; gap: 0.5rem;">
        <div style="width: {size}px; height: {size}px;">{svg}</div>
        <div style="font-size: 1.2rem; font-weight: bold;">{text}</div>
    </div>
    """
    (st.sidebar if sidebar else st).markdown(html_content, unsafe_allow_html=True)

# ---------------- Post Loading ---------------- #
def load_posts(posts_dir="posts"):
    posts = []
    for md_file in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        meta, body = parse_front_matter(content)
        meta["filename"] = os.path.basename(md_file)
        meta["body"] = body
        # Get file modification time for secondary sorting
        meta["mtime"] = os.path.getmtime(md_file)
        posts.append(meta)
    
    # Convert date strings to datetime objects for proper sorting
    for post in posts:
        date_str = post.get("date", "")
        try:
            # Try to parse the date string
            post["date_obj"] = datetime.strptime(date_str, "%Y-%m-%d")
        except (ValueError, TypeError):
            # If date parsing fails, use a very old date
            post["date_obj"] = datetime(1900, 1, 1)
    
    # Sort by date (newest first), then by modification time (most recent first)
    return sorted(posts, key=lambda x: (x.get("date_obj"), x.get("mtime", 0)), reverse=True)

def parse_front_matter(md_text):
    match = re.match(r"---\n(.*?)---\n(.*)", md_text, re.DOTALL)
    if match:
        meta = yaml.safe_load(match.group(1))
        body = match.group(2)
    else:
        meta, body = {}, md_text
    if "date" in meta and not isinstance(meta["date"], str):
        meta["date"] = str(meta["date"])
    return meta, body

def render_markdown(md, images_dir="images"):
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import plotly.express as px
    import io
    import contextlib
    import mistune
    import re
    import os

    markdown = mistune.create_markdown(plugins=[
        'strikethrough', 'table', 'task_lists', 'footnotes', 'url'
    ])

    # Regex patterns for features
    patterns = {
        'exec': r"~~~python\n([\s\S]*?)~~~",
        'image': r'!\[([^\]]*)\]\(([^)]+)\)',
        'math_block': r"\$\$([\s\S]+?)\$\$",
    }
    combined = f"({patterns['exec']})|({patterns['image']})|({patterns['math_block']})"
    pos = 0

    for match in re.finditer(combined, md):
        start, end = match.start(), match.end()

        # Render markdown between blocks
        if pos < start:
            chunk = md[pos:start]

            # Convert inline math $...$ to Streamlit-renderable format
            def replace_inline_math(text):
                return re.sub(r"\$(.+?)\$", lambda m: f"`$${m.group(1)}$$`", text)

            processed = replace_inline_math(chunk)
            html = markdown(processed)
            st.markdown(html, unsafe_allow_html=True)

        if match.group(2):  # Executable Python block
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(match.group(2), {"st": st, "plt": plt, "pd": pd, "px": px})
            except Exception as e:
                st.error(f"Error: {e}")

        elif match.group(5):  # Image
            alt_text, img_path = match.group(4), match.group(5)
            width = None
            if "|" in alt_text:
                parts = alt_text.split("|")
                alt_text = parts[0].strip()
                for part in parts[1:]:
                    if part.strip().startswith("width="):
                        try:
                            width = int(part.strip().split("=")[1])
                        except:
                            pass
            while img_path.startswith(("../", "./")):
                img_path = img_path[img_path.find("/") + 1:]
            if not os.path.isabs(img_path) and not img_path.startswith(images_dir + "/"):
                img_path = os.path.join(images_dir, img_path)
            if os.path.exists(img_path):
                st.image(img_path, caption=alt_text, width=width)
            else:
                st.warning(f"Image not found: {img_path}")

        elif match.group(7):  # Display math block
            st.latex(match.group(7).strip())

        pos = end

    # Final tail render
    if pos < len(md):
        chunk = md[pos:]

        def replace_inline_math(text):
            return re.sub(r"\$(.+?)\$", lambda m: f"`$${m.group(1)}$$`", text)

        processed = replace_inline_math(chunk)
        html = markdown(processed)
        st.markdown(html, unsafe_allow_html=True)
