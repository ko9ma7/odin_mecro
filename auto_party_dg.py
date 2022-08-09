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
        print(auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8)
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
        print(auto_1, auto_2, auto_3, auto_4, auto_5, auto_6, auto_7, auto_8)
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
        sleep(20)                    
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
        sleep(20)

# 파티던전 입장 
# dg_course : 맹독의뱀둥지 - 1, 잊혀진거인의동굴 - 2, 난쟁이왕가의무덤 - 3    
# 비공개 파티, 솔로 플레이, 보통 난이도만 가능
def party_dg_entrance(dg_level):
    sleep(1)
    main_back()
    sleep(1)
    main_back()
    sleep(1)
    main_back()

    if odin[0].isActive == True:
        sleep(1)
        # 파티생성
        pyautogui.press('F8')
        sleep(2)
        party_dg_end = pyautogui.locateOnScreen('image\\party_dg\\party_dg_end.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
        sleep(1)
        if party_dg_end:
            print('파티 던전 모두 소진(입장권 있어도 불가능) - 입장권은 다음주에 쓰세요')
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
            pyautogui.click(23, 329) # 비공개 파티 체크
            sleep(2)
            pyautogui.click(895, 494) # 파티 생성
            sleep(2)
            pyautogui.click(532, 332)
            sleep(3)

            while True:
                party_dg_start = pyautogui.locateOnScreen('image\\party_dg\\party_dg_start.jpg', confidence=0.8, region=(0, 0, 960, 540)) 
                sleep(1)
                print('파티 던전 시작하기 상태', party_dg_start)
                auto_play()

                if party_dg_start:
                    pyautogui.click(party_dg_start)
                    sleep(2)
                    pyautogui.click(533, 331)
                    sleep(2)
                    pyautogui.click(533, 331)
                    sleep(2)
                else:
                    pyautogui.click(933, 141)
                    sleep(2)
                if end_party() == 1: # 파티 해제 된 경우 = 파티 던전 종료
                    break

    elif odin[1].isActive == True:
        sleep(1)
        # 파티생성
        pyautogui.press('F8')
        sleep(2)
        party_dg_end = pyautogui.locateOnScreen('image\\party_dg\\party_dg_end.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
        sleep(1)
        if party_dg_end:
            print('파티 던전 모두 소진(입장권 있어도 불가능) - 입장권은 다음주에 쓰세요')
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
            pyautogui.click(983, 329) # 비공개 파티 체크
            sleep(2)
            pyautogui.click(1855, 494) # 파티 생성
            sleep(2)
            pyautogui.click(1492, 332)
            sleep(3)

            while True:
                party_dg_start = pyautogui.locateOnScreen('image\\party_dg\\party_dg_start.jpg', confidence=0.8, region=(960, 0, 960, 540)) 
                sleep(1)
                print('파티 던전 시작하기 상태', party_dg_start)
                auto_play()

                if party_dg_start:
                    pyautogui.click(party_dg_start)
                    sleep(2)
                    pyautogui.click(1493, 331)
                    sleep(2)
                    pyautogui.click(1493, 331)
                    sleep(2)
                else:
                    pyautogui.click(1893, 141)
                    sleep(2)
                if end_party() == 1: # 파티 해제 된 경우 = 파티 던전 종료
                    break



get_mecro()
active_mecro_1() # ODIN1 WINDOW
disable_sleep_mode()
main_back()

# 1번 캐릭터
char_change(1)
go_town()
party_dg_entrance(2)

# 2번 캐릭터
char_change(2)
go_town()
party_dg_entrance(1)

# 3번 캐릭터
char_change(3)
go_town()
party_dg_entrance(1)

# 4번 캐릭터
char_change(4)
go_town()
party_dg_entrance(1)

# 5번 캐릭터
char_change(5)
go_town()
party_dg_entrance(1)

# 1번 캐릭터로 복귀 후 첫번째 저장된 위치 사냥
sleep(10)
char_change(1)
pyautogui.click(21, 137)
sleep(2)
pyautogui.click(213, 189)
sleep(20)
pyautogui.press('g')
auto_play()

#########################################################

active_mecro_2() # ODIN1 WINDOW
disable_sleep_mode()
main_back()

# 1번 캐릭터
char_change(1)
go_town()
party_dg_entrance(2)

# 2번 캐릭터
char_change(2)
go_town()
party_dg_entrance(1)

# 3번 캐릭터
char_change(3)
go_town()
party_dg_entrance(1)

# 4번 캐릭터
char_change(4)
go_town()
party_dg_entrance(1)

# 5번 캐릭터
char_change(5)
go_town()
party_dg_entrance(1)

# 1번 캐릭터로 복귀 후 첫번째 저장된 위치 사냥
sleep(10)
char_change(1)
pyautogui.click(981, 137)
sleep(2)
pyautogui.click(1173, 189)
sleep(20)
pyautogui.press('g')
auto_play()