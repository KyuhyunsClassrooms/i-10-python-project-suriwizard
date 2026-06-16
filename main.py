# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 21007 김수영
# 프로젝트 주제: 5*5 행렬 기반의 플레이페어 대칭키 암호화 및 복호화 시스템
def create_matrix(key_str):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key_str = key_str.upper().replace("J", "I")
    
    temp_list = []
    
    for char in key_str:
        if char in alphabet and char not in temp_list:
            temp_list.append(char)
            
    for char in alphabet:
        if char not in temp_list:
            temp_list.append(char)
            
    new_matrix = []
    for i in range(0, 25, 5):
        row = temp_list[i:i+5]
        new_matrix.append(row)
        
    return new_matrix


def prepare_text(plain_text):
    plain_text = plain_text.upper().replace("J", "I").replace(" ", "")
    processed_text = ""
    
    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        
        if i + 1 < len(plain_text):
            char2 = plain_text[i+1]
            if char1 == char2:
                processed_text += char1 + "X"
                i += 1 
            else:
                processed_text += char1 + char2
                i += 2 
        else:
            processed_text += char1
            i += 1
            
    if len(processed_text) % 2 != 0:
        processed_text += "X"
        
    return processed_text


def find_position(char, PlayFair):
    for row in range(5):
        for col in range(5):
            if PlayFair[row][col] == char:
                return row, col
    return -1, -1


def cipher_pair(char1, char2, PlayFair, mode):
    r1, c1 = find_position(char1, PlayFair)
    r2, c2 = find_position(char2, PlayFair)
    
    if mode == "encrypt":
        shift = 1
    elif mode == "decrypt":
        shift = -1
        
    if r1 == r2:
        new_c1 = (c1 + shift) % 5
        new_c2 = (c2 + shift) % 5
        new_char1 = PlayFair[r1][new_c1]
        new_char2 = PlayFair[r2][new_c2]

    elif c1 == c2:
        new_r1 = (r1 + shift) % 5
        new_r2 = (r2 + shift) % 5
        new_char1 = PlayFair[new_r1][c1]
        new_char2 = PlayFair[new_r2][c2]
        
    else:
        new_char1 = PlayFair[r1][c2]
        new_char2 = PlayFair[r2][c1]
        
    return new_char1, new_char2


def process_all_text(text, PlayFair, mode):
    result_text = ""
    
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        
        new_char1, new_char2 = cipher_pair(char1, char2, PlayFair, mode)
        result_text += new_char1 + new_char2
        
    return result_text


def main():
    PlayFair = []
    
    while True:
        print("\n=== 플레이페어 암호 프로그램 ===")
        print("1. 암호화")
        print("2. 복호화")
        print("3. 프로그램 종료")
        
        choice = input("원하는 기능을 선택하세요 (1, 2, 3): ").strip()
        
        if choice == '1':
            mode = "encrypt"
            key_str = input("비밀 대칭키를 입력하세요: ").strip()
            plain_text = input("암호화할 본문을 입력하세요: ").strip()
            
            PlayFair = create_matrix(key_str)
            processed_text = prepare_text(plain_text)
            result_text = process_all_text(processed_text, PlayFair, mode)
            
            pairs_list = []
            for i in range(0, len(processed_text), 2):
                pairs_list.append([processed_text[i], processed_text[i+1]])
            
            print(f"\n[!] 생성된 5x5 비밀키 행렬(PlayFair): {PlayFair}")
            print(f"[!] 두 글자씩 묶은 2차원 리스트: {pairs_list}")
            print(f"[!] 최종 암호문: {result_text}")
            
        elif choice == '2':
            mode = "decrypt"
            key_str = input("비밀 대칭키를 입력하세요: ").strip()
            cipher_text = input("복호화할 본문을 입력하세요: ").strip()
            
            processed_text = cipher_text.upper().replace("J", "I").replace(" ", "")
            
            if len(processed_text) % 2 != 0:
                print("\n[오류] 올바른 암호문 형식이 아닙니다. (유효한 알파벳 글자 수가 홀수입니다.)")
                continue
                
            PlayFair = create_matrix(key_str)
            result_text = process_all_text(processed_text, PlayFair, mode)
            
            pairs_list = []
            for i in range(0, len(processed_text), 2):
                pairs_list.append([processed_text[i], processed_text[i+1]])
            
            print(f"\n[!] 생성된 5x5 비밀키 행렬(PlayFair): {PlayFair}")
            print(f"[!] 두 글자씩 묶은 2차원 리스트: {pairs_list}")
            print(f"[!] 최종 복호화문: {result_text}")
            
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 다시 입력해주세요.")


if __name__ == "__main__":
    main()