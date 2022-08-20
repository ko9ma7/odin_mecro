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
        try:
            pywinauto.application.Application().connect(handle=odin[0]._hWnd).top_window().set_focus()
            odin[0].resizeTo(974, 527)  # 창 사이즈 (변경금지)
            odin[0].moveTo(-7, 0)       # 창 위치 (변경금지)
            odin[0].activate()
        except:
            print('1번 프로그램 활성화 오류')

# 2번 프로그램 활성화
def active_mecro_2():
    if odin[1].isActive == False:
        try:
            pywinauto.application.Application().connect(handle=odin[1]._hWnd).top_window().set_focus()
            odin[1].resizeTo(974, 527)  # 창 사이즈 (변경금지)
            odin[1].moveTo(953, 0)      # 창 위치(변경금지)
            odin[1].activate()
        except:
            print('2번 프로그램 활성화 오류')

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
        else:
            return 1

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
        else:
            return 1

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

# 이미지 체크 - 화면 전체
def image_check(jpg_image):
    if odin[0].isActive == True:
        image = pyautogui.locateOnScreen('image\\' + jpg_image + '.jpg', grayscale=True, confidence=0.9, region=(0, 0, 960, 540))
    if odin[1].isActive == True:
        image = pyautogui.locateOnScreen('image\\' + jpg_image + '.jpg', grayscale=True, confidence=0.9, region=(960, 0, 960, 540))
    return image

# 이미지 체크 - 마을의뢰 > 왼쪽 상단 리스트
def tr_image_check(jpg_image):
    if odin[0].isActive == True:
        image = pyautogui.locateOnScreen('image\\' + jpg_image + '.jpg', grayscale=True, confidence=0.8, region=(0, 100, 50, 50))
    if odin[1].isActive == True:
        image = pyautogui.locateOnScreen('image\\' + jpg_image + '.jpg', grayscale=True, confidence=0.8, region=(960, 100, 50, 50))
    return image    

# 던전 난이도 1, 2, 3 = 1단계, 2단계, 3단계
def dg_level_choice(dg_level):
    sleep(2)
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

# 각 던전 위치 (1~4, 좌측부터)
def where_dg(dg_location):
    if odin[0].isActive == True:
        if dg_location == 1:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(18, 319, 220, 120))
        if dg_location == 2:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(248, 319, 220, 120))
        if dg_location == 3:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(478, 319, 220, 120))
        if dg_location == 4:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(708, 319, 220, 120))
    if odin[1].isActive == True:
        if dg_location == 1:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(978, 319, 220, 120))
        if dg_location == 2:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(1208, 319, 220, 120))
        if dg_location == 3:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(1438, 319, 220, 120))
        if dg_location == 4:
            location = pyautogui.locateOnScreen('image\\dg_time.jpg', confidence=0.8, region=(1668, 319, 220, 120))
    return location
        
# 맵 체크 - 던전인지 아닌지
def dg_map_check():
    pyautogui.press('m')
    sleep(3)
    if odin[0].isActive == True:
        image = pyautogui.locateOnScreen('image\\map_check.jpg', grayscale=True, confidence=0.8, region=(0, 0, 960, 540)) 
        if image:
            pyautogui.press('m')
        else:
            main_back()
    if odin[1].isActive == True:
        image = pyautogui.locateOnScreen('image\\map_check.jpg', grayscale=True, confidence=0.8, region=(960, 0, 960, 540)) 
        if image:
            pyautogui.press('m')
        else:
            main_back()
    return image      

# 1번 저장된 위치 이동 사냥 (field_play 메소드 연계)
def favorite_go():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        print('오딘1 - 즐겨찾기 1번으로 이동 후 자동사냥 실시')
        pyautogui.press('v')
        sleep(2)
        pyautogui.click(212, 183) # 1번 저장된 위치 이동
        sleep(10)
        pyautogui.press('g')
    if odin[1].isActive == True:
        print('오딘2 - 즐겨찾기 1번으로 이동 후 자동사냥 실시')
        pyautogui.press('v')
        sleep(2)
        pyautogui.click(1172, 183) # 1번 저장된 위치 이동
        sleep(10)
        pyautogui.press('g')

