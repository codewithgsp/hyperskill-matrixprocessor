import itertools

# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
#
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
#
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]

for combi1, comb2, combi3 in itertools.product(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)):
    if combi1[1] + comb2[1] +combi3[1] <= 30:
        print(combi1[0], comb2[0], combi3[0], str(combi1[1] + comb2[1] +combi3[1]))
# for c_main, p_main in zip(main_courses, price_main_courses):
#     for c_dessert, p_dessert in zip(desserts, price_desserts):
#         for c_drink, p_drink in zip(drinks, price_drinks):
#             total_price = p_main + p_dessert + p_drink
#             if total_price <= 30:
#                 unique_combi.add((c_main, c_dessert, c_drink, str(total_price)))
# for combi in unique_combi:
#     print(" ".join(combi))