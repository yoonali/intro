import re

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$"
    if re.match(pattern, password):
        return True
    return False

while True:
    test_passwords = input("비밀번호를 입력해주세요(!quit를 입력하시면 프로그램이 종료됩니다.): ")

    if test_passwords.lower() == '!quit':
        print("프로그램을 종료합니다.")
        break

    print(f"{test_passwords}: {'Valid' if test_passwords else 'Invalid'}")
