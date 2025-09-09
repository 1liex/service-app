from flask import Flask, request, jsonify
from flask_cors import CORS
from googleapiclient.discovery import build

import json
import os

app = Flask(__name__)
CORS(app)


youtube_api_key = "AIzaSyBc3c6Tb4q_VBujqd-1BYBSA_M8njefVMM"


to = {
    "student": "server/data/studentData.json",
    "teacher": "server/data/teacherData.json"
}

#====== Functions ======

def open_files(path):

    with open(path, "r") as f:
        data = json.load(f)     
        return data
    
def add_data(path, keyword_data):
    data = open_files(path)
    
 
    if isinstance(keyword_data, dict) and "keyword" in keyword_data:
        keyword = keyword_data["keyword"]
    else:
        keyword = str(keyword_data)
    
  
    if not any(d.get("keyword") == keyword for d in data if isinstance(d, dict)):
        data.append({"keyword": keyword})
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def search_youtube(keyword, max_results=5):
    """بحث على يوتيوب حسب الكلمة المفتاحية"""
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    
    request = youtube.search().list(
        q=keyword,
        part='snippet',
        maxResults=max_results,
        type='video',
        relevanceLanguage='en'
    )
    
    response = request.execute()
    
    results = []
    for item in response.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url = f"https://www.youtube.com/watch?v={video_id}"
        results.append({
            "title": title,
            "url": url
        })
    
    return results

def search():
    keywords = open_files(to["teacher"])  # [{'keyword': 'html'}, ...]
    all_results = {}

    for kw in keywords:
        keyword_str = kw.get("keyword")  # نأخذ قيمة الكلمة
        if keyword_str:
            videos = search_youtube(keyword_str)
            all_results[keyword_str] = videos

    # حفظ النتائج في ملف JSON جديد
    with open(to["student"], "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=4, ensure_ascii=False)


@app.route("/get/<role>", methods = ["GET", "POST"])
def get(role):
    if role == "student" and request.method == "GET":
        return jsonify(open_files(to["student"]))
    
    if role == "teacher" and request.method == "POST":
        keyword = request.get_json()
        add_data(to["teacher"], keyword)
        search()
    return jsonify({"error": "invalid role or method"}), 404


if __name__ == "__main__":
    app.run(debug=True)