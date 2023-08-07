import random


def handle_response(message) -> str:
    # make message lowercase
    p_message = message.lower()

    if p_message == 'hello':
      return 'Hello there'
    
    if p_message == 'roll':
      return str(random.randint(1, 6))
    
    if p_message == '!help':
      return '`Commands: !roll, !help, !hello`'
    
    return 'I don\'t understand that command. Try !help'