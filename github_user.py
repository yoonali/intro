import requests
import sys

# GitHub 사용자 정보와 저장소 정보를 가져오는 함수
def get_github_user_and_repos(username, repo_name):
    """
    주어진 GitHub 계정(username)과 저장소(repo_name)의 정보 조회 함수.
    
    :param username: GitHub 사용자명
    :param repo_name: GitHub 저장소명
    :return: 사용자명과 저장소명 또는 오류 메시지
    """
    # 사용자 정보 URL
    user_url = f"https://api.github.com/users/{username}"
    user_response = requests.get(user_url)
    
    # 저장소 정보 URL
    repo_url = f"https://api.github.com/repos/{username}/{repo_name}"
    repo_response = requests.get(repo_url)

    if user_response.status_code == 200:
        user_info = user_response.json()  # JSON 형식의 사용자 정보
    else:
        return {"error": f"Failed to fetch user data. Status code: {user_response.status_code}"}

    if repo_response.status_code == 200:
        repo_info = repo_response.json()  # JSON 형식의 저장소 정보
    else:
        return {"error": f"Failed to fetch repo data. Status code: {repo_response.status_code}"}

    # 사용자 이름과 저장소 이름을 반환
    return {"user_name": user_info.get("login", "Unknown"), "repo_name": repo_info.get("name", "Unknown")}

# 메인 함수
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 github_user.py <username> <repo_name>")
        sys.exit(1)

    # 명령줄 인자로부터 사용자명과 저장소명 받기
    username = sys.argv[1]
    repo_name = sys.argv[2]
    
    data = get_github_user_and_repos(username, repo_name)
    
    print("🔍 데이터 확인:", data)  # 데이터 출력해서 확인
    
    if "user_name" in data and "repo_name" in data:
        print(f"✅ 정상 사용자와 저장소 테스트 통과")
        print(f"📌 사용자 이름: {data['user_name']}")
        print(f"📌 저장소 이름: {data['repo_name']}")
    else:
        print(f"❌ 오류 발생: {data['error']}")

# 실행 코드
if __name__ == "__main__":
    main()
