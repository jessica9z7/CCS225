start_day = int(input("Enter the starting day number (0 = Sunday, 1 = Monday, ..., 6 = Saturday): "))
stay_length = int(input("Enter the length of your stay in nights: "))
return_day = (start_day + stay_length) % 7
print(f"You will return on day number (return_day)")