print("****Welcome to Stats Tracker 3000****")

sched_hours = 120
objective = 2.1

# total reaches
input_reaches = input("Enter reaches separated by space then hit enter:  ")
reach_list = input_reaches.split()
reach_total = []
for num in reach_list:
    reach_total.append(int(num))
print(sum(reach_total))

# total attempts
input_attempts = input("Enter attempts separated by space then hit enter:  ")
attempt_list = input_attempts.split()
attempt_total = []
for attempt in attempt_list:
    attempt_total.append(int(attempt))
print(sum(attempt_total))

# WOOT totals from available time and aux
input_woot = input("Enter WOOT time separate by space:  ")
woot_list = input_woot.split()
woot_total = []
for woot in woot_list:
    woot_total.append(float(woot))
print(sum(woot_total))

# days out includes sick, vacation
input_days_out = input("How many days were you off?: ")
hours_out = int(input_days_out) * 8

engagements = int(input("How many engagements do you have?:  "))
print("You have {} engagements".format(engagements))
time_for_eng = int(input("How much time per engagement? (minutes):  "))
total_eng_woot = (engagements * time_for_eng) / 60.00
print("Your total time back for engagements: {} hours".format(total_eng_woot))

# bonus woot = attempts + reaches divided by 60
bonus_woot = ((sum(attempt_total) + sum(reach_total)) /60.00)

# adjusted WOOT = total woot + hours out + bonus woot + engagement adjustment
adjusted_woot = sum(woot_total) + hours_out + bonus_woot + total_eng_woot
#productive hours = scheduled hours - adjusted total woot
prod_hrs = round(sched_hours - adjusted_woot,3)
adj_rpph = round(sum(reach_total) / prod_hrs,3)
woot_final = round(adj_rpph / objective,3)


print("\n")
print("March 2021 Stats")
print("Productive hours: " + str(prod_hrs))
print("Adjusted RPProdH: " + str(adj_rpph))
print("WOOT total: " + str(sum(woot_total)))

print("Reaches: " + str(sum(reach_total)))
print("Attempts: " + str(sum(attempt_total)))
print("Bonus WOOT: " + str(bonus_woot))
print("WOOT %: " + str(woot_final*100))
