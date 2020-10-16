"""Given the names and grades for each student in a Physics class of students, store them in a nested list
 and print the name(s) of any student(s) having the second lowest grade."""

if __name__ == '__main__':
   score_list = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
result = new_list[1][1]
result.sort()
for i in result:
    print (i)

