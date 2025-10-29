# tools/extract_frames.py
import cv2
import os
import argparse

def extract_frames(video_path, output_dir, fps=1):
    """
    Extrae frames de un video y los guarda como imágenes.
    :param video_path: ruta al archivo de video (.mp4, .avi, etc.)
    :param output_dir: carpeta donde se guardan los frames
    :param fps: cantidad de frames por segundo a extraer
    """
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(round(video_fps / fps))

    count, saved = 0, 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % frame_interval == 0:
            filename = f"frame_{saved:05d}.jpg"
            cv2.imwrite(os.path.join(output_dir, filename), frame)
            saved += 1
        count += 1

    cap.release()
    print(f"✅ Extraídos {saved} frames en {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", help="Ruta al archivo de video")
    parser.add_argument("output_dir", help="Carpeta de salida para los frames")
    parser.add_argument("--fps", type=int, default=1, help="Frames por segundo a extraer")
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_dir, args.fps)
