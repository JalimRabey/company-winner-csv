def pick_winner(result):
  if (result.get('Marvel') > result.get('DC')):
    return 'Marvel'
  else:
    return 'DC'
