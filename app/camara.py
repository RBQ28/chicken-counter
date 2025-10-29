import cv2
from ultralytics import YOLO

def run_camera():
    cap = cv2.VideoCapture("data/videos/pollos1.mp4")  # O usa 0 para webcam
    if not cap.isOpened():
        print("❌ No se pudo abrir la cámara o video")
        return

    model = YOLO("models/yolo_best.pt")
    max_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, verbose=False)
        count = len(results[0].boxes)
        if count > max_count:
            max_count = count

        frame = results[0].plot()
        cv2.putText(frame, f"YOLO: {count}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Max pollos detectados: {max_count}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Chicken Counter", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_camera()
