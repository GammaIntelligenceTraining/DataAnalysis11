# # empty = dict()
# # print(type(empty))
# # print(bool(empty))
# #
# # person = {
# #     'first_name': 'Jack',
# #     'last_name': 'Smith',
# #     'age': 20,
# #     'nickname': 'Jack',
# # }
# #
# # person['first_name'] = 'Bob'
# # person['phone'] = '555-555-5555'
# # print(person)
# #
# # # print(person['email'])
# # print(person.get('email', 'nothing found'))
# #
# # del person['nickname']
# # print(person)
# #
# # deleted = person.pop('last_name')
# # print(deleted)
# # person.update(email='jack@example.com', nickname='terminator')
# # person.update({'height': 178, 'weight': 85})
# # print(person)
# #
# # for x in person:
# #     print(person[x])
# #
# # print(person.keys())
# # print(person.values())
# # print(person.items())
# #
# # for key, val in person.items():
# #     print(key, val)
# #
# # x = [1, 2, 3, 4, 5, 6, 7]
# # y = {}
# #
# # for num in x:
# #     y[num] = num ** 2
# #
# # print(y)
# #
#
# my_car = {
#     'make': 'Honda',
#     'model': 'Civic',
#     'info': {
#         'mileage': 10000,
#         'color': 'red'
#     },
#     'owners': [
#         {
#             'name': 'Jack',
#             'surname': 'Smith'
#         },
#         {
#             'name': 'Sarah',
#             'surname': 'Gold'
#         }
#     ]
# }
#
# print(my_car['info']['mileage'])
# print(my_car['owners'][1]['surname'])

# def sort_lst(x):
#     return x[1]
#
#
# lst = [[1, 3], [5, 2], [6, 1], [2, 7], [4, 11]]
# lst.sort(key=lambda x: x[1])
# print(lst)

# x = lambda name: print(f'Hello {name}!')
# x('Jack')
#
# def say_hello(name):
#     print(f'Hello {name}!')


# a = [1, 2, 3, 4, 5]
# b = ['a', 'b', 'c', 'd']
# res = list(zip(a, b, a, a, a, a, range(100, 1000, 100)))
# print(res)
#
# print(list(enumerate(b, 10000)))

# def filter_evens(num):
#     return num % 2 == 0
#
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # evens = filter(lambda num: num % 2 == 0, x)
# evens = filter(filter_evens, x)
#
# print(list(evens))

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = map(lambda num: num ** 2, x)
#
# print(list(squares))
# info = map(lambda num: {
#     'number': num,
#     'oddOrEven': 'even' if num % 2 == 0 else 'odd'
# }, x)
# print(list(info))
#
#
# def remap(num):
#     result = {}
#     result['number'] = num
#     if num % 2 == 0:
#         result['oddOrEven'] = 'even'
#     else:
#         result['oddOrEven'] = 'odd'
#     return result
# print(remap(10))

numbers = [1, 2, 3, 4, 5, 6]
squares = [num ** 2 for num in numbers]
print(squares)
evens = [num for num in numbers if num % 2 == 0]
print(evens)
labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(labels)

# for num1 in range(10):
#     for num2 in range(10):
#         for num3 in range(10):
#             print(num1, num2, num3)

pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)