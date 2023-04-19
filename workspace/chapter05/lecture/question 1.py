def StarCount(height):
    h_cnt = s_cnt = 0

    while h_cnt < height:
        h_cnt +=1 #h_cnt = h_cnt + 1
        print('*'* h_cnt)
        s_cnt +=h_cnt #s_cnt = S_cnt + h_cnt

        return s_cnt

    print('star 개수 : ', StarCount(3))
