# encoding: utf-8
import openpyxl
import time
import os

def teacher():
    localtime = time.localtime(time.time())
    curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    day = int(time.strftime("%d", time.localtime()))

    namelistmorning = []
    namelistnight = []

    molist = [
        14775936917,  # 李晨玮
        15502011622,  # 刘金金
        17680241606,  # 郭凯
        17327567819]  # 蒋洋

    path = os.path.join(os.path.abspath(__file__).split('.')[0][:-6],
                        'files', '12月排班表.xlsx')

    wb = openpyxl.load_workbook(path)

    ws = wb.active
    for col in ws.iter_cols(min_col=3, values_only=False):
        if int(col[0].value) == day:
            for c in range(1, 5):
                if col[c].value == '班':

                    namelistmorning.append(molist[c-1])

                elif col[c].value == '晚班':

                    namelistnight.append(molist[c-1])

    return namelistmorning, namelistnight


def infos():
    print(1)
