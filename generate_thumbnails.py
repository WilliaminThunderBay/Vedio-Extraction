import cv2
import os

# 修改为实际完整路径
VIDEO_DIR = r'E:\NLP-project\Ec2\vedio'
THUMBNAIL_DIR = r'E:\NLP-project\Ec2\static\thumbnails'
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

def generate_thumbnail(video_path, thumbnail_path, time_frame=1):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, time_frame * 1000)
    success, image = cap.read()
    if success:
        cv2.imwrite(thumbnail_path, image)
        print(f'Thumbnail generated: {thumbnail_path}')
    else:
        print(f'Failed to generate thumbnail: {video_path}')
    cap.release()

if __name__ == '__main__':
    for video in os.listdir(VIDEO_DIR):
        if video.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(VIDEO_DIR, video)
            thumbnail_path = os.path.join(THUMBNAIL_DIR, f"{video}.jpg")
            generate_thumbnail(video_path, thumbnail_path)
