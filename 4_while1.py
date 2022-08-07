def hello_user(talk):
    while True:
      user_say = input('как дела? ')
      if user_say == 'хорошо':
          print('у меня тоже')
          break
      else:
          print('что значит {}?'.format(user_say))
    
if __name__ == "__main__":
    hello_user('')