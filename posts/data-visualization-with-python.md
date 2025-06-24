---
title: "📝Data Visualization with Python"
date: "2025-06-20"
tags: ["python", "visualization", "matplotlib"]
---

In this post, we'll plot a simple chart using `matplotlib` and display a code snippet.

## 1. Example Chart

Below is a sample chart generated from a CSV file:

![Sample Chart|width=200](images/sample-post/sample-chart.png)

## 2. Code Example

```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/sample-data.csv')
plt.plot(data['x'], data['y'])
plt.title('Sample Data Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

## 3. Charts

You can also embed charts directly in your posts using Streamlit!

~~~python
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/sample-data.csv')
plt.plot(data['x'], data['y'])
plt.title('Sample Data Plot')
plt.xlabel('X')
plt.ylabel('Y')
st.pyplot(plt)

st.subheader("Plotly Chart Example")
fig2 = px.line(data, x="x", y="y", title="Sample Data Plot (Plotly)")
st.plotly_chart(fig2)
~~~