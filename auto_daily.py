# -*- coding: utf-8 -*-

import sys
from time import sleep
import pyautogui
import pywinauto

# 1920 * 1080
# 메크로 1 = 0, 0 >> 960, 540       메크로2 = 960, 0 >> 960, 540

odin = []

# 오딘 프로그램 찾기 
# 타이틀이 ODIN으로 같기 때문에 실행 시 계정 순서가 바뀔 수 있음 그래서 하단 메소드에 창위치를 변경해주게끔 수정
# 먼저 getWindowsWithTitle 한 프로그램부터 왼쪽부터 정렬된다. 2개까지
def get_mecro():
    for i in pyautogui.getWindowsWithTitle('ODIN'):
        if i.title.strip() == 'ODIN':
            print(i.title, i.size)
            odin.append(i)

# 1번 프로그램 활성화
def active_mecro_1():
    if odin[0].isActive == False:
        pywinauto.application.Application().connect(handle=odin[0]._hWnd).top_window().set_focus()
        odin[0].resizeTo(974, 527)  # 창 사이즈 (변경금지)
        odin[0].moveTo(-7, 0)       # 창 위치 (변경금지)
        odin[0].activate()

# 2번 프로그램 활성화
def active_mecro_2():
    if odin[1].isActive == False:
        pywinauto.application.Application().connect(handle=odin[1]._hWnd).top_window().set_focus()
        odin[1].resizeTo(974, 527)  # 창 사이즈 (변경금지)
        odin[1].moveTo(953, 0)      # 창 위치(변경금지)
        odin[1].activate()

# 절전모드 해제 및 게임화면으로 이동
def disable_sleep_mode():
    sleep(1)
    if odin[0].isActive == True:
        sleep_mode = pyautogui.locateOnScreen('image\disable_sleep_mode.jpg', confidence=0.8, region=(0, 0, 960, 540))
        print(sleep_mode , '절전모드 아님')
        if sleep_mode is not None:
            pyautogui.moveTo(480, 270)
            pyautogui.dragTo(680, 270, 1, button='left')
    elif odin[1].isActive == True:
        sleep_mode = pyautogui.locateOnScreen('image\disable_sleep_mode.jpg', confidence=0.8, region=(960, 0, 960, 540))
        print(sleep_mode , '절전모드 아님')
        if sleep_mode is not None:
            pyautogui.moveTo(1440, 270)
            pyautogui.dragTo(1640, 270, 1, button='left')

