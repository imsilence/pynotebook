#encoding: utf-8

languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']

stat_dict = {}

for language in languages:
    stat_dict[language] = stat_dict.get(language, 0) + 1

print(stat_dict)
