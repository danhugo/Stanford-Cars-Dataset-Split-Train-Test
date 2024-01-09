The most currently available **Standford Cars Dataset** you can find is downloaded from [kaggle](https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset?select=cars_annos.mat). It contains:
```
cars_train
    00001.jpg
    ...
    08144.jpg

cars_test
    00001.jpg
    ...
    08041.jpg

cars_annos.mat
```

However, cars_annos.mat only has annotations for images from the complete folder
```
['car_imgs/000001.jpg', ..., ('class','0'), ('test','0')],
...
['car_imgs/016185.jpg', ..., ('class','0'), ('test','0')],

``` 
, which is impossible for user to obtain Train/Test folders.

This repository comes to address this problem. 

# Annotation Files
- `cars_annos.mat` is downloaded from Kaggle
- `cars_test_annos.mat` and `cars_train_annos.mat` download links are no longer available. If you can find it please notify me.
# Run
Modify path in `split_train_test.py`
```
python split_train_test.py
```