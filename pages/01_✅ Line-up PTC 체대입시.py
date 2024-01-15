import os
from PIL import Image
import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts


def load_body_image(name):
    file_lst = os.listdir('data')
    print(file_lst)
    file_lst = [file for file in file_lst if file.endswith('png')]
    if name + '.png' in file_lst:
        img_path = 'data/' + name + '.png'
    elif name + '.jpg' in file_lst:
        img_path = 'data/' + name + '.jpg'
    else:
        st.error(f"Image {name} not found.")
        return None
    img = Image.open(img_path)
    return img

def main(data):
    try:
        name = side_bar()
        #print(name)
        for col in data.columns:
            if col != '이름':
                data[col] = data[col].astype(float)
        # 이름 데이터 선택
        if '😎 ' in name:
            name = name.replace('😎 ', '')
        idx = data[data['이름'] == name].index
        idx = idx.values[0]
    
        # 성별별로 육각 차트 표시
        if name.split('(')[1] == '남)':
            # 속성 값 정리
            lst = data.loc[idx].tolist()[1:-1]
            if 8.3 - lst[1] > 0:
                lst[1] = 8.3 - (8.3 - lst[1]) + 0.5
            else:
                lst[1] = 8.3 + (8.3 - lst[1])
    
            if 13.8 - lst[2] > 0:
                lst[2] = 13.8 - (13.8 - lst[2])
            else:
                lst[2] = 13.8 + (13.8 - lst[2]) + 0.5
    
            option = Option_man(data, name, idx, lst)
            charts = st_echarts(option, height="500px",)
    
    
        else:
            # 속성 값 정리
            lst = data.loc[idx].tolist()[1:-1]
            if 8.3 - lst[1] > 0:
                lst[1] = 8.3 - (8.3 - lst[1]) + 0.5
            else:
                lst[1] = 8.3 + (8.3 - lst[1])
    
            if 13.8 - lst[2] > 0:
                lst[2] = 13.8 - (13.8 - lst[2]) + 0.5
            else:
                lst[2] = 13.8 + (13.8 - lst[2])
    
            option = Option_woman(data, name, idx, lst)
            charts = st_echarts(option, height="500px")
        tab0, tab3 = st.tabs(['개인현황', '인바디'])
    
    
        data2 = data.copy()
        #data2 = data2.rename(columns={'m_10': '10m', 'm_20': '20m'})
        data2_view = data2[data2['이름'] == name]
        # 개인 점수 표시테이블
        one_table = 점수표준화_개인(data2_view, name)
        tab0.dataframe(one_table.style.set_properties(**{'background-color': 'black', 'color': 'white'}),hide_index=True)
    
        # tab 나누기
        tab1, tab2 = st.tabs(["전체 상황판", "월별통계"])
    
    
        # 각 운동 점수화 및 전체 상황 테이블
        tab1.dataframe(점수표준화(data), column_config={'m_10': '10m', 'm_20': '20m'}, hide_index=True)
        # 인바디 이미지
        print('create table 표준화')
        img = load_body_image(name)
        tab3.image(img)
    except Exception as e:
        print(e)
        pass


