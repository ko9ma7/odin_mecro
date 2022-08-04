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

# 메인화면 백 버튼 클릭
def main_back():
    sleep(1)
    if odin[0].isActive == True:
        back_click = pyautogui.locateOnScreen('image\main_back.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if back_click is not None:
            pyautogui.click(back_click)

    elif odin[1].isActive == True:
        back_click = pyautogui.locateOnScreen('image\main_back.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if back_click is not None:
            pyautogui.click(back_click)

# 뒤로가기 버튼 클릭
def previous_back():
    sleep(1)
    if odin[0].isActive == True:
        back_click = pyautogui.locateOnScreen('image\previous_back.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        pyautogui.click(back_click)
    elif odin[1].isActive == True:
        back_click = pyautogui.locateOnScreen('image\previous_back.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        pyautogui.click(back_click)

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
    
# 파티던전 입장 
# dg_course : 맹독의뱀둥지 - 1, 잊혀진거인의동굴 - 2, 난쟁이왕가의무덤 - 3    
# df_level : 보통 - 1, 어려움 - 2, 매우 어려움 - 3, 극악 - 4
# 무조건 비공개 파티로 체크되고 솔로 플레이됨
def party_dg_entrance(dg_course, dg_level):
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        sleep(1)
        pyautogui.press('F8')
        sleep(2)
        p_dg = pyautogui.locateOnScreen('image\party_dg_on.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        print('파티던전 탭 확인: ', p_dg)
        if p_dg is None:
            print("파티던전 탭 선택안됨")
            pyautogui.click(p_dg)
        sleep(2)
        # 무료 입장 체크 (가능 = 1반환, 불가능 = 0반환)
        free_check = pyautogui.locateOnScreen('image\party_dg_free_check.jpg', confidence=0.8, region=(374, 442, 124, 26)) 
        print('무료 입장 체크', free_check)
        if free_check:
            check_value = 0
            print('무료 입장 모두 소진함')
            main_back()
            # 무료 입장횟수 없음 - 다시 안들어오게 없다고 디비 저장 코딩하면 됨
        else:
            check_value = 1
            if dg_course == 1:
                course_dg = pyautogui.locateOnScreen('image\party_step_1.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print(course_dg)
                pyautogui.click(course_dg)
            if dg_course == 2:
                course_dg = pyautogui.locateOnScreen('image\party_step_2.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print(course_dg)
                pyautogui.click(course_dg)
            if dg_course == 3:
                course_dg = pyautogui.locateOnScreen('image\party_step_3.jpg', confidence=0.8, region=(0, 0, 960, 540))
                print(course_dg)
                pyautogui.click(course_dg)
        sleep(2)
        # 파티찾기 화면
        p_dg_2 = pyautogui.locateOnScreen('image\party_dg_step2_check.jpg', confidence=0.8, region=(15, 280, 100, 50)) 
        print(p_dg_2)
        if p_dg_2 is None:
            print("파티던전 2단계 화면 아님")
            check_value = 0
            sleep(1)
            main_back() 
        else:
            if dg_level == 1:
                pyautogui.click(49, 303)
                sleep(2)
            elif dg_level == 2:
                pyautogui.click(113, 303)
                sleep(2)
            elif dg_level == 3:
                pyautogui.click(169, 303)
                sleep(2)
            elif dg_level == 4:
                pyautogui.click(236, 303)
                sleep(2)
            p_private_check = pyautogui.locateOnScreen('image\party_private_check.jpg', confidence=0.8, region=(0, 300, 80, 70)) 
            print('비공개 파티 체크 여부 : ', p_private_check)
            if p_private_check is None:
                pyautogui.click(26, 333) # 비공개 파티 체크
                sleep(2)
            make_party = pyautogui.locateOnScreen('image\make_party_dg.jpg', confidence=0.8, region=(800, 440, 160, 70)) 
            print('파티생성 버튼 여부', make_party)
            if make_party:
                pyautogui.click(899, 497) # 파티 생성
                sleep(2)
                pyautogui.click(529, 331) # 팝업창 확인 클릭
                main_back() # 파티생성 후 메인으로 돌아가기
                sleep(2)
                party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
                if party_dg_start:
                    pyautogui.click(party_dg_start) # 파티던전 시작
                    sleep(2)
                    p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
                    if p_member:
                        pyautogui.click(530, 330) # 파티정원 확인창 확인 클릭
                    sleep(10)
                    pyautogui.press('g') #오토시작
                else: # 파티던전 시작하기 버튼이 없을 경우
                    main_back()
                    confirm_party = pyautogui.locateOnScreen('image\out_party.jpg', confidence=0.8, region=(900, 70, 50, 160))  # 파티 생성 여부 확인
                    if confirm_party:
                        check_value = 0 # 파티 생성되었는데도 버튼이 안보이므로 0 리턴
                    else:
                        main_party_tab = pyautogui.locateOnScreen('image\main_party_tab.jpg', confidence=0.8, region=(900, 70, 50, 160)) 
                        if main_party_tab:
                            pyautogui.click(main_party_tab) # 파티탭 클릭
                            party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(0, 0, 960, 540))
                            if party_dg_start:
                                pyautogui.click(party_dg_start) # 파티던전 시작
                                sleep(2)
                                p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
                                if p_member:
                                    pyautogui.click(530, 330) # 파티정원 확인창 확인 클릭
                                sleep(10)
                                pyautogui.press('g') #오토시작
                            else:
                                check_value = 0
                        else:
                            main_back()
                            check_value = 0 # 파티탭 찾을 수 없음 0리턴
            elif make_party is None:
                cancel_party = pyautogui.locateOnScreen('image\cancel_party.jpg', confidence=0.8, region=(800, 440, 160, 70))  # 파티 생성 여부 확인
                if cancel_party:
                    main_back() # 이미 파티 생성 중이라 메인화면으로 이동
                    sleep(2)
                    confirm_party = pyautogui.locateOnScreen('image\out_party.jpg', confidence=0.8, region=(900, 70, 50, 160))  # 파티 생성 여부 확인
                    print("파티 생성 여부 확인 : ", confirm_party)
                    if confirm_party:
                        party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(0, 0, 960, 540))
                        if party_dg_start:
                            pyautogui.click(party_dg_start) # 파티던전 시작
                            sleep(2)
                            p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
                            if p_member:
                                pyautogui.click(530, 330) # 파티정원 확인창 확인 클릭
                            sleep(10)
                            pyautogui.press('g') #오토시작
                            print('파티던전 시작')
                            check_value = 1
                        else:
                            check_value = 0                            
                    else:
                        main_party_tab = pyautogui.locateOnScreen('image\main_party_tab.jpg', confidence=0.8, region=(900, 70, 50, 160)) 
                        sleep(2)
                        if main_party_tab:
                            print('파티 탭 클릭')
                            pyautogui.click(main_party_tab) # 파티탭 클릭
                            sleep(2)
                            party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(0, 0, 960, 540))
                            if party_dg_start:
                                pyautogui.click(party_dg_start) # 파티던전 시작
                                sleep(2)
                                p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
                                if p_member:
                                    pyautogui.click(530, 330) # 파티정원 확인창 확인 클릭
                                sleep(10)
                                pyautogui.press('g') #오토시작
                                check_value = 1
                            else:
                                check_value = 0
                        else:
                            main_back()
                            check_value = 0 # 파티탭 찾을 수 없음 0리턴
                else:
                    check_value = 0
            else:
                print('파티생성 버튼 오류')
                check_value = 0
    elif odin[1].isActive == True:
        sleep(1)
        pyautogui.press('F8')
        sleep(2)
        p_dg = pyautogui.locateOnScreen('image\party_dg_on.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if p_dg is None:
            print("파티던전 탭 선택안됨")
            pyautogui.click(p_dg)
        sleep(2)
        free_check = pyautogui.locateOnScreen('image\party_dg_free_check.jpg', confidence=0.8, region=(1334, 442, 124, 26)) 
        if free_check:
            check_value = 0
            print('무료 입장 모두 소진함')
            main_back()
            # 무료 입장횟수 없음 - 다시 안들어오게 없다고 디비 저장 코딩하면 됨
        else:
            check_value = 1
            if dg_course == 1:
                course_dg = pyautogui.locateOnScreen('image\party_step_1.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print(course_dg)
                pyautogui.click(course_dg)
            if dg_course == 2:
                course_dg = pyautogui.locateOnScreen('image\party_step_2.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print(course_dg)
                pyautogui.click(course_dg)
            if dg_course == 3:
                course_dg = pyautogui.locateOnScreen('image\party_step_3.jpg', confidence=0.8, region=(960, 0, 960, 540))
                print(course_dg)
                pyautogui.click(course_dg)
        sleep(2)
        # 파티찾기 화면
        p_dg_2 = pyautogui.locateOnScreen('image\party_dg_step2_check.jpg', confidence=0.8, region=(975, 280, 100, 50)) 
        if p_dg_2 is None:
            print("파티던전 2단계 화면 아님")
            check_value = 0
            sleep(1)
            main_back() 
        else:
            if dg_level == 1:
                pyautogui.click(1009, 303)
                sleep(2)
            elif dg_level == 2:
                pyautogui.click(1073, 303)
                sleep(2)
            elif dg_level == 3:
                pyautogui.click(1129, 303)
                sleep(2)
            elif dg_level == 4:
                pyautogui.click(1196, 303)
                sleep(2)
            p_private_check = pyautogui.locateOnScreen('image\party_private_check.jpg', confidence=0.8, region=(960, 300, 80, 70)) 
            print('비공개 파티 체크 여부 : ', p_private_check)
            if p_private_check is None:
                pyautogui.click(986, 333) # 비공개 파티 체크
                sleep(2)
            make_party = pyautogui.locateOnScreen('image\make_party_dg.jpg', confidence=0.8, region=(1760, 440, 160, 70)) 
            print('파티생성 버튼 여부', make_party)
            if make_party:
                pyautogui.click(1859, 497) # 파티 생성
                sleep(2)
                pyautogui.click(1489, 331) # 팝업창 확인 클릭
                main_back() # 파티생성 후 메인으로 돌아가기
                sleep(2)
                party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
                if party_dg_start:
                    pyautogui.click(party_dg_start) # 파티던전 시작
                    sleep(2)
                    p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
                    if p_member:
                        pyautogui.click(1490, 330) # 파티정원 확인창 확인 클릭
                    sleep(10)
                    pyautogui.press('g') #오토시작
                else: # 파티던전 시작하기 버튼이 없을 경우
                    main_back()
                    confirm_party = pyautogui.locateOnScreen('image\out_party.jpg', confidence=0.8, region=(1860, 70, 50, 160))  # 파티 생성 여부 확인
                    if confirm_party:
                        check_value = 0 # 파티 생성되었는데도 버튼이 안보이므로 0 리턴
                    else:
                        main_party_tab = pyautogui.locateOnScreen('image\main_party_tab.jpg', confidence=0.8, region=(1860, 70, 50, 160)) 
                        if main_party_tab:
                            pyautogui.click(main_party_tab) # 파티탭 클릭
                            party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(960, 0, 960, 540))
                            if party_dg_start:
                                pyautogui.click(party_dg_start) # 파티던전 시작
                                sleep(2)
                                p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
                                if p_member:
                                    pyautogui.click(1490, 330) # 파티정원 확인창 확인 클릭
                                sleep(10)
                                pyautogui.press('g') #오토시작
                            else:
                                check_value = 0
                        else:
                            main_back()
                            check_value = 0 # 파티탭 찾을 수 없음 0리턴
            elif make_party is None:
                cancel_party = pyautogui.locateOnScreen('image\cancel_party.jpg', confidence=0.8, region=(1760, 440, 160, 70))  # 파티 생성 여부 확인
                if cancel_party:
                    main_back() # 이미 파티 생성 중이라 메인화면으로 이동
                    sleep(2)
                    confirm_party = pyautogui.locateOnScreen('image\out_party.jpg', confidence=0.8, region=(1860, 70, 50, 160))  # 파티 생성 여부 확인
                    print("파티 생성 여부 확인 : ", confirm_party)
                    if confirm_party:
                        party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(960, 0, 960, 540))
                        if party_dg_start:
                            pyautogui.click(party_dg_start) # 파티던전 시작
                            sleep(2)
                            p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
                            if p_member:
                                pyautogui.click(1490, 330) # 파티정원 확인창 확인 클릭
                            sleep(10)
                            pyautogui.press('g') #오토시작
                            print('파티던전 시작')
                            check_value = 1
                        else:
                            check_value = 0                            
                    else:
                        main_party_tab = pyautogui.locateOnScreen('image\main_party_tab.jpg', confidence=0.8, region=(1860, 70, 50, 160)) 
                        sleep(2)
                        if main_party_tab:
                            print('파티 탭 클릭')
                            pyautogui.click(main_party_tab) # 파티탭 클릭
                            sleep(2)
                            party_dg_start = pyautogui.locateOnScreen('image\party_dg_start.jpg', confidence=0.8, region=(960, 0, 960, 540))
                            if party_dg_start:
                                pyautogui.click(party_dg_start) # 파티던전 시작
                                sleep(2)
                                p_member = pyautogui.locateOnScreen('image\party_member_confirm.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
                                if p_member:
                                    pyautogui.click(1490, 330) # 파티정원 확인창 확인 클릭
                                sleep(10)
                                pyautogui.press('g') #오토시작
                                check_value = 1
                            else:
                                check_value = 0
                        else:
                            main_back()
                            check_value = 0 # 파티탭 찾을 수 없음 0리턴
                else:
                    check_value = 0
            else:
                print('파티생성 버튼 오류')
                check_value = 0
    return check_value

# 마을의뢰 - 고급 및 최고급 의뢰만 진행하며, 골드로만 갱신함
def town_request():
    sleep(1)
    pyautogui.press('j')
    sleep(1)
    # 전체 의뢰 완료 여부 확인 - 전체개수 및 수락함 의뢰 있는지 여부
    # 전체개수 full & 수락함 의뢰 없으면 마을의뢰 종료
    # 완료 전이면 0을 리턴, 완료했다면 1을 리턴
    def town_request_all_complete():
        sleep(1)
        if odin[0].isActive == True:
            all_complete_map1 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_1.jpg', region=(150, 450, 50, 40))
            all_complete_map2 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_2.jpg', region=(150, 450, 50, 40))
            all_complete_map3 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_3.jpg', region=(150, 450, 50, 40))
            all_complete_map4 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_4.jpg', region=(150, 450, 50, 40))
            print(all_complete_map1, all_complete_map2, all_complete_map3, all_complete_map4)
            if all_complete_map1 or all_complete_map2 or all_complete_map3 or all_complete_map4:
                # 리스트 가장 아래 의뢰 시작 - 지상 이동
                pyautogui.moveTo(120, 430)
                pyautogui.dragTo(120, 100, 3, button='left')
                sleep(1)
                already_ok = pyautogui.locateOnScreen('image\\town_request_already_ok.jpg', confidence=0.9, region=(170, 150, 70, 310))
                if already_ok:
                    pyautogui.click(already_ok)
                    sleep(1)
                    go_onfoot = pyautogui.locateOnScreen('image\\town_request_onfoot.jpg', confidence=0.9, region=(580, 470, 200, 50))
                    pyautogui.click(go_onfoot)
                else:
                    print('일일 의뢰 완료 또는 오류 발생')
                    main_back()
                return 1
            else:
                return 0
        elif odin[1].isActive == True:
            all_complete_map1 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_1.jpg', region=(1110, 450, 50, 40))
            all_complete_map2 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_2.jpg', region=(1110, 450, 50, 40))
            all_complete_map3 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_3.jpg', region=(1110, 450, 50, 40))
            all_complete_map4 = pyautogui.locateOnScreen('image\\town_request_all_complete_check_4.jpg', region=(1110, 450, 50, 40))
            print(all_complete_map1, all_complete_map2, all_complete_map3, all_complete_map4)
            if all_complete_map1 or all_complete_map2 or all_complete_map3 or all_complete_map4:
                # 리스트 가장 아래 의뢰 시작 - 지상 이동
                pyautogui.moveTo(1080, 430)
                pyautogui.dragTo(1080, 100, 3, button='left')
                sleep(1)
                already_ok = pyautogui.locateOnScreen('image\\town_request_already_ok.jpg', confidence=0.9, region=(1130, 150, 70, 310))
                if already_ok:
                    pyautogui.click(already_ok)
                    sleep(1)
                    go_onfoot = pyautogui.locateOnScreen('image\\town_request_onfoot.jpg', confidence=0.9, region=(1540, 470, 200, 50))
                    pyautogui.click(go_onfoot)
                else:
                    print('일일 의뢰 완료 또는 오류 발생')
                    main_back()
                return 1
            else:
                return 0

    # 완료 퀘스트 확인 및 보상 수령
    def town_request_complete_ckeck():
        print('완료 퀘스트 및 보상 수령 시작')
        sleep(1)
        if odin[0].isActive == True:
            # 변동 이미지라서 3번 체크로 유무 확인
            while True:
                check_atr = pyautogui.locateOnScreen('image\\town_request_complete_click.jpg', confidence=0.9, region=(0, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request_complete_click.jpg', confidence=0.9, region=(0, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request_complete_click.jpg', confidence=0.9, region=(0, 100, 50, 50))
                sleep(1)
                if check_atr:
                    print('완료 퀘스트 있음')
                    click_reward = pyautogui.locateOnScreen('image\\town_request_reward.jpg', confidence=0.9, region=(810, 470, 150, 50))
                    pyautogui.click(click_reward)
                    sleep(4)
                    click_randaom = pyautogui.locateOnScreen('image\\town_request_reward_random.jpg', confidence=0.9, region=(450, 310, 60, 50))
                    pyautogui.click(click_randaom)
                    sleep(3)
                    pyautogui.click(470, 440)
                    sleep(2)
                else:
                    break

        elif odin[1].isActive == True:
            # 변동 이미지라서 3번 체크로 유무 확인
            while True:
                check_atr = pyautogui.locateOnScreen('image\\town_request_complete_click.jpg', confidence=0.9, region=(960, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request_complete_click.jpg', confidence=0.9, region=(960, 100, 50, 50))
                if check_atr is None:
                    sleep(0.5)
                    check_atr = pyautogui.locateOnScreen('image\\town_request_complete_click.jpg', confidence=0.9, region=(960, 100, 50, 50))
                sleep(1)
                if check_atr:
                    print('완료 퀘스트 있음')
                    click_reward = pyautogui.locateOnScreen('image\\town_request_reward.jpg', confidence=0.9, region=(1770, 470, 150, 50))
                    pyautogui.click(click_reward)
                    sleep(4)
                    click_randaom = pyautogui.locateOnScreen('image\\town_request_reward_random.jpg', confidence=0.9, region=(1410, 310, 60, 50))
                    pyautogui.click(click_randaom)
                    sleep(3)
                    pyautogui.click(1430, 440)
                    sleep(2)
                else:
                    break
        print('완료 퀘스트 및 보상 수령 완료!!!')


    # 퀘스트 난이도 확인 및 의뢰수락 (상급, 최상급만 선택)
    def town_request_level_confirm():
        print('퀘스트 난이도 확인 및 의뢰수락(골드의뢰만 수락함)')
        sleep(1)
        if odin[0].isActive == True:
            #상급, 최상급 퀘스트만 선택
            while True:
                trl_confirm_q1 = pyautogui.locateOnScreen('image\\town_request_q1.jpg', confidence=0.9, region=(230, 100, 60, 60))
                trl_confirm_q2 = pyautogui.locateOnScreen('image\\town_request_q2.jpg', confidence=0.9, region=(230, 100, 60, 60))
                trl_confirm_q3 = pyautogui.locateOnScreen('image\\town_request_q3.jpg', confidence=0.9, region=(230, 100, 60, 60))
                trl_ok = pyautogui.locateOnScreen('image\\town_request_ok.jpg', confidence=0.9, region=(820, 470, 140, 50))
                trl_max = pyautogui.locateOnScreen('image\\town_request_deal_max.jpg', confidence=0.9, region=(910, 60, 60, 40))
                trl_refresh = pyautogui.locateOnScreen('image\\town_request_gold_click.jpg', confidence=0.9, region=(130, 460, 70, 70))
                # 완료 퀘스트 체크
                town_request_all_complete()
                # 진행 중인 의뢰가 가득일 경우 out   
                if trl_max:
                    break
                elif trl_confirm_q2 or trl_confirm_q3:
                    print('상급 또는 최상급 퀘스트 존재 - 수락하기 클릭')
                    pyautogui.click(trl_ok)
                    sleep(5)
                elif trl_refresh:
                    print('상급, 최상급 마을의뢰 없음 - 골드 초기화 실행')
                    pyautogui.click(trl_refresh)
                    sleep(5)
                    trl_gold_ok = pyautogui.locateOnScreen('image\\town_request_confirm.jpg', confidence=0.9, region=(460, 310, 170, 70)) 
                    pyautogui.click(trl_gold_ok)
                    sleep(2)
                # 골드 갱신이 없다면 보통 의뢰 수락
                elif trl_refresh is None:
                    pyautogui.click(trl_ok)
                    sleep(5)
            # 리스트 가장 아래 의뢰 시작 - 지상 이동
            pyautogui.moveTo(120, 430)
            pyautogui.dragTo(120, 100, 3, button='left')
            sleep(2)
            already_ok = pyautogui.locateOnScreen('image\\town_request_already_ok.jpg', confidence=0.9, region=(170, 150, 70, 310))
            if already_ok:
                pyautogui.click(already_ok)
                sleep(1)
                go_onfoot = pyautogui.locateOnScreen('image\\town_request_onfoot.jpg', confidence=0.9, region=(580, 470, 200, 50))
                sleep(1)
                pyautogui.click(go_onfoot)
            else:
                print('수락한 퀘스트 없거나 오류발생')
                main_back()
        elif odin[1].isActive == True:
            #상급, 최상급 퀘스트만 선택
            while True:
                trl_confirm_q1 = pyautogui.locateOnScreen('image\\town_request_q1.jpg', confidence=0.9, region=(1190, 100, 60, 60))
                trl_confirm_q2 = pyautogui.locateOnScreen('image\\town_request_q2.jpg', confidence=0.9, region=(1190, 100, 60, 60))
                trl_confirm_q3 = pyautogui.locateOnScreen('image\\town_request_q3.jpg', confidence=0.9, region=(1190, 100, 60, 60))
                trl_ok = pyautogui.locateOnScreen('image\\town_request_ok.jpg', confidence=0.9, region=(1780, 470, 140, 50))
                trl_max = pyautogui.locateOnScreen('image\\town_request_deal_max.jpg', confidence=0.9, region=(1870, 60, 60, 40))
                trl_refresh = pyautogui.locateOnScreen('image\\town_request_gold_click.jpg', confidence=0.9, region=(1090, 460, 70, 70))
                # 완료 퀘스트 체크
                town_request_all_complete()
                # 진행 중인 의뢰가 가득일 경우 out                
                if trl_max:
                    break
                elif trl_confirm_q2 or trl_confirm_q3:
                    print('상급 또는 최상급 퀘스트 존재 - 수락하기 클릭')
                    pyautogui.click(trl_ok)
                    sleep(5)
                elif trl_refresh:
                    print('상급, 최상급 마을의뢰 없음 - 골드 초기화 실행')
                    pyautogui.click(trl_refresh)
                    sleep(5)
                    trl_gold_ok = pyautogui.locateOnScreen('image\\town_request_confirm.jpg', confidence=0.9, region=(1420, 310, 170, 70)) 
                    pyautogui.click(trl_gold_ok)
                    sleep(2)
                # 골드 갱신이 없다면 보통 의뢰 수락
                elif trl_refresh is None:
                    pyautogui.click(trl_ok)
                    sleep(5)
            # 리스트 가장 아래 의뢰 시작 - 지상 이동
            pyautogui.moveTo(1080, 430)
            pyautogui.dragTo(1080, 100, 3, button='left')
            sleep(2)
            already_ok = pyautogui.locateOnScreen('image\\town_request_already_ok.jpg', confidence=0.9, region=(1130, 150, 70, 310))
            if already_ok:
                pyautogui.click(already_ok)
                sleep(1)
                go_onfoot = pyautogui.locateOnScreen('image\\town_request_onfoot.jpg', confidence=0.9, region=(1540, 470, 200, 50))
                sleep(1)
                pyautogui.click(go_onfoot)
            else:
                print('수락한 퀘스트 없거나 오류발생')
                main_back()
        print('퀘스트 난이도 확인 및 의뢰수락 완료!!!!')

        
    town_request_complete_ckeck()
    all_clear = town_request_all_complete()
    if all_clear == 0:
        town_request_complete_ckeck()
        sleep(1)
        town_request_level_confirm()
    elif all_clear == 1:
        print('마을 의뢰 완료! >>>>>> ', all_clear)

# 마을 귀환 > 포션 구입 > 저장된 사냥터 이동
def get_potion():
    sleep(1)
    # # hp 체크 - 멀티 스레딩 또는 while문을 빠져나오는 방법을 강구해야 함 그리고 간헐적 에러가 발생하기에 우선 사용 안함
    # def check_hp():
    #     while True:
    #         sleep(5)
    #         # 거의 hp 30% 정도일때 귀환함 (좌표의 RGB로 체크)
    #         try:
    #             x_1, y_1 = pyautogui.position(78, 46)
    #             r_1,g_1,b_1 = pyautogui.pixel(x_1, y_1)
    #             print('ODIN1 hp 체크중....', r_1)
    #         except:
    #             x_1, y_1 = pyautogui.position(78, 46)
    #             r_1,g_1,b_1 = pyautogui.pixel(x_1, y_1)
    #             print('ODIN1 hp 체크중....', r_1)
    #         if r_1 < 40:
    #             odin[0].activate()
    #             break
    #         try:
    #             x_2, y_2 = pyautogui.position(1038, 46)
    #             r_2, g_2, b_2 = pyautogui.pixel(x_2, y_2)
    #             print('ODIN2 hp 체크중....', r_2)
    #         except:
    #             x_2, y_2 = pyautogui.position(1038, 46)
    #             r_2, g_2, b_2 = pyautogui.pixel(x_2, y_2)
    #             print('ODIN2 hp 체크중....', r_2)
    #         if r_2 < 40:
    #             odin[1].activate()
    #             breakooooo
    #         if pyautogui.press('o'):
    #             break

    # 물약 사러 귀환
    def go_town():
        sleep(1)
        if odin[0].isActive == True:
            main_back()
            sleep(2)
            pyautogui.click(22, 203)
            sleep(2)
            gotown_click = pyautogui.locateOnScreen('image\\gotown_ok.jpg', confidence=0.8, region=(450, 290, 180, 80))
            if gotown_click:
                print('물약 사러 마을로 갑니다~!')
                pyautogui.click(gotown_click)
                sleep(15)
                pyautogui.press('4')
                sleep(15)
                pyautogui.click(120, 130) # 대형물약
                sleep(3)
                pyautogui.click(547, 313) # 최대
                sleep(3)
                pyautogui.click(530, 388) # 구매하기
                sleep(3)
                main_back()
                sleep(3)
                pyautogui.click(19, 138) # 저장된 장소
                sleep(3)
                pyautogui.click(211, 184) # 이동
                sleep(10)
                pyautogui.press('g')
            else: 
                print('마을 가는 확인창 찾을 수 없음')
                main_back()
        elif odin[1].isActive == True:
            main_back()
            sleep(2)
            pyautogui.click(982, 203)
            sleep(2)
            gotown_click = pyautogui.locateOnScreen('image\\gotown_ok.jpg', confidence=0.8, region=(1410, 290, 180, 80))
            if gotown_click:
                print('물약 사러 마을로 갑니다~!')
                pyautogui.click(gotown_click)
                sleep(10)
                pyautogui.press('4')
                sleep(10)
                pyautogui.click(1080, 130) # 대형물약
                sleep(3)
                pyautogui.click(1507, 313) # 최대
                sleep(3)
                pyautogui.click(1490, 388) # 구매하기
                sleep(3)
                main_back()
                sleep(3)
                pyautogui.click(979, 138) # 저장된 장소
                sleep(3)
                pyautogui.click(1171, 184) # 이동
                sleep(10)
                pyautogui.press('g')
            else: 
                print('마을 가는 확인창 찾을 수 없음')
                main_back()

# 부활하기
def resurrection():
    sleep(1)
    if odin[0].isActive == True:
        # 빨간색이 껌벅거려서 3번 체크함
        make_res = pyautogui.locateOnScreen('image\\resurrection.jpg', confidence=0.8, region=(477, 423, 150, 50))
        sleep(1)
        make_res = pyautogui.locateOnScreen('image\\resurrection.jpg', confidence=0.8, region=(477, 423, 150, 50))
        sleep(1)
        make_res = pyautogui.locateOnScreen('image\\resurrection.jpg', confidence=0.8, region=(477, 423, 150, 50))
        if make_res:
            print('죽었습니다. 부활합니다.')
            pyautogui.click(make_res)
            sleep(15)
            pyautogui.click(213, 47) # 상단 부활하기 체크
            sleep(3)
            pyautogui.click(337, 188) # 리스트에 사망 클릭 (첫번째)
            sleep(3)
            pyautogui.click(536, 400) # 무료 복구 클릭
            sleep(3)
            pyautogui.press('4')
            sleep(15)
            pyautogui.click(120, 130) # 대형물약
            sleep(3)
            pyautogui.click(547, 313) # 최대
            sleep(3)
            pyautogui.click(530, 388) # 구매하기
            sleep(3)
            main_back()
            sleep(3)
            pyautogui.click(19, 138) # 저장된 장소
            sleep(3)
            pyautogui.click(211, 184) # 이동
            sleep(10)
            pyautogui.press('g')
            return 0
        else: 
            print('죽지 않음 패스')
            main_back()
            return 1
    elif odin[1].isActive == True:
        # 빨간색이 껌벅거려서 3번 체크함
        make_res = pyautogui.locateOnScreen('image\\resurrection.jpg', confidence=0.8, region=(1437, 423, 150, 50))
        sleep(1)
        make_res = pyautogui.locateOnScreen('image\\resurrection.jpg', confidence=0.8, region=(1437, 423, 150, 50))
        sleep(1)
        make_res = pyautogui.locateOnScreen('image\\resurrection.jpg', confidence=0.8, region=(1437, 423, 150, 50))
        if make_res:
            print('죽었습니다. 부활합니다.')
            pyautogui.click(make_res)
            sleep(15)
            pyautogui.click(1173, 47) # 상단 부활하기 체크
            sleep(3)
            pyautogui.click(1297, 188) # 리스트에 사망 클릭 (첫번째)
            sleep(3)
            pyautogui.click(1496, 400) # 무료 복구 클릭
            sleep(3)
            pyautogui.press('4')
            sleep(15)
            pyautogui.click(1080, 130) # 대형물약
            sleep(3)
            pyautogui.click(1507, 313) # 최대
            sleep(3)
            pyautogui.click(1490, 388) # 구매하기
            sleep(3)
            main_back()
            sleep(3)
            pyautogui.click(979, 138) # 저장된 장소
            sleep(3)
            pyautogui.click(1171, 184) # 이동
            sleep(10)
            pyautogui.press('g')
            return 0
        else: 
            print('죽지 않음 패스')
            main_back()
            return 1

get_mecro()
active_mecro_1()
disable_sleep_mode()
# elite_dg_entrance(4, 5)
# party_dg_entrance(2, 1)
town_request()
# resurrection()

sleep(2)
active_mecro_2()
disable_sleep_mode()
# elite_dg_entrance(4, 5)
# party_dg_entrance(2, 1)
town_request()
# resurrection()

# active_mecro_2()
# disable_sleep_mode()
# party_dg_entrance(2, 1)
# elite_dg_entrance(4, 5)

# test_1 = party_dg_step1(2)
# print('step_1 check_value : ', test_1)
# test_2 = party_dg_step2(1)
# print('step_2 check_value : ', test_2)
# active_mecro_2()
# disable_sleep_mode()