import os
import easyocr

# 配置图片与输出目录（请根据实际情况修改路径）
IMAGES_DIR = r'E:\NLP-project\Ec2\static\thumbnails'
OUTPUT_DIR = r'E:\NLP-project\Ec2\static\text'

# 创建 EasyOCR 读取器，参数中指定语言（例如英文 'en' 或中文 'ch_sim'）
reader = easyocr.Reader(['en'])  # 如果需要中文可以使用 ['en', 'ch_sim']

def read_text_from_images():
    # 检查图片目录是否存在
    if not os.path.exists(IMAGES_DIR):
        print(f"Directory {IMAGES_DIR} not found!")
        return

    # 如果输出目录不存在，则创建
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for file in os.listdir(IMAGES_DIR):
        # 仅处理 .jpg 文件
        if file.lower().endswith('.jpg'):
            image_path = os.path.join(IMAGES_DIR, file)
            try:
                # 使用 EasyOCR 读取文字，detail=0 返回纯文字结果
                result = reader.readtext(image_path, detail=0, paragraph=True)
                text = "\n".join(result)

                # 构建输出文件路径
                base_name, _ = os.path.splitext(file)
                output_path = os.path.join(OUTPUT_DIR, base_name + '.txt')

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)

                print(f"Processed {file} -> {output_path}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == '__main__':
    read_text_from_images()
