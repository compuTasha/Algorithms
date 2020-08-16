import os
import subprocess

section_num = input("type section number: ")
file_num = input("type file number: ")
section = "section" + section_num

file_path = "/Users/mijoo/Algorithms/inflearn/Algorithm_problem_solving_with_python/section" + section_num + "/" + file_num + ".py"
input_path = "/Users/mijoo/Algorithms/inflearn/Algorithm_problem_solving_with_python/section" + section_num + "/" + file_num

f = open(input_path + "/in" + "1" + ".txt", 'r')
data = f.read()
print(data)

command = 'python 3 ' + file_path

out = subprocess.run(command, shell=True, text=True, args=data)

# for i in range(5):
#     f = open(input_path + "/in" + "1" + ".txt", 'r')
#     data = f.read()
#     print(data)
#     os.system('python3 ' + file_path.format + data)
#     f.close()

# os.system('python3 ' + file_path.format(args=data))

# exec(open(file_path).read())

print("end")