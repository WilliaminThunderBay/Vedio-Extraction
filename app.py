from flask import Flask, render_template, request, send_from_directory
import os, re
from gensim import corpora, models
from gensim.matutils import cossim

app = Flask(__name__)

# 路径配置
VIDEO_DIR = './vedio'
THUMBNAIL_DIR = './static/thumbnails'
KEY_PHRASE_DIR = './key_phrase'
TOPIC_DIR = './topics'
TRANSCRIPT_DIR = './transcripts'

# 加载视频文件列表（例如：Mod01_Course Overview.mp4, Mod02_Intro.mp4, …）
videos = [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

# 此处使用你提供的描述数据覆盖方案（已删除不需要的条目）
descriptions_override = {
    'Mod01_Course Overview.mp4': [
        'AWS Academy Machine Learning Foundations Module 1: Welcome to AWS Academy Machine Learning Foundations'
    ],
    'Mod02_Intro.mp4': [
        'AWS Academy Machine Learning Foundations Module 2: Introduction to Machine Learning'
    ],
    'Mod02_Sect01.mp4': [
        'Module 2: Introduction to Machine Learning',
        'Section 1: What is machine learning ?'
    ],
    'Mod02_Sect02.mp4': [
        'Module 2: Introduction to Machine Learning Section 2: Business problems solved with machine learning'
    ],
    'Mod02_Sect03.mp4': [
        'Module 2: Introduction to Machine Learning Section 3: Machine learning process'
    ],
    'Mod02_Sect04.mp4': [
        'Module 2: Introduction to Machine Learning Section 4: Machine learning tools overview'
    ],
    'Mod02_Sect05.mp4': [
        'Module 2: Introduction to Machine Learning Section 5: Machine learning challenges'
    ],
    'Mod02_WrapUp.mp4': [
        'Module 2: Introduction to Machine Learning',
        'Module wrap-up'
    ],
    'Mod03_Intro.mp4': [
        'AWS Academy Machine Learning Foundations Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker'
    ],
    'Mod03_Sect01.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 1: Formulating machine learning problems'
    ],
    'Mod03_Sect02_part1.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 2: Collecting and securing data'
    ],
    'Mod03_Sect02_part2.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 2a: Extracting, transforming and loading data'
    ],
    'Mod03_Sect02_part3.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 2b: Securing your data'
    ],
    'Mod03_Sect03_part1.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 3: Evaluating your data'
    ],
    'Mod03_Sect03_part2.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 3a: Describing your data'
    ],
    'Mod03_Sect03_part3.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 3b: Finding correlations'
    ],
    'Mod03_Sect04_part1.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 4: Feature engineering'
    ],
    'Mod03_Sect04_part2.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 4a: Cleaning your data'
    ],
    'Mod03_Sect04_part3.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker Section 4b Dealing with outliers and selecting features'
    ],
    'Mod03_Sect05.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker Section 5: Training'
    ],
    'Mod03_Sect06.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 6: Hosting and using the model'
    ],
    'Mod03_Sect07_part1.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker Section 7: Evvaluating the accuracy of the model'
    ],
    'Mod03_Sect07_part2.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker Section 7a: Calculating classification metrics'
    ],
    'Mod03_Sect07_part3.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker Section 7b: Selecting classification thresholds'
    ],
    'Mod03_Sect08.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Section 8: Hyperparameter and model tuning'
    ],
    'Mod03_WrapUp.mp4': [
        'Module 3: Implementing a Machine Learning Pipeline with Amazon SageMaker',
        'Module wrap-up'
    ],
    'Mod04_Intro.mp4': [
        'AWS Academy Machine Learning Foundations Module 4: Introducing Forecasting'
    ],
    'Mod04_Sect01.mp4': [
        'Module 4: Introducing Forecasting',
        'Section 1: Forecasting overview'
    ],
    'Mod04_Sect02_part1.mp4': [
        'Module 4: Introducing Forecasting',
        'Section 2: Processing time series data'
    ],
    'Mod04_Sect02_part2.mp4': [
        'Module 4: Introducing Forecasting',
        'Section 2a: Special considerations for time series data'
    ],
    'Mod04_Sect02_part3.mp4': [
        'Module 4: Introducing Forecasting',
        'Section 3: Using Amazon Forecast'
    ],
    'Mod04_WrapUp.mp4': [
        'Module 4: Introducing Forecasting',
        'Module wrap-up'
    ],
    'Mod05_Intro.mp4': [
        'AWS Academy Machine Learning Foundations Module 5: Introducing Computer Vision'
    ],
    'Mod05_Sect01_ver2.mp4': [
        'Module 5: Introduction to Computer Vision',
        'Section 1: Introduction to computer vision'
    ],
    'Mod05_Sect02_part1_ver2.mp4': [
        'Module 5: Introduction to Computer Vision',
        'Section 2: Image and video analysis'
    ],
    'Mod05_Sect02_part2.mp4': [
        'Module 5: Introducing Computer Vision Section 2a: Facial recognition'
    ],
    'Mod05_Sect03_part1.mp4': [
        'Module 5: Introducing Computer Vision Section 3: Preparing custom datasets for computer vision'
    ],
    'Mod05_Sect03_part2.mp4': [
        'Module 5: Introducing Computer Vision Section 3a: Creating the training dataset'
    ],
    'Mod05_Sect03_part3.mp4': [
        'Module 5: Introducing Computer Vision Section 3b: Creating the test dataset'
    ],
    'Mod05_Sect03_part4_ver2.mp4': [
        'Module 5: Introduction to Computer Vision Section 3c: Evaluating and improving your model'
    ],
    'Mod05_WrapUp_ver2.mp4': [
        'Module 5: Introduction to Computer Vision',
        'Module wrap-up'
    ],
    'Mod06_Intro.mp4': [
        'AWS Academy Machine Learning Foundations Module 6: Introducing Natural Language Processing'
    ],
    'Mod06_Sect01.mp4': [
        'Module 6: Introducing Natural Language Processing Section 1: Overview of natural language processing'
    ],
    'Mod06_Sect02.mp4': [
        'Module 6: Introducing Natural Language Processing Section 2: Natural language processing managed services'
    ],
    'Mod06_WrapUp.mp4': [
        'Module 6: Introducing Natural Language Processing Module wrap-up'
    ],
    'Mod07_Sect01.mp4': [
        'AWS Academy Machine Learning Foundations Module 7: Course Wrap-up'
    ]
}

