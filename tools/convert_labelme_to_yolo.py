import os
import json
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools import generate_density_maps

# Clases (solo gallina = 0)
CLASSES = {"gallina": 0}

input_dir = "data/images_yolo"
output_dir = "data/labels_yolo"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith(".json"):
        path = os.path.join(input_dir, file)
        with open(path, "r") as f:
            data = json.load(f)
        
        txt_name = file.replace(".json", ".txt")
        out_path = os.path.join(output_dir, txt_name)

        with open(out_path, "w") as out:
            for shape in data["shapes"]:
                label = shape["label"]
                if label not in CLASSES:
                    continue
                cls_id = CLASSES[label]

                # coordenadas
                (x1, y1), (x2, y2) = shape["points"]
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2
                w = abs(x2 - x1)
                h = abs(y2 - y1)

                # normalizar [0,1]
                img_w = data["imageWidth"]
                img_h = data["imageHeight"]
                cx /= img_w
                cy /= img_h
                w /= img_w
                h /= img_h

                out.write(f"{cls_id} {cx} {cy} {w} {h}\n")

print("✅ Conversión completa")
