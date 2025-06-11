import requests

data = {
    'word_count': 82,
    'char_count': 476,
    'has_media': 1,
    'hour': 10,
    'sentiment': 0.9,
    'company_avg_likes': 800,
    'weekday': 'wednesday'
}

response = requests.post('http://localhost:5000/predict', json=data)
print(response.json())

#Gives predicted likes as 210
