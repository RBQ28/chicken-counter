# app/infer_yolo.py
import os
import cv2
from ultralytics import YOLO

def run_yolo(image_path, model_path="models/yolo_best.pt", out_path="exports/results_yolo/out.jpg"):
    model = YOLO(model_path)
    results = model.predict(source=image_path, save=True, save_txt=False)

    # YOLO ya guarda automáticamente la imagen procesada en "runs/detect/predict..."
    # pero si quieres copiar el resultado a tu carpeta de exports:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cv2.imwrite(out_path, results[0].plot())

    return len(results[0].boxes), out_path

if __name__ == "__main__":
    img_path = "data/images_yolo/val/img0001.jpg"
    count, out = run_yolo(img_path)
    print(f"✅ YOLO detectó {count} gallinas")
    print(f"Resultado guardado en: {out}")