# 미미르 샘물 먹기
def mimir_eat():
    sleep(1)
    main_back()
    i = 0 # 미미르 5개까지 먹기 위해 변수
    if odin[0].isActive == True:
        while True:
            pyautogui.press('f4')
            print('오딘1 - 미미르 샘물 냠냠')
            sleep(2)
            i = i + 1
            mimir_check = image_check('mimir_cancel')
            if mimir_check:
                print('오딘1 - 미미르 샘물 가득찼다. 그만 먹자')
                sleep(1)
                pyautogui.click(mimir_check)
                break
            if i > 5:
                break
    if odin[1].isActive == True:
        while True:
            pyautogui.press('f4')
            print('오딘2 - 미미르 샘물 냠냠')
            sleep(2)
            i = i + 1
            mimir_check = image_check('mimir_cancel')
            if mimir_check:
                print('오딘2 - 미미르 샘물 가득찼다. 그만 먹자')
                sleep(1)
                pyautogui.click(mimir_check)
                break
            if i > 5:
                break

# 우편물 받기
def get_post():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('f7')
        sleep(2)
        pyautogui.click(895, 496) # 모두 받기
        sleep(2)
        mimir_check = image_check('mimir_cancel')
        if mimir_check:
            print('오딘1 - 우편 미미르 샘물이 많다. 나중에 받자')
            sleep(1)
            pyautogui.click(mimir_check)
            sleep(2)
        pyautogui.click(173, 84) # 계정 우편 탭
        sleep(2)
        pyautogui.click(895, 496) # 모두 받기
        main_back()
    if odin[1].isActive == True:
        pyautogui.press('f7')
        sleep(2)
        pyautogui.click(1855, 496) # 모두 받기
        sleep(2)
        mimir_check = image_check('mimir_cancel')
        if mimir_check:
            print('오딘2 - 우편 미미르 샘물이 많다. 나중에 받자')
            sleep(1)
            pyautogui.click(mimir_check)
            sleep(2)
        pyautogui.click(1133, 84) # 계정 우편 탭
        sleep(2)
        pyautogui.click(1855, 496) # 모두 받기
        main_back()

# 일일 골드 상품 구매
def daily_gold_item():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('u')
        print('오딘1 - 캐쉬 페이지 이동')
        sleep(3)
        pyautogui.click(64, 436) # 일괄 구매 
        confirm = image_check('confirm') # 이미지 다시 찍어야 함 다 받아서 얼럿 창을 못봄
        if confirm:
            pyautogui.click(confirm) # 팝업 골드 구매 클릭
            print('오딘1 - 골드 상품 일괄 구매 완료')
            sleep(2)
        else:
            print('오딘1 - 골드 상품 구매했거나, 구매할 수 없는 상태')
        main_back()
    if odin[1].isActive == True:
        pyautogui.press('u')
        print('오딘2 - 캐쉬 페이지 이동')
        sleep(3)
        pyautogui.click(1024, 436) # 일괄 구매 
        confirm = image_check('confirm') # 이미지 다시 찍어야 함 다 받아서 얼럿 창을 못봄
        if confirm:
            pyautogui.click(confirm) # 팝업 골드 구매 클릭
            print('오딘2 - 골드 상품 일괄 구매 완료')
            sleep(2)
        else:
            print('오딘2 - 골드 상품 구매했거나, 구매할 수 없는 상태')
        main_back()

# 길드 출석 체크 및 주화 사기
def guild_check():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('f6')
        print('오딘1 - 길드 페이지 이동')
        sleep(5)
        pyautogui.click(470, 350) # 아무대나 클릭 (출석보상 보상 화면)
        sleep(2)
        pyautogui.click(139, 86) # 길드 정보 탭
        print('오딘1 - 길드 정보 탭 이동')
        sleep(2)
        guild_gibu = image_check('guild_gibu')
        if guild_gibu:
            print('오딘1 - 길드 기부 시작')
            pyautogui.click(325, 465) # 골드 기부
            sleep(3)
            pyautogui.click(325, 465) # 아무대나 클릭
            sleep(3)
            pyautogui.click(325, 465) # 골드 기부
            sleep(3)
            pyautogui.click(325, 465) # 아무대나 클릭
            sleep(3)
            pyautogui.click(325, 465) # 골드 기부
            sleep(3)
            pyautogui.click(325, 465) # 아무대나 클릭
            sleep(3)
            main_back()
        else:
            print('오딘1 - 길드 가입 안했거나, 이미 기부한 상태')
            main_back()
            pass
    if odin[1].isActive == True:
        pyautogui.press('f6')
        print('오딘2 - 길드 페이지 이동')
        sleep(5)
        pyautogui.click(1430, 350) # 아무대나 클릭 (출석보상 보상 화면)
        sleep(2)
        pyautogui.click(1099, 86) # 길드 정보 탭
        print('오딘2 - 길드 정보 탭 이동')
        sleep(2)
        guild_gibu = image_check('guild_gibu')
        if guild_gibu:
            print('오딘2 - 길드 기부 시작')
            pyautogui.click(1285, 465) # 골드 기부
            sleep(3)
            pyautogui.click(1285, 465) # 아무대나 클릭
            sleep(3)
            pyautogui.click(1285, 465) # 골드 기부
            sleep(3)
            pyautogui.click(1285, 465) # 아무대나 클릭
            sleep(3)
            pyautogui.click(1285, 465) # 골드 기부
            sleep(3)
            pyautogui.click(1285, 465) # 아무대나 클릭
            sleep(3)
            main_back()
        else:
            print('오딘2 - 길드 가입 안했거나, 이미 기부한 상태')
            main_back()
            pass

