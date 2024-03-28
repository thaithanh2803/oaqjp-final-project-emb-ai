from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    function to analyze text
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = f'''For the given statement, the system response is 
        {', '.join(f"'{key}': {value}" for key, value in list(response.items())[:-2])}
        and '{list(response.keys())[-2]}': {list(response.values())[-2]}.
        The dominant emotion is {response['dominant_emotion']}'''
    return response_text


@app.route("/")
def render_index_page():
    '''
    render HTML
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