# 제자리, m_10, m_20, 윗몸, 배근력, 좌전굴
def check_점수(data):
    제자리 = []
    m_10 = []
    m_20 = []
    윗몸 = []
    배근력 = []
    좌전굴 = []

    for idx, row in data.iterrows():
        if row['이름'].split('(')[1] == '남)':
            if row['제자리멀리뛰기'] >= 300:
                제자리.append(100)
            elif 298 <= row['제자리멀리뛰기'] <= 299:
                제자리.append(98)
            elif 296 <= row['제자리멀리뛰기'] <= 297:
                제자리.append(96)
            elif 294 <= row['제자리멀리뛰기'] <= 295:
                제자리.append(94)
            elif 292 <= row['제자리멀리뛰기'] <= 293:
                제자리.append(92)
            elif 290 <= row['제자리멀리뛰기'] <= 291:
                제자리.append(90)
            elif 288 <= row['제자리멀리뛰기'] <= 289:
                제자리.append(88)
            elif 286 <= row['제자리멀리뛰기'] <= 287:
                제자리.append(86)
            elif 284 <= row['제자리멀리뛰기'] <= 285:
                제자리.append(84)
            elif 282 <= row['제자리멀리뛰기'] <= 283:
                제자리.append(82)
            elif 280 <= row['제자리멀리뛰기'] <= 281:
                제자리.append(80)
            elif 278 <= row['제자리멀리뛰기'] <= 279:
                제자리.append(78)
            elif 276 <= row['제자리멀리뛰기'] <= 277:
                제자리.append(76)
            elif 274 <= row['제자리멀리뛰기'] <= 275:
                제자리.append(74)
            elif 272 <= row['제자리멀리뛰기'] <= 273:
                제자리.append(72)
            elif 270 <= row['제자리멀리뛰기'] <= 271:
                제자리.append(70)
            elif 268 <= row['제자리멀리뛰기'] <= 269:
                제자리.append(68)
            elif 266 <= row['제자리멀리뛰기'] <= 267:
                제자리.append(66)
            elif 264 <= row['제자리멀리뛰기'] <= 265:
                제자리.append(64)
            elif 262 <= row['제자리멀리뛰기'] <= 263:
                제자리.append(62)
            elif 260 <= row['제자리멀리뛰기'] <= 261:
                제자리.append(60)
            elif 258 <= row['제자리멀리뛰기'] <= 259:
                제자리.append(58)
            elif 256 <= row['제자리멀리뛰기'] <= 257:
                제자리.append(56)
            elif 254 <= row['제자리멀리뛰기'] <= 255:
                제자리.append(54)
            elif 252 <= row['제자리멀리뛰기'] <= 253:
                제자리.append(52)
            elif row['제자리멀리뛰기'] <= 251:
                제자리.append(50)

            if row['m_10'] < 8.3 and row['m_10'] > 0:
                m_10.append(100)
            elif 8.3 <= row['m_10'] <= 8.5:
                m_10.append(95)
            elif 8.6 <= row['m_10'] <= 8.8:
                m_10.append(90)
            elif 8.9 <= row['m_10'] <= 9.1:
                m_10.append(85)
            elif 9.2 <= row['m_10'] <= 9.4:
                m_10.append(80)
            elif 9.5 <= row['m_10'] <= 9.7:
                m_10.append(75)
            elif 9.8 <= row['m_10'] <= 10.0:
                m_10.append(70)
            elif 10.1 <= row['m_10'] <= 10.3:
                m_10.append(65)
            elif 10.4 <= row['m_10'] <= 10.6:
                m_10.append(60)
            elif 10.7 <= row['m_10'] <= 10.9:
                m_10.append(55)
            elif 11.0 <= row['m_10'] <= 11.2:
                m_10.append(50)
            elif row['m_10'] >= 11.3:
                m_10.append(23)
            else:
                m_10.append(23)



            if row['배근력'] >= 220:
                배근력.append(100)
            elif 216 <= row['배근력'] <= 219.9:
                배근력.append(98)
            elif 212 <= row['배근력'] <= 215.9:
                배근력.append(96)
            elif 208 <= row['배근력'] <= 211.9:
                배근력.append(94)
            elif 204 <= row['배근력'] <= 207.9:
                배근력.append(92)
            elif 200 <= row['배근력'] <= 203.9:
                배근력.append(90)
            elif 196 <= row['배근력'] <= 199.9:
                배근력.append(88)
            elif 192 <= row['배근력'] <= 195.9:
                배근력.append(86)
            elif 188 <= row['배근력'] <= 191.9:
                배근력.append(84)
            elif 184 <= row['배근력'] <= 187.9:
                배근력.append(82)
            elif 180 <= row['배근력'] <= 183.9:
                배근력.append(80)
            elif 176 <= row['배근력'] <= 179.9:
                배근력.append(78)
            elif 172 <= row['배근력'] <= 175.9:
                배근력.append(76)
            elif 168 <= row['배근력'] <= 171.9:
                배근력.append(74)
            elif 164 <= row['배근력'] <= 167.9:
                배근력.append(72)
            elif 160 <= row['배근력'] <= 163.9:
                배근력.append(70)
            elif 156 <= row['배근력'] <= 159.9:
                배근력.append(68)
            elif 152 <= row['배근력'] <= 155.9:
                배근력.append(66)
            elif 148 <= row['배근력'] <= 151.9:
                배근력.append(64)
            elif 144 <= row['배근력'] <= 147.9:
                배근력.append(62)
            elif 140 <= row['배근력'] <= 143.9:
                배근력.append(60)
            elif 136 <= row['배근력'] <= 139.9:
                배근력.append(58)
            elif 132 <= row['배근력'] <= 135.9:
                배근력.append(56)
            elif 128 <= row['배근력'] <= 131.9:
                배근력.append(54)
            elif 124 <= row['배근력'] <= 127.9:
                배근력.append(52)
            elif row['배근력'] <= 123.9:
                배근력.append(50)



            if row['m_20'] <= 13.8 and row['m_20'] > 0:
                m_20.append(100)
            elif 13.9 <= row['m_20'] <= 14.0:
                m_20.append(95)
            elif 14.1 <= row['m_20'] <= 14.2:
                m_20.append(90)
            elif 14.3 <= row['m_20'] <= 14.4:
                m_20.append(85)
            elif 14.5 <= row['m_20'] <= 14.6:
                m_20.append(80)
            elif 14.7 <= row['m_20'] <= 14.8:
                m_20.append(75)
            elif 14.9 <= row['m_20'] <= 15.0:
                m_20.append(70)
            elif 15.1 <= row['m_20'] <= 15.2:
                m_20.append(65)
            elif 15.3 <= row['m_20'] <= 15.4:
                m_20.append(60)
            elif 15.5 <= row['m_20'] <= 15.6:
                m_20.append(55)
            elif 15.7 <= row['m_20'] <= 15.8:
                m_20.append(50)
            elif 15.9 <= row['m_20'] <= 16.0:
                m_20.append(45)
            elif 16.1 <= row['m_20'] <= 16.2:
                m_20.append(40)
            elif 16.3 <= row['m_20'] <= 16.4:
                m_20.append(35)
            elif 16.5 <= row['m_20'] <= 16.6:
                m_20.append(30)
            elif 16.7 <= row['m_20'] <= 16.8:
                m_20.append(25)
            elif 16.9 <= row['m_20'] <= 17.0:
                m_20.append(20)
            elif 17.1 <= row['m_20'] <= 17.2:
                m_20.append(15)
            elif 17.3 <= row['m_20'] <= 17.4:
                m_20.append(10)
            elif 17.5 <= row['m_20'] <= 17.6:
                m_20.append(5)
            elif 17.7 <= row['m_20'] <= 17.8:
                m_20.append(0)
            elif row['m_20'] >= 17.9:
                m_20.append(0)
            else:
                m_20.append(0)




            if row['윗몸일으키기'] >=75:
                윗몸.append(25)
            elif row['윗몸일으키기'] == 74:
                윗몸.append(24)
            elif row['윗몸일으키기'] == 73:
                윗몸.append(23)
            elif row['윗몸일으키기'] == 72:
                윗몸.append(22)
            elif row['윗몸일으키기'] == 71:
                윗몸.append(21)
            elif row['윗몸일으키기'] == 70:
                윗몸.append(20)
            elif row['윗몸일으키기'] == 69:
                윗몸.append(19)
            elif row['윗몸일으키기'] == 68:
                윗몸.append(18)
            elif row['윗몸일으키기'] == 67:
                윗몸.append(17)
            elif row['윗몸일으키기'] == 66:
                윗몸.append(16)
            elif row['윗몸일으키기'] == 65:
                윗몸.append(15)
            elif row['윗몸일으키기'] == 64:
                윗몸.append(14)
            elif row['윗몸일으키기'] == 63:
                윗몸.append(13)
            elif row['윗몸일으키기'] == 62:
                윗몸.append(12)
            elif row['윗몸일으키기'] == 61:
                윗몸.append(11)
            elif row['윗몸일으키기'] <= 60:
                윗몸.append(10)


            if row['좌전굴'] >=26:
                좌전굴.append(50)
            elif row['좌전굴'] == 25:
                좌전굴.append(49)
            elif row['좌전굴'] == 24:
                좌전굴.append(48)
            elif row['좌전굴'] == 23:
                좌전굴.append(47)
            elif row['좌전굴'] == 22:
                좌전굴.append(46)
            elif row['좌전굴'] == 21:
                좌전굴.append(45)
            elif row['좌전굴'] == 20:
                좌전굴.append(44)
            elif row['좌전굴'] == 19:
                좌전굴.append(43)
            elif row['좌전굴'] == 18:
                좌전굴.append(42)
            elif row['좌전굴'] == 17:
                좌전굴.append(41)
            elif row['좌전굴'] == 16:
                좌전굴.append(40)
            elif row['좌전굴'] == 15:
                좌전굴.append(39)
            elif row['좌전굴'] == 14:
                좌전굴.append(38)
            elif row['좌전굴'] == 13:
                좌전굴.append(37)
            elif row['좌전굴'] == 12:
                좌전굴.append(36)
            elif row['좌전굴'] <= 11:
                좌전굴.append(35)
            elif row['좌전굴'] <= 10:
                좌전굴.append(34)
            elif row['좌전굴'] <= 9:
                좌전굴.append(33)
            elif row['좌전굴'] <= 8:
                좌전굴.append(32)
            elif row['좌전굴'] <= 7:
                좌전굴.append(31)
            elif row['좌전굴'] <= 6:
                좌전굴.append(30)
            elif row['좌전굴'] <= 5:
                좌전굴.append(29)
            elif row['좌전굴'] <= 4:
                좌전굴.append(28)
            elif row['좌전굴'] <= 3:
                좌전굴.append(27)
            elif row['좌전굴'] <= 2:
                좌전굴.append(26)
            elif row['좌전굴'] <= 1:
                좌전굴.append(25)
            else:
                좌전굴.append(0)


        else:
            # 여자 --------------------------------
            if row['제자리멀리뛰기'] >= 250:
                제자리.append(100)
            elif 248 <= row['제자리멀리뛰기'] <= 249:
                제자리.append(98)
            elif 246 <= row['제자리멀리뛰기'] <= 247:
                제자리.append(96)
            elif 244 <= row['제자리멀리뛰기'] <= 245:
                제자리.append(94)
            elif 242 <= row['제자리멀리뛰기'] <= 243:
                제자리.append(92)
            elif 240 <= row['제자리멀리뛰기'] <= 241:
                제자리.append(90)
            elif 238 <= row['제자리멀리뛰기'] <= 239:
                제자리.append(88)
            elif 236 <= row['제자리멀리뛰기'] <= 237:
                제자리.append(86)
            elif 234 <= row['제자리멀리뛰기'] <= 235:
                제자리.append(84)
            elif 232 <= row['제자리멀리뛰기'] <= 233:
                제자리.append(82)
            elif 230 <= row['제자리멀리뛰기'] <= 231:
                제자리.append(80)
            elif 228 <= row['제자리멀리뛰기'] <= 229:
                제자리.append(78)
            elif 226 <= row['제자리멀리뛰기'] <= 227:
                제자리.append(76)
            elif 224 <= row['제자리멀리뛰기'] <= 225:
                제자리.append(74)
            elif 222 <= row['제자리멀리뛰기'] <= 223:
                제자리.append(72)
            elif 220 <= row['제자리멀리뛰기'] <= 221:
                제자리.append(70)
            elif 218 <= row['제자리멀리뛰기'] <= 219:
                제자리.append(68)
            elif 216 <= row['제자리멀리뛰기'] <= 217:
                제자리.append(66)
            elif 214 <= row['제자리멀리뛰기'] <= 215:
                제자리.append(64)
            elif 212 <= row['제자리멀리뛰기'] <= 213:
                제자리.append(62)
            elif 210 <= row['제자리멀리뛰기'] <= 211:
                제자리.append(60)
            elif 208 <= row['제자리멀리뛰기'] <= 209:
                제자리.append(58)
            elif 206 <= row['제자리멀리뛰기'] <= 207:
                제자리.append(56)
            elif 204 <= row['제자리멀리뛰기'] <= 205:
                제자리.append(54)
            elif 202 <= row['제자리멀리뛰기'] <= 203:
                제자리.append(52)
            elif row['제자리멀리뛰기'] <= 201:
                제자리.append(50)


            if row['m_10'] < 9.3 and row['m_10'] > 0:
                m_10.append(100)
            elif 9.3 <= row['m_10'] <= 9.5:
                m_10.append(95)
            elif 9.6 <= row['m_10'] <= 9.8:
                m_10.append(90)
            elif 9.9 <= row['m_10'] <= 10.1:
                m_10.append(85)
            elif 10.2 <= row['m_10'] <= 10.4:
                m_10.append(80)
            elif 10.5 <= row['m_10'] <= 10.7:
                m_10.append(75)
            elif 10.8 <= row['m_10'] <= 11.0:
                m_10.append(70)
            elif 11.1 <= row['m_10'] <= 11.3:
                m_10.append(65)
            elif 11.4 <= row['m_10'] <= 11.6:
                m_10.append(60)
            elif 11.7 <= row['m_10'] <= 11.9:
                m_10.append(55)
            elif 12.0 <= row['m_10'] <= 12.2:
                m_10.append(50)
            elif row['m_10'] >= 12.3:
                m_10.append(23)
            else:
                m_10.append(0)


            if row['배근력'] >= 140:
                배근력.append(100)
            elif 136 <= row['배근력'] <= 139.9:
                배근력.append(98)
            elif 132 <= row['배근력'] <= 135.9:
                배근력.append(96)
            elif 128 <= row['배근력'] <= 131.9:
                배근력.append(94)
            elif 124 <= row['배근력'] <= 127.9:
                배근력.append(92)
            elif 120 <= row['배근력'] <= 123.9:
                배근력.append(90)
            elif 116 <= row['배근력'] <= 119.9:
                배근력.append(88)
            elif 112 <= row['배근력'] <= 115.9:
                배근력.append(86)
            elif 108 <= row['배근력'] <= 111.9:
                배근력.append(84)
            elif 104 <= row['배근력'] <= 107.9:
                배근력.append(82)
            elif 100 <= row['배근력'] <= 103.9:
                배근력.append(80)
            elif 96 <= row['배근력'] <= 99.9:
                배근력.append(78)
            elif 92 <= row['배근력'] <= 95.9:
                배근력.append(76)
            elif 88 <= row['배근력'] <= 92.9:
                배근력.append(74)
            elif 84 <= row['배근력'] <= 87.9:
                배근력.append(72)
            elif 80 <= row['배근력'] <= 83.9:
                배근력.append(70)
            elif 76 <= row['배근력'] <= 79.9:
                배근력.append(68)
            elif 72 <= row['배근력'] <= 75.9:
                배근력.append(66)
            elif 68 <= row['배근력'] <= 71.9:
                배근력.append(64)
            elif 62 <= row['배근력'] <= 67.9:
                배근력.append(62)
            elif 58 <= row['배근력'] <= 61.9:
                배근력.append(60)
            elif 54 <= row['배근력'] <= 57.9:
                배근력.append(58)
            elif 50 <= row['배근력'] <= 53.9:
                배근력.append(56)
            elif 46 <= row['배근력'] <= 49.9:
                배근력.append(54)
            elif 42 <= row['배근력'] <= 45.9:
                배근력.append(52)
            elif row['배근력'] <= 41.9:
                배근력.append(50)



            if row['m_20'] <= 15.6 and row['m_20'] > 0:
                m_20.append(100)
            elif 15.7 <= row['m_20'] <= 15.8:
                m_20.append(95)
            elif 15.9 <= row['m_20'] <= 16.0:
                m_20.append(90)
            elif 16.1 <= row['m_20'] <= 16.2:
                m_20.append(85)
            elif 16.3 <= row['m_20'] <= 16.4:
                m_20.append(80)
            elif 16.5 <= row['m_20'] <= 16.6:
                m_20.append(75)
            elif 16.7 <= row['m_20'] <= 16.8:
                m_20.append(70)
            elif 16.9 <= row['m_20'] <= 17.0:
                m_20.append(65)
            elif 17.1 <= row['m_20'] <= 17.2:
                m_20.append(60)
            elif 17.3 <= row['m_20'] <= 17.4:
                m_20.append(55)
            elif 17.5 <= row['m_20'] <= 17.6:
                m_20.append(50)
            elif 17.7 <= row['m_20'] <= 17.8:
                m_20.append(45)
            elif 17.9 <= row['m_20'] <= 18.0:
                m_20.append(40)
            elif 18.1 <= row['m_20'] <= 18.2:
                m_20.append(35)
            elif 18.3 <= row['m_20'] <= 18.4:
                m_20.append(30)
            elif 18.5 <= row['m_20'] <= 18.6:
                m_20.append(25)
            elif 18.7 <= row['m_20'] <= 18.8:
                m_20.append(20)
            elif 18.9 <= row['m_20'] <= 19.0:
                m_20.append(15)
            elif 19.1 <= row['m_20'] <= 19.2:
                m_20.append(10)
            elif 19.3 <= row['m_20'] <= 19.4:
                m_20.append(5)
            elif 19.5 <= row['m_20'] <= 19.6:
                m_20.append(0)
            elif row['m_20'] >= 19.7:
                m_20.append(0)
            else:
                m_20.append(0)


            if row['윗몸일으키기'] >=75:
                윗몸.append(25)
            elif row['윗몸일으키기'] == 74:
                윗몸.append(24)
            elif row['윗몸일으키기'] == 73:
                윗몸.append(23)
            elif row['윗몸일으키기'] == 72:
                윗몸.append(22)
            elif row['윗몸일으키기'] == 71:
                윗몸.append(21)
            elif row['윗몸일으키기'] == 70:
                윗몸.append(20)
            elif row['윗몸일으키기'] == 69:
                윗몸.append(19)
            elif row['윗몸일으키기'] == 68:
                윗몸.append(18)
            elif row['윗몸일으키기'] == 67:
                윗몸.append(17)
            elif row['윗몸일으키기'] == 66:
                윗몸.append(16)
            elif row['윗몸일으키기'] == 65:
                윗몸.append(15)
            elif row['윗몸일으키기'] == 64:
                윗몸.append(14)
            elif row['윗몸일으키기'] == 63:
                윗몸.append(13)
            elif row['윗몸일으키기'] == 62:
                윗몸.append(12)
            elif row['윗몸일으키기'] == 61:
                윗몸.append(11)
            elif row['윗몸일으키기'] <= 60:
                윗몸.append(10)


            if row['좌전굴'] >=32:
                좌전굴.append(50)
            elif row['좌전굴'] == 31:
                좌전굴.append(49)
            elif row['좌전굴'] == 30:
                좌전굴.append(48)
            elif row['좌전굴'] == 29:
                좌전굴.append(47)
            elif row['좌전굴'] == 28:
                좌전굴.append(46)
            elif row['좌전굴'] == 27:
                좌전굴.append(45)
            elif row['좌전굴'] == 26:
                좌전굴.append(44)
            elif row['좌전굴'] == 25:
                좌전굴.append(43)
            elif row['좌전굴'] == 24:
                좌전굴.append(42)
            elif row['좌전굴'] == 23:
                좌전굴.append(41)
            elif row['좌전굴'] == 22:
                좌전굴.append(40)
            elif row['좌전굴'] == 21:
                좌전굴.append(39)
            elif row['좌전굴'] == 20:
                좌전굴.append(38)
            elif row['좌전굴'] == 19:
                좌전굴.append(37)
            elif row['좌전굴'] == 18:
                좌전굴.append(36)
            elif row['좌전굴'] <= 17:
                좌전굴.append(35)
            elif row['좌전굴'] <= 16:
                좌전굴.append(34)
            elif row['좌전굴'] <= 15:
                좌전굴.append(33)
            elif row['좌전굴'] <= 14:
                좌전굴.append(32)
            elif row['좌전굴'] <= 13:
                좌전굴.append(31)
            elif 11 <= row['좌전굴'] <= 12:
                좌전굴.append(30)
            elif 9 <=row['좌전굴'] <= 10:
                좌전굴.append(29)
            elif 7 <= row['좌전굴'] <= 8:
                좌전굴.append(28)
            elif 5 <= row['좌전굴'] <= 6:
                좌전굴.append(27)
            elif 3 <= row['좌전굴'] <= 4:
                좌전굴.append(26)
            elif 1 <= row['좌전굴'] <= 2:
                좌전굴.append(25)
            else:
                좌전굴.append(0)

    return 제자리, m_10, m_20, 윗몸, 배근력, 좌전굴