# ------------------ 过滤不需要的行 ------------------
remove_list = ['aWS academy', '2020, Amazon Web Services; Inc. or its Affiliates  All rights reserved:']
for key, lines in descriptions_override.items():
    descriptions_override[key] = [line for line in lines if line not in remove_list]

# 使用过滤后的描述数据
descriptions = descriptions_override

# 加载其他文本数据（关键词、主题、转录文本）
def load_text_data(folder):
    data = {}
    for fname in os.listdir(folder):
        if fname.endswith('.txt'):
            with open(os.path.join(folder, fname), 'r', encoding='utf-8') as f:
                data[os.path.splitext(fname)[0]] = f.read().splitlines()
    return data

key_phrases = load_text_data('./key_phrase')
topics = load_text_data('./topics')
transcripts = load_text_data('./transcripts')

# 初始化 LDA 模型（使用 key_phrases 中的文本）
texts = [line for lines in key_phrases.values() for line in lines]
tokenized = [t.lower().split() for t in texts]
import gensim
dictionary = corpora.Dictionary(tokenized)
corpus = [dictionary.doc2bow(" ".join(lines).lower().split()) for lines in key_phrases.values()]
video_map = dict(enumerate(key_phrases.keys()))
lda_model = models.LdaModel(corpus, num_topics=20, id2word=dictionary, passes=50)

def highlight(text, keywords):
    for word in keywords:
        text = re.sub(rf'\b({re.escape(word)})\b', r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    return text

# ---------------- 路由 ----------------

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('query', '').lower().strip()
    filtered_videos = videos
    if query:
        filtered_videos = [v for v in videos if query in v.lower()]
    
    # 构造 text_data：对每个视频，使用 descriptions 中的描述列表（用空格连接）
    text_data = { video: " ".join(descriptions.get(video, ["No description available."])) 
                  for video in filtered_videos }
    
    return render_template('index.html', videos=filtered_videos, query=query, text_data=text_data)

@app.route('/video/<filename>')
def video_detail(filename):
    video_name = os.path.splitext(filename)[0]
    return render_template(
        'video_detail.html',
        video_file=filename,
        title=video_name,
        key_phrases=key_phrases.get(video_name, []),
        topics=topics.get(video_name, []),
        recommendations=[v for v in videos if v != filename],
        videos=videos  # ← 这里传入
    )


@app.route('/vedio/<path:filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_DIR, filename)

@app.route('/semantic_search', methods=['GET', 'POST'])
def semantic_search():
    results = []
    query = ''
    mode = 'lda'
    threshold = 0.6
    if request.method == 'POST':
        query = request.form['query'].strip().lower()
        mode = request.form['mode']
        threshold = float(request.form.get('threshold', 0.6))
        query_tokens = query.split()

        if mode == 'lda':
            query_bow = dictionary.doc2bow(query_tokens)
            query_topics = lda_model.get_document_topics(query_bow)
            for i, doc_topics in enumerate(lda_model[corpus]):
                sim = cossim(query_topics, doc_topics)
                if sim > threshold:
                    video_file = video_map[i] + ".mp4"
                    results.append((sim, video_file))
            results.sort(reverse=True)
        else:
            for video_name, lines in transcripts.items():
                matched_lines = [line for line in lines if any(q in line.lower() for q in query_tokens)]
                if matched_lines:
                    video_file = video_name + ".mp4"
                    snippet = highlight(' ... '.join(matched_lines[:2]), query_tokens)
                    results.append((snippet, video_file))

    return render_template('semantic_search.html',
                           results=results,
                           query=query,
                           mode=mode,
                           threshold=threshold,
                           videos=videos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
