# Write unittests for this function:

def count_letter_in_string(string, letter):
  if type(string) != str:
    return 0
  count = 0
  for current_letter in string:
    if current_letter == letter:
      count += 1
  return count

print(count_letter_in_string("madarka", "a"))
