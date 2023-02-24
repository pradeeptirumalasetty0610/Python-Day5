student_heights = input("Input a list of student heights ").split()
sum,i=0,0
for n in student_heights:
  sum+= int(n)
  i+=1

avg=sum/i

print(round(avg))