# 아이템 일괄 분해
def item_bunhae():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('i')
        sleep(2)
        pyautogui.click(740, 490) # 일괄 분해
        sleep(2)
        pyautogui.click(908, 495) # 분해
        sleep(2)
        bunhae_confirm = image_check('bunhae_confirm')
        if bunhae_confirm:
            print('오딘1 - 분해 아이템 있음')
            pyautogui.click(bunhae_confirm) # 분해 확인
            sleep(3)
            pyautogui.click(470, 350) # 아무대나 클릭 (분해 확인 창)
            sleep(2)
            main_back()
            pass
        else:
            print('오딘1 - 분해 아이템 없음')
            sleep(2)
            main_back()
    if odin[1].isActive == True:
        pyautogui.press('i')
        sleep(2)
        pyautogui.click(1700, 490) # 일괄 분해
        sleep(2)
        pyautogui.click(1868, 495) # 분해
        sleep(2)
        bunhae_confirm = image_check('bunhae_confirm')
        if bunhae_confirm:
            print('오딘2 - 분해 아이템 있음')
            pyautogui.click(bunhae_confirm) # 분해 확인
            sleep(3)
            pyautogui.click(1430, 350) # 아무대나 클릭 (분해 확인 창)
            sleep(2)
            main_back()
            pass
        else:
            print('오딘2 - 분해 아이템 없음')
            sleep(2)
            main_back()

# 이벤트 던전 입장
def event_dg_entrance(dg_level):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘1 - 이벤트 던전 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)
            #던전 체크
            event_dg = image_check('event_dg')
            if event_dg:
                print('오딘1 - 이벤트 던전 확인됨')
                dg_time = where_dg(1) # 1번 = 이벤트던전
                if dg_time:
                    print('오딘1 - 이벤트 던전 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘1 - 이벤트 던전 시작함')
                    pyautogui.click(event_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1
    if odin[1].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘2 - 이벤트 던전 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)
            #던전 체크
            event_dg = image_check('event_dg')
            sleep(2)
            if event_dg:
                print('오딘2 - 이벤트 던전 확인됨')
                dg_time = where_dg(1) # 1번 = 이벤트던전
                if dg_time:
                    print('오딘2 - 이벤트 던전 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘2 - 이벤트 던전 시작함')
                    pyautogui.click(event_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1

# 머니 던전 입장
def money_dg_entrance(dg_level):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘1 - 머니 던전 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)
            #던전 체크
            money_dg = image_check('money_dg')
            sleep(2)
            if money_dg:
                print('오딘1 - 머니 던전 확인됨')
                dg_time = where_dg(3) # 3번 = 머니던전
                if dg_time:
                    print('오딘1 - 머니 던전 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘1 - 머니 던전 시작함')
                    pyautogui.click(money_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1
    if odin[1].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘2 - 머니 던전 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)
            #던전 체크
            money_dg = image_check('money_dg')
            sleep(2)
            if money_dg:
                print('오딘2 - 머니 던전 확인됨')
                dg_time = where_dg(3) # 3번 = 머니던전
                if dg_time:
                    print('오딘2 - 머니 던전 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘2 - 머니 던전 시작함')
                    pyautogui.click(money_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1

# 스크롤 던전 입장
def scroll_dg_entrance(dg_level):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘1 - 스크롤 던전 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)
            #던전 체크
            scroll_dg = image_check('scroll_dg')
            sleep(2)
            if scroll_dg:
                print('오딘1 - 스크롤 던전 확인됨')
                dg_time = where_dg(4) # 4번 = 스크롤던전
                if dg_time:
                    print('오딘1 - 스크롤 던전 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘1 - 스크롤 던전 시작함')
                    pyautogui.click(scroll_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1
    if odin[1].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘2 - 스크롤 던전 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)
            #던전 체크
            scroll_dg = image_check('scroll_dg')
            sleep(2)
            if scroll_dg:
                print('오딘2 - 스크롤 던전 확인됨')
                dg_time = where_dg(4) # 4번 = 스크롤던전
                if dg_time:
                    print('오딘2 - 스크롤 던전 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘2 - 스크롤 던전 시작함')
                    pyautogui.click(scroll_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1

# 지하감옥 입장
def week_dg_entrance(dg_level):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘1 - 지하감옥 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)
            #던전 체크 - 지하감옥은 드래그가 필요(이벤트 던전 때문에)
            pyautogui.moveTo(640, 260)
            pyautogui.dragTo(340, 260, 3, button='left')
            sleep(1)
            week_dg = image_check('week_dg')
            sleep(2)
            if week_dg:
                print('오딘1 - 지하감옥 확인됨')
                dg_time = where_dg(4) # 4번 = 지하감옥(드래그했기 때문에 4번임)
                if dg_time:
                    print('오딘1 - 지하감옥 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘1 - 지하감옥 시작함')
                    pyautogui.click(week_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1
    if odin[1].isActive == True:
        dmc = dg_map_check()
        if dmc:
            print('오딘2 - 지하감옥 플레이 중 .. ')
            auto_play()
            pass
        else:
            sleep(1)
            pyautogui.press('F8')
            sleep(2)
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)
            #던전 체크 - 지하감옥은 드래그가 필요(이벤트 던전 때문에)
            pyautogui.moveTo(1600, 260)
            pyautogui.dragTo(1300, 260, 3, button='left')
            sleep(1)
            week_dg = image_check('week_dg')
            sleep(2)
            if week_dg:
                print('오딘2 - 지하감옥 확인됨')
                dg_time = where_dg(4) # 4번 = 지하감옥(드래그했기 때문에 4번임)
                if dg_time:
                    print('오딘2 - 지하감옥 시간 없음, 게임화면으로 이동')
                    main_back()
                    return 1
                else:
                    print('오딘2 - 지하감옥 시작함')
                    pyautogui.click(week_dg) 
                    dg_level_choice(dg_level)
            else:
                return 1

# 저장된 위치 1번 사냥터 자동사냥
def field_play():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        auto_status = auto_play() # 자동샤냥 중인지 체크
        if auto_status == 1: # 1이면 자동사냥 중
            print('오딘1 - 자동 사냥 중.....')
            pass
        else:
            print('오딘1 - 놀고 있음 사냥터 이동')
            favorite_go() # 자동사냥 중 아니면 즐겨찾기 1번 이동 및 자동사냥
    if odin[1].isActive == True:
        auto_status = auto_play()
        if auto_status == 1:
            print('오딘2 - 자동 사냥 중.....')
            pass
        else:
            print('오딘2 - 놀고 있음 사냥터 이동')
            favorite_go()

#사용안함 - 구버전
def elite_dg_entrance(event_dg_level, money_dg_level, scroll_dg_level):
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

