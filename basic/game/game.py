# 절차적 프로그래밍
# step 1-1 : 
# 게임이 시작하면 다음의 프롬프트가 나온다 : "게임 제목을 입력하시오"

# 28자 이내로 입력하면     => 입력하신 "xx" 게임 제목은 최대 28자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요..\n
# 아무것도 입력하지 않으면 => 아무것도 입력하지 않았습니다. 다시!!\n
# 정상 입력

game_msg = {
    
    'INPUT_TITLE' : '게임 제목을 입력하시오. \n',
    'INPUT_TITLE_ERR_OUTOFBOUND' : '입력하신 "{0}" 게임 제목은 최대 28자(현재 {1}자 입력)를 초과할 수 없습니다. 다시 입력하세요. \n',   
    'INPUT_TITLE_ERR_NULL' : '아무것도 입력하지 않았습니다. 다시!! \n',
    
    'INPUT_NAME' : '게이머의 이름을 입력하세요. \n',
    'INPUT_NAME_ERR_NULL' : '이름이 입력되지 않았습니다. 다시 ~\n',
    'WELCOME_MSG' : '{0}님, 환영합니다! \n',

    'GAME_INTRO' : '0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요. \n',

    'INPUT_NUM_ERR_NULL' : '값을 정확하게 입력하세요. \n',  
    'INPUT_NUM_ERR_NOTNUM' : '숫자가 아닙니다. \n',
    'INPUT_NUM_ERR_OUTOFBOUND' : '값이 범위를 넘었습니다. 0~99 사이로 다시 입력 \n',

    'CHECK_BIGGER' : 'ai_num보다 큽니다. \n',
    'CHECK_SMALLER' : 'ai_num보다 작습니다. \n',
    'CHECK_SUCCESS' : '''정답입니다. 게이머 : {0}, AI : {1}
                {2}님의 총 시도 횟수는 {3}회입니다.
                획득 점수는 {4}점입니다. \n''',

    'ASK_RETRY' : '다시 게임을 할까요?(yes/no) 대소문자 관계없이 입력 \n',
    'INPUT_RETRY_ERR_NOTYESORNO' : '정확하게 (yes/no)로 입력하세요. \n',
    
    'GAMEOVER_MSG' : 'game over!! bye bye ~ \n'
}

game_title = input(game_msg['INPUT_TITLE'])
while True :
    if len(game_title) > 28 : # 28자 초과입력한 경우
        game_title = input(game_msg['INPUT_TITLE_ERR_OUTOFBOUND'] .format(game_title, len(game_title)))
    elif not game_title : # 아무것도 입력하지 않은 경우
        game_title = input(game_msg['INPUT_TITLE_ERR_NULL'])
    else : # 정상 입력
        print('[{}]'.format(game_title))   # print('[%s]' % game_title)
        break    # 반복문 종료


# step 1-2 :
# 게임 프럼프트 출력 (가로 26칸), 한글 제목일 경우 간격 안 맞는 부분은 배제
#==============================
#=          게임제목           =
#=           v1.0.0           =
#==============================

# print('='*26)
# print('={0:^24}=' .format(game_title))
# print('={0:^24}=' .format('v1.0.0'))
# print('='*26)

# 26이란 수치를 40으로 변경되어도 잘 적응되게 코드를 보정
cell_amt = 40
print('='*cell_amt)
print('={0:^{1}}=' .format(game_title, cell_amt-2)) # print(('={0:^%s}=' % (cell_amt-2)) .format(game_title))
print('={0:^{1}}=' .format('v1.0.0', cell_amt-2))
print('='*cell_amt)

# step 2 : 
# 게이머의 이름을 입력하세요
# 입력되지 않으면 => 이름이 입력되지 않았습니다. 다시 ~'

gamer_name = input(game_msg['INPUT_NAME'])
nameCheck = True  # flag 변수 : 상황을 통제/구분하는 변수
while nameCheck :
    if not gamer_name :
        gamer_name = input(game_msg['INPUT_NAME_ERR_NULL'])
        # 다시 조건 체크, 코드를 더 이상 진행하지 말고
        continue    
    # 이름 정상 입력 -> 반복문 종료    
    nameCheck = False
print(game_msg['WELCOME_MSG'] .format(gamer_name))

# 본게임 시작
while True :
    
    # step 3 :  
    # AI가 숫자 하나를 랜덤으로 생성한다 0 ~ 99 사이로 1회
    import random
    ai_num = random.randint(0, 99)
    print("ai_num : ", ai_num)

    gamer_num = input(game_msg['GAME_INTRO'])
    tryCnt = 0

    # step 4 :
    # "0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요" 출력하고 다시 입력 대기
    # 아무 값도 입력하지 않은 경우 ->'값을 정확하게 입력하세요' 출력하고 다시 입력 대기
    # '숫자가 아닙니다' 출력하고 다시 대기 입력
    # '값이 범위를 넘었습니다. 0~99 사이로 다시 입력' 출력하고, 다시 입력 대기 

    # step 5 : 
    # AI의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다 => 맞출때까지 반복
    # 정답이면 
    # 정답입니다. 게이머:입력값X, AI:세팅값Y
    #            xxx님의 총 시도 횟수는 XX회 입니다.
    #            획득 점수는 XX점 입니다.
    # 점수 : 100 - 시도횟수 * 10

    while True :
        if not gamer_num :  
            gamer_num = input(game_msg['INPUT_NUM_ERR_NULL']).strip()
            continue
        elif not gamer_num.isnumeric() :    # False인 값은 정수값이 될 수 없다 -> 정수가 아니다
            gamer_num = input(game_msg['INPUT_NUM_ERR_NOTNUM']).strip()
            continue
        elif int(gamer_num) <0 or int(gamer_num) > 99 :  # 범위를 넘은 경우
            gamer_num = input(game_msg['INPUT_NUM_ERR_OUTOFBOUND']).strip()
            continue
        else :      # 정상 입력
            tryCnt = tryCnt+1
            if int(gamer_num) == ai_num :
                score = 100 - (tryCnt-1)*10
                print(game_msg['CHECK_SUCCESS'] .format(gamer_num, ai_num, gamer_name, tryCnt, score))
                break
            while not int(gamer_num) == ai_num :
                if int(gamer_num) > ai_num :
                    gamer_num = input(game_msg['CHECK_BIGGER'])
                    break
                elif int(gamer_num) < ai_num : 
                    gamer_num = input(game_msg['CHECK_SMALLER'])
                    break

    # step6 :
    # 다시 게임을 할까요?(yes/no) 대소문자 관계 없이 입력
    # '정확하게 (yes/no)로 입력하세요'
    # no => 'game over !! bye bye~'
    # yes => 본게임 시작 으로 이동하여 진행

    reTry = input(game_msg['ASK_RETRY']).strip()
    while reTry not in ('yes', 'no') :
        reTry = input(game_msg['INPUT_RETRY_ERR_NOTYESORNO']).strip()
    if reTry == 'no' :
        print(game_msg['GAMEOVER_MSG'])
        break
    else :
        continue

import sys
sys.exit()
