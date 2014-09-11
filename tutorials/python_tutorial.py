import sys
print(sys.version_info[:])

# list slices
a = [1, 2, 3, 4, 5, 6, 7, 8]

# a[start:end] start is inclusive, end is exclusive
print(a[0:3])

# check whether an item appears on a list
a = ['apple', 'pear', 'peach']

print('pear' in a)

if 'pear' in a:
    print('there is a pear')

if 'grape' in a:
    print('there is a grape')

# python dictionaries
a = {'name': 'bob'}
print(a['name'])

print('name' in a)

# json is just a combination of dictionaries and lists
a = {'name': 'Fidel Abella', 'Interests': ['cycling', 'running', 'golf']}

print(a)

a['Interests'].append('swimming')

print(a)

# for loops
fruit = ['apple', 'orange', 'grape', 'apple', 'orange', 'grape']

new_fruit = []

for item in fruit:
    print(item)

    new_fruit.append(item)

print(new_fruit)


def analyze_list(l):
    counts = {}
    for item in l:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1

    return counts


print(analyze_list(fruit))