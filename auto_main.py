# -*- coding: utf-8 -*-
# 일일 던전, 마을의뢰 플레이

import sys
from time import sleep
import time
import pyautogui
import pywinauto
import auto_daily_2 as ad
import os

def odin1_write(stage):
    with open("odin1.txt", "w") as f:
        f.write(stage)

def odin2_write(stage):
    with open("odin2.txt", "w") as f:
        f.write(stage)

def odin1_read():
    with open("odin1.txt", "r") as f:
        stage = f.read()
    return stage

def odin2_read():
    with open("odin2.txt", "r") as f:
        stage = f.read()
    return stage

# 데일리 오딘1 스케줄
def play_odin1():
    # 1번 캐릭터
    if odin1 == 1:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('3')
            ad.get_post() # 우편 받기
            ad.daily_gold_item() # 매일 골드 상품 구매
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin1 == 2:
        ad.active_mecro_1()
        event_dg_end = ad.event_dg_entrance(2)
        if event_dg_end == 1:
            odin1_write('3')

    if odin1 == 3:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin1_write('4')

    if odin1 == 4:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin1_write('5')
            ad.char_change(2)

    # 2번 캐릭터
    if odin1 == 5:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('7')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin1 == 6:
        ad.active_mecro_1()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin1_write('7')

    if odin1 == 7:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin1_write('8')

    if odin1 == 8:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin1_write('9')
            ad.char_change(3)

    # 3번 캐릭터
    if odin1 == 9:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('11')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin1 == 10:
        ad.active_mecro_1()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin1_write('11')

    if odin1 == 11:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin1_write('12')

    if odin1 == 12:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin1_write('21')
            ad.char_change(1)     #5캐릭시 수정       
                        

    # 4번 캐릭터
    if odin1 == 13:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('15')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin1 == 14:
        ad.active_mecro_1()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin1_write('15')

    if odin1 == 15:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin1_write('16')

    if odin1 == 16:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin1_write('17')
            ad.char_change(5)


    # 5번 캐릭터
    if odin1 == 17:
        ad.active_mecro_1()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin1_write('19')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin1 == 18:
        ad.active_mecro_1()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin1_write('19')

    if odin1 == 19:
        ad.active_mecro_1()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin1_write('20')

    if odin1 == 20:
        ad.active_mecro_1()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin1_write('21')
            ad.char_change(1)

# 데일리 오딘2 스케줄
def play_odin2():
    # 1번 캐릭터
    if odin2 == 1:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('3')
            ad.get_post() # 우편 받기
            ad.daily_gold_item() # 매일 골드 상품 구매
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin2 == 2:
        ad.active_mecro_2()
        event_dg_end = ad.event_dg_entrance(2)
        if event_dg_end == 1:
            odin2_write('3')

    if odin2 == 3:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(2)
        if money_dg_end == 1:
            odin2_write('4')

    if odin2 == 4:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(2)
        if scroll_dg_end == 1:
            odin2_write('5')
            ad.char_change(2)

    # 2번 캐릭터
    if odin2 == 5:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('7')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin2 == 6:
        ad.active_mecro_2()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin2_write('7')

    if odin2 == 7:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin2_write('8')

    if odin2 == 8:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin2_write('9')
            ad.char_change(3)

    # 3번 캐릭터
    if odin2 == 9:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('11')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin2 == 10:
        ad.active_mecro_2()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin2_write('11')

    if odin2 == 11:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin2_write('12')

    if odin2 == 12:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin2_write('21')
            ad.char_change(1)    # 5캐릭시 수정        
                        

    # 4번 캐릭터
    if odin2 == 13:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('15')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin2 == 14:
        ad.active_mecro_2()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin2_write('15')

    if odin2 == 15:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin2_write('16')

    if odin2 == 16:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin2_write('17')
            ad.char_change(5)


    # 5번 캐릭터
    if odin2 == 17:
        ad.active_mecro_2()
        tr_end = ad.town_request()
        if tr_end == 1:
            odin2_write('19')
            ad.guild_check() # 길드 출석 체크
            # ad.item_bunhae() # 아이템 분해
            # ad.mimir_eat() # 미미르 샘물 먹기
            ad.go_town() # 물약 구매

    if odin2 == 18:
        ad.active_mecro_2()
        event_dg_end = ad.event_dg_entrance(1)
        if event_dg_end == 1:
            odin2_write('19 ')

    if odin2 == 19:
        ad.active_mecro_2()
        money_dg_end = ad.money_dg_entrance(1)
        if money_dg_end == 1:
            odin2_write('20')

    if odin2 == 20:
        ad.active_mecro_2()
        scroll_dg_end = ad.scroll_dg_entrance(1)
        if scroll_dg_end == 1:
            odin2_write('21')
            ad.char_change(1)

