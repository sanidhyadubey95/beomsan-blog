---
title: "Journey of Computer Vision"
date: "2025-06-20"
tags: ["python", "visualization", "matplotlib"]
---

To begin your journey of mastering Computer Vision (CV) with Deep Learning (DL) as a complete beginner, it's best to follow a step-by-step paper-reading curriculum that starts with foundational concepts and progresses toward more advanced topics. Here's a curated roadmap of seminal and beginner-friendly research papers, grouped by topic and difficulty level, along with guidance for each.

## 1. 🏰 Stage 1: Foundation of Computer Vision and Deep Learning

### 1.1. ImageNet Classification with Deep Convolutional Neural Networks (AlexNet) – 2012
Authors: Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton

Why: First major breakthrough applying CNNs to large-scale vision.

Focus Areas: Convolutional layers, ReLU, dropout, GPU training

Paper Link

### 1.2. Very Deep Convolutional Networks for Large-Scale Image Recognition (VGGNet) – 2014
Authors: Karen Simonyan, Andrew Zisserman

Why: Simple yet deeper CNN; key for learning architecture design.

Focus Areas: Depth, layer stacking, simplicity of 3x3 convs

Paper Link

### 1.3. Deep Residual Learning for Image Recognition (ResNet) – 2015
Authors: Kaiming He et al.

Why: Introduced residual connections to allow training very deep networks.

Focus Areas: Residual blocks, degradation problem

Paper Link

## 2. 🧠 Stage 2: Understanding Object Detection & Localization

### 2.1. Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation (R-CNN) – 2014
Authors: Ross Girshick et al.

Why: Kickstarted deep learning in object detection.

Focus Areas: Region proposals, classification, SVM

Paper Link

### 2.2. Faster R-CNN – 2015
Authors: Shaoqing Ren et al.
Why: Introduced Region Proposal Networks (RPN), making detection much faster.
Focus Areas: End-to-end object detections
Paper Link

### 2.3. You Only Look Once (YOLOv1) – 2016
Authors: Joseph Redmon et al.
Why: Unified real-time object detection.
Focus Areas: Single-stage detector, speed vs accuracy trade-off.
Paper Link

## 3. 🧩 Stage 3: Image Segmentation

### 3.1. Fully Convolutional Networks for Semantic Segmentation (FCN) – 2015
Authors: Jonathan Long et al.

Why: First deep learning model for pixel-level segmentation

Focus Areas: Deconvolution, pixel-wise prediction

Paper Link

### 3.2. U-Net: Convolutional Networks for Biomedical Image Segmentation – 2015
Authors: Olaf Ronneberger et al.

Why: Popular architecture for segmentation with skip connections

Focus Areas: Encoder-decoder, skip connections

Paper Link

## 4. 📷 Stage 4: Visual Understanding (Classification + Context)

### 4.1. SqueezeNet – 2016
Why: Model with fewer parameters but competitive accuracy; great for mobile devices.

Focus: Efficiency in architecture

Paper Link

### 4.2. Attention Is All You Need – 2017
Authors: Vaswani et al.

Why: Though NLP-focused, it introduced Transformers — key to modern CV.

Paper Link

## 5. 📌 Stage 5: Transformers in Vision

### 5.1. An Image is Worth 16x16 Words: Vision Transformers (ViT) – 2020
Authors: Dosovitskiy et al.

Why: Applied Transformers directly to images — shifted CV landscape

Focus Areas: Patch embeddings, position encodings

Paper Link

## 6. 🛠️ How to Read These Papers as a Beginner:
1. Skim First – Read abstract, intro, and conclusion.
2. Re-read with Notes – Focus on methods and visuals.
3. Google Terms – Pause to understand concepts like IoU, mAP, non-max suppression, etc.
4. Re-implement Simplified Versions – Use PyTorch or TensorFlow.
5. Supplement with Tutorials – Look up YouTube videos or blog posts explaining the paper.

Here are some excellent survey / review / SOTA papers specifically in deep learning (DL) with computer vision (CV) — these types of papers summarize discoveries and progress in the whole domain:

## 7. 📄 Classic & General Surveys

### 7.1. "Deep Learning for Computer Vision: A Brief Review"
(Zhang et al., 2018)
Gives a broad overview of how DL transformed CV — CNNs, object detection, segmentation, image generation.

### 7.2. "Recent Advances in Deep Learning for Object Detection"
(Zou et al., 2019)
Focused survey of deep learning-based object detection models (R-CNN, YOLO, SSD, etc.).

### 7.3. "Deep Learning for Image and Video Processing"
(Guo et al., 2016)
Covers various DL techniques in both static images and video understanding.

## 8. 🖼️ Modern Surveys (Transformer Era)

### 8.1. "A Survey on Visual Transformers"
(Khan et al., 2022)
Covers vision transformers (ViTs), their architectures, applications, and comparison to CNNs.

### 8.2. "A Survey on Deep Learning for Visual Understanding"
(Yang et al., 2023)
One of the most up-to-date reviews of DL in vision: covers CNNs, transformers, self-supervised learning, generative models.

### 8.3. 📺 Task-specific Surveys
"A Comprehensive Review on Semantic Segmentation with Deep Learning"
Focused on semantic segmentation techniques in DL.

### 8.4. "Deep Learning for Video Understanding: A Review"
Focused on video classification, action recognition, video captioning, etc.

## 9. 🖼️ Generative CV

### 9.1. "Generative Adversarial Networks: A Survey"
A review of GANs, variants, applications in image synthesis, super-resolution, image-to-image translation.

### 9.2. 📽️ YouTube Talks / Playlists Explaining CV+DL Surveys
These videos summarize key papers and review trends — great for understanding surveys visually:

## 10. "CVPR / ICCV / ECCV Highlights & Trends"
Many channels cover each year's top trends in computer vision. Examples:

Yannic Kilcher

Henry AI Labs

Aman AI

Deep Learning AI (Andrew Ng)

## 11. "Transformers in Vision"
Talks that review vision transformers:

Khan et al. Visual Transformers Survey — Explained (various channels)

Example: Yannic Kilcher's ViT video

## 12. "Object Detection Deep Dive"
Talks that explain object detection surveys:

YOLO evolution

RCNN family of detectors

Two-stage vs. one-stage detectors
(Check Aladdin Persson and Augmented Startups on YouTube)

## 13. "GAN Survey Videos"

Many GAN survey summaries are on Henry AI Labs

Example: "GANs in 2023: What's New"

Conferences' Official Channels

CVPR official YouTube

ICCV official YouTube

NeurIPS official
They often upload "SOTA in CV" or "Trends in Vision" keynote talks.

## 14. 🛠️ Tools to Stay Updated on New Surveys

### 14.1. Papers with Code
https://paperswithcode.com
Has a "Trending Papers" and "Survey Papers" filter
SOTA tables for every CV task!

### 14.2. Arxiv Sanity Preserver
http://www.arxiv-sanity.com
Sort latest arXiv papers on cs.CV and cs.LG
Filter by "Survey" keyword in title/abstract

### 14.3. Connected Papers
https://www.connectedpapers.com
Visual tool to explore papers connected to a key survey you like
Helps find new surveys in the same topic

### 14.4. Litmaps
https://www.litmaps.com
Tracks how new papers cite your favorite surveys

### 14.5. Arxiv Digest Email
Subscribe to cs.CV or cs.LG
Filter for "survey" / "review" keywords