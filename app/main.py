import sys
from infer_yolo import run_yolo

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py ruta_imagen")
        return

    img_path = sys.argv[1]
    count, out = run_yolo(img_path)
    print(f"[YOLO] Gallinas detectadas: {count}, guardado en {out}")

if __name__ == "__main__":
    main()