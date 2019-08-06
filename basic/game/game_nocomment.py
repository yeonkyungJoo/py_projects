
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
    if len(game_title) > 28 : 
        game_title = input(game_msg['INPUT_TITLE_ERR_OUTOFBOUND'] .format(game_title, len(game_title)))
        pass
    elif not game_title : 
        game_title = input(game_msg['INPUT_TITLE_ERR_NULL'])
        pass
    else : 
        print('[{}]'.format(game_title))   
        break    

cell_amt = 40
print('='*cell_amt)
print('={0:^{1}}=' .format(game_title, cell_amt-2))
print('={0:^{1}}=' .format('v1.0.0', cell_amt-2))
print('='*cell_amt)

gamer_name = input(game_msg['INPUT_NAME'])
nameCheck = True  

while nameCheck :
    if not gamer_name :
        gamer_name = input(game_msg['INPUT_NAME_ERR_NULL'])
        continue       
    nameCheck = False
print(game_msg['WELCOME_MSG'] .format(gamer_name))

# 본게임 시작
while True :

    import random
    ai_num = random.randint(0, 99)
    print("ai_num : ", ai_num)

    gamer_num = input(game_msg['GAME_INTRO'])
    tryCnt = 0

    while True :
        if not gamer_num :  
            gamer_num = input(game_msg['INPUT_NUM_ERR_NULL'])
            continue
        elif not gamer_num.isnumeric() :    
            gamer_num = input(game_msg['INPUT_NUM_ERR_NOTNUM'])
            continue
        elif int(gamer_num) <0 or int(gamer_num) > 99 : 
            gamer_num = input(game_msg['INPUT_NUM_ERR_OUTOFBOUND'])
            continue
        else :     
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


    reTry = input(game_msg['ASK_RETRY'])
    while reTry not in ('yes', 'no') :
        reTry = input(game_msg['INPUT_RETRY_ERR_NOTYESORNO'])
    if reTry == 'no' :
        print(game_msg['GAMEOVER_MSG'])
        break
    else :
        continue

import sys
sys.exit()
