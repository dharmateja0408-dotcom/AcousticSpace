



from app.ai.report_generator import generate_report

data = {

    "filename": "sample.wav",

    "prediction": "Real",

    "confidence": 98.42,

    "risk": "Low",

    "duration": 42.01,

    "sample_rate": 44100,

    "analysis_time": 0.73,

    "recommendation":
    "No spoofing characteristics were detected.",

}

path = generate_report(data)

print(path)