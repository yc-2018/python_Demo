import cv2  # 无法导入cv2模块   pip3 install opencv-python
import numpy as np

WH_SIZE = 300
HQ = cv2.imread('hq.png', cv2.IMREAD_UNCHANGED)
HQ = cv2.resize(HQ, (WH_SIZE, WH_SIZE))


def h_linear_mask(start, end, width=WH_SIZE):
    h_line = np.linspace(start, end, width)
    h_mask = np.vstack([h_line for _ in range(WH_SIZE)])
    h_mask = np.clip(h_mask, 0, 1)
    return h_mask


def v_linear_mask(start, end, height=WH_SIZE):
    v_line = np.linspace(start, end, height)
    v_line = np.reshape(v_line, (height, 1))
    v_mask = np.hstack([v_line for _ in range(WH_SIZE)])
    v_mask = np.clip(v_mask, 0, 1)
    return v_mask


def creat_hq(mask):
    mask = np.expand_dims(mask, -1)
    out = np.clip(mask * HQ, 0, 255).astype(np.uint8)
    return out


def h_two_stage_hq(start, mid, end, seg_len):
    mask_1 = h_linear_mask(start, mid, seg_len)
    mask_2 = h_linear_mask(mid, end, WH_SIZE - seg_len)
    mask = np.hstack([mask_1, mask_2])
    return creat_hq(mask)


def v_two_stage_hq(start, mid, end, seg_len):
    mask_1 = v_linear_mask(start, mid, seg_len)
    mask_2 = v_linear_mask(mid, end, WH_SIZE - seg_len)
    mask = np.vstack([mask_1, mask_2])
    return creat_hq(mask)


def style_1(prename):
    hq_1 = creat_hq(h_linear_mask(1, 0))
    hq_2 = creat_hq(v_linear_mask(1, 0))
    hq_3 = h_two_stage_hq(0.8, 0.7, 0, int(WH_SIZE * 2 / 3))
    hq_4 = h_two_stage_hq(0.2, 0.7, 0.8, int(WH_SIZE / 3))
    hq_5 = v_two_stage_hq(0.8, 0.7, 0, int(WH_SIZE * 2 / 3))
    hq_6 = v_two_stage_hq(0.2, 0.7, 0.8, int(WH_SIZE / 3))

    cv2.imwrite(prename + '1.png', hq_1)
    cv2.imwrite(prename + '2.png', hq_2)
    cv2.imwrite(prename + '3.png', hq_3)
    cv2.imwrite(prename + '4.png', hq_4)
    cv2.imwrite(prename + '5.png', hq_5)
    cv2.imwrite(prename + '6.png', hq_6)


def style_2(prename):
    gq = cv2.imread('gq.png', cv2.IMREAD_UNCHANGED)
    gq = cv2.resize(gq, (90, 60))
    mini_bg = np.ones((70, 100, 4), dtype=np.uint8) * 255
    mini_bg[5:65, 5:95, :] = gq
    bg = np.zeros((WH_SIZE, WH_SIZE, 4), dtype=np.uint8)
    h, w, c = mini_bg.shape
    hq_1 = bg.copy()
    hq_1[WH_SIZE - h:, WH_SIZE - w:, :] = mini_bg
    hq_2 = bg.copy()
    hq_2[0:h, 0:w, :] = mini_bg
    cv2.imwrite(prename + '1.png', hq_1)
    cv2.imwrite(prename + '2.png', hq_2)


style_1('style_1_')
style_2('style_2_')
