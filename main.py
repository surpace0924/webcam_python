import os
import cv2
import time

def save_webcam_image():
    # 保存間隔を設定
    dt = 10

    # ウェブカメラにアクセス
    cap = cv2.VideoCapture(0)

    # 前回の保存時間を初期化
    last_save_time = time.time() - dt

    # 1分ごとの保存を行うためのループ
    while True:
        # 現在の時間を取得
        current_time = time.time()
        
        # カメラから画像を取得
        ret, frame = cap.read()

        if ret:
            # 時間経過したかを確認し、経過していれば画像を保存
            if current_time - last_save_time >= dt:

                # 保存用のファイル名を作成
                current_time_str = time.strftime("%Y%m%d%H%M%S")
                filename = os.path.join('captured', f'{current_time_str}.jpg')
                
                # 画像を保存
                cv2.imwrite(filename, frame)
                print(f"Saved: {filename}")

                # 前回の保存時間を更新
                last_save_time = current_time
        else:
            print("Error: Failed to capture image.")
            break
        
        time.sleep(dt/10)
        

    # カメラリソースの解放
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    save_webcam_image()
