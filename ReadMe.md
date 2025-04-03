# AWS-Extraction ReadMe

## Table of Contents
- [AWS-Extraction ReadMe](#aws-extraction-readme)
  - [Table of Contents](#table-of-contents)
  - [1. Project Overview](#1-project-overview)
  - [2. Tools, Technologies, and Dataset](#2-tools-technologies-and-dataset)
    - [Tools and Technologies](#tools-and-technologies)
    - [Dataset](#dataset)
  - [3. Dataset Setup Instructions](#3-dataset-setup-instructions)
  - [4. NLP Integration and Analysis](#4-nlp-integration-and-analysis)
    - [4.1 Key Phrases Extraction](#41-key-phrases-extraction)
    - [4.2 Topic Extraction](#42-topic-extraction)
    - [4.3 Search Function](#43-search-function)
  - [5. Dashboard and Workflow](#5-dashboard-and-workflow)
  - [6. Results and Validation](#6-results-and-validation)
  - [7. Conclusion](#7-conclusion)
  - [8. References](#8-references)

---

## 1. Project Overview

**Course Information**  
- **Course Code**: COMP-5014-WDE – Natural Language Processing  
- **Instructor**: Dr. Amin Safaei  
- **Institution**: Lakehead University  

**Project Focus**  
Use the tools and techniques learned throughout the NLP course to build an end-to-end solution that extracts and analyzes text data from multiple videos stored in an Amazon S3 bucket.  

**Problem Description**  
The goal is to produce an interactive dashboard that allows users to:
1. **Transcribe** video content (audio-to-text).  
2. **Normalize** and prepare text data for analysis.  
3. **Extract** key phrases and topics.  
4. **Provide** multiple search modes (text-based and LDA-based).  

This solution involves both back-end NLP processing (transcription, tokenization, lemmatization, TF-IDF, LDA) and front-end user interaction (Flask-based dashboards).

[Back to Top](#aws-extraction-readme)

---

## 2. Tools, Technologies, and Dataset

### Tools and Technologies

- **Cloud Environment**: Amazon Web Services (AWS)  
- **Programming Language**: Python  
- **Speech Recognition**: `speech_recognition` library (for transcribing videos)  
- **NLP Techniques**:  
  - Tokenization, stopword removal, lemmatization  
  - TF-IDF-based key phrase extraction  
  - Topic extraction (TF-IDF + MMF)  
  - LDA-based semantic search  
- **Web Framework**: Flask (for building dashboard pages)  

### Dataset

The dataset consists of multiple videos that have been uploaded to an AWS S3 bucket. Each video is transcribed into text using a speech recognition library, and the text is then processed (normalization, tokenization, etc.).  

[Back to Top](#aws-extraction-readme)

---

## 3. Dataset Setup Instructions

1. **Upload Videos to S3**  
   - Store all your video files in a dedicated Amazon S3 bucket.  
   - Make sure you have the correct access credentials (IAM) configured on your EC2 instance or wherever your code is running.

2. **Local or EC2 Environment**  
   - Ensure that the machine running the code has network permission to read files from the specified S3 bucket (or that your code is co-located in the same AWS environment).

3. **Transcription Step**  
   - Run the transcription script (using `speech_recognition`) to convert all uploaded videos from speech to text.  
   - Confirm the output text files (or transcribed strings) are correctly saved or stored in a location accessible to your application.

4. **Text Normalization**  
   - Convert to lowercase, remove punctuation and extra whitespace.  
   - Tokenize into words, remove stopwords, and lemmatize tokens.  
   - You should now have clean text data ready for further analysis.

[Back to Top](#aws-extraction-readme)

---

## 4. NLP Integration and Analysis

### 4.1 Key Phrases Extraction
- **Method**: TF-IDF  
- **Process**:  
  1. Build TF-IDF vectors for the normalized text.  
  2. Identify terms with high TF-IDF scores as key phrases.  

### 4.2 Topic Extraction
- **Method**: TF-IDF + MMF  
- **Process**:  
  1. Generate TF-IDF for each document.  
  2. Use an MMF (Maximum Matching Function) or similar technique to group terms into coherent topics.  

### 4.3 Search Function
- **Text-based Search**  
  - A straightforward keyword matching approach powered by TF-IDF indexing.  
- **LDA-based Search**  
  - A semantic search approach employing LDA (Latent Dirichlet Allocation) to capture topic-level similarities.

[Back to Top](#aws-extraction-readme)

---

## 5. Dashboard and Workflow

The project provides three main dashboard pages:

1. **Index Page**  
   - Acts as the main landing page, displaying a grid of video thumbnails.  
   - Includes a top bar with a search field for finding videos by title or description.  
   - A sidebar offers quick links to *Home*, *Semantic Search*, and *Subscriptions*, each linking to a detailed page.

2. **Video Detail Page**  
   - Dedicated page for playing a selected video and highlighting its key phrases and extracted topics.  
   - A top navigation bar and an offcanvas sidebar enable quick navigation.  
   - Recommended videos appear on the right side to maintain engagement.

3. **Semantic Search Page**  
   - Offers text-based or LDA-based search for finding relevant videos.  
   - An adjustable similarity threshold refines results in real time when using LDA.  
   - Hover-based previews let users quickly evaluate search results without fully loading each video.

**Overall Workflow**:  
1. **Transcribe** → 2. **Normalize** → 3. **Extract Key Phrases / Topics** → 4. **Dashboard Display & Search** → 5. **User Interaction & Feedback**.

[Back to Top](#aws-extraction-readme)

---

## 6. Results and Validation

1. **Functionality**  
   - Successfully retrieved and transcribed video content from S3.  
   - Normalized text data using Python’s NLP pipelines.  
   - Extracted key phrases via TF-IDF and performed topic extraction with TF-IDF + MMF.

2. **Search Efficiency**  
   - Text search quickly matches against TF-IDF indexes.  
   - LDA-based search provides more robust semantic retrieval, giving better results for ambiguous or concept-based queries.

3. **Dashboard Engagement**  
   - The front-end design (Flask + Bootstrap) demonstrates a clear and responsive UI, making it easy to navigate videos and search results.

[Back to Top](#aws-extraction-readme)

---

## 7. Conclusion

**Key Takeaways**  
- Successfully integrated NLP pipelines (transcription, normalization, TF-IDF, LDA) into a cohesive AWS-based platform.  
- Demonstrated how to build an interactive dashboard for exploring, viewing, and semantically searching video content.  
- Showed how advanced topic modeling (LDA) and TF-IDF can improve search relevance compared to basic keyword methods.

**Future Enhancements**  
- Additional NLP improvements such as named entity recognition (NER) or sentiment analysis.  
- More robust recommendation algorithms on the **Video Detail** page.  
- Integration of advanced AWS AI services (e.g., Amazon Transcribe, Amazon Comprehend) for improved pipeline performance.

[Back to Top](#aws-extraction-readme)

---

## 8. References

- **OpenNLP Documentation**. (2023). *Apache Software Foundation*.  
  [https://opennlp.apache.org/docs](https://opennlp.apache.org/docs)

- **Clojure Programming Language**. Hickey, R. (2023).  
  [https://clojure.org/](https://clojure.org/)

- **Text Analytics for Crime Investigation**. Victor, K. (2019). *Fighting Crime with Text Analytics*. Medium.  
  [https://medium.com/@krishvictor/fighting-crime-with-text-analytics-2bcbaf7ff6c4](https://medium.com/@krishvictor/fighting-crime-with-text-analytics-2bcbaf7ff6c4)

- **NLP in Forensics and Authorship Analysis**. Gelbukh, A., & Sidorov, G. (2013). *Authorship Attribution through Text Analysis*.  
  [https://www.thinkmind.org/download.php?articleid=immm_2013_5_30_20048](https://www.thinkmind.org/download.php?articleid=immm_2013_5_30_20048)

[Back to Top](#aws-extraction-readme)
