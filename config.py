import os.path as osp

''' data iter setting '''
# train_root = '/home/wangjq/license_plate_dataset/licence-plate/train'
# val_root = '/home/wangjq/license_plate_dataset/licence-plate/val'
train_root = 'data/double-recognition-7/train'
val_root = 'data/double-recognition-7/val'

workers = 8
batch_size = 24
input_size = (80, 192)
pixel_mean = [0.485, 0.456, 0.406]
pixel_std = [0.229, 0.224, 0.225]
bright_prob = 0.2
saturation_prob = 0.2
contrast_prob = 0.2
hue_prob = 0.2
grayScale_prob = 0.2
pad = 3

text_length = 7

# provinces = "BCEGHJKLQSVWZ皖沪津渝冀晋蒙辽吉黑苏浙京闽赣鲁豫鄂湘粤桂琼川贵云藏陕甘青宁新"
# alphabets = "学挂警港澳ABCDEFGHJKLMNPQRSTUVWXYZ0123456789川粤-**"

provinces = "皖沪津渝冀晋蒙辽吉黑苏浙京闽赣鲁豫鄂湘粤桂琼川贵云藏陕甘青宁新学挂警港澳武ABCDEFGHJKLMNPQRSTUVWXYZ0123456789-"

provinces2idx = {v: k for k, v in dict(enumerate(provinces)).items()}
# alphabets2idx = {v: k for k, v in dict(enumerate(alphabets)).items()}


''' solver setting '''
nepoch = 40
device = 'cuda'
device_id = "3"

pre_trained = ''
output = 'models/logs'
displayInterval = 100
num_test_display = 10
lr = 0.001
beta1 = 0.9
adam = False
adadelta = True
keep_ratio = False
random_sample = False
manual_seed = 666
nc = 3
lr_step_size = 15
lr_gamma = 0.5

# resume_file = "restart"
# resume_file = "models/trained/DpNet_AM_SW_F128_acc0.98694.pth"
# resume_file = "models/logs/DpNetV3_SR_Acc0.98285.pth"
resume_file = "models/logs/DpNetV3_AM_Double_acc0.93691.pth"
