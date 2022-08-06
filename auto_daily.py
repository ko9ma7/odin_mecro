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
        back_click = pyautogui.locateOnScreen('image\\main_back.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if back_click:
            pyautogui.click(back_click)
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
            sleep(15)
        else: 
            print('마을이거나 귀환 불가 지역')
        pyautogui.press('4')
        sleep(15)
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
            sleep(15)
        else: 
            print('마을이거나 귀환 불가 지역')
        pyautogui.press('4')
        sleep(15)
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

        print(auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8)
        if auto_1:
            pyautogui.click(auto_1)
        if auto_2:
            pyautogui.click(auto_2)
        if auto_3:
            pyautogui.click(auto_3)
        if auto_4:
            pyautogui.click(auto_4)
        if auto_5:
            pyautogui.click(auto_5)
        if auto_6:
            pyautogui.click(auto_6)
        if auto_7:
            pyautogui.click(auto_7)
        if auto_8:
            pyautogui.click(auto_8)

    elif odin[1].isActive == True:
        auto_1 = pyautogui.locateOnScreen('image\\auto_play\\auto_1.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_2 = pyautogui.locateOnScreen('image\\auto_play\\auto_2.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_3 = pyautogui.locateOnScreen('image\\auto_play\\auto_3.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_4 = pyautogui.locateOnScreen('image\\auto_play\\auto_4.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_5 = pyautogui.locateOnScreen('image\\auto_play\\auto_5.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_6 = pyautogui.locateOnScreen('image\\auto_play\\auto_6.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_7 = pyautogui.locateOnScreen('image\\auto_play\\auto_7.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_8 = pyautogui.locateOnScreen('image\\auto_play\\auto_8.jpg', confidence=0.8, region=(960, 0, 960, 540))

        print(auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8)
        if auto_1:
            pyautogui.click(auto_1)
        if auto_2:
            pyautogui.click(auto_2)
        if auto_3:
            pyautogui.click(auto_3)
        if auto_4:
            pyautogui.click(auto_4)
        if auto_5:
            pyautogui.click(auto_5)
        if auto_6:
            pyautogui.click(auto_6)
        if auto_7:
            pyautogui.click(auto_7)
        if auto_8:
            pyautogui.click(auto_8)

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
        sleep(5)
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
        sleep(7)                    
    elif odin[1].isActive == True:
        pyautogui.press('o')
        sleep(2)
        pyautogui.click(1760, 395)
        sleep(2)
        pyautogui.click(1488, 331)
        sleep(5)
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
        sleep(15)

# 정예던전 입장
# chioce_dg : 1 - 이벤트 던전, 2 - 공허의 유적, 3 - 난쟁이 비밀통로, 4 - 지하감옥
# chioce_level : 1단계, 2단계, 3단계, 4단계 ~~~ (층 또는 단계 숫자로 입력)
# 던전 입장 가능한지 체크 안됨 - 추후 개발할까?
def elite_dg_entrance(chioce_dg, choice_level):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        sleep(1)
        pyautogui.press('F8')
        sleep(2)
        e_dg = pyautogui.locateOnScreen('image\elite_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
        print(e_dg)
        pyautogui.click(e_dg)
        if chioce_dg == 1:
            e_dg = pyautogui.locateOnScreen('image\event_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            sleep(1)
            # 던전 못 찾을 경우 옆으로 드레그
            if e_dg is None:
                pyautogui.moveTo(480, 270)
                pyautogui.dragTo(280, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\event_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            # 던전 난이도 클릭 및 사냥시작
            if choice_level == 1:
                pyautogui.click(120, 93)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(112, 129)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(111, 181)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(111, 222)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
        elif chioce_dg == 2:
            e_dg = pyautogui.locateOnScreen('image\gold_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            sleep(1)
            if e_dg is None:
                pyautogui.moveTo(480, 270)
                pyautogui.dragTo(280, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\gold_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            # 던전 난이도 클릭 및 사냥시작
            if choice_level == 1:
                pyautogui.click(120, 93)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(112, 129)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(111, 181)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(111, 222)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 5:
                pyautogui.click(117, 258)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 6:
                pyautogui.click(127, 304)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
        elif chioce_dg == 3:
            e_dg = pyautogui.locateOnScreen('image\inchant_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            sleep(1)
            if e_dg is None:
                pyautogui.moveTo(480, 270)
                pyautogui.dragTo(280, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\inchant_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            # 던전 난이도 클릭 및 사냥시작
            if choice_level == 1:
                pyautogui.click(120, 93)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(112, 129)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(111, 181)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(111, 222)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 5:
                pyautogui.click(117, 258)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 6:
                pyautogui.click(127, 304)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
        elif chioce_dg == 4:
            e_dg = pyautogui.locateOnScreen('image\down_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
            sleep(1)
            if e_dg is None:
                pyautogui.moveTo(480, 270)
                pyautogui.dragTo(280, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\down_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            # 던전 난이도 클릭 및 사냥시작
            if choice_level == 1:
                pyautogui.click(120, 93)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(112, 129)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(111, 181)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(111, 222)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 5:
                pyautogui.click(117, 258)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 6:
                pyautogui.click(127, 304)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 7:
                pyautogui.click(103, 344)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 8:
                pyautogui.click(110, 389)
                sleep(2)
                pyautogui.click(880, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
    elif odin[1].isActive == True:
        sleep(1)
        pyautogui.press('F8')
        sleep(2)
        e_dg = pyautogui.locateOnScreen('image\elite_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
        print(e_dg)
        pyautogui.click(e_dg)
        if chioce_dg == 1:
            e_dg = pyautogui.locateOnScreen('image\event_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            sleep(1)
            # 던전 못 찾을 경우 옆으로 드레그
            if e_dg is None:
                pyautogui.moveTo(1440, 270)
                pyautogui.dragTo(1240, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\event_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            if choice_level == 1:
                pyautogui.click(1081, 92)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(1072, 129)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(1072, 181)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(1072, 222)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
        elif chioce_dg == 2:
            e_dg = pyautogui.locateOnScreen('image\gold_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            sleep(1)
            if e_dg is None:
                pyautogui.moveTo(1440, 270)
                pyautogui.dragTo(1240, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\gold_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            if choice_level == 1:
                pyautogui.click(1072, 93)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(1072, 129)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(1072, 181)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(1072, 222)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 5:
                pyautogui.click(1072, 258)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 6:
                pyautogui.click(1072, 304)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 7:
                pyautogui.click(1072, 344)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 8:
                pyautogui.click(1072, 389)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
        elif chioce_dg == 3:
            e_dg = pyautogui.locateOnScreen('image\inchant_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            sleep(1)
            if e_dg is None:
                pyautogui.moveTo(1440, 270)
                pyautogui.dragTo(1240, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\inchant_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            if choice_level == 1:
                pyautogui.click(1072, 93)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(1072, 129)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(1072, 181)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(1072, 222)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 5:
                pyautogui.click(1072, 258)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 6:
                pyautogui.click(1072, 304)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 7:
                pyautogui.click(1072, 344)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 8:
                pyautogui.click(1072, 389)
                sleep(2)
                pyautogui.click(1840, 482)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
        elif chioce_dg == 4:
            e_dg = pyautogui.locateOnScreen('image\down_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
            sleep(1)
            if e_dg is None:
                pyautogui.moveTo(1440, 270)
                pyautogui.dragTo(1240, 270, 2, button='left')
                e_dg = pyautogui.locateOnScreen('image\down_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
                sleep(1)
            print(e_dg)
            pyautogui.click(e_dg)
            sleep(1)
            if choice_level == 1:
                pyautogui.click(1081, 92)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 2:
                pyautogui.click(1075, 138)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 3:
                pyautogui.click(1067, 176)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 4:
                pyautogui.click(1060, 220)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 5:
                pyautogui.click(1066, 260)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 6:
                pyautogui.click(1067, 305)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 7:
                pyautogui.click(1068, 342)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')
            if choice_level == 8:
                pyautogui.click(1060, 386)
                sleep(2)
                pyautogui.click(1836, 488)
                sleep(20)
                pyautogui.press('F5')
                sleep(10)
                pyautogui.press('g')

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
                level_1 = pyautogui.locateOnScreen('image\\town_request\\level_1.jpg', confidence=0.9, region=(230, 100, 60, 60))
                level_2 = pyautogui.locateOnScreen('image\\town_request\\level_2.jpg', confidence=0.9, region=(230, 100, 60, 60))
                level_3 = pyautogui.locateOnScreen('image\\town_request\\level_3.jpg', confidence=0.9, region=(230, 100, 60, 60))
                gold_change = pyautogui.locateOnScreen('image\\town_request\\gold_change.jpg', confidence=0.9, region=(130, 460, 70, 70))
                if level_1 or level_2 or level_3:
                    if level_2 or level_3:
                        pyautogui.click(891, 496)
                        sleep(1)
                    if level_1:
                        if gold_change:
                            pyautogui.click(gold_change)
                            sleep(2)
                            pyautogui.click(535, 347)
                            sleep(3)
                        else:
                            pyautogui.click(891, 496)
                            sleep(1)
                    max_request = pyautogui.locateOnScreen('image\\town_request\\max_request.jpg', confidence=0.9, region=(0, 0, 960, 540))
                    no_more_request = pyautogui.locateOnScreen('image\\town_request\\no_more_request.jpg', confidence=0.9, region=(0, 0, 960, 540))
                    if  no_more_request:
                        print('오딘1 - 마을 의뢰 가득참')
                        pyautogui.moveTo(120, 430)
                        pyautogui.dragTo(120, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.9, region=(170, 150, 70, 310))
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
                        print('오딘1 - 하루 마을 의뢰 완료')
                        pyautogui.moveTo(120, 430)
                        pyautogui.dragTo(120, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.9, region=(170, 150, 70, 310))
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
                    pyautogui.click(475, 339)
                    sleep(3)
                    pyautogui.click(470, 440)
                    sleep(2)
        elif odin[1].isActive == True:
            #상급, 최상급 퀘스트만 선택
            while True:
                level_1 = pyautogui.locateOnScreen('image\\town_request\\level_1.jpg', confidence=0.9, region=(1190, 100, 60, 60))
                level_2 = pyautogui.locateOnScreen('image\\town_request\\level_2.jpg', confidence=0.9, region=(1190, 100, 60, 60))
                level_3 = pyautogui.locateOnScreen('image\\town_request\\level_3.jpg', confidence=0.9, region=(1190, 100, 60, 60))
                gold_change = pyautogui.locateOnScreen('image\\town_request\\gold_change.jpg', confidence=0.9, region=(1090, 460, 70, 70))
                if level_1 or level_2 or level_3:
                    if level_2 or level_3:
                        pyautogui.click(1851, 496)
                        sleep(1)
                    if level_1:
                        if gold_change:
                            pyautogui.click(gold_change)
                            sleep(2)
                            pyautogui.click(1495, 347)
                            sleep(3)
                        else:
                            pyautogui.click(1851, 496)
                            sleep(1)
                    max_request = pyautogui.locateOnScreen('image\\town_request\\max_request.jpg', confidence=0.9, region=(960, 0, 960, 540))
                    no_more_request = pyautogui.locateOnScreen('image\\town_request\\no_more_request.jpg', confidence=0.9, region=(960, 0, 960, 540))
                    if  no_more_request:
                        print('오딘2 - 마을 의뢰 가득참')
                        pyautogui.moveTo(1080, 430)
                        pyautogui.dragTo(1080, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.9, region=(1130, 150, 70, 310))
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
                        print('오딘2 - 하루 마을 의뢰 완료')
                        pyautogui.moveTo(1080, 430)
                        pyautogui.dragTo(1080, 100, 3, button='left')
                        sleep(2)
                        request_ok = pyautogui.locateOnScreen('image\\town_request\\request_ok.jpg', confidence=0.9, region=(1130, 150, 70, 310))
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
                    pyautogui.click(1435, 339)
                    sleep(3)
                    pyautogui.click(1430, 440)
                    sleep(2)

    town_request_get_reward()
    town_request_level_confirm()



get_mecro()

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
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)


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
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)


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
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)


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
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)


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
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)

active_mecro_1()
disable_sleep_mode()
town_request()
sleep(2)
active_mecro_2()
disable_sleep_mode()
town_request()
sleep(1200)