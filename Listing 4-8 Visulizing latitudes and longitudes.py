import plotly.express as px
fig = px.scatter_geo(lat=[ 40.63,  40.53,  40.86], lon=[22.95, 22.81, 23.51])
fig.update_layout(title = 'Random points', title_x=0.5)
fig.show()
