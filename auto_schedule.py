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

# 정예던전 입장 1단계
def dg_step1():
    sleep(1)
    pyautogui.press('F8')
    sleep(2)
    if odin[0].isActive == True:
        e_dg = pyautogui.locateOnScreen('image\elite_dg.jpg', confidence=0.8, region=(0, 0, 960, 540))
        print(e_dg)
        pyautogui.click(e_dg)
    elif odin[1].isActive == True:
        e_dg = pyautogui.locateOnScreen('image\elite_dg.jpg', confidence=0.8, region=(960, 0, 960, 540))
        print(e_dg)
        pyautogui.click(e_dg)

# 정예던전 입장 2단계 (던전 초이스)
# chioce_dg : 1 - 이벤트 던전, 2 - 공허의 유적, 3 - 난쟁이 비밀통로, 4 - 지하감옥
# chioce_level : 1단계, 2단계, 3단계, 4단계 ~~~ (층 또는 단계 숫자로 입력)
def dg_step2(chioce_dg, choice_level):
    sleep(1)
    if odin[0].isActive == True:
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

# 파티던전 입장 1단계
# 맹독의뱀둥지 - 1, 잊혀진거인의동굴 - 2, 난쟁이왕가의무덤 - 3
def party_dg_step1(dg_course):
    sleep(1)
    pyautogui.press('F8')
    sleep(2)
    if odin[0].isActive == True:
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
    elif odin[1].isActive == True:
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
    return check_value
    
# 파티던전 입장 2단계
# df_level : 보통 - 1, 어려움 - 2, 매우 어려움 - 3, 극악 - 4
# 무조건 비공개 파티로 체크되고 솔로 플레이됨
def party_dg_step2(dg_level):
    print('2단계 시작')
    sleep(1)
    if odin[0].isActive == True:
        p_dg = pyautogui.locateOnScreen('image\party_dg_step2_check.jpg', confidence=0.8, region=(15, 280, 100, 50)) 
        if p_dg is None:
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
        p_dg = pyautogui.locateOnScreen('image\party_dg_step2_check.jpg', confidence=0.8, region=(975, 280, 100, 50)) 
        if p_dg is None:
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


get_mecro()
active_mecro_2()
test_1 = party_dg_step1(2)
print('step_1 check_value : ', test_1)
test_2 = party_dg_step2(1)
print('step_2 check_value : ', test_2)
# disable_sleep_mode()
# dg_step1()
# dg_step2(4, 5)
# active_mecro_2()
# disable_sleep_mode()
# dg_step1()
# dg_step2(4, 5)





    
    
    