def 점수표준화(data):
    data_v = data.copy()
    data_v['제v'], data_v['m10_v'], data_v['m20_v'], data_v['윗v'], data_v['배v'], data_v['좌v'] = check_점수(data)
    data_v['총합'] = data_v['제v'] +  data_v['m10_v'] + data_v['m20_v'] + data_v['윗v'] + data_v['배v'] + data_v['좌v']

    data_view = data_v[['이름', '제자리멀리뛰기', 'm_10', 'm_20', '윗몸일으키기', '배근력', '좌전굴', '총합']]
    data_view = data_view.sort_values('총합', ascending=False)
    data_view = data_view.rename(columns = {'m_10': '10m', 'm_20':'20m', '총합': '🏋️총합🏋️'})

    # 타입 변경
    data_view['제자리멀리뛰기'] = data_view['제자리멀리뛰기'].map(lambda x: str(x).split('.')[0])
    data_view['윗몸일으키기'] = data_view['윗몸일으키기'].map(lambda x: str(x).split('.')[0])
    data_view['좌전굴'] = data_view['좌전굴'].map(lambda x: str(x).split('.')[0])
    data_view['배근력'] = data_view['배근력'].map(lambda x: str(x).split('.')[0])
    data_view['10m'] = data_view['10m'].map(lambda x: str(x).split('.')[0] + '.'+str(x).split('.')[1][:2])
    data_view['20m'] = data_view['20m'].map(lambda x: str(x).split('.')[0] + '.'+str(x).split('.')[1][:2])
    return data_view