# 마을의뢰 - 상급 및 최상급 의뢰만 진행하며, 골드로만 갱신함
def town_request():
    sleep(1)
    main_back()
    sleep(1)
    pyautogui.press('j')
    if odin[0].isActive == True:
        while True:
            # 마을의뢰 완료 이미지는 변동형이라 3번 체크
            check_atr = tr_image_check('request_reward')
            if check_atr is None:
                sleep(0.5)
                check_atr = tr_image_check('request_reward')
            if check_atr is None:
                sleep(0.5)
                check_atr = tr_image_check('request_reward')
            tr_level_1 = tr_image_check('tr_level_1') # 보통의뢰
            tr_level_2 = tr_image_check('tr_level_2') # 상급의뢰
            tr_level_3 = tr_image_check('tr_level_3') # 최상급의뢰
            gold_change = image_check('gold_change')  # 골드 새로고침 체크
            gold_change_2 = image_check('gold_change_2') # 골드 새로고침 체크 - 노트북 호환
            sleep(1)
            # 마을의뢰 완료 체크 보상받기
            if check_atr:
                print('오딘1 - 완료한 마을의뢰 있음')
                pyautogui.click(901, 496)
                sleep(4)
                pyautogui.click(475, 339)
                sleep(3)
                pyautogui.click(470, 440)
                sleep(2)
            elif tr_level_2:
                pyautogui.click(891, 496) # 상급의뢰 수락하기
            elif tr_level_3:
                pyautogui.click(891, 496) # 최상급의뢰 수락하기
            elif tr_level_1:
                if gold_change or gold_change_2:
                    pyautogui.click(122, 497) # 보통 마을의뢰 골드 새로고침
                    sleep(2)
                    pyautogui.click(535, 347)
                    sleep(3)
                else:
                    pyautogui.click(891, 496) # 골드 새로고침 소진 시 보통의뢰 수락하기

            # 마을의뢰 완료 체크 여부
            sleep(1) # 1초 딜레이 줘야 인식 가능
            max_request = image_check('max_request')
            no_more_request = image_check('no_more_request')
            if max_request or no_more_request:
                print('오딘1 - 더이상 마을의뢰를 받을 수 없습니다.')
                pyautogui.moveTo(120, 430) # 의뢰 리스트로 이동
                pyautogui.dragTo(120, 100, 3, button='left') # 하단 드래그 - 수락함 있는지 체크
                sleep(2)
                request_ok = image_check('request_ok')
                if request_ok:
                    print('오딘1 - 남은 마을의뢰 진행')
                    pyautogui.click(request_ok) # 수락함 체크
                    sleep(1)
                    pyautogui.click(676, 496)
                    break
                else:
                    main_back()
                    print('오딘1 - 마을의뢰 완료')
                    return 1
                    break
    elif odin[1].isActive == True:
        while True:
            # 마을의뢰 완료 이미지는 변동형이라 3번 체크
            check_atr = tr_image_check('request_reward')
            if check_atr is None:
                sleep(0.5)
                check_atr = tr_image_check('request_reward')
            if check_atr is None:
                sleep(0.5)
                check_atr = tr_image_check('request_reward')
            tr_level_1 = tr_image_check('tr_level_1') # 보통의뢰
            tr_level_2 = tr_image_check('tr_level_2') # 상급의뢰
            tr_level_3 = tr_image_check('tr_level_3') # 최상급의뢰
            gold_change = image_check('gold_change')  # 골드 새로고침 체크
            gold_change_2 = image_check('gold_change_2') # 골드 새로고침 체크 - 노트북 호환
            sleep(1)
            # 마을의뢰 완료 체크 보상받기
            if check_atr:
                print('오딘2 - 완료한 마을의뢰 있음')
                pyautogui.click(1861, 496)
                sleep(4)
                pyautogui.click(1435, 339)
                sleep(3)
                pyautogui.click(1430, 440)
                sleep(2)
            elif tr_level_2:
                pyautogui.click(1851, 496) # 상급의뢰 수락하기
            elif tr_level_3:
                pyautogui.click(1851, 496) # 최상급의뢰 수락하기
            elif tr_level_1:
                if gold_change or gold_change_2:
                    pyautogui.click(1082, 497) # 보통 마을의뢰 골드 새로고침
                    sleep(2)
                    pyautogui.click(1495, 347)
                    sleep(3)
                else:
                    pyautogui.click(1851, 496) # 골드 새로고침 소진 시 보통의뢰 수락하기

            # 마을의뢰 완료 체크 여부
            sleep(1) # 1초 딜레이 줘야 인식 가능
            max_request = image_check('max_request')
            no_more_request = image_check('no_more_request')
            if max_request or no_more_request:
                print('오딘2 - 더이상 마을의뢰를 받을 수 없습니다.')
                pyautogui.moveTo(1080, 430) # 의뢰 리스트로 이동
                pyautogui.dragTo(1080, 100, 3, button='left') # 하단 드래그 - 수락함 있는지 체크
                sleep(2)
                request_ok = image_check('request_ok')
                if request_ok:
                    print('오딘2 - 남은 마을의뢰 진행')
                    pyautogui.click(request_ok) # 수락함 체크
                    sleep(1)
                    pyautogui.click(1636, 496)
                    break
                else:
                    main_back()
                    print('오딘2 - 마을의뢰 완료')
                    return 1
                    break


