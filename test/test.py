# dict1={'first_name':'ALi',
#        'last_name':'M',
#        'age':'220',
#        'city':'Florida'}
# print(dict1)
# print(dict1.get('first_name','NONE').upper())
# print(dict1.get('last_name','NONE').upper())
# print(dict1['age'])
# print(f"name:{dict1['first_name'],dict1['last_name']},age:{dict1['age']},city:{dict1['city']}")


# dict_numbers={'A':'2',
#               'B':'3',
#               'C':'4',
#               'D':'5',
#               'E':'6',}
# for key,value in dict_numbers.items():
#     print(key,value)
# for key in dict_numbers.keys():
#     print(key)
# for value in dict_numbers.values():
#     print(value)

# rivers={'nile':'egypt',
#         'changjiang':'china',
#         'huanghe':'china',}
# for river,country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")
# for country in set(rivers.values()):
#     print(country.title())


favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t{language.title()}")

