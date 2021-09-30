

def daily_print(day, the_file):
#creates function that takes a parameter of the numeric day and the file name to pull data from

        
        print("Day ", day)
        #prints the day the user supplied
        the_file = open(the_file)
        #opens the file the user supplied

        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
            #goes through each line of the file, strips right whitespace, splits each into a list

            melon = words[0]
            count = words[1]
            amount = words[2]
            #creates variables that point to each part of the list

            print(f"Delivered {count} {melon}s for total of ${amount}")
            #Print the data pulled from each line of the file
        the_file.close()
        
        

daily_print(1,"um-deliveries-20140519.txt")
#call the function to test

"""""
print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()

"""