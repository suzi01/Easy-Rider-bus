# Write your awesome code here
import re
import itertools

data_2 = eval(input())
bus_id_count = 0
stop_id_count = 0
stop_name_count = 0
next_stop_count = 0
stop_type_count = 0
a_time_count = 0
stop_name_list = []
stop_type_list = []
bus_id_list = []

#################################### STAGES 1, 2 & 3
# ints = [0,1,3]
# strings = [2,5]
# chars = [4]
# for index in range(len(data_2)):
#     #print(len(data_2[index]))
#     for key in data_2[index]:
#         #print([index])
#         #print(data_2[index][key])
#         #print(key)
#         if key == "bus_id":
#             #print(data_2[index][key])
#             if not isinstance(data_2[index][key],int):
#                 bus_id_count += 1
#             else:
#                 bus_id_list.append(data_2[index][key])
#                 #print('bus',bus_id_count)
#         if key == "stop_id":
#              if not isinstance(data_2[index][key],int):
#                  stop_id_count += 1
#         if key == "stop_name":
#             # need to create a regex for this
#             # if ((not isinstance(data_2[index][key],str)) or (len(data_2[index][key]) == 0)):
#             stop_name_list.append(data_2[index][key])
#             pattern = '^[A-Z].*(Road|Avenue|Boulevard|Street)$'
#             stop_name_string = data_2[index][key]
#             if not re.match(pattern, stop_name_string):
#                 stop_name_list.append(stop_name_string)
#                 stop_name_count += 1
#              #  stop_name_count += 1
#         if key == "next_stop":
#              if not isinstance(data_2[index][key],int):
#                  next_stop_count += 1
#         if key == "stop_type":
#             # need to create regex for this
#             # if ((not isinstance(data_2[index][key],str)) or (len(data_2[index][key]) >1)):
#             stop_type_list.append(data_2[index][key])
#             pattern2 = '^($|S|O|F)$'
#             stop_type_string = data_2[index][key]
#             if not re.match(pattern2, stop_type_string):
#                 stop_type_list.append(stop_type_string)
#                 stop_type_count += 1
#         if key == "a_time":
#             # need to create a regex for this
#             # if ((not isinstance(data_2[index][key],str)) or (len(data_2[index][key]) == 0)):
#             pattern3 = '(0[1-9]|1\d|2[0-4]):(0\d|1\d|2\d|3\d|4\d|5\d)$'
#             a_time_string = data_2[index][key]
#             if not re.match(pattern3, a_time_string):
#                 a_time_count += 1
# total = bus_id_count + stop_id_count + stop_name_count + next_stop_count + stop_type_count + a_time_count
# print(f"Type and required field validation:", total , " errors")
# print('bus_id :', bus_id_count)
# print('stop_id :', stop_id_count)
# print('stop_name:',stop_name_count)
# print('next_stop:',next_stop_count)
# print('stop_type:',stop_type_count)
# print('a_time:',a_time_count)
# print(stop_type_list)
# print(stop_name_list)
# print(bus_id_list)
#
# for x in bus_id_list:
#     print("bus_id: " + str(x) + ", stops: " + str(bus_id_list.count(x)))
#     print(x)
# print("bus_id: 128, stops:", bus_id_list.count(128))
# print("bus_id: 256, stops:", bus_id_list.count(256))
# print("bus_id: 512, stops:", bus_id_list.count(512))


bus_id_set = set(bus_id_list)
incorrect_list = []
start_list = []
stop_list = []
others = []
on_demand = []


##################################################### STAGE 4: SPECIAL STOPS
#     # print('This is i', i)
#
#
# for k in data_2:
#     if k['stop_type'] == 'S':
#         start_list.append(k['stop_name'])
#     if k['stop_type'] == 'F':
#         stop_list.append(k['stop_name'])
#     if k['stop_type'] == 'S' or k['stop_type'] == 'F':
#         # bus = k['bus_id']
#         # print(k.values())
#         incorrect_list.append(k['bus_id'])
#         others.append(k['stop_name'])
#         # print(k)
#         # print(incorrect_list)
#     else:
#         others.append(k['stop_name'])
#
#
# if len(incorrect_list) % 2 != 0:
#     for x in incorrect_list:
#         if incorrect_list.count(x) != 2:
#             print('There is no start or end stop for the line: {}.'.format(x))
# else:
#     # print(others)
#     start_set = set(start_list)
#     others_set = set(others)
#     finish_set = set(stop_list)
#     sorted_start = sorted(list(start_set))
#     sorted_finish = sorted(list(finish_set))
#     sorted_set = filter(lambda x: others.count(x) > 1, others_set)
#     sorted_others = sorted(list(sorted_set))
#     #print('my-list', mylist)
#     #print('myset',myset)
#     # for i in others_set:
#     #     if others.count(i) < 2:
#     #         others_set.discard(i)
#     # print(others_set)
#     # print(sorted_start)
#     # print(sorted_others)
#     # print(sorted_finish)
#
#     print('Start stops:', len(sorted_start), sorted_start)
#     print('Transfer stops:', len(sorted_others), sorted_others)
#     print('Finish stops:', len(sorted_finish), sorted_finish)


