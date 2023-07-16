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
  while True:
    answer = input(prompt)
    if answer in valid_choices:
      return answer
    print("Invalid choice. Please try again.")
