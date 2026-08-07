# Simple OCR with OpenCV and Tesseract

> **Disclaimer:** This is a legacy script written exactly a year ago as a learning exercise in Computer Vision and Optical Character Recognition (OCR). I am uploading it today to consolidate my projects and build my professional portfolio.

## Description
This project is a straightforward Python script that demonstrates image preprocessing and text extraction. It takes an image (e.g., a stop sign), applies standard OpenCV filters to isolate the text, and feeds it into Tesseract OCR for recognition.

## Pipeline Steps
1. **Grayscale Conversion:** Removes unnecessary color channels.
2. **Gaussian Blur:** Reduces image noise (5x5 kernel).
3. **Binary Thresholding:** Forces a black-and-white high-contrast aspect for better OCR accuracy.
4. **Text Extraction:** Uses `pytesseract` with Page Segmentation Mode (PSM) 6 to read the processed image.

## Prerequisites
To run this script locally, you will need:
* Python 3.x
* `opencv-python` (`cv2`)
* `pytesseract`
* [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) installed on your machine (the script expects it at `C:\Program Files\Tesseract-OCR\tesseract.exe`).
