


import requests



i = requests.get("https://newsapi.org/v2/everything?sources=cnn&pagesize=10&page=1&apiKey=2d2757dedcbb49398de5f5ea3342068a",verify=False)


story = []

for n in range(0, 3):
    print(n)
    try:
        story.append(i.json()['articles'][n])
        print(story)
    except:
        print("news scrape error")

    print('\n')

print("thanks!")