def 점수표준화_개인(data, name):
    data_v = data.copy()
    data_v['제v'], data_v['m10_v'], data_v['m20_v'], data_v['윗v'], data_v['배v'], data_v['좌v'] = check_점수(data)
    data_v['총합'] = data_v['제v'] +  data_v['m10_v'] + data_v['m20_v'] + data_v['윗v'] + data_v['배v'] + data_v['좌v']

    data_view = data_v[['이름', '제자리멀리뛰기', 'm_10', 'm_20', '윗몸일으키기', '배근력', '좌전굴', '총합']]
    data_view = data_view.sort_values('총합', ascending=False)
    data_view = data_view.rename(columns = {'m_10': '10m', 'm_20':'20m', '총합': '🏋️총합🏋️'})

    # 타입 변경
    data_view['제자리멀리뛰기'] = data_view['제자리멀리뛰기'].map(lambda x: str(x).split('.')[0])
    data_view['윗몸일으키기'] = data_view['윗몸일으키기'].map(lambda x: str(x).split('.')[0])
    data_view['좌전굴'] = data_view['좌전굴'].map(lambda x: str(x).split('.')[0])
    data_view['배근력'] = data_view['배근력'].map(lambda x: str(x).split('.')[0])
    data_view['10m'] = data_view['10m'].map(lambda x: str(x).split('.')[0] + '.'+str(x).split('.')[1][:2])
    data_view['20m'] = data_view['20m'].map(lambda x: str(x).split('.')[0] + '.'+str(x).split('.')[1][:2])
    return data_view