# 메인화면 돌아가기
def main_back():
    sleep(1)
    if odin[0].isActive == True:
        main_back = pyautogui.locateOnScreen('image\\main_back.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if main_back:
            pyautogui.click(main_back)
            sleep(1)
        main_back_nb = pyautogui.locateOnScreen('image\\main_back_nb.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if main_back_nb:
            pyautogui.click(main_back_nb)
            sleep(1)
        previous_back = pyautogui.locateOnScreen('image\\previous_back.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if previous_back:
            pyautogui.click(previous_back)
            sleep(1)
        click_x = pyautogui.locateOnScreen('image\\click_x.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if click_x:
            pyautogui.click(click_x)
            sleep(1)

    elif odin[1].isActive == True:
        back_click = pyautogui.locateOnScreen('image\\main_back.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if back_click:
            pyautogui.click(back_click)
            sleep(1)
        main_back_nb = pyautogui.locateOnScreen('image\\main_back_nb.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if main_back_nb:
            pyautogui.click(main_back_nb)
            sleep(1)
        previous_back = pyautogui.locateOnScreen('image\\previous_back.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if previous_back:
            pyautogui.click(previous_back)
            sleep(1)
        click_x = pyautogui.locateOnScreen('image\\click_x.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if click_x:
            pyautogui.click(click_x)
            sleep(1)

# 물약 구매
def go_town():
    sleep(1)
    if odin[0].isActive == True:
        main_back()
        sleep(2)
        pyautogui.click(22, 203)
        sleep(2)
        gotown_click = pyautogui.locateOnScreen('image\\gotown_ok.jpg', confidence=0.8, region=(0, 0, 960, 540))
        if gotown_click:
            print('물약 사러 마을로 갑니다~!')
            sleep(2)
            pyautogui.click(gotown_click)
            sleep(20)
        else: 
            print('마을이거나 귀환 불가 지역')
        pyautogui.press('4')
        sleep(20)
        pyautogui.click(120, 130) # 대형물약
        sleep(3)
        pyautogui.click(547, 313) # 최대
        sleep(3)
        pyautogui.click(530, 388) # 구매하기
        sleep(3)
        main_back()
    elif odin[1].isActive == True:
        main_back()
        sleep(2)
        pyautogui.click(982, 203)
        sleep(2)
        gotown_click = pyautogui.locateOnScreen('image\\gotown_ok.jpg', confidence=0.8, region=(960, 0, 960, 540))
        if gotown_click:
            print('물약 사러 마을로 갑니다~!')
            sleep(2)
            pyautogui.click(gotown_click)
            sleep(20)
        else: 
            print('마을이거나 귀환 불가 지역')
        pyautogui.press('4')
        sleep(20)
        pyautogui.click(1080, 130) # 대형물약
        sleep(3)
        pyautogui.click(1507, 313) # 최대
        sleep(3)
        pyautogui.click(1490, 388) # 구매하기
        sleep(3)
        main_back()

# 자동 사냥 켜기
def auto_play():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        auto_1 = pyautogui.locateOnScreen('image\\auto_play\\auto_1.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_2 = pyautogui.locateOnScreen('image\\auto_play\\auto_2.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_3 = pyautogui.locateOnScreen('image\\auto_play\\auto_3.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_4 = pyautogui.locateOnScreen('image\\auto_play\\auto_4.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_5 = pyautogui.locateOnScreen('image\\auto_play\\auto_5.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_6 = pyautogui.locateOnScreen('image\\auto_play\\auto_6.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_7 = pyautogui.locateOnScreen('image\\auto_play\\auto_7.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_8 = pyautogui.locateOnScreen('image\\auto_play\\auto_8.jpg', confidence=0.8, region=(0, 0, 960, 540))
        print('자동사냥 체크 :',auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8)
        if auto_1:
            pyautogui.click(auto_1)
            sleep(1)
        elif auto_2:
            pyautogui.click(auto_2)
            sleep(1)
        elif auto_3:
            pyautogui.click(auto_3)
            sleep(1)
        elif auto_4:
            pyautogui.click(auto_4)
            sleep(1)            
        elif auto_5:
            pyautogui.click(auto_5)
            sleep(1)
        elif auto_6:
            pyautogui.click(auto_6)
            sleep(1)
        elif auto_7:
            pyautogui.click(auto_7)
            sleep(1)
        elif auto_8:
            pyautogui.click(auto_8)
            sleep(1)

    elif odin[1].isActive == True:
        auto_1 = pyautogui.locateOnScreen('image\\auto_play\\auto_1.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_2 = pyautogui.locateOnScreen('image\\auto_play\\auto_2.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_3 = pyautogui.locateOnScreen('image\\auto_play\\auto_3.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_4 = pyautogui.locateOnScreen('image\\auto_play\\auto_4.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_5 = pyautogui.locateOnScreen('image\\auto_play\\auto_5.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_6 = pyautogui.locateOnScreen('image\\auto_play\\auto_6.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_7 = pyautogui.locateOnScreen('image\\auto_play\\auto_7.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_8 = pyautogui.locateOnScreen('image\\auto_play\\auto_8.jpg', confidence=0.8, region=(960, 0, 960, 540))
        print('자동사냥 체크 :',auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8)
        if auto_1:
            pyautogui.click(auto_1)
            sleep(1)
        elif auto_2:
            pyautogui.click(auto_2)
            sleep(1)
        elif auto_3:
            pyautogui.click(auto_3)
            sleep(1)
        elif auto_4:
            pyautogui.click(auto_4)
            sleep(1)            
        elif auto_5:
            pyautogui.click(auto_5)
            sleep(1)
        elif auto_6:
            pyautogui.click(auto_6)
            sleep(1)
        elif auto_7:
            pyautogui.click(auto_7)
            sleep(1)
        elif auto_8:
            pyautogui.click(auto_8)
            sleep(1)

# 캐릭터 변경 (1~5번)
def char_change(ch_num):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('o')
        sleep(2)
        pyautogui.click(800, 395)
        sleep(2)
        pyautogui.click(528, 331)
        sleep(20)
        if ch_num == 1:
            pyautogui.click(915, 89)
            sleep(2)
        if ch_num == 2:
            pyautogui.click(915, 155)
            sleep(2)
        if ch_num == 3:
            pyautogui.click(915, 219)
            sleep(2)
        if ch_num == 4:
            pyautogui.click(915, 280)
            sleep(2)
        if ch_num == 5:
            pyautogui.click(915, 344)
            sleep(2)
        pyautogui.click(877, 484)
        sleep(20)                    
    elif odin[1].isActive == True:
        pyautogui.press('o')
        sleep(2)
        pyautogui.click(1760, 395)
        sleep(2)
        pyautogui.click(1488, 331)
        sleep(20)
        if ch_num == 1:
            pyautogui.click(1875, 89)
            sleep(2)
        if ch_num == 2:
            pyautogui.click(1875, 155)
            sleep(2)
        if ch_num == 3:
            pyautogui.click(1875, 219)
            sleep(2)
        if ch_num == 4:
            pyautogui.click(1875, 280)
            sleep(2)
        if ch_num == 5:
            pyautogui.click(1875, 344)
            sleep(2)
        pyautogui.click(1837, 484)
        sleep(20)

# 정예던전 입장 - 입장시간이 0초인지 아닌지만 체크, 0초가 아니면 플레이
# 각 던전 레벨을 넣어줘야 함, 던전 타이틀로 해당 던전 확인함
def elite_dg_entrance(event_dg_level, money_dg_level, scroll_dg_level):

    # 던전 난이도 1, 2, 3 = 1단계, 2단계, 3단계
    def dg_level_choice(dg_level):
        sleep(1)
        if odin[0].isActive == True:
            if dg_level == 1:
                pyautogui.click(108, 92)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(2)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
                
            if dg_level == 2:
                pyautogui.click(108, 134)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 3:
                pyautogui.click(108, 174)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 4:
                pyautogui.click(108, 216)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 5:
                pyautogui.click(108, 263)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 6:
                pyautogui.click(108, 300)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 7:
                pyautogui.click(108, 342)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 8:
                pyautogui.click(108, 384)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 9:
                pyautogui.click(108, 422)
                sleep(2)
                pyautogui.click(880, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(20, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
        elif odin[1].isActive == True:
            if dg_level == 1:
                pyautogui.click(1068, 92)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 2:
                pyautogui.click(1068, 134)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 3:
                pyautogui.click(1068, 174)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 4:
                pyautogui.click(1068, 216)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 5:
                pyautogui.click(1068, 263)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 6:
                pyautogui.click(1068, 300)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 7:
                pyautogui.click(1068, 342)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 8:
                pyautogui.click(1068, 384)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0
            if dg_level == 9:
                pyautogui.click(1068, 422)
                sleep(2)
                pyautogui.click(1840, 488)
                sleep(20)
                dg_move = pyautogui.locateOnScreen('image\\elite_dg\\dg_move.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print('던전 입장 여부(None이면 입장, 좌표 나오면 입장시간 0초) : ',dg_move)
                if dg_move:
                    sleep(1)
                    pyautogui.click(980, 47)
                    sleep(2)
                    return 1
                else:
                    pyautogui.press('F5')
                    sleep(10)
                    pyautogui.press('g')
                    return 0

    sleep(1)
    main_back()
    if odin[0].isActive == True:
        sleep(1)
        pyautogui.press('F8')
        sleep(2)
        pyautogui.click(175, 85)
        sleep(2)
        while True:
            #던전 체크
            event_dg = pyautogui.locateOnScreen('image\\elite_dg\\event_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            print('오딘1 던전 확인 : event_dg : ', event_dg)
            if event_dg:
                pyautogui.click(event_dg)
                sleep(2)
                e_dg_level = dg_level_choice(event_dg_level)
                print('오딘1 이벤트 던전 진행 여부(0이면 진행, 1이면 시간없음(완료)) :', e_dg_level)
                if e_dg_level == 0:
                    print('오딘1 이벤트 던전 시작, while문 종료')
                    break
                elif e_dg_level == 1:
                    pass
            money_dg = pyautogui.locateOnScreen('image\\elite_dg\\money_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            print('오딘1 던전 확인 : money_dg : ', money_dg)
            if money_dg:
                pyautogui.click(money_dg)
                m_dg_level = dg_level_choice(money_dg_level)
                print('오딘1 머니 던전 진행 여부(0이면 진행, 1이면 시간없음(완료)) :', m_dg_level)
                if m_dg_level == 0:
                    print('오딘1 머니 던전 시작, while문 종료')
                    break
                elif m_dg_level == 1:
                    pass
            scroll_dg = pyautogui.locateOnScreen('image\\elite_dg\\scroll_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            print('오딘1 던전 확인 : scroll_dg : ', scroll_dg)
            if scroll_dg:
                pyautogui.click(scroll_dg)
                s_dg_level = dg_level_choice(scroll_dg_level)
                print('오딘1 스크롤 던전 진행 여부(0이면 진행, 1이면 시간없음(완료)) :', s_dg_level)
                if s_dg_level == 0:
                    print('오딘1 스크롤 던전 시작, while문 종료')
                    break
                elif s_dg_level == 1:
                    print('오딘1 모든 던전 완료, while문 종료, 리턴값 1')
                    return 1
                    main_back()
                    break
    elif odin[1].isActive == True:
        sleep(1)
        pyautogui.press('F8')
        sleep(2)
        pyautogui.click(1135, 85)
        sleep(2)
        while True:
            #던전 체크
            event_dg = pyautogui.locateOnScreen('image\\elite_dg\\event_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            print('오딘2 던전 확인 : event_dg : ', event_dg)
            if event_dg:
                pyautogui.click(event_dg)
                sleep(2)
                e_dg_level = dg_level_choice(event_dg_level)
                print('오딘2 이벤트 던전 진행 여부(0이면 진행, 1이면 시간없음(완료)) :', e_dg_level)
                if e_dg_level == 0:
                    print('오딘2 이벤트 던전 시작, while문 종료')
                    break
                elif e_dg_level == 1:
                    pass
            money_dg = pyautogui.locateOnScreen('image\\elite_dg\\money_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            print('오딘2 던전 확인 : money_dg : ', money_dg)
            if money_dg:
                pyautogui.click(money_dg)
                m_dg_level = dg_level_choice(money_dg_level)
                print('오딘2 머니 던전 진행 여부(0이면 진행, 1이면 시간없음(완료)) :', m_dg_level)
                if m_dg_level == 0:
                    print('오딘2 머니 던전 시작, while문 종료')
                    break
                elif m_dg_level == 1:
                    pass
            scroll_dg = pyautogui.locateOnScreen('image\\elite_dg\\scroll_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            print('오딘2 던전 확인 : scroll_dg : ', scroll_dg)
            if scroll_dg:
                pyautogui.click(scroll_dg)
                s_dg_level = dg_level_choice(scroll_dg_level)
                print('오딘2 스크롤 던전 진행 여부(0이면 진행, 1이면 시간없음(완료)) :', s_dg_level)
                if s_dg_level == 0:
                    print('오딘2 스크롤 던전 시작, while문 종료')
                    break
                elif s_dg_level == 1:
                    print('오딘2 모든 던전 완료, while문 종료, 리턴값 1')
                    return 1
                    main_back()
                    break

# 마을의뢰 - 고급 및 최고급 의뢰만 진행하며, 골드로만 갱신함
def town_request():
    sleep(1)
    main_back()
    sleep(1)
    pyautogui.press('j')

    # 완료 퀘스트 확인 및 보상 수령
    def town_request_get_reward():
        print('완료 퀘스트 및 보상 수령 시작')
        sleep(1)
        if odin[0].isActive == True:
            # 변동 이미지라서 3번 체크로 유무 확인
            while True:
                check_atr = pyautogui.locateOnScreen('image\\town_request\\request_reward.jpg', confidence=0.9, region=(0, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request\\request_reward.jpg', confidence=0.9, region=(0, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request\\request_reward.jpg', confidence=0.9, region=(0, 100, 50, 50))
                sleep(1)
                if check_atr:
                    print('오딘1 - 완료 퀘스트 있음')
                    pyautogui.click(901, 496)
                    sleep(4)
                    pyautogui.click(475, 339)
                    sleep(3)
                    pyautogui.click(470, 440)
                    sleep(2)
                else:
                    print('오딘1 - 완료 퀘스트 및 보상 수령 완료!!!')
                    break

        elif odin[1].isActive == True:
            # 변동 이미지라서 3번 체크로 유무 확인
            while True:
                check_atr = pyautogui.locateOnScreen('image\\town_request\\request_reward.jpg', confidence=0.9, region=(960, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request\\request_reward.jpg', confidence=0.9, region=(960, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request\\request_reward.jpg', confidence=0.9, region=(960, 100, 50, 50))
                sleep(1)
                if check_atr:
                    print('오딘2 - 완료 퀘스트 있음')
                    pyautogui.click(1861, 496)
                    sleep(4)
                    pyautogui.click(1435, 339)
                    sleep(3)
                    pyautogui.click(1430, 440)
                    sleep(2)
                else:
                    print('오딘2- 완료 퀘스트 및 보상 수령 완료!!!')
                    break

    # 퀘스트 난이도 확인 및 의뢰수락
    def town_request_level_confirm():
        print('퀘스트 난이도 확인 및 의뢰수락(골드의뢰만 수락함)')
        sleep(1)
        if odin[0].isActive == True:
            #상급, 최상급 퀘스트만 선택
            while True:
                level_1 = pyautogui.locateOnScreen('image\\town_request\\level_1.jpg', confidence=0.8, region=(230, 100, 60, 60))
                level_2 = pyautogui.locateOnScreen('image\\town_request\\level_2.jpg', confidence=0.8, region=(230, 100, 60, 60))
                level_3 = pyautogui.locateOnScreen('image\\town_request\\level_3.jpg', confidence=0.8, region=(230, 100, 60, 60))
                level_1_nb = pyautogui.locateOnScreen('image\\town_request\\level_1_nb.jpg', confidence=0.8, region=(230, 100, 60, 60))
                level_2_nb = pyautogui.locateOnScreen('image\\town_request\\level_2_nb.jpg', confidence=0.8, region=(230, 100, 60, 60))
                level_3_nb = pyautogui.locateOnScreen('image\\town_request\\level_3_nb.jpg', confidence=0.8, region=(230, 100, 60, 60))
                gold_change = pyautogui.locateOnScreen('image\\town_request\\gold_change.jpg', confidence=0.8, region=(130, 460, 70, 70))
                gold_change_2 = pyautogui.locateOnScreen('image\\town_request\\gold_change_2.jpg', confidence=0.8, region=(130, 460, 70, 70))
                print('데스크탑 이미지 인식 ', level_1, level_2, level_3)
                print('노트북 이미지 인식 및 골드 표시 인식', level_1_nb, level_2_nb, level_3_nb, gold_change)
                if level_1 or level_2 or level_3 or level_1_nb or level_2_nb or level_3_nb:
                    if level_2 or level_3 or level_2_nb or level_3_nb:
                        pyautogui.click(891, 496)
                        sleep(1)
                    if level_1:
                        if gold_change or gold_change_2:
                            pyautogui.click(gold_change)
                            sleep(2)
                            pyautogui.click(535, 347)
                            sleep(3)
                        else:
                            pyautogui.click(891, 496)
                            sleep(1)
                    max_request = pyautogui.locateOnScreen('image\\town_request\\max_request.jpg', confidence=0.8, region=(0, 0, 960, 540))
                    no_more_request = pyautogui.locateOnScreen('image\\town_request\\no_more_request.jpg', confidence=0.8, region=(0, 0, 960, 540))
                    if  no_more_request:
                        print('오딘1 - 마을 의뢰 가득참')
                        pyautogui.moveTo(120, 430)
                        pyautogui.dragTo(120, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.8, region=(170, 150, 70, 310))
                        if request_ok:
                            pyautogui.click(request_ok)
                            sleep(1)
                            pyautogui.click(676, 496)
                            sleep(3)
                            auto_play()
                            break
                        else:
                            main_back()
                            sleep(3)
                            auto_play()
                            break
                    if max_request:
                        print('오딘1 - 일일 마을 의뢰 완료')
                        return 1
                        pyautogui.moveTo(120, 430)
                        pyautogui.dragTo(120, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.8, region=(170, 150, 70, 310))
                        if request_ok:
                            pyautogui.click(request_ok)
                            sleep(1)
                            pyautogui.click(676, 496)
                            sleep(3)
                            auto_play()
                            break
                        else:
                            main_back()
                            sleep(3)
                            auto_play()
                            break
                else:
                    # 의뢰 수령 중에 완료된 경우가 있는 경우
                    main_back()
                    pyautogui.click(475, 339)
                    sleep(3)
                    pyautogui.click(470, 440)
                    sleep(2)
                    auto_play()
        elif odin[1].isActive == True:
            #상급, 최상급 퀘스트만 선택
            while True:
                level_1 = pyautogui.locateOnScreen('image\\town_request\\level_1.jpg', confidence=0.8, region=(1190, 100, 60, 60))
                level_2 = pyautogui.locateOnScreen('image\\town_request\\level_2.jpg', confidence=0.8, region=(1190, 100, 60, 60))
                level_3 = pyautogui.locateOnScreen('image\\town_request\\level_3.jpg', confidence=0.8, region=(1190, 100, 60, 60))
                level_1_nb = pyautogui.locateOnScreen('image\\town_request\\level_1_nb.jpg', confidence=0.8, region=(1190, 100, 60, 60))
                level_2_nb = pyautogui.locateOnScreen('image\\town_request\\level_2_nb.jpg', confidence=0.8, region=(1190, 100, 60, 60))
                level_3_nb = pyautogui.locateOnScreen('image\\town_request\\level_3_nb.jpg', confidence=0.8, region=(1190, 100, 60, 60))
                gold_change = pyautogui.locateOnScreen('image\\town_request\\gold_change.jpg', confidence=0.8, region=(1090, 460, 70, 70))
                gold_change_2 = pyautogui.locateOnScreen('image\\town_request\\gold_change_2.jpg', confidence=0.8, region=(1090, 460, 70, 70))
                print('데스크탑 이미지 인식 ', level_1, level_2, level_3)
                print('노트북 이미지 인식 및 골드 표시 인식', level_1_nb, level_2_nb, level_3_nb, gold_change)
                if level_1 or level_2 or level_3 or level_1_nb or level_2_nb or level_3_nb:
                    if level_2 or level_3 or level_2_nb or level_3_nb:
                        pyautogui.click(1851, 496)
                        sleep(1)
                    if level_1:
                        if gold_change or gold_change_2:
                            pyautogui.click(gold_change)
                            sleep(2)
                            pyautogui.click(1495, 347)
                            sleep(3)
                        else:
                            pyautogui.click(1851, 496)
                            sleep(1)
                    max_request = pyautogui.locateOnScreen('image\\town_request\\max_request.jpg', confidence=0.8, region=(960, 0, 960, 540))
                    no_more_request = pyautogui.locateOnScreen('image\\town_request\\no_more_request.jpg', confidence=0.8, region=(960, 0, 960, 540))
                    if  no_more_request:
                        print('오딘2 - 마을 의뢰 가득참')
                        pyautogui.moveTo(1080, 430)
                        pyautogui.dragTo(1080, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.8, region=(1130, 150, 70, 310))
                        if request_ok:
                            pyautogui.click(request_ok)
                            sleep(1)
                            pyautogui.click(1636, 496)
                            sleep(3)
                            auto_play()
                            break
                        else:
                            main_back()
                            sleep(3)
                            auto_play()
                            break
                    if max_request:
                        print('오딘2 - 일일 마을 의뢰 완료')
                        return 1
                        pyautogui.moveTo(1080, 430)
                        pyautogui.dragTo(1080, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.8, region=(1130, 150, 70, 310))
                        if request_ok:
                            pyautogui.click(request_ok)
                            sleep(1)
                            pyautogui.click(1636, 496)
                            sleep(3)
                            auto_play()
                            break
                        else:
                            main_back()
                            sleep(3)
                            auto_play()
                            break
                else:
                    # 의뢰 수령 중에 완료된 경우가 있는 경우
                    main_back()
                    pyautogui.click(1435, 339)
                    sleep(3)
                    pyautogui.click(1430, 440)
                    sleep(2)
                    auto_play()

    town_request_get_reward()
    town_request_level_confirm()

get_mecro()

# 정예던전 시작(이벤트 던전 포함 현재 3개)
# 캐릭1번
# active_mecro_1()
# disable_sleep_mode()
# char_change(1)
# go_town()
# elite_dg_entrance(3, 5, 5)
# active_mecro_2()
# disable_sleep_mode()
# char_change(1)
# go_town()
# elite_dg_entrance(3, 5, 5)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(3, 5, 5)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(3, 5, 5)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(3, 5, 5)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(3, 5, 5)

# sleep(3660)

# # 캐릭2번
# active_mecro_1()
# disable_sleep_mode()
# char_change(2)
# go_town()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# char_change(2)
# go_town()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# # 캐릭3번
# active_mecro_1()
# disable_sleep_mode()
# char_change(3)
# go_town()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# char_change(3)
# go_town()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# # 캐릭4번
# active_mecro_1()
# disable_sleep_mode()
# char_change(4)
# go_town()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# char_change(4)
# go_town()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# # 캐릭5번
# active_mecro_1()
# disable_sleep_mode()
# char_change(5)
# go_town()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# char_change(5)
# go_town()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# active_mecro_1()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)
# active_mecro_2()
# disable_sleep_mode()
# elite_dg_entrance(1, 1, 1)

# sleep(3660)

# 마을 의뢰 시작
#캐릭1번 
active_mecro_1()
disable_sleep_mode()
char_change(1)
go_town()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
char_change(1)
go_town()
town_request()
sleep(2000)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

#캐릭2번
active_mecro_1()
disable_sleep_mode()
char_change(2)
go_town()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
char_change(2)
go_town()
town_request()
sleep(2000)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

#캐릭3번
active_mecro_1()
disable_sleep_mode()
char_change(3)
go_town()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
char_change(3)
go_town()
town_request()
sleep(2000)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

#캐릭4번
active_mecro_1()
disable_sleep_mode()
char_change(4)
go_town()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
char_change(4)
go_town()
town_request()
sleep(2000)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

#캐릭5번
active_mecro_1()
disable_sleep_mode()
char_change(5)
go_town()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
char_change(5)
go_town()
town_request()
sleep(2000)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

# 1번 캐릭터로 복귀 후 첫번째 저장된 위치 사냥
sleep(10)
active_mecro_1() # ODIN1 WINDOW
main_back()
char_change(1)
pyautogui.click(981, 137)
sleep(2)
pyautogui.click(1173, 189)
sleep(5)
pyautogui.press('g')

sleep(10)
active_mecro_2() # ODIN2 WINDOW
main_back()
char_change(1)
pyautogui.click(981, 137)
sleep(2)
pyautogui.click(1173, 189)
sleep(5)
pyautogui.press('g')