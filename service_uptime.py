# Calculate uptime percentage of a service
# Take 2 parameters, Total Hours and Down Hours
# Return uptime percentage rounded to two decimal places 


total_hours = 6
down_hours = .32


def service_uptime(total_hours, down_hours):
    uptime = (total_hours - down_hours) / total_hours
    print(f"The service's uptime is {uptime:.2%}.")

service_uptime()

