# -*- coding: utf-8 -*-
import sys
import os

# 设置stdout编码
sys.stdout.reconfigure(encoding='utf-8')

def extract_text_pdf(pdf_path, label):
    """提取PDF文本内容"""
    import pdfplumber
    print(f"\n{'='*60}")
    print(f"文件: {label}")
    print(f"路径: {pdf_path}")
    print(f"{'='*60}")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"总页数: {len(pdf.pages)}")
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and text.strip():
                    print(f"\n--- 第 {i+1} 页 ---")
                    print(text)
                else:
                    print(f"\n--- 第 {i+1} 页 (无文本，可能是图片) ---")
    except Exception as e:
        print(f"pdfplumber出错: {e}")

def extract_with_pymupdf(pdf_path, label):
    """用pymupdf提取（对图片型PDF更鲁棒）"""
    import fitz
    print(f"\n{'='*60}")
    print(f"[pymupdf] 文件: {label}")
    print(f"{'='*60}")
    try:
        doc = fitz.open(pdf_path)
        print(f"总页数: {len(doc)}")
        for i, page in enumerate(doc):
            text = page.get_text()
            if text and text.strip():
                print(f"\n--- 第 {i+1} 页 ---")
                print(text.strip())
            else:
                # 检查图片数量
                images = page.get_images()
                print(f"\n--- 第 {i+1} 页 (纯图片，含{len(images)}张图) ---")
        doc.close()
    except Exception as e:
        print(f"pymupdf出错: {e}")

if __name__ == "__main__":
    base = r"D:\Projects\mine\thought-hub"

    # 文字稿
    transcript = os.path.join(base, "文字稿20260709【科技特训营】存储产业⻛⼝深度解读【第7季-第8期】.pdf")
    if os.path.exists(transcript):
        extract_text_pdf(transcript, "文字稿")
    else:
        print("文字稿文件不存在")

    # PPT
    ppt = os.path.join(base, "PPT20260709 存储产业风口深度解读.pdf")
    if os.path.exists(ppt):
        extract_with_pymupdf(ppt, "PPT")
    else:
        print("PPT文件不存在")
