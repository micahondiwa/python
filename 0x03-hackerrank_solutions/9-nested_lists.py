if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])
    students.sort(key=lambda x: (x[1], x[0]))
    second_lowest = students[0][1]
    for student in students:
        if student[1] > second_lowest:
            second_lowest = student[1]
            break
    result = [student[0]
              for student in students if student[1] == second_lowest]
    result.sort()
    for i in result:
        print(i)
