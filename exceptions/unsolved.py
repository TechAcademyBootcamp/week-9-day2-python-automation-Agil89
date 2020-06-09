
def parse_input(user_input):
    input_list = user_input.split(' ')
    return input_list[0],input_list[1],input_list[2]
    ## write codes and exceptions
    ## this function must return number1, operation, number2



def calculate(n1, op, n2):
  try:
    if op == '+':
      return n1 + n2
    if op == '-':
      return n1 - n2
    if op == '*':
      return n1 * n2
    if op == '/':
      try:
        return n1 / n2
      except Exception as err:
        print(err)
  except Exception as a:
    print(a)
  #write exception


while True:
  try:
    user_input = input('>>> ')
    if user_input == 'quit':
      break
    n1, op, n2 = parse_input(user_input)
    result = calculate(n1, op, n2)
    print(result)
  except Exception as a:
    print(a)
