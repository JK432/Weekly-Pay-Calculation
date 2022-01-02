#An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays overtime pay and an employee’s total weekly pay.
h=int(input())
r=int(input())
o=int(input())
op=int(o*1.5*h)
wp=int((h*r)+op)
print((op))
print((wp))