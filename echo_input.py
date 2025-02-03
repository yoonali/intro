# 1. 사용자로부터 문장을 입력받고 입력 받은 문자를 그대로 출력

while True:
    user_input = input("문장을 입력하세요 (종료하려면 'exit' 입력): ")
    
    if user_input.lower() == '!quit':
        print("프로그램을 종료합니다.")
        break
    
    print("입력한 문장:", user_input)