def side_bar():
    name_lst = data['이름'].tolist()
    name_lst = ['😎 ' + name if name == '최영우(남)' else name for name in name_lst ]
    with st.sidebar:
        name = st.selectbox(
            "이름:",
            (name_lst),
            index=None,
            placeholder="Select contact method...",
        )
        st.markdown('<div style= "text-align: right;"> Copyright Line-up & Son</div>', unsafe_allow_html=True)
    return name


def Option_man(data, name, idx, lst):
    option = {
        "title": {"text": "💪 Line-up PTC"},
        "grid": {
            "backgroundColor": 'rgba(40, 40, 40, 1)',
            "show": True
        },
        "textStyle": {'color': '#FF8400', 'fontWeight': 'bold'},
        "legend": {"data": ["현재", "목표"]},
        "radar": {
            "indicator": [
                {"name": "제자리멀리뛰기 (순발력)", "max": 310},
                {"name": "10m (민첩성)", "max": 8.4},
                {"name": "20m (민첩성)", "max": 13.8},
                {"name": "윗몸일으키기 (근지구력)", "max": 78},
                {"name": "배근력 (근력)", "max": 235},
                {"name": "좌전굴 (유연성)", "max": 27}
            ]}
        ,


        "series": [
            {
                "name": "현재 vs 목표",
                "type": "radar",

                "data": [
                    {
                        "value": lst,
                        "name": "현재",
                        'lineStyle': {'color': 'rgba(0,0,205)'},
                        'areaStyle': {'color': 'rgba(0, 0, 205, 0.3)'}
                    },
                    {
                        "value": [int(300), int(8.3), int(13.8), int(75), int(226), int(26)],
                        "name": "목표",
                        "symbol": 'rect',
                        'symbolSize': '12',
                        'lineStyle': {'type':'dashed', 'color': 'rgba(255,0,0)'}

                    },
                ],
            }
        ],
    }
    #print(data.loc[0].tolist()[1:])
    return option