# ############################## STAGE 5 UNLOST IN TIME

# last_time = ""
# last_bus_id = data_2[0]['bus_id']
# # print('last time', last_time)
# # print(last_bus_id)
# incorrect_dict = {}


# print(data_2[0]['bus_id'])
# for i in bus_id_set:
#     print('this is i', i)
#     while data_2:
#         # if key == "a_time":
#         #     print(k['a_time'])
#         #     a_time_string1 = k['a_time'].split(':')
#         #     print(a_time_string1[0])
#         #     a_time_int = [int(i) for i in a_time_string1]
#         #     print(a_time_int)
#         #     time_list.append(a_time_int)
#     # print(time_list[0])
#         current_bus_id = k['bus_id']
#         print('bus id', current_bus_id)
#         current_time = k['a_time']
#         print('current time', current_time)
#         if current_bus_id != last_bus_id:
#             last_time = ""
#         if current_time < last_time:
#             d1 = {current_bus_id: k['stop_name']}
#             incorrect_dict.update(d1)
#             print(incorrect_dict)
#             break
#         #
#         # print('incorrect', incorrect_dict)
#
#         last_time = current_time
#         last_bus_id = current_bus_id
# print(incorrect_dict)
# print('Arrival time test:')
# if incorrect_dict:
#     print(incorrect_dict)
#         #print('bus_id line',bus,': wrong time on station', stop)
# else:
#     print('OK')
#

# for i in bus_id_set:
#     # print('this is i', i)
#     var = 0
#     last_time = ""
#     while var < len(data_2):
#         # print('last_time', last_time)
#         last_bus_id = i
#         current_bus_id = data_2[var]['bus_id']
#         # print('bus id', current_bus_id)
#         # print('last bus',last_bus_id)
#         current_time = data_2[var]['a_time']
#         # print('current time', current_time)
#         # print('last_time', last_time)
#         if current_bus_id != last_bus_id:
#             # print('current, last', current_bus_id, last_bus_id)
#             last_time = ""
#             current_time = ""
#             # print('last time check', last_time)
#         if current_time < last_time:
#             d1 = {current_bus_id: data_2[var]['stop_name']}
#             incorrect_dict.update(d1)
#             # print(incorrect_dict)
#             last_time = current_time
#             last_bus_id = current_bus_id
#             # print('last bus id', last_bus_id)
#             break
#         #
#         # print('incorrect', incorrect_dict)
#
#         last_time = current_time
#         last_bus_id = current_bus_id
#         var += 1
# #print(incorrect_dict)
# print('Arrival time test:')
# if incorrect_dict:
#     for key, value in incorrect_dict.items():
#         print('bus_id',key,': wrong time on station', value)
# else:
#     print('OK')

############################# STAGE 6: on-demand stops cannot be initial, final, or transfer stops

for k in data_2:
    if k['stop_type'] == 'S':
        start_list.append(k['stop_name'])
    if k['stop_type'] == 'F':
        stop_list.append(k['stop_name'])
    if k['stop_type'] == 'S' or k['stop_type'] == 'F':
        incorrect_list.append(k['bus_id'])
        others.append(k['stop_name'])
    if k['stop_type'] == 'O':
        on_demand.append(k['stop_name'])
        others.append(k['stop_name'])
    else:
        others.append(k['stop_name'])

start_set = set(start_list)
others_set = set(others)
finish_set = set(stop_list)
sorted_start = sorted(list(start_set))
sorted_finish = sorted(list(finish_set))
sorted_set = filter(lambda x: others.count(x) > 1, others_set)
sorted_others = sorted(list(sorted_set))

incorrect_demand = []
# print(on_demand)
# print(sorted_start)
# print(sorted_others)
# print(sorted_finish)

for stop in on_demand:
    if stop in itertools.chain(sorted_start, sorted_others, sorted_finish):
        incorrect_demand.append(stop)
# print(incorrect_demand)

print('On demand stops test:')
if incorrect_demand:
    print('Wrong stop type:', sorted(incorrect_demand))
else:
    print('OK')


