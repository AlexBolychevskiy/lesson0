calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string_new = []
    string_new.append(len(string))
    a = string.upper()
    string_new.append(a)
    b = string.lower()
    string_new.append(b)
    string_new1 = tuple(string_new)
    count_calls()
    return string_new1
def is_contains(string,list_to_search):
     c = string.upper()
     uppercase_list = [s.upper() for s in list_to_search]
     if c in uppercase_list:
           result = True
     elif c not in uppercase_list:
        result = False
     return result
     count_calls()
string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
