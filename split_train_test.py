import scipy.io as sio
import os
import shutil
train_dir = "/home/daoduyhung/data/car/train"
test_dir = "/home/daoduyhung/data/car/test"

train_annos_path = "annos/cars_train_annos.mat"
test_annos_path = "annos/cars_test_annos.mat"
full_annos_path = "annos/cars_annos.mat"

def create_folder():
    num_classes = 196
    for dir in [train_dir, test_dir]:
        for i in range(num_classes):
            os.makedirs(os.path.join(dir, str(i+1)), exist_ok=True)

def format_name(name):
    import re
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    return name

def move_img(dir, annos_path):
    annos = sio.loadmat(annos_path)
    annotations = annos['annotations'][0]
    for anno in annotations:
        img_name = anno[5][0]
        class_id = anno[4][0][0]
        shutil.move(os.path.join(dir, img_name), os.path.join(dir, str(class_id), img_name))

def rename_folder(dir):
    classes = sio.loadmat(full_annos_path)['class_names'][0]
    classes = [c[0] for c in classes]
    for i, class_name in enumerate(classes):
        class_name = format_name(class_name)
        os.rename(os.path.join(dir, str(i+1)), os.path.join(dir, f'{i+1:03}.{class_name}'))

if __name__ == '__main__':
    create_folder()
    move_img(train_dir, train_annos_path)
    move_img(test_dir, test_annos_path)
    rename_folder(train_dir)
    rename_folder(test_dir)
    