import matplotlib.pyplot as plt
#グラフを描くためにmatplotlib.pyplotモジュールを読み込む。
import math
#三角関数を使うためにmathモジュールを読み込む。
import  numpy as np
#配列を作るためにnumpyモジュールを読み込む。
set={"sin","cos","tan","q"}
while True :
    #条件が満たされている間、以下の操作を繰り返す。
    question="sin,cos,tanのいずれかを半角で入力してください。qで終了:"
    tf=input(question)
    #「sin,cos,tanのいずれかを半角で入力してください。qで終了」と入力を求める。
    if tf not in set :
    #setの集合内の文字以外が入力された場合以下の操作を行う。
        print("指示された文字を入力してください。")
        continue
    #questionに入力された文字がsetの集合に含まれていなければ再度入力を求める。
    if tf=="q" :
    #qが入力された場合、以下の操作を行う。
        break
    #qを入力するとプログラムを終了する。
    angle="角度を入力してください。"
    x=input(angle)
    try :
        I=float(x)
    #ｘに入力された数値を浮動小数点に型変換する。
    except :
        print("値のみを入力してください。")
        continue
    #angleに入力した文字がfloatで浮動小数点に型変換できない時、再度入力を求める。
    if tf=="sin" :
       #sinと入力されたとき以下の操作を行う。
        Xs=range(-360,360)
        Ss=[math.sin(math.radians(d)) for d in Xs]
        """
        -360～360度までのリストを作り、リスト内の要素を順にdに取り出していき、
        math.radians(d)でラジアンに変換した値をmath.sinで計算する。
        """
        xmin,xmax=-360,360
        #X軸の最大値、最小値を設定する。
        ymin,ymax=-1,1
        #Y軸の最大値、最小値を設定する。
        plt.xlim([-360,360])
        #X軸をｰ360～360度まで図に記す。
        plt.ylim([-1,1])
        #Y軸をｰ1～1まで図に記す。
        plt.xticks(np.linspace(-360,360,25,endpoint=True))
        #角度（angle)の目盛りをｰ360～360度まで30度毎に図に記す。
        splot=round(math.sin(math.radians(I)),3)
        #sinの値を小数点第三位まで出力する。
        svalue="sinの値は{}です。"
        text=svalue.format(splot)
        #splotの値を{}の中に出力する。
        plt.plot(Xs,Ss)
        #sinのグラフをｰ360～360度まで描く。
        plt.plot(I,splot,marker="o")
        #入力された角度に対する値をy=sinxのグラフに点を打つ。
        plt.plot([xmin,xmax],[0,0],c="black")
        plt.plot([0,0],[ymin,ymax],c="black")
        #x=0,y=0の直線を作成する。
        print(text)
        #textを出力する。
        plt.grid(True)
        #グリッドをグラフに表示する。
        plt.xlabel("angle")
        #X軸のラベルをangleと表示する。
        plt.ylabel("value")
        #Y軸のラベルをvalueと表示する。
        plt.title("The value of sine")
        #グラフのタイトルをThe value of sineと表示する。
        plt.show()
        #作ったグラフを表示する。
    if tf=="cos" :
        #cosと入力されたとき以下の操作を行う。
        Xc=range(-360,360)
        Sc=[math.cos(math.radians(d)) for d in Xc]
        """
        -360～360度までのリストを作り、リスト内の要素を順にdに取り出していき、
        math.radians(d)でラジアンに変換した値をmath.cosで計算する。
        """
        xmin,xmax=-360,360
        #X軸の最大値、最小値を設定する。
        ymin,ymax=-1,1
        #Y軸の最大値、最小値を設定する。
        plt.xlim([-360,360])
        #X軸をｰ360～360度まで図に記す。
        plt.ylim([-1,1])
        #Y軸をｰ1～1まで図に記す。
        plt.xticks(np.linspace(-360,360,25,endpoint=True))
        #角度（angle)の目盛りをｰ360～360度まで30度毎に図に記す。
        cplot=round(math.cos(math.radians(I)),3)
        #cosの値を小数点第三位まで出力する。
        cvalue="cosの値は{}です。"
        text=cvalue.format(cplot)
        #cplotの値を{}の中に出力する。
        plt.plot(Xc,Sc)
        #cosのグラフをｰ360～360度まで描く。
        plt.plot(I,cplot,marker="o")
        #入力された角度に対する値をy=cosxのグラフに点を打つ。
        plt.plot([xmin,xmax],[0,0],c="black")
        plt.plot([0,0],[ymin,ymax],c="black")
        #x=0,y=0の直線を作成する。
        print(text)
        #textを出力する。
        plt.grid(True)
        #グリッドをグラフに表示する。
        plt.xlabel("angle")
        #X軸のラベルをangleと表示する。
        plt.ylabel("value")
        #Y軸のラベルをvalueと表示する。
        plt.title("The value of cosine")
        #グラフのタイトルをThe value of cosineと表示する。
        plt.show()
        #作ったグラフを表示する。
    if tf=="tan" :
        #tanと入力されたとき以下の操作を行う。
        Xt=range(-360,360)
        St=[math.tan(math.radians(d)) for d in Xt]
        """
        -360～360度までのリストを作り、リスト内の要素を順にdに取り出していき、
        math.radians(d)でラジアンに変換した値をmath.tanで計算する。
        """
        xmin,xmax=-360,360
        #X軸の最大値、最小値を設定する。
        ymin,ymax=-20,20
        #Y軸の最大値、最小値を設定する。
        plt.xlim([-360,360])
        #X軸をｰ360～360度まで図に記す。
        plt.ylim([-20,20])
        #Y軸をｰ20～20まで図に記す。
        plt.xticks(np.linspace(-360,360,25,endpoint=True))
        #角度（angle)の目盛りをｰ360～360度まで30度毎に図に記す。
        tplot=round(math.tan(math.radians(I)),3)
        #tanの値を小数点第三位まで出力する。
        tvalue="tanの値は{}です。"
        text=tvalue.format(tplot)
        #tplotの値を{}の中に出力する。
        plt.plot(Xt,St)
        #tanのグラフをｰ360～360度まで描く。
        plt.plot(I,tplot,marker="o")
        #入力された角度に対する値をy=tanxのグラフに点を打つ。
        plt.plot([xmin,xmax],[0,0],c="black")
        plt.plot([0,0],[ymin,ymax],c="black")
        #x=0,y=0の直線を作成する。
        print(text)
        #textを出力する。
        plt.grid(True)
        #グリッドをグラフに表示する。
        plt.xlabel("angle")
        #X軸のラベルをangleと表示する。
        plt.ylabel("value")
        #Y軸のラベルをvalueと表示する。
        plt.title("The value of tangent")
        #グラフのタイトルをThe value of tangentと表示する。
        plt.show()
        #作ったグラフを表示する。
