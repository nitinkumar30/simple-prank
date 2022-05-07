import pyautogui


name = pyautogui.prompt('Your good name please')

while True:
    a = pyautogui.confirm('Are you a dumb?',buttons=['Yes', 'No'])
    if a == 'Yes':
        pyautogui.alert('HAHAHA %s You\'re dumb as hell.!'%name)
        break



