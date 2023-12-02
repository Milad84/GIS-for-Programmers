import plotly.express as px
fig = px.scatter_geo(dframe,lat='Lat',lon='Long', hover_name="SITE_NAME")
fig.update_layout(title = 'Texas Air Quality Stations', title_x=0.5)
fig.show()

  
