import numpy as np
import nibabel
import matplotlib.pyplot as plt
from skimage import morphology
import argparse

#client = girder_client.GirderClient(apiUrl='http://34.229.214.79/api/v1')
#client.authenticate(apiKey='sLrP2DWBEUCZWnc5FiWT4I2WufA9AaFuRQm8bi1j')
#client.downloadItem(itemId='5963f36c4d2d8d07eb720b09', dest='.')

parser = argparse.ArgumentParser(description='ct bone segmentation example')
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
parser.add_argument('--closing-radius', required=False, type=int, default=2)
parser.add_argument('--threshold', required=False, type=int, default=250)

args = parser.parse_args()


#nib_img = nibabel.load('./head_ct_small.nii.gz')
nib_img = nibabel.load(args.input)

img = nib_img.get_data()
img.shape, img.dtype, type(img)
#print(img)
binary_img = img > args.threshold
closed_img = morphology.binary_closing(binary_img, selem=morphology.ball(radius=args.closing-radius))
out_img = nibabel.Nifti1Image(closed_img.astype(np.uint8), nib_img.affine)
#out_img.to_filename('./segmented_bones.nii.gz')
out_img.to_filename(args.output)
