import argparse
import json
import nibabel
import numpy as np


parser = argparse.ArgumentParser(
    prog='compare_images', description='compute similarity of two binary images')

parser.add_argument('--test', help='The path to the test image.', required=True)
parser.add_argument('--truth', help='The path to the ground truth image.', required=True)
args = parser.parse_args()


test_nib_img = nibabel.load(args.test)
truth_nib_img = nibabel.load(args.truth)
test_img = test_nib_img.get_data()
truth_img = truth_nib_img.get_data()

test_img = test_img.astype(np.bool)
truth_img = truth_img.astype(np.bool)

intersection = np.logical_and(test_img, truth_img)
union = np.logical_or(test_img, truth_img)
jaccard = intersection.sum() / float(union.sum())

#return {'Jaccard': jaccard}
print(json.dumps({'Jaccard': jaccard}))