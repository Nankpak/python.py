hide_password = input("enter your password \n")
short_length = hide_password[1:-1]
start= hide_password[0]
end = hide_password[-1]
stars = "*" * len(short_length)
print(f"{start}{stars}{end}")

