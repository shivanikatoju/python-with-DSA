def dayOfWeek(date_input):
    dd, mm, yyyy = map(int, date_input.split(','))
    
    if mm < 3:
        mm += 12
        yyyy -= 1
    
    q = dd
    m = mm
    K = yyyy % 100
    J = yyyy // 100
    
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    print(f"The day of the week for {dd}/{mm}/{yyyy} is {days[h]}.")

date_input = input("Enter the date in dd,mm,yyyy format: ")
dayOfWeek(date_input)