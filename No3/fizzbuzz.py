x = 0
while x == 0 :
    print('数字を入力してください')
    inputStr = input()
    if not inputStr.isdecimal() :
        print('数字以外の入力を確認しました')
        print('処理を終了します。')
        x = x + 1
    elif  int(inputStr) == 0 :
        print('処理を終了します。')
        x = x + 1
    else :
        print('入力された文字は'+inputStr+'です')
        print('fizbuzz判定を行います')
        # 以下にfizzbuzz判定を記載してください。
    