# 오딘1 지하감옥 스케줄
def play_week_dg_odin1():
    if odin1 == 21:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('22')
            ad.char_change(2)
    
    if odin1 == 22:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('23')
            ad.char_change(3)

    if odin1 == 23:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('26')
            ad.char_change(1)

    if odin1 == 24:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('25')
            ad.char_change(5)
    
    if odin1 == 25:
        ad.active_mecro_1()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin1_write('26')
            ad.char_change(1)

# 오딘2 지하감옥 스케줄
def play_week_dg_odin2():
    # 1번 캐릭터
    if odin2 == 21:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('22')
            ad.char_change(2)

    if odin2 == 22:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('23')
            ad.char_change(3)

    if odin2 == 23:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('26')
            ad.char_change(1)

    if odin2 == 24:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('25')
            ad.char_change(5)

    if odin2 == 25:
        ad.active_mecro_2()
        week_end = ad.week_dg_entrance(1)
        if week_end == 1: # 리턴값이 1일 경우 종료
            odin2_write('26')
            ad.char_change(1)

# 필드 사냥(즐겨찾기 1번)
def field_play(): 
    if odin1 == 26:
        ad.active_mecro_1()
        fp = ad.field_play()
    if odin2 == 26:
        ad.active_mecro_2()
        fp = ad.field_play()

############################### 오딘 플레이 ###############################
# 매크로 시작 오딘 창 불러오기
ad.get_mecro()

#최초 실행시 어디까지 진행했는지 읽어옴
odin1 = int(odin1_read())
odin2 = int(odin2_read())

# # 오딘1 진행상황에 따른 캐릭터 선택
# ad.active_mecro_1()
# if odin1 == 1 or odin1 == 2 or odin1 == 3 or odin1 == 4 or odin1 == 21:
#     ad.char_change(1)
# elif odin1 == 5 or odin1 == 6 or odin1 == 7 or odin1 == 8 or odin1 == 22:
#     ad.char_change(2)
# elif odin1 == 9 or odin1 == 10 or odin1 == 11 or odin1 == 12 or odin1 == 23:
#     ad.char_change(3)
# elif odin1 == 13 or odin1 == 14 or odin1 == 15 or odin1 == 16 or odin1 == 24:
#     ad.char_change(4)
# elif odin1 == 17 or odin1 == 18 or odin1 == 19 or odin1 == 20 or odin1 == 25:
#     ad.char_change(5)

# # 오딘2 진행상황에 따른 캐릭터 선택
# ad.active_mecro_2()
# if odin2 == 1 or odin2 == 2 or odin2 == 3 or odin2 == 4 or odin2 == 21:
#     ad.char_change(1)
# elif odin2 == 5 or odin2 == 6 or odin2 == 7 or odin2 == 8 or odin2 == 22:
#     ad.char_change(2)
# elif odin2 == 9 or odin2 == 10 or odin2 == 11 or odin2 == 12 or odin2 == 23:
#     ad.char_change(3)
# elif odin2 == 13 or odin2 == 14 or odin2 == 15 or odin2 == 16 or odin2 == 24:
#     ad.char_change(4)
# elif odin2 == 17 or odin2 == 18 or odin2 == 19 or odin2 == 20 or odin2 == 25:
#     ad.char_change(5)


while True:
    try:
        # 스테이지 불러오기
        odin1 = int(odin1_read())
        odin2 = int(odin2_read())

        ad.active_mecro_1()
        # 오딘 1 - 물약 및 부활 체크
        ad.no_potion()
        ad.resurrection()

        play_odin1()
        
        ad.active_mecro_2()
        # 오딘 2 - 물약 및 부활 체크
        ad.no_potion()
        ad.resurrection()

        play_odin2()
        
        play_week_dg_odin1()
        play_week_dg_odin2()
        field_play()
        ad.active_mecro_1()

        # 6시 초기화
        find_hour = time.strftime('%H', time.localtime(time.time()))
        print('시간체크 :' + find_hour + '시(6시 초기화)')
        if find_hour == '06':
            if odin1 == 1 or odin1 == 2 or odin1 == 3 or odin1 == 4: # 1, 2번 이면 초기화 안함
                print('1, 2, 3, 4번 진행 시라면 초기화 하지 않음')
                pass
            else:
                odin1_write('1')
                ad.active_mecro_1()
                ad.char_change(1)
            
            if odin2 == 1 or odin2 == 2 or odin2 == 3 or odin2 == 4:
                print('1, 2, 3, 4번 진행 시라면 초기화 하지 않음')
                pass
            else:
                odin2_write('1')
                ad.active_mecro_2()
                ad.char_change(1)

        # 체크 주기
        sleep(30)
    except:
        sleep(5)
        print('오류 발생')
        os.execl(sys.executable, sys.executable, *sys.argv)