def Option_woman(data, name, idx, lst):
    option = {
        "title": {"text": "💪 너네 주스텟 몇이야?"},
        "grid": {
            "backgroundColor": 'rgba(40, 40, 40, 1)',
            "show": True
        },
        "textStyle": {'color': '#FF8400', 'fontWeight': 'bold'},
        "legend": {"data": ["현재", "목표"]},
        "radar": {
            "indicator": [
                {"name": "제자리멀리뛰기 (순발력)", "max": 250},
                {"name": "10m (민첩성)", "max": 9.3},
                {"name": "20m (민첩성)", "max": 15.6},
                {"name": "윗몸일으키기 (근지구력)", "max": 75},
                {"name": "배근력 (근력)", "max": 146},
                {"name": "좌전굴 (유연성)", "max": 32},
            ]
        },

        # "tooltip": {"triggerOn": "click",},

        "series": [
            {
                "name": "현재 vs 목표",
                "type": "radar",

                "data": [
                    {
                        "value": lst,
                        "name": "현재",
                        'lineStyle': {'color': 'rgba(0,0,205)'},
                        'areaStyle': {'color': 'rgba(0, 0, 205, 0.3)'}
                    },
                    {
                        "value": [int(250), int(9.3), int(15.6), int(75), int(146), int(32)],
                        "name": "목표",
                        "symbol": 'rect',
                        'symbolSize': '12',
                        'lineStyle': {'type':'dashed', 'color': 'rgba(255,0,0)'}
                    },
                ],
            }
        ],
    }
    #print(data.loc[0].tolist()[1:])
    return option





if __name__ == '__main__':
    # sys.argv = [
    #     "streamlit",
    #     "run",
    #     resolve_path("lineup.py"),
    #     "--global.developmentMode=false"]
    data = pd.read_excel('data/SMG_test.xlsx', sheet_name='status')
    main(data)
