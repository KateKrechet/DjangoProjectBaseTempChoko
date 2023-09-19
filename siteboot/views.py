from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'index.html')


def chocolate(req, id):
    id = int(id)
    # name = ''
    # text = ''
    # img = ''
    # if id == 0:
    #     name = 'Snikers'
    #     img = 'img/s.jpg'
    #     text = 'Не тормози - сникерсни!'
    name = ['Snikers', 'Mars', 'Bounty', 'Nuts', 'Аленка']
    imgs = ['img/s.jpg', 'img/m.jpg', 'img/bounty.jpg', 'img/n.jpg', 'img/a.jpeg']
    text = ['Не тормози - сникерсни', 'Еще больше карамели', 'Райское наслаждение', 'Еще больше орехов', 'Вкус детства']
    logo = ['img/mars-logo.jpg', 'img/mars-logo.jpg', 'img/mars-logo.jpg', 'img/n-logo.jpg', 'img/redoct-logo.png']
    logo_href = ['https://ru.wikipedia.org/wiki/Mars', 'https://ru.wikipedia.org/wiki/Mars',
                 'https://ru.wikipedia.org/wiki/Mars', 'https://www.nestle.ru/',
                 'https://www.uniconf.ru/factories/krasny-octyabr/']
    data = {'k1': name[id], 'k2': imgs[id], 'k3': text[id], 'k4': logo[id], 'k5': logo_href[id]}
    return render(req, 'proshokolad.html', context=data)
