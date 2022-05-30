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
        pyautogui.click(back_click)
    elif odin[1].isActive == True:
        back_click = pyautogui.locateOnScreen('image\main_back.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
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
        if p_dg is None:
            print("파티던전 탭 선택안됨")
            pyautogui.click(p_dg)
        sleep(2)
        # 무료 입장 체크 (가능 = 1반환, 불가능 = 0반환)
        free_check = pyautogui.locateOnScreen('image\party_dg_free_check.jpg', confidence=0.8, region=(374, 442, 124, 26)) 
        if free_check is not None:
            check_value = 0
            back_click = pyautogui.locateOnScreen('image\main_back.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
            pyautogui.click(back_click)
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
        if free_check is not None:
            check_value = 0
            back_click = pyautogui.locateOnScreen('image\main_back.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
            pyautogui.click(back_click)
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
# 무조건 비공개 파티로 체크됨
def party_dg_step2(dg_level, op):
    sleep(1)
    if odin[0].isActive == True:
        p_dg = pyautogui.locateOnScreen('image\party_dg_step2_check.jpg', confidence=0.8, region=(15, 280, 100, 50)) 
        if p_dg is None:
            print("파티던전 2단계 화면 아님")
            sleep(1)
            main_back() 
        else:
            if dg_level == 1:
                pyautogui.click(49, 303)
                sleep(2)
                pyautogui.click(25, 333)
            elif dg_level == 2:
                pyautogui.click(113, 303)
                sleep(2)
                pyautogui.click(25, 333)
            elif dg_level == 3:
                pyautogui.click(169, 303)
                sleep(2)
                pyautogui.click(25, 333)
            elif dg_level == 4:
                pyautogui.click(236, 303)
                sleep(2)
                pyautogui.click(25, 333)
        sleep(2)
        pyautogui.click(899, 497)
        sleep(2)
        pyautogui.click(529, 331)
        
        
    return check_value


get_mecro()
active_mecro_2()
test = party_dg_step1(2)
print('check_value : ', test)
# disable_sleep_mode()
# dg_step1()
# dg_step2(4, 5)
# active_mecro_2()
# disable_sleep_mode()
# dg_step1()
# dg_step2(4, 5)





    
    
    


