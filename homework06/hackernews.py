from bottle import (route, run, template, request, redirect)
from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route('/add_label/')
def add_label():
    # 1. Получить значения параметров label и id из GET-запроса
    # 2. Получить запись из БД с соответствующим id (такая запись только одна!)
    # 3. Изменить значение метки записи на значение label
    # 4. Сохранить результат в БД
    id = request.query.id
    label = request.query.label
    s = session()
    row = s.query(News).filter(News.id == id).one()
    row.label = label
    s.commit()
    redirect("/news")


@route('/update_news')
def update_news():
    # 1. Получить данные с новостного сайта
    # 2. Проверить, каких новостей еще нет в БД. Будем считать,
    #    что каждая новость может быть уникально идентифицирована
    #    по совокупности двух значений: заголовка и автора
    # 3. Сохранить в БД те новости, которых там нет
    s = session()
    news_list = get_news("https://news.ycombinator.com/newest")
    for news in news_list:
        if s.query(News).filter(News.title == news["title"], News.author == news['author']).first():
            row = News(title=news['title'], author=news['author'], url=news['url'], comments=news['comments'],
                       points=news['points'])
            s.add(row)
            s.commit()
    redirect('/news')


@route("/classify")
def classify_news():
    s = session()
    X_train = [news.title for news in s.query(News).filter(News.label != None)]
    y_train = [news.label for news in s.query(News).filter(News.label != None)]
    model = NaiveBayesClassifier()
    model.fit(X_train, y_train)
    no_label = s.query(News).filter(News.label == None)
    X = [news.title for news in no_label]
    y = model.predict(X)
    good, maybe, never = [], [], []
    for i, label in enumerate(y):
        if label == 'good':
            good.append(no_label[i])
        elif label == 'maybe':
            maybe.append(no_label[i])
        elif label == 'never':
            never.append(no_label[i])
    return template('news_recommendations', good=good, maybe=maybe, never=never)


if __name__ == "__main__":
    run(host="localhost", port=8080)
