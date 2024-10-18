import json
import os

# 분석된 데이터를 시각화할 HTML 파일 경로 설정
output_html_path = "output/report.html"

# 분석된 데이터를 가져오는 함수 (예시 데이터로 대체)
def load_analyzed_data():
    # 실제 데이터가 있는 경우 이 부분을 데이터베이스 또는 파일에서 불러오도록 수정
    return {
        "pet_name": "Happy",
        "behavior_analysis": [
            {"label": "놀기", "value": 30},
            {"label": "휴식", "value": 50},
            {"label": "식사", "value": 10},
            {"label": "기타", "value": 10}
        ],
        "emotion_prediction": [
            {"label": "행복", "value": 70},
            {"label": "불안", "value": 20},
            {"label": "스트레스", "value": 10}
        ]
    }

# Chart.js 스크립트를 포함하는 HTML 생성 함수
def generate_html_report(analyzed_data):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HappyPet Analysis Report</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>{analyzed_data['pet_name']}의 행동 분석</h1>

        <h2>행동 분석</h2>
        <canvas id="behaviorChart" width="400" height="200"></canvas>

        <h2>감정 상태</h2>
        <canvas id="emotionChart" width="400" height="200"></canvas>

        <script>
            const behaviorData = {{
                labels: {json.dumps([item['label'] for item in analyzed_data['behavior_analysis']])},
                datasets: [{{
                    label: '행동 분석',
                    data: {json.dumps([item['value'] for item in analyzed_data['behavior_analysis']])},
                    backgroundColor: ['rgba(75, 192, 192, 0.2)'],
                    borderColor: ['rgba(75, 192, 192, 1)'],
                    borderWidth: 1
                }}]
            }};

            const emotionData = {{
                labels: {json.dumps([item['label'] for item in analyzed_data['emotion_prediction']])},
                datasets: [{{
                    label: '감정 예측',
                    data: {json.dumps([item['value'] for item in analyzed_data['emotion_prediction']])},
                    backgroundColor: ['rgba(255, 99, 132, 0.2)'],
                    borderColor: ['rgba(255, 99, 132, 1)'],
                    borderWidth: 1
                }}]
            }};

            const configBehavior = {{
                type: 'bar',
                data: behaviorData,
            }};

            const configEmotion = {{
                type: 'pie',
                data: emotionData,
            }};

            new Chart(
                document.getElementById('behaviorChart'),
                configBehavior
            );

            new Chart(
                document.getElementById('emotionChart'),
                configEmotion
            );
        </script>
    </body>
    </html>
    """
    return html_template

# 분석된 데이터를 HTML 파일로 저장하는 함수
def save_html_report(html_content):
    # 출력 디렉토리가 없는 경우 생성
    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)

    # HTML 파일로 저장
    with open(output_html_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"보고서가 {output_html_path}에 저장되었습니다.")

if __name__ == "__main__":
    analyzed_data = load_analyzed_data()  # 분석된 데이터 로드
    html_content = generate_html_report(analyzed_data)  # HTML 생성
    save_html_report(html_content)  # HTML 파일로 저장
