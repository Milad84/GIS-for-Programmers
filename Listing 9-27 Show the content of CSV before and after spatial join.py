points_before_join_df = pd.read_csv('points_before_join.csv')

print("Data before Spatial Join:")
print(points_before_join_df)

joined_data_df = pd.read_csv('joined_data.csv')

print("\nData after Spatial Join:")
print(joined_data_df)
