from random import sample

# All used characters
uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercases = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()[]{}-_+=?~`|"

# Combine all used characters
all_used = uppercases + lowercases + numbers + symbols

# Set password length
length = 8 # 8 chars

# Make a password
password = ''.join(sample(all_used, length))

# Print the password
print("Generated Password:", password)
