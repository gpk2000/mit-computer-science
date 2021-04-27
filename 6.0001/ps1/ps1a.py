annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12

month_cnt = 0
while True:
    if current_savings > total_cost * portion_down_payment:
        break
    month_cnt += 1
    current_savings += (current_savings*r)/12 + portion_saved * monthly_salary

print("Number of months:", month_cnt)
