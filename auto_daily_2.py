# -*- coding: utf-8 -*-

import sys
from time import sleep
import pyautogui
import pywinauto

# 1920 * 1080
# 메크로 1 = 0, 0 >> 960, 540       메크로2 = 960, 0 >> 960, 540

odin = []
image = ''

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
            sleep(1)
            odin[0].activate()
            sleep(1)
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
            sleep(1)
            odin[1].activate()
            sleep(1)
        except:
            print('2번 프로그램 활성화 오류')

# 절전모드 해제 및 게임화면으로 이동
def disable_sleep_mode():
    sleep(1)
    if odin[0].isActive == True:
        sleep_mode = pyautogui.locateOnScreen('image\\disable_sleep_mode.jpg', confidence=0.8, region=(0, 0, 960, 540))
        print(sleep_mode , '절전모드 아님')
        if sleep_mode is not None:
            pyautogui.moveTo(480, 270)
            pyautogui.dragTo(680, 270, 1, button='left')
    elif odin[1].isActive == True:
        sleep_mode = pyautogui.locateOnScreen('image\\disable_sleep_mode.jpg', confidence=0.8, region=(960, 0, 960, 540))
        print(sleep_mode , '절전모드 아님')
        if sleep_mode is not None:
            pyautogui.moveTo(1440, 270)
            pyautogui.dragTo(1640, 270, 1, button='left')

