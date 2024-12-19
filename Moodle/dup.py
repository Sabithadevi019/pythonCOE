sample_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_values = set()
result_list = []
for item in sample_list:
    if item not in unique_values:
        unique_values.add(item)
        result_list.append(item)
print(result_list)
