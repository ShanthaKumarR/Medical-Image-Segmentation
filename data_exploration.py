import numpy as np
import nibabel as nib
import itk
import itkwidgets
from ipywidgets import interact, interactive, IntSlider, ToggleButtons
import matplotlib.pyplot as plt
import seaborn as sns

# path to the train image directory 
train_dir = 'D:/material_science/mri_data/Task01_BrainTumour/imagesTr/BRATS_001.nii.gz'
# path to the train label directory 
label_dir = 'D:/material_science/mri_data/Task01_BrainTumour/labelsTr/BRATS_001.nii.gz'
classes_dict = {
    'Normal': 0.,
    'Edema': 1.,
    'Non-enhancing tumor': 2.,
    'Enhancing tumor': 3. 
}


class data_explorations:
    def __init__(self, train_dir, label_dir, classes_dict):
        self.train_dir = train_dir
        self.label_dir = label_dir
        self.classes_dict = classes_dict 
    def load_data_label(self):
        image_obj = nib.load(self.train_dir)      
        image_data = image_obj.get_fdata()       
        print(image_data.shape)
        return image_data
    
    def data_visualization(self, channel = 2):
        image_data = self.load_data_label()
        plt.figure(figsize=(16,4))
        for j in range(3):
            maxval = 154
            i = np.random.randint(0, maxval)
            print(f"Plotting Layer {i} Channel {channel} of Image")    
            plt.subplot(131+j)
            plt.title(f"Layer {i} Channel {channel}", fontsize=16)    
            plt.imshow(image_data[:, :, i, channel], cmap='gray')
            plt.axis('off');
        plt.show()

    def explore_label(self):
        label_obj = nib.load(self.label_dir)
        label_obj = label_obj.get_fdata()
        return label_obj

    def label_visualization(self, layer = 75):
        label_array = self.explore_label()
        fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(50, 30))
        for i in range(4):
            img_label_str = list(self.classes_dict.keys())[i]
            img = label_array[:,:,layer]
            mask = np.where(img == classes_dict[img_label_str], 255, 0)
            ax[i].imshow(mask)
            ax[i].set_title(f"Layer {layer} for {img_label_str}", fontsize=15)
            ax[i].axis('off')
        plt.tight_layout()
        plt.show()



X = data_explorations(train_dir = train_dir, label_dir = label_dir, classes_dict=classes_dict)
X.load_data_label()
X.data_visualization()
X.label_visualization()