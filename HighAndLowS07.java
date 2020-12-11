package jp.co.f1.superintro.ch08;

import java.util.Scanner;

public class HighAndLowS07 {

	public static void main(String[] args) {

				//タイトル
				System.out.println("************");
				System.out.println("* High&Low *");
				System.out.println("************");

				//空白
				System.out.println("");

				//無限ループでゲームに勝った場合にループさせる
				while(true) {

				//変数leftcard1に１～９のランダムな整数を代入
						int leftcard=(int)(Math.random()*9)+1;
						int rightcard=(int)(Math.random()*9)+1;



				System.out.println(" [問題表示]");
				//画面にトランプを並べる
				System.out.println("*****  *****");
				System.out.println("*   *  * * *");
				System.out.println("* "+leftcard+" *  * * *");
				System.out.println("*   *  * * *");
				System.out.println("*****  *****");

				//HighかLowか選択させる
				Scanner select=new Scanner(System.in);
				System.out.print("High or Low ?(h/l)>");
				String sc=select.nextLine();

				if(sc.equals("h")) {
					System.out.println("→Highを選択しました。");
				}else if(!(sc.equals("h"))){
					System.out.println("→Lowを選択しました。");
				}

				//空白
				System.out.println("");

				//ゲーム結果
				System.out.println(" [結果表示]");
				//画面にトランプを並べる
				System.out.println("*****  *****");
				System.out.println("*   *  *   *");
				System.out.println("* "+leftcard+" *  * "+rightcard+" *");
				System.out.println("*   *  *   *");
				System.out.println("*****  *****");

				//左側と右側の数を比較してHighかLowか判断し判定結果を変数resultに代入する
				String result;
				if(leftcard<rightcard) {
					 result="h";
				}else if(leftcard>rightcard){
					 result="l";
				}else{
					 result=sc;
				}

				//勝敗結果のメッセージを画面に表示
				if(result.equals(sc)) {
					System.out.println("You Win!");
					System.out.println("");//空白
				}else if(!(result.equals(sc))) {
					System.out.println("You Lose...");
					System.out.println("");//空白
				}
				//外れた場合にループ抜ける
				if(!(result.equals(sc))) {
					break;
				}

			}

				//空白
				System.out.println("");
				//ゲーム終了
				System.out.println("--ゲーム終了--");


	}

}
