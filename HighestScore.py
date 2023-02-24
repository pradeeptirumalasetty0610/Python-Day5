student_scores = input("Input a list of student scores ").split()
temp=int(student_scores[0])
for n in range(1,len(student_scores)):
  if temp<int(student_scores[n]):
      temp=int(student_scores[n])
print(temp)