# 메인화면 돌아가기
def main_back():
    sleep(1)
    # 팝업이 뜬다... ㅅㅂ
    while True:
        click_x_3 = pyautogui.locateOnScreen('image\\click_x_3.jpg', confidence=0.8, region=(0, 0, 1920, 1080)) 
        if click_x_3:
            pyautogui.click(click_x_3)
            sleep(1)
        else:
            break

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
        click_x_2 = pyautogui.locateOnScreen('image\\click_x_2.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        if click_x_2:
            pyautogui.click(click_x_2)
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
        click_x_2 = pyautogui.locateOnScreen('image\\click_x_2.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        if click_x_2:
            pyautogui.click(click_x_2)
            sleep(1)

# 물약 구매
def go_town():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        main_back()
        sleep(1)
        pyautogui.click(18, 172)
        sleep(1)
        gotown_click = pyautogui.locateOnScreen('image\\gotown_ok.jpg', confidence=0.8, region=(0, 0, 960, 540))
        if gotown_click:
            print('물약 사러 마을로 갑니다~!')
            pyautogui.click(gotown_click)
            sleep(30)
        else: 
            print('마을이거나 귀환 불가 지역')
        pyautogui.press('4')
        sleep(20)
        pyautogui.click(137, 494) # 지정 구매
        sleep(2)
        main_back()
    elif odin[1].isActive == True:
        main_back()
        sleep(1)
        pyautogui.click(978, 172)
        sleep(1)
        gotown_click = pyautogui.locateOnScreen('image\\gotown_ok.jpg', confidence=0.8, region=(960, 0, 960, 540))
        if gotown_click:
            print('물약 사러 마을로 갑니다~!')
            pyautogui.click(gotown_click)
            sleep(30)
        else: 
            print('마을이거나 귀환 불가 지역')
        pyautogui.press('4')
        sleep(20)
        pyautogui.click(1097, 494) # 지정 구매
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
        auto_9 = pyautogui.locateOnScreen('image\\auto_play\\auto_9.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_10 = pyautogui.locateOnScreen('image\\auto_play\\auto_10.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_11 = pyautogui.locateOnScreen('image\\auto_play\\auto_11.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_12 = pyautogui.locateOnScreen('image\\auto_play\\auto_12.jpg', confidence=0.8, region=(0, 0, 960, 540))
        auto_13 = pyautogui.locateOnScreen('image\\auto_play\\auto_13.jpg', confidence=0.8, region=(0, 0, 960, 540))
        print('자동사냥 체크 :',auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8, auto_9, auto_10, auto_11)
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
        elif auto_9:
            pyautogui.click(auto_9)
            sleep(1)
        elif auto_10:
            pyautogui.click(auto_10)
            sleep(1)
        elif auto_11:
            pyautogui.click(auto_11)
            sleep(1)
        elif auto_12:
            pyautogui.click(auto_12)
            sleep(1)
        elif auto_13:
            pyautogui.click(auto_13)
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
        auto_9 = pyautogui.locateOnScreen('image\\auto_play\\auto_9.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_10 = pyautogui.locateOnScreen('image\\auto_play\\auto_10.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_11 = pyautogui.locateOnScreen('image\\auto_play\\auto_11.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_12 = pyautogui.locateOnScreen('image\\auto_play\\auto_12.jpg', confidence=0.8, region=(960, 0, 960, 540))
        auto_13 = pyautogui.locateOnScreen('image\\auto_play\\auto_13.jpg', confidence=0.8, region=(960, 0, 960, 540))
        print('자동사냥 체크 :',auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8, auto_9, auto_10, auto_11)
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
        elif auto_9:
            pyautogui.click(auto_9)
            sleep(1)
        elif auto_10:
            pyautogui.click(auto_10)
            sleep(1)
        elif auto_11:
            pyautogui.click(auto_11)
            sleep(1)
        elif auto_12:
            pyautogui.click(auto_12)
            sleep(1)
        elif auto_13:
            pyautogui.click(auto_13)
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
        image = pyautogui.locateOnScreen('image\\' + jpg_image + '.jpg', grayscale=True, confidence=0.8, region=(0, 0, 960, 540))
    if odin[1].isActive == True:
        image = pyautogui.locateOnScreen('image\\' + jpg_image + '.jpg', grayscale=True, confidence=0.8, region=(960, 0, 960, 540))
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            sleep(30)
            # 팝업 유무
            ck_popup()
            sleep(2)
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
            if i > 8:
                break

# 물약 소진 시 물약사러 가기
def no_potion():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        print('오딘1 - 물약체크 중... ')
        get_potion = image_check('get_potion')
        get_potion_2 = image_check('get_potion_2')
        get_potion_3 = image_check('get_potion_3')
        get_potion_4 = image_check('get_potion_4')
        get_potion_5 = image_check('get_potion_5')
        get_potion_6 = image_check('get_potion_6')
        if get_potion or get_potion_2 or get_potion_3 or get_potion_4 or get_potion_5 or get_potion_6:
            print('오딘1 - 물약 소진 확인 마을 귀환')
            go_town()
    if odin[1].isActive == True:
        print('오딘2 - 물약체크 중... ')
        get_potion = image_check('get_potion')
        get_potion_2 = image_check('get_potion_2')
        get_potion_3 = image_check('get_potion_3')
        get_potion_4 = image_check('get_potion_4')
        get_potion_5 = image_check('get_potion_5')
        get_potion_6 = image_check('get_potion_6')
        if get_potion or get_potion_2 or get_potion_3 or get_potion_4 or get_potion_5 or get_potion_6:
            print('오딘2 - 물약 소진 확인 마을 귀환')
            go_town()
            
# 팝업 체크
def ck_popup():
    sleep(1)
    if odin[0].isActive == True:
        print('오딘1 - 팝업 체크')
        ch_popup = image_check('ch_popup')
        sleep(1)
        if ch_popup:
            pyautogui.click(ch_popup)
        else:
            pass

    if odin[1].isActive == True:
        print('오딘2 - 팝업 체크')
        ch_popup = image_check('ch_popup')
        sleep(1)
        if ch_popup:
            pyautogui.click(ch_popup)
        else:
            pass

# 죽었을 경우 부활하기
def resurrection():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        print('오딘1 - 부활 체크 중......')
        resurrection = image_check('resurrection')
        resurrection2 = image_check('resurrection2')
        print(resurrection, resurrection2)
        if resurrection or resurrection2:
            print('오딘1 - 사망 확인 부활함 ..')
            pyautogui.click(556, 445)
            sleep(1)
            pyautogui.click(556, 445)
            sleep(20)
            go_town()
            # 복구 아이콘 2개 검색(가끔 검색 안될때가 있어서 2개 검색 넣음)
            resurrection_click = image_check('resurrection_click')
            resurrection_click2 = image_check('resurrection_click2')
            print(resurrection_click, resurrection_click2)
            print('오딘1 - 부활 복구 시작!')
            if resurrection_click:
                pyautogui.click(resurrection_click)
            elif resurrection_click2:
                pyautogui.click(resurrection_click2)
            else:
                pyautogui.click(215, 52)
                pass
                sleep(3)
            while True:
                resurrection_check = pyautogui.locateOnScreen('image\\resurrection_check.jpg', confidence=0.8, region=(315, 166, 50, 50))
                resurrection_check2 = pyautogui.locateOnScreen('image\\resurrection_check2.jpg', confidence=0.8, region=(315, 166, 50, 50))
                sleep(1)
                if resurrection_check or resurrection_check2:
                    pyautogui.click(492, 187)
                    sleep(1)
                    pyautogui.click(492, 187)
                    sleep(2)
                    resurrection_free = image_check('resurrection_free')
                    resurrection_gold = image_check('resurrection_gold')
                    if resurrection_free:
                        pyautogui.click(resurrection_free)
                    else:
                        pyautogui.click(resurrection_gold)
                    sleep(5)
                else:
                    break
    if odin[1].isActive == True:
        print('오딘2 - 부활 체크 중......')
        resurrection = image_check('resurrection')
        resurrection2 = image_check('resurrection2')
        print(resurrection, resurrection2)
        if resurrection or resurrection2:
            print('오딘2 - 사망 확인 부활함 ..')
            pyautogui.click(1516, 445)
            sleep(1)
            pyautogui.click(1516, 445)
            sleep(20)
            go_town()
            # 복구 아이콘 2개 검색(가끔 검색 안될때가 있어서 2개 검색 넣음)
            resurrection_click = image_check('resurrection_click')
            resurrection_click2 = image_check('resurrection_click2')
            print(resurrection_click, resurrection_click2)
            print('오딘2 - 부활 복구 시작!')
            if resurrection_click:
                pyautogui.click(resurrection_click)
            elif resurrection_click2:
                pyautogui.click(resurrection_click2)
            else:
                pyautogui.click(1175, 52)
                sleep(3)
            while True:
                resurrection_check = pyautogui.locateOnScreen('image\\resurrection_check.jpg', confidence=0.8, region=(1275, 166, 50, 50))
                resurrection_check2 = pyautogui.locateOnScreen('image\\resurrection_check2.jpg', confidence=0.8, region=(1275, 166, 50, 50))
                sleep(1)
                if resurrection_check or resurrection_check2:
                    pyautogui.click(1452, 187)
                    sleep(1)
                    pyautogui.click(1452, 187)
                    sleep(2)
                    resurrection_free = image_check('resurrection_free')
                    resurrection_gold = image_check('resurrection_gold')
                    if resurrection_free:
                        pyautogui.click(resurrection_free)
                    else:
                        pyautogui.click(resurrection_gold)
                    sleep(5)
                else:
                    break

# 우편물 미미르 먹거나 미미르 포션 먹기
def get_mimir():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('f7')
        sleep(2)
        mimir_frist = pyautogui.locateOnScreen('image\\mimir_frist.jpg', confidence=0.8, region=(865, 107, 85, 45))
        if mimir_frist:
            pyautogui.click(mimir_frist) # 상단 첫번째 미미르 받기
            sleep(5)
            mimir_check = image_check('mimir_cancel')    
            if mimir_check:
                pyautogui.click(mimir_check) # 미미르가 가득 차 있다면 취소 클릭
                sleep(3)
            else:
                pyautogui.click(mimir_frist) # 아무곳이나 클릭
                sleep(3)
            main_back() # 게임 화면으로 이동
        else:
            mimir_eat()
            sleep(1)
            main_back()
    if odin[1].isActive == True:
        pyautogui.press('f7')
        sleep(2)
        mimir_frist = pyautogui.locateOnScreen('image\\mimir_frist.jpg', confidence=0.8, region=(1825, 107, 85, 45))
        if mimir_frist:
            pyautogui.click(mimir_frist) # 상단 첫번째 미미르 받기
            sleep(5)
            mimir_check = image_check('mimir_cancel')    
            if mimir_check:
                pyautogui.click(mimir_check) # 미미르가 가득 차 있다면 취소 클릭
                sleep(3)
            else:
                pyautogui.click(mimir_frist) # 아무곳이나 클릭
                sleep(3)
            main_back() # 게임 화면으로 이동
        else:
            mimir_eat()
            sleep(1)
            main_back()
        
# 우편물 받기 - 구버전 사용안함
def get_post():
    if odin[0].isActive == True:
        pyautogui.press('f7')
        sleep(2)
        pyautogui.click(895, 496) # 모두 받기
        sleep(5)
        # mimir_check = image_check('mimir_cancel')
        mimir_check = image_check('mimir_ok')
        if mimir_check:
            print('오딘1 - 우편 미미르 샘물이 많다. 그래도 먹자')
            sleep(3)
            # pyautogui.click(mimir_check)
            pyautogui.click(mimir_check)
            sleep(3)
            pyautogui.click(mimir_check)
            sleep(3)
        else:
            print('오딘1 - 미미르 완전 만땅!!!!')
        pyautogui.click(173, 84) # 계정 우편 탭
        sleep(3)
        pyautogui.click(895, 496) # 모두 받기
        main_back()
        sleep(2)
        main_back()
        sleep(2)
    if odin[1].isActive == True:
        pyautogui.press('f7')
        sleep(2)
        pyautogui.click(1855, 496) # 모두 받기
        sleep(5)
        # mimir_check = image_check('mimir_cancel')
        mimir_check = image_check('mimir_ok')
        if mimir_check:
            print('오딘2 - 우편 미미르 샘물이 많다. 그래도 먹자')
            sleep(3)
            # pyautogui.click(mimir_check)
            pyautogui.click(mimir_check)
            sleep(3)
            pyautogui.click(mimir_check)
            sleep(3)
        else:
            print('오딘2 - 미미르 완전 만땅!!!!')
        pyautogui.click(1133, 84) # 계정 우편 탭
        sleep(3)
        pyautogui.click(1855, 496) # 모두 받기
        main_back()

# 일일 골드 상품 구매
def daily_gold_item():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('u')
        print('오딘1 - 캐쉬 페이지 이동')
        sleep(5)
        pyautogui.click(64, 436) # 일괄 구매 
        sleep(2)
        gold_gumae = image_check('gold_gumae') # 골드 상품 구매
        if gold_gumae:
            pyautogui.click(gold_gumae) # 팝업 골드 구매 클릭
            print('오딘1 - 골드 상품 일괄 구매 완료')
            sleep(3)
            main_back()
        else:
            print('오딘1 - 골드 상품 구매했거나, 구매할 수 없는 상태')
        main_back()
    if odin[1].isActive == True:
        pyautogui.press('u')
        print('오딘2 - 캐쉬 페이지 이동')
        sleep(5)
        pyautogui.click(1024, 436) # 일괄 구매 
        sleep(2)
        gold_gumae = image_check('gold_gumae') # 골드 상품 구매
        if gold_gumae:
            pyautogui.click(gold_gumae) # 팝업 골드 구매 클릭
            print('오딘2 - 골드 상품 일괄 구매 완료')
            sleep(3)
            main_back()
        else:
            print('오딘2 - 골드 상품 구매했거나, 구매할 수 없는 상태')
        main_back()
        sleep(2)
        main_back()
        sleep(2)

# 길드 출석 체크 및 주화 사기
def guild_check():
    sleep(2)
    main_back()
    if odin[0].isActive == True:
        pyautogui.press('f6')
        print('오딘1 - 길드 페이지 이동')
        sleep(10)
        pyautogui.click(470, 350) # 아무대나 클릭 (출석보상 보상 화면)
        sleep(2)
        pyautogui.click(470, 350) # 아무대나 클릭 (출석보상 보상 화면)
        sleep(2)
        pyautogui.click(139, 86) # 길드 정보 탭
        print('오딘1 - 길드 정보 탭 이동')
        sleep(2)
        guild_gibu = image_check('guild_gibu')
        if guild_gibu:
            print('오딘1 - 길드 기부 시작')
            pyautogui.click(325, 465) # 골드 기부
            sleep(5)
            pyautogui.click(325, 465) # 아무대나 클릭
            sleep(5)
            pyautogui.click(325, 465) # 골드 기부
            sleep(5)
            pyautogui.click(325, 465) # 아무대나 클릭
            sleep(5)
            pyautogui.click(325, 465) # 골드 기부
            sleep(5)
            pyautogui.click(325, 465) # 아무대나 클릭
            sleep(5)
            main_back()
        else:
            print('오딘1 - 길드 가입 안했거나, 이미 기부한 상태')
            main_back()
            pass
    if odin[1].isActive == True:
        pyautogui.press('f6')
        print('오딘2 - 길드 페이지 이동')
        sleep(10)
        pyautogui.click(1430, 350) # 아무대나 클릭 (출석보상 보상 화면)
        sleep(2)
        pyautogui.click(1430, 350) # 아무대나 클릭 (출석보상 보상 화면)
        sleep(2)
        pyautogui.click(1099, 86) # 길드 정보 탭
        print('오딘2 - 길드 정보 탭 이동')
        sleep(2)
        guild_gibu = image_check('guild_gibu')
        if guild_gibu:
            print('오딘2 - 길드 기부 시작')
            pyautogui.click(1285, 465) # 골드 기부
            sleep(5)
            pyautogui.click(1285, 465) # 아무대나 클릭
            sleep(5)
            pyautogui.click(1285, 465) # 골드 기부
            sleep(5)
            pyautogui.click(1285, 465) # 아무대나 클릭
            sleep(5)
            pyautogui.click(1285, 465) # 골드 기부
            sleep(5)
            pyautogui.click(1285, 465) # 아무대나 클릭
            sleep(5)
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
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)            
            #던전 체크
            money_dg = image_check('money_dg')
            sleep(2)
            if money_dg:
                print('오딘1 - 머니 던전 확인됨')
                dg_time = where_dg(3)  # 이벤트 던전 생기면 4번 , 아니면 3번 
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
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)            
            #던전 체크
            money_dg = image_check('money_dg')
            sleep(2)
            if money_dg:
                print('오딘2 - 머니 던전 확인됨')
                dg_time = where_dg(3)  # 이벤트 던전 생기면 4번
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
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)            
            #던전 체크
            pyautogui.moveTo(640, 260)
            pyautogui.dragTo(140, 260, 4, button='left')
            sleep(1)            
            scroll_dg = image_check('scroll_dg')
            sleep(2)
            if scroll_dg:
                print('오딘1 - 스크롤 던전 확인됨')
                dg_time = where_dg(3) 
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
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)            
            #던전 체크
            pyautogui.moveTo(1600, 260)
            pyautogui.dragTo(1100, 260, 4, button='left')
            sleep(1)                
            scroll_dg = image_check('scroll_dg')
            sleep(2)
            if scroll_dg:
                print('오딘2 - 스크롤 던전 확인됨')
                dg_time = where_dg(3) 
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
            pyautogui.click(175, 85) # 정예던전 탭
            sleep(2)            
            #던전 체크 - 지하감옥은 드래그가 필요(이벤트 던전 때문에)
            pyautogui.moveTo(640, 260)
            pyautogui.dragTo(140, 260, 4, button='left')
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
            pyautogui.click(1135, 85) # 정예던전 탭
            sleep(2)            
            #던전 체크 - 지하감옥은 드래그가 필요(이벤트 던전 때문에)
            pyautogui.moveTo(1600, 260)
            pyautogui.dragTo(1100, 260, 4, button='left')
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
        safe_zone = image_check('safe_zone')
        if safe_zone: # 안전 지역이면 1번 자동사냥 시작
            print('오딘1 - 마을에서 놀고 있음. 자동사냥 시작')
            favorite_go() 
        else:
            print('오딘1 - 열심히 자동사냥 중.. 즐겨찾기 1번.. ')
            auto_play() # 자동사냥 
            pass
    if odin[1].isActive == True:
        safe_zone = image_check('safe_zone')
        if safe_zone: # 안전 지역이면 1번 자동사냥 시작
            print('오딘2 - 마을에서 놀고 있음. 자동사냥 시작')
            favorite_go() 
        else:
            print('오딘2 - 열심히 자동사냥 중.. 즐겨찾기 1번.. ')
            auto_play() # 자동사냥 체크
            pass

# 메인 퀘스트 실행
def main_quest():
    sleep(1)
    main_back()
    if odin[0].isActive == True:
        sleep(1)
        pyautogui.click(913, 98) 
        print('오딘1 - 메인 퀘스트 진행 빠른이동 클릭')
        sleep(3)
        # 골드 이동 이미지 체킹
        fast_move_by_gold = image_check('fast_move_by_gold')
        fast_move_by_gold2 = image_check('fast_move_by_gold2')
        fast_move_by_free = image_check('fast_move_by_free')
        quest_confirm = image_check('quest_confirm')
        play_quest = image_check('play_quest')
        if fast_move_by_gold:
            print('오딘1 - 골드 빠른이동 클릭')
            pyautogui.click(fast_move_by_gold)  # 골드 빠른 이동
        elif fast_move_by_gold2:
            print('오딘1 - 골드 빠른이동 클릭')
            pyautogui.click(fast_move_by_gold2)  # 골드 빠른 이동
        elif fast_move_by_free: 
            print('오딘1 - 무료 빠른이동 클릭(마을가기)')
            pyautogui.click(fast_move_by_free)  # 무료 빠른 이동
        elif quest_confirm: 
            print('오딘1 - 확인버튼 클릭')
            pyautogui.click(quest_confirm)  # 던전 입장 확인 버튼
        elif play_quest: 
            print('오딘1 - 메인 퀘스트 진행 중...')
            pass
        else:
            while True:
                #skip 이미지 체킹 후 있으면 클릭 후 5초 대기
                get_reword = image_check('get_reword')
                # get_reword_1 = image_check('get_reword_1')
                # get_reword_2 = image_check('get_reword_2')
                # quest_boss = image_check('quest_boss')
                quest_complete_3 = image_check('quest_complete_3')
                story_skip = image_check('story_skip')
                # story_skip_1 = image_check('story_skip_1')
                story_skip_2 = image_check('story_skip_2')
                story_skip_3 = image_check('story_skip_3')
                story_skip_side = image_check('story_skip_side')
                story_skip_side_2 = image_check('story_skip_side_2')
                story_skip_top = image_check('story_skip_top')
                story_skip_top_2 = image_check('story_skip_top_2')
                story_skip_top_3 = image_check('story_skip_top_3')
                print('오딘1 - 스킵 이미지 체크 중.........')
                if get_reword:
                    pyautogui.click(get_reword)
                # elif get_reword_1:
                #     pyautogui.click(get_reword_1)
                # elif get_reword_2:
                #     pyautogui.click(get_reword_2)
                # elif quest_boss:
                #     pyautogui.click(quest_boss)
                elif quest_complete_3:
                    pyautogui.click(quest_complete_3)
                elif story_skip:
                    pyautogui.click(story_skip)
                # elif story_skip_1:
                #     pyautogui.click(story_skip_1)
                elif story_skip_2:
                    pyautogui.click(story_skip_2)
                elif story_skip_3:
                    pyautogui.click(story_skip_3)
                elif story_skip_side:
                    pyautogui.click(story_skip_side)
                elif story_skip_side_2:
                    pyautogui.click(story_skip_side_2)
                elif story_skip_top:
                    pyautogui.click(story_skip_top)
                elif story_skip_top_2:
                    pyautogui.click(story_skip_top_2)
                elif story_skip_top_3:
                    pyautogui.click(story_skip_top_3)
                else:
                    pyautogui.click(913, 98) 
                    sleep(2)
                    # 골드 이동 이미지 체킹
                    fast_move_by_gold = image_check('fast_move_by_gold')
                    fast_move_by_free = image_check('fast_move_by_free')
                    play_quest = image_check('play_quest')
                    if fast_move_by_gold:
                        print('오딘1 - 골드 빠른이동 클릭')
                        pyautogui.click(fast_move_by_gold)  # 골드 빠른 이동
                        break
                    elif fast_move_by_gold2:
                        print('오딘1 - 골드 빠른이동 클릭')
                        pyautogui.click(fast_move_by_gold2)  # 골드 빠른 이동
                        break
                    elif fast_move_by_free: 
                        print('오딘1 - 무료 빠른이동 클릭(마을가기)')
                        pyautogui.click(fast_move_by_free)  # 무료 빠른 이동
                        break
                    elif play_quest: 
                        print('오딘1 - 메인 퀘스트 진행 중...')
                        break
                    else:
                        break

    elif odin[1].isActive == True:
        sleep(1)
        pyautogui.click(1873, 98) 
        print('오딘2 - 메인 퀘스트 진행 빠른이동 클릭')
        sleep(3)
        # 골드 이동 이미지 체킹
        fast_move_by_gold = image_check('fast_move_by_gold')
        fast_move_by_gold2 = image_check('fast_move_by_gold2')
        fast_move_by_free = image_check('fast_move_by_free')
        quest_confirm = image_check('quest_confirm')
        play_quest = image_check('play_quest')
        if fast_move_by_gold:
            print('오딘2 - 골드 빠른이동 클릭')
            pyautogui.click(fast_move_by_gold)  # 골드 빠른 이동
        elif fast_move_by_gold2:
            print('오딘2 - 골드 빠른이동 클릭')
            pyautogui.click(fast_move_by_gold2)  # 골드 빠른 이동
        elif fast_move_by_free: 
            print('오딘2 - 무료 빠른이동 클릭(마을가기)')
            pyautogui.click(fast_move_by_free)  # 무료 빠른 이동
        elif quest_confirm: 
            print('오딘2 - 확인버튼 클릭')
            pyautogui.click(quest_confirm)  # 던전 입장 확인 버튼
        elif play_quest: 
            print('오딘2 - 메인 퀘스트 진행 중...')
            pass
        else:
            while True:
                #skip 이미지 체킹 후 있으면 클릭 후 5초 대기
                get_reword = image_check('get_reword')
                # get_reword_1 = image_check('get_reword_1')
                # get_reword_2 = image_check('get_reword_2')
                # quest_boss = image_check('quest_boss')
                quest_complete_3 = image_check('quest_complete_3')
                story_skip = image_check('story_skip')
                # story_skip_1 = image_check('story_skip_1')
                story_skip_2 = image_check('story_skip_2')
                story_skip_3 = image_check('story_skip_3')
                story_skip_side = image_check('story_skip_side')
                story_skip_side_2 = image_check('story_skip_side_2')
                story_skip_top = image_check('story_skip_top')
                story_skip_top_2 = image_check('story_skip_top_2')
                story_skip_top_3 = image_check('story_skip_top_3')
                print('오딘2 - 스킵 이미지 체크 중.........')
                if get_reword:
                    pyautogui.click(get_reword)
                # elif get_reword_1:
                #     pyautogui.click(get_reword_1)
                # elif get_reword_2:
                #     pyautogui.click(get_reword_2)
                # elif quest_boss:
                #     pyautogui.click(quest_boss)
                elif quest_complete_3:
                    pyautogui.click(quest_complete_3)
                elif story_skip:
                    pyautogui.click(story_skip)
                # elif story_skip_1:
                #     pyautogui.click(story_skip_1)
                elif story_skip_2:
                    pyautogui.click(story_skip_2)
                elif story_skip_3:
                    pyautogui.click(story_skip_3)
                elif story_skip_side:
                    pyautogui.click(story_skip_side)
                elif story_skip_side_2:
                    pyautogui.click(story_skip_side_2)
                elif story_skip_top:
                    pyautogui.click(story_skip_top)
                elif story_skip_top_2:
                    pyautogui.click(story_skip_top_2)
                elif story_skip_top_3:
                    pyautogui.click(story_skip_top_3)
                else:
                    pyautogui.click(1873, 98) 
                    sleep(1)
                    # 골드 이동 이미지 체킹
                    fast_move_by_gold = image_check('fast_move_by_gold')
                    fast_move_by_free = image_check('fast_move_by_free')
                    play_quest = image_check('play_quest')
                    if fast_move_by_gold:
                        print('오딘2 - 골드 빠른이동 클릭')
                        pyautogui.click(fast_move_by_gold)  # 골드 빠른 이동
                        break
                    elif fast_move_by_gold2:
                        print('오딘2 - 골드 빠른이동 클릭')
                        pyautogui.click(fast_move_by_gold2)  # 골드 빠른 이동
                        break
                    elif fast_move_by_free: 
                        print('오딘2 - 무료 빠른이동 클릭(마을가기)')
                        pyautogui.click(fast_move_by_free)  # 무료 빠른 이동
                        break
                    elif play_quest: 
                        print('오딘2 - 메인 퀘스트 진행 중...')
                        break
                    else:
                        break


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
                hidden_quest = image_check('hidden_quest')
                if hidden_quest:
                    pyautogui.click(475, 339) # 한번 더 선택
                    sleep(3)                
                    pyautogui.click(470, 440) # 보상 선택후 임의의 장소 2번 클릭함. 에러때문에
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
                    sleep(2)
                    main_back()
                    sleep(5)
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
                hidden_quest = image_check('hidden_quest')
                if hidden_quest:
                    pyautogui.click(1435, 339) # 한번 더 선택
                    sleep(3)
                    pyautogui.click(1430, 440) # 보상 선택후 임의의 장소 2번 클릭함. 에러때문에
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
                    sleep(2)
                    main_back()
                    sleep(5)
                    print('오딘2 - 마을의뢰 완료')
                    return 1
                    break

# 파티던전 끝낫는지 파악
def end_party():
    sleep(1)
    if odin[0].isActive == True:
        end_1 = pyautogui.locateOnScreen('image\\party_dg\\end_1.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_2 = pyautogui.locateOnScreen('image\\party_dg\\end_2.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_3 = pyautogui.locateOnScreen('image\\party_dg\\end_3.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_4 = pyautogui.locateOnScreen('image\\party_dg\\end_4.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_5 = pyautogui.locateOnScreen('image\\party_dg\\end_5.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_6 = pyautogui.locateOnScreen('image\\party_dg\\end_6.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_7 = pyautogui.locateOnScreen('image\\party_dg\\end_7.jpg', confidence=0.8, region=(0, 0, 960, 540))
        end_8 = pyautogui.locateOnScreen('image\\party_dg\\end_8.jpg', confidence=0.8, region=(0, 0, 960, 540))
                
        if end_1:
            print('end_1')
            return 1
        if end_2:
            print('end_2')
            return 1
        if end_3:
            print('end_3')
            return 1
        if end_4:
            print('end_4')
            return 1
        if end_5:
            print('end_5')
            return 1
        if end_6:
            print('end_6')
            return 1
        if end_7:
            print('end_7')
            return 1
        if end_8:
            print('end_8')
            return 1

    elif odin[1].isActive == True:
        end_1 = pyautogui.locateOnScreen('image\\party_dg\\end_1.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_2 = pyautogui.locateOnScreen('image\\party_dg\\end_2.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_3 = pyautogui.locateOnScreen('image\\party_dg\\end_3.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_4 = pyautogui.locateOnScreen('image\\party_dg\\end_4.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_5 = pyautogui.locateOnScreen('image\\party_dg\\end_5.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_6 = pyautogui.locateOnScreen('image\\party_dg\\end_6.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_7 = pyautogui.locateOnScreen('image\\party_dg\\end_7.jpg', confidence=0.8, region=(960, 0, 960, 540))
        end_8 = pyautogui.locateOnScreen('image\\party_dg\\end_8.jpg', confidence=0.8, region=(960, 0, 960, 540))
                
        if end_1:
            print('end_1')
            return 1
        if end_2:
            print('end_2')
            return 1
        if end_3:
            print('end_3')
            return 1
        if end_4:
            print('end_4')
            return 1
        if end_5:
            print('end_5')
            return 1
        if end_6:
            print('end_6')
            return 1
        if end_7:
            print('end_7')
            return 1
        if end_8:
            print('end_8')
            return 1

# 파티던전 입장 
# dg_course : 맹독의뱀둥지 - 1, 잊혀진거인의동굴 - 2, 난쟁이왕가의무덤 - 3    
# 비공개 파티, 솔로 플레이, 보통 난이도만 가능
def create_party(dg_level):
    sleep(1)
    # main_back()
    if odin[0].isActive == True:
        sleep(1)
        # 파티생성
        if end_party() == 1: # 파티 중인지 체크 1이면 파티중 아님
            pyautogui.press('F8')
            sleep(2)
            party_dg_end = pyautogui.locateOnScreen('image\\party_dg\\party_dg_end.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
            sleep(1)
            if party_dg_end:
                print('오딘1 : 파티 던전 모두 소진(입장권 있어도 불가능) - 입장권은 다음주에 쓰세요')
                main_back()
                pass
            else:
                if dg_level == 1:
                    pyautogui.click(128, 284) # 맹독의 뱀 둥지
                elif dg_level == 2:
                    pyautogui.click(363, 280) # 잊혀진 거인의 동굴 
                elif dg_level == 3:
                    pyautogui.click(587, 293) # 난쟁이 왕가의 무덤
                sleep(2)
                already_party = pyautogui.locateOnScreen('image\\party_dg\\already_party.jpg', confidence=0.8, region=(830, 460, 120, 50)) 
                if already_party:
                    print('오딘1 : 파티 이미 생성됨!!! 뒤로가기!')
                    main_back()
                else:
                    pyautogui.click(23, 329) # 비공개 파티 체크
                    sleep(2)
                    pyautogui.click(895, 494) # 파티 생성
                    sleep(2)
                    pyautogui.click(532, 332)
                    print('오딘1 : 파티생성 완료!!!! 뒤로가기 !')
                    sleep(3)
                    main_back()
        else: # 파티 중이면 아무것도 안함
            pass
    elif odin[1].isActive == True:
        sleep(1)
        # 파티생성
        if end_party() == 1: # 파티 중인지 체크 1이면 파티중 아님
            pyautogui.press('F8')
            sleep(2)
            party_dg_end = pyautogui.locateOnScreen('image\\party_dg\\party_dg_end.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
            sleep(1)
            if party_dg_end:
                print('오딘2 : 파티 던전 모두 소진(입장권 있어도 불가능) - 입장권은 다음주에 쓰세요')
                main_back()
                pass
            else:
                if dg_level == 1:
                    pyautogui.click(1088, 284) # 맹독의 뱀 둥지
                elif dg_level == 2:
                    pyautogui.click(1323, 280) # 잊혀진 거인의 동굴 
                elif dg_level == 3:
                    pyautogui.click(1547, 293) # 난쟁이 왕가의 무덤
                sleep(2)
                already_party = pyautogui.locateOnScreen('image\\party_dg\\already_party.jpg', confidence=0.8, region=(1790, 460, 120, 50)) 
                if already_party:
                    print('오딘2 : 파티 이미 생성됨!!! 뒤로가기!')
                    main_back()
                else:
                    pyautogui.click(983, 329) # 비공개 파티 체크
                    sleep(2)
                    pyautogui.click(1855, 494) # 파티 생성
                    sleep(2)
                    pyautogui.click(1492, 332)
                    print('오딘2 : 파티생성 완료!!!! 뒤로가기 !')
                    sleep(3)
                    main_back()
        else: # 파티 중이면 아무것도 안함
            pass

# 파티던전 플레이
def paly_party_dg():
    sleep(1)
    main_back()
    if odin[0].isActive == True:    
        # 파티던전 시작하기 버튼 찾기
        print('오딘1 : 시작하기 버튼 체크')
        party_dg_start = pyautogui.locateOnScreen('image\\party_dg\\party_dg_start.jpg', confidence=0.8, region=(810, 130, 120, 80)) 
        # 파티던전 탭이 안눌러져 있을 경우 대비 탭 한번 클릭하고 시작버튼 다시 서치
        if party_dg_start:
            pass
        else:
            pyautogui.click(935, 141)
            sleep(2)
            party_dg_start = pyautogui.locateOnScreen('image\\party_dg\\party_dg_start.jpg', confidence=0.8, region=(810, 130, 120, 80)) 
        sleep(1)
        if party_dg_start:
            print('오딘1 : 파티던전 시작하기!!')
            pyautogui.click(party_dg_start)
            sleep(2)
            pyautogui.click(533, 331) # 입장 클릭
            sleep(2)
            pyautogui.click(533, 331) # 입장권 입장 시 한번 더 클릭
            sleep(10) # 입장 대기 시간
            auto_play()
        else:
            if end_party() == 1: #종료
                print('오딘1 : 파티던전 종료!!')
                print('오딘1 : ', end_party())
                return 1
            else:
                print('오딘1 : 파티던전 진행중!!')
                pass
    elif odin[1].isActive == True:
        # 파티던전 시작하기 버튼 찾기
        print('오딘2 : 시작하기 버튼 체크')
        party_dg_start = pyautogui.locateOnScreen('image\\party_dg\\party_dg_start.jpg', confidence=0.8, region=(1770, 130, 120, 80)) 
        # 파티던전 탭이 안눌러져 있을 경우 대비 탭 한번 클릭하고 시작버튼 다시 서치
        if party_dg_start:
            pass
        else:
            pyautogui.click(1895, 141)
            sleep(2)
            party_dg_start = pyautogui.locateOnScreen('image\\party_dg\\party_dg_start.jpg', confidence=0.8, region=(1770, 130, 120, 80)) 
        sleep(1)
        if party_dg_start:
            print('오딘2 : 파티던전 시작하기!!')
            pyautogui.click(party_dg_start)
            sleep(2)
            pyautogui.click(1493, 331) # 입장 클릭
            sleep(2)
            pyautogui.click(1493, 331) # 입장권 입장 시 한번 더 클릭
            sleep(10) # 입장 대기 시간
            auto_play()
        else:
            if end_party() == 1: #종료
                print('오딘2 : 파티던전 종료!!')
                print('오딘2 : ', end_party())
                return 1
            else:
                print('오딘2 : 파티던전 진행중!!')
                pass

# 페이지 로딩 체크 - 로딩 페이지의 경우 패스하는 로직 추가
def loding_page():
    sleep(1)
    main_back()
    if odin[0].isActive == True:    
        print('오딘1 : 로딩 중 체크')
        loding_1 = pyautogui.locateOnScreen('image\\loding_1.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_2 = pyautogui.locateOnScreen('image\\loding_2.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_3 = pyautogui.locateOnScreen('image\\loding_3.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_4 = pyautogui.locateOnScreen('image\\loding_4.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_5 = pyautogui.locateOnScreen('image\\loding_5.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_6 = pyautogui.locateOnScreen('image\\loding_6.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_7 = pyautogui.locateOnScreen('image\\loding_7.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_8 = pyautogui.locateOnScreen('image\\loding_8.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        loding_9 = pyautogui.locateOnScreen('image\\loding_9.jpg', confidence=0.8, region=(840, 450, 110, 65)) 
        if loding_1 or loding_2 or loding_3 or loding_4 or loding_5 or loding_6 or loding_7 or loding_8 or loding_9:
            print('오딘1 - 현재 로딩 페이지 중')
            return 1
        else:
            return 0
    elif odin[1].isActive == True:
        print('오딘2 : 로딩 중 체크')
        loding_1 = pyautogui.locateOnScreen('image\\loding_1.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_2 = pyautogui.locateOnScreen('image\\loding_2.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_3 = pyautogui.locateOnScreen('image\\loding_3.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_4 = pyautogui.locateOnScreen('image\\loding_4.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_5 = pyautogui.locateOnScreen('image\\loding_5.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_6 = pyautogui.locateOnScreen('image\\loding_6.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_7 = pyautogui.locateOnScreen('image\\loding_7.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_8 = pyautogui.locateOnScreen('image\\loding_8.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        loding_9 = pyautogui.locateOnScreen('image\\loding_9.jpg', confidence=0.8, region=(1800, 450, 110, 65)) 
        if loding_1 or loding_2 or loding_3 or loding_4 or loding_5 or loding_6 or loding_7 or loding_8 or loding_9:
            print('오딘2 - 현재 로딩 페이지 중')
            return 1
        else:
            return 0

# get_mecro()
# active_mecro_1()
# main_quest()
# sleep(5)
# active_mecro_2()
# main_quest()