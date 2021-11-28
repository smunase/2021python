ans=input('프로그램을 실행하시겠습니까? (Y/N) : ' )
gamelist=['무궁화꽃이 피었습니다', '달고나 뽑기', '줄다리기', '구슬치기', '징검다리 건너기', '오징어게임']
if ans =='Y':
    gabun =1
    a=int(input('참가자 인원수를 입력하시오: '))
    print('게임은 총 6라운드로 진행됩니다. 그리고 총상금은', a, '억원 입니다.')
    while gabun < 7 :

        if gabun == 1 :
            print('%d라운드 게임은 %s 입니다.' %(gabun, gamelist[gabun-1]))
            b=int(input('%d라운드 탈락자 수를 입력하시오 (단, 과반수 이상이 탈락할 시 게임은 중단됩니다.):'%(gabun)))
            c=a-b
            print('현재 생존자 수는', c, '명입니다.')
        else :
            print('%d라운드 게임은 %s 입니다.' %(gabun, gamelist[gabun-1]))
            b=int(input('%d라운드 탈락자 수를 입력하시오 (단, 과반수 이상이 탈락할 시 프로그램은 중단됩니다.):' %(gabun)))
            c=c-b
            if c < b :
                print('탈락자 수가 과반수를 넘었으므로 프로그램을 종료합니다.')
                break
            print('현재 생존자 수는', c, '명입니다.')
        gabun=gabun+1

else :
    print('프로그램을 종료합니다.')

if c>b:
    print('최종 생존자 수는', c, '명이고, 상금은', a/c, '억원 입니다.')
elif c==0:
    print('생존자가 없으므로 상금을 받을 수 없습니다.')
