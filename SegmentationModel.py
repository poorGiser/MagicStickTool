'''
Author: cy 2449471714@qq.com
Date: 2024-03-12 16:10:57
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-21 13:50:25
FilePath: \代码\MagicStickTool\SegmentationModel.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
分割模型
'''
import cv2
import numpy as np
from segment_anything import SamPredictor, sam_model_registry
class SegmmentationModel():
    def __init__(self, device,type='vit_h'):
        self.device = device
        self.type = type
        
        self.model = None
        self.predictor = None
        
        self.currentImage = None
    def loadModel(self):
        if self.type == 'vit_h':
            self.model = sam_model_registry[self.type](checkpoint="./ckpts/sam_vit_h_4b8939.pth")
        elif self.type == 'vit_b':
            self.model = sam_model_registry[self.type](checkpoint="./ckpts/sam_vit_b_01ec64.pth")
        elif self.type == 'vit_l':
            self.model = sam_model_registry[self.type](checkpoint="./ckpts/sam_vit_l_0b3195.pth")
        self.model.to(self.device)
        self.predictor = SamPredictor(self.model)
    #read current image
    def setCurrentImage(self,imagePath):
        self.currentImage = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)
        self.predictor.set_image(self.currentImage)
    #to output mask
    def predict(self,positivate_prompt=None,negative_prompt=None,boxes_prompt=None):
        #points labels and boxes
        points = []
        positive_point_num = 0
        if positivate_prompt is not None and len(positivate_prompt) > 0:
            positive_point_num = len(positivate_prompt)
            points += positivate_prompt
            
        negative_point_num = 0
        if negative_prompt is not None and len(negative_prompt) > 0:
            negative_point_num = len(negative_prompt)
            points += negative_prompt
        labels = [1] * positive_point_num + [0] * negative_point_num
        
        if len(points) != 0:
            points = np.asarray(points)
            labels = np.asarray(labels)
            
        else:
            points = None
            labels = None
        
        if boxes_prompt is not None and len(boxes_prompt) > 0:
            box = np.asarray(boxes_prompt)
        else:
            box = None
        
        mask, _, _ = self.predictor.predict(point_coords=points,point_labels=labels,multimask_output=False,box=box)
        mask = mask[0].astype(np.uint8)
        split_masks = self.splitMask(mask)
        return split_masks
        #split mask
    def splitMask(self,mask):
        num_labels, labeled_mask, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
        split_masks = []
        for label in range(1, num_labels):
            area = stats[label, cv2.CC_STAT_AREA]
            if area < 256:
                continue
            split_mask = np.zeros_like(mask)
            split_mask[labeled_mask == label] = 1
            split_masks.append(split_mask)
        return split_masks

        
        
        