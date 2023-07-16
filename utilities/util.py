# Helper function for input validation
def get_valid_choice(prompt, valid_choices):
  """
    Get valid input from the user based on a list of valid choices.

    Args:
        prompt (str): The prompt to display to the user.
        valid_choices (list): A list of valid choices.

    Returns:
        str: The valid input from the user.
    """
  # always run the while loop
  while True:

    # take the input store in answer
    answer = input(prompt)
    # if answer is in the valid choices list then return the answer
    if answer in valid_choices:
      # escape function if valid choice
      return answer

    # print if invalid choice, restart loop.
    print("Invalid choice. Please try again.")
