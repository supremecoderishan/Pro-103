import pandas as pd
import ploty.express as px
df = pd.read_csv("Covid.csv")

fig = px.line(df, x = "date", y = "cases", color = "country")
fig.show()
