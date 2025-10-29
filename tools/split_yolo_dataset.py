import os
import shutil
import random

# Rutas base
img_dir = "data/images_yolo"
label_dir = "data/labels_yolo"

out_img_train = "data/images_yolo/train"
out_img_val = "data/images_yolo/val"
out_label_train = "data/labels_yolo/train"
out_label_val = "data/labels_yolo/val"

# Crear carpetas si no existen
for d in [out_img_train, out_img_val, out_label_train, out_label_val]:
    os.makedirs(d, exist_ok=True)

# Listar imágenes
images = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png'))]
random.shuffle(images)

# 80% train, 20% val
split_idx = int(0.8 * len(images))
train_imgs = images[:split_idx]
val_imgs = images[split_idx:]

def move_files(img_list, out_img_dir, out_label_dir):
    for img in img_list:
        # mover imagen
        src_img = os.path.join(img_dir, img)
        dst_img = os.path.join(out_img_dir, img)
        shutil.copy(src_img, dst_img)

        # mover label correspondiente
        label_name = os.path.splitext(img)[0] + ".txt"
        src_label = os.path.join(label_dir, label_name)
        dst_label = os.path.join(out_label_dir, label_name)
        if os.path.exists(src_label):
            shutil.copy(src_label, dst_label)
        else:
            print(f"⚠️ No se encontró label para {img}")

# Mover train y val
move_files(train_imgs, out_img_train, out_label_train)
move_files(val_imgs, out_img_val, out_label_val)

print(f"✅ Dataset dividido: {len(train_imgs)} train, {len(val_imgs)} val")
