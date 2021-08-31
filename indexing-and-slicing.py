message = input("Enter a message: ")

print("Length of message:", int(len(message)))
print("First character:", message[0])
print("Last character:", message[-1])
print("Middle character:", message[int(len(message) / 2 )])
print("Reversed message:", message[::-1])