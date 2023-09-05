# Open and read the document 'D:\\exercise1\\file_to_read.txt'
with open('D:\\exercise1\\file_to_read.txt', 'r') as file1:
    file_content = file1.read()
word_count = file_content.count('terrible')

occurrence = 0
new_content = ''
for word in file_content.split():
    if word == 'terrible':
        occurrence += 1

# Replace the even occurrence of "terrible" with "pathetic" and the odd occurrence of "terrible" with "marvellous".        
        if occurrence % 2 == 0:
            new_content += 'pathetic'
        else:
            new_content += 'marvellous'
    else:
        new_content += word 
    new_content += ' '

with open('D:\\exercise1\\result.txt', 'w') as file2:
    file2.write(new_content)

# Print the number of occurrences of the word "terrible"
print("The number of occurrences of the word 'terrible'：", word_count)