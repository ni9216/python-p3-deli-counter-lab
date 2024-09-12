# The local deli is putting in a new computerized queue to keep track of their customers and improve productivity. At the beginning of the day, the deli is empty so the queue should be represented by an empty list:
katz_deli = []

# Build the line() function that shows everyone their current place in the line. If there is nobody in line, it should say "The line is currently empty.".
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        alert = "The line is currently:"
        for i in range(len(katz_deli)):
            alert = alert + f' {i + 1}. {katz_deli[i]}'
        print(alert)

# Build a function that a new customer will use when entering the deli. The take_a_number() function should accept two arguments, the list for the current line of people (katz_deli), and a string containing the name of the person joining the end of the line. The function should call out (i.e., print) the person's name along with their position in line. Top-Tip: Remember that people like to count from 1, not from 0 like computers.
def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. You are number {len(katz_deli)} in line.')

#  Testing
take_a_number(katz_deli, 'Ada')

# Build the now_serving() function which should call out (print) the next person in line and then remove them from the front. If there is nobody in line, it should call out (print) that "There is nobody waiting to be served!".
def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]