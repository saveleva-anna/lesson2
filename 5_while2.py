questions_and_answers = {
  'как дела?':'хорошо',
  'что делаешь?':'программирую',
  'как погода?':'солнечно'
}

while True:
  user_say=input('введите вопрос ')
  a = questions_and_answers.get(user_say,0)
  if not a == 0:
    print(a)
  else:
    print ('я не знаю ответ')
    break

