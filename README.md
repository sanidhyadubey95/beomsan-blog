# My Streamlit Blog

A public knowledge-sharing blog built with Streamlit. Write posts in Markdown, embed images and charts, and share code snippets with syntax highlighting. Fully public, no authentication required.

## 🚀 Features
- Write blog posts in Markdown
- Embed images and charts
- Syntax-highlighted code snippets
- Responsive sidebar navigation
- No authentication, fully public
- Ready for Streamlit Cloud deployment

## 📂 Project Structure
```
my-streamlit-blog/
├── app.py                 # Main Streamlit application
├── posts/                 # Blog post markdown files
│   ├── welcome.md        # Sample welcome post
│   └── sample-post.md    # Sample technical post with code/charts
├── images/               # Image assets for blog posts
│   └── sample-chart.png  # Sample chart image
├── data/                 # Optional CSV/data files for dynamic charts
│   └── sample-data.csv   # Sample dataset
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .streamlit/          # Streamlit configuration
    └── config.toml      # App configuration
```

## 🛠 Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd my-streamlit-blog
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```
4. **Add your posts:**
   - Write Markdown files in the `posts/` directory.
   - Add images to the `images/` folder.
   - Add data files to the `data/` folder if needed.

## 🌐 Deployment (Streamlit Cloud)
1. Push your repository to GitHub.
2. Connect your repo to [Streamlit Cloud](https://streamlit.io/cloud).
3. Set the main file to `app.py`.
4. Deploy and share your public blog!

## 📄 Post Format
Each post should start with YAML front matter:
```markdown
---
title: "Post Title"
date: "2024-01-01"
tags: ["python", "data-science"]
---

# Your content here
```

## 📋 Features Demonstrated
- Markdown formatting
- Image embedding
- Code snippets
- Data visualizations

## 🎨 Styling
- Clean, modern, responsive design
- Mobile-friendly navigation

## 🤝 Contributing
Pull requests welcome! For major changes, open an issue first.

## 📧 License
MIT 