import random

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import networkx as nx
from pyvis.network import Network
from faker import Faker

app = FastAPI()

data = []
fake = Faker()

departments = ["IT", "HR", "Маркетинг"]
interests_list = ["Футбол", "Шахматы", "Танцы", "Кино", "Гольф", "Музыка", "Путешествия", "Гитара", "Йога", "Рисование", "Театр", "Кулинария", "Фотография", "Программирование"]
cities = ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург", "Новосибирск", "Челябинск", "Томск", "Омск", "Волгоград", "Краснодар", "Воронеж", "Рязань", "Пермь", "Тула", "Саратов", "Сочи", "Ростов-на-Дону", "Иркутск", "Барнаул", "Владивосток"]

for _ in range(300):
    name = fake.last_name() + fake.first_name() + fake.file_name() + str(random.randint(0, 100000))
    city = random.choice(cities)
    department = random.choice(departments)
    role = random.choice(["Разработчик", "Менеджер", "Аналитик", "Дизайнер", "HR-менеджер", "Программист", "Маркетолог", "Системный администратор", "Рекрутер", "Технический писатель", "Системный аналитик"])
    interests = random.sample(interests_list, random.randint(1, 3))  # Случайное количество интересов (от 1 до 3)

    data.append([name, interests, role, city, department])

# # Пример данных (сотрудники могут иметь несколько интересов)
# data = [
#     ("Иван", ["Футбол", "Шахматы"], "Разработчик", "Москва", "IT"),
#     ("Мария", ["Танцы"], "Менеджер", "Санкт-Петербург", "HR"),
#     ("Алексей", ["Футбол"], "Аналитик", "Москва", "IT"),
#     ("Елена", ["Шахматы"], "Разработчик", "Москва", "IT"),
#     ("Дмитрий", ["Танцы", "Шахматы"], "Менеджер", "Санкт-Петербург", "HR"),
#     ("Ольга", ["Футбол"], "Дизайнер", "Москва", "Маркетинг"),
#     ("Анна", ["Футбол", "Танцы"], "Менеджер", "Москва", "HR"),
#     ("Сергей", ["Кино", "Футбол"], "Программист", "Москва", "IT"),
#     ("Анастасия", ["Танцы"], "HR-менеджер", "Санкт-Петербург", "HR"),
#     ("Евгений", ["Танцы", "Шахматы"], "Технический писатель", "Казань", "IT"),
#     ("Ирина", ["Кулинария", "Танцы"], "Маркетолог", "Москва", "Маркетинг"),
#     ("Петр", ["Музыка", "Футбол"], "Разработчик", "Нижний Новгород", "IT"),
#     ("Марина", ["Шахматы", "Кино"], "Менеджер", "Челябинск", "HR"),
#     ("Виктор", ["Программирование", "Гольф"], "Системный администратор", "Москва", "IT"),
#     ("Светлана", ["Путешествия", "Фотография"], "Менеджер", "Санкт-Петербург", "HR"),
#     ("Максим", ["Футбол", "Шахматы"], "Дизайнер", "Москва", "Маркетинг"),
#     ("Татьяна", ["Танцы", "Йога"], "Менеджер", "Москва", "HR"),
#     ("Андрей", ["Футбол", "Гитара"], "Разработчик", "Казань", "IT"),
#     ("Владимир", ["Кулинария", "Футбол"], "Технический специалист", "Москва", "IT"),
#     ("Наталья", ["Йога", "Шахматы"], "HR-менеджер", "Санкт-Петербург", "HR"),
#     ("Денис", ["Футбол", "Гольф"], "Маркетолог", "Краснодар", "Маркетинг"),
#     ("Роман", ["Футбол", "Фотография"], "Аналитик", "Саратов", "IT"),
#     ("Людмила", ["Рисование", "Танцы"], "Менеджер", "Москва", "HR"),
#     ("Ксения", ["Танцы", "Театр"], "Рекрутер", "Екатеринбург", "HR"),
#     ("Анатолий", ["Шахматы", "Музыка"], "Разработчик", "Томск", "IT"),
#     ("Елизавета", ["Кино", "Танцы"], "Менеджер", "Омск", "HR"),
#     ("Галина", ["Танцы", "Гитара"], "Системный аналитик", "Ростов-на-Дону", "IT"),
#     ("Рустам", ["Шахматы", "Кулинария"], "Дизайнер", "Уфа", "Маркетинг"),
#     ("Инна", ["Футбол", "Йога"], "Менеджер", "Тюмень", "HR"),
#     ("Кирилл", ["Футбол", "Кулинария"], "Разработчик", "Волгоград", "IT"),
#     ("Леонид", ["Танцы", "Кино"], "Аналитик", "Пермь", "HR"),
#     ("Юлия", ["Шахматы", "Футбол"], "HR-менеджер", "Челябинск", "HR"),
#     ("Дмитрий", ["Футбол", "Танцы"], "Маркетолог", "Томск", "Маркетинг"),
#     ("Игорь", ["Гольф", "Кино"], "Программист", "Иркутск", "IT"),
#     ("Оксана", ["Шахматы", "Гитара"], "Менеджер", "Воронеж", "HR"),
#     ("Александр", ["Танцы", "Шахматы"], "Системный администратор", "Сочи", "IT"),
#     ("Нина", ["Кулинария", "Танцы"], "Маркетолог", "Москва", "Маркетинг"),
#     ("Валерия", ["Йога", "Футбол"], "Менеджер", "Рязань", "HR"),
#     ("Екатерина", ["Кино", "Шахматы"], "HR-менеджер", "Тольятти", "HR"),
#     ("Константин", ["Футбол", "Кулинария"], "Разработчик", "Владивосток", "IT"),
#     ("Антон", ["Танцы", "Футбол"], "Менеджер", "Новосибирск", "HR"),
#     ("Надежда", ["Шахматы", "Гитара"], "Маркетолог", "Владимир", "Маркетинг"),
#     ("Сергей", ["Гольф", "Йога"], "Аналитик", "Москва", "IT"),
#     ("Елена", ["Футбол", "Танцы"], "Дизайнер", "Екатеринбург", "Маркетинг"),
#     ("Павел", ["Шахматы", "Футбол"], "Рекрутер", "Казань", "HR"),
#     ("Алиса", ["Йога", "Шахматы"], "Менеджер", "Барнаул", "HR"),
#     ("Артур", ["Футбол", "Гитара"], "Разработчик", "Самара", "IT"),
#     ("Валентин", ["Танцы", "Йога"], "Системный администратор", "Сургут", "IT"),
#     ("Лариса", ["Кулинария", "Гольф"], "Маркетолог", "Оренбург", "Маркетинг"),
#     ("Маргарита", ["Футбол", "Танцы"], "Менеджер", "Калуга", "HR"),
#     ("Максим", ["Гольф", "Шахматы"], "Программист", "Челябинск", "IT"),
#     ("Егор", ["Шахматы", "Танцы"], "Дизайнер", "Вологда", "Маркетинг"),
#     ("Кирилл", ["Танцы", "Гольф"], "Менеджер", "Тула", "HR"),
#     ("Валерий", ["Футбол", "Шахматы"], "HR-менеджер", "Красноярск", "HR")
# ]

# Цвета для отделов
dept_colors = {
    "IT": "red",
    "HR": "blue",
    "Маркетинг": "green",
}


# Генерация графа для всех данных
def generate_graph(data, filter_type=None):
    G = nx.Graph()

    # Добавляем узлы сотрудников
    for emp, interests, role, city, dept in data:
        color = "pink"
        G.add_node(emp, title=f"Роль: {role}<br>Город: {city}<br>Отдел: {dept}", color=color)

    # Добавляем узлы городов, интересов и отделов
    cities = {city for _, _, _, city, _ in data}
    interests = {interest for _, interest_list, _, _, _ in data for interest in interest_list}
    departments = {dept for _, _, _, _, dept in data}

    if not filter_type:
        for city in cities:
            G.add_node(city, title=f"Город: {city}", color="yellow", size=40)
        for interest in interests:
            G.add_node(interest, title=f"Интерес: {interest}", color="lightblue", size=20)
        for dept in departments:
            G.add_node(dept, title=f"Отдел: {dept}", color="red", size=30)
    elif filter_type == "city":
        for city in cities:
            G.add_node(city, title=f"Город: {city}", color="yellow", size=40)
    elif filter_type == "department":
        for dept in departments:
            G.add_node(dept, title=f"Отдел: {dept}", color="red", size=30)
    elif filter_type == "interest":
        for interest in interests:
            G.add_node(interest, title=f"Интерес: {interest}", color="lightblue", size=20)

    # Добавляем связи
    for emp, interest_list, _, city, dept in data:
        if not filter_type:
            G.add_edge(emp, city, title=f"Город: {city}", weight=3, color="yellow")
            G.add_edge(emp, dept, title=f"Отдел: {dept}", weight=2, color="red")
            for interest in interest_list:
                G.add_edge(emp, interest, title=f"Интерес: {interest}", weight=1, color="lightblue")
        elif filter_type == "city":
            G.add_edge(emp, city, title=f"Город: {city}", weight=3, color="yellow")
        elif filter_type == "department":
            G.add_edge(emp, dept, title=f"Отдел: {dept}", weight=2, color="red")
        elif filter_type == "interest":
            for interest in interest_list:
                G.add_edge(emp, interest, title=f"Интерес: {interest}", weight=1, color="lightblue")

    # Создаём интерактивный граф
    net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white")
    net.force_atlas_2based(gravity=-50)  # Улучшенная кластеризация
    net.toggle_physics(True)  # Включение физики для хорошей группировки
    net.show_buttons(filter_=["physics"])  # Показываем кнопки управления
    net.from_nx(G)
    return net.generate_html()


@app.get("/", response_class=HTMLResponse)
async def show_network():
    html_content = generate_graph(data)
    return HTMLResponse(content=html_content)


@app.get("/cities", response_class=HTMLResponse)
async def show_cities():
    html_content = generate_graph(data, filter_type="city")
    return HTMLResponse(content=html_content)


@app.get("/interests", response_class=HTMLResponse)
async def show_interests():
    html_content = generate_graph(data, "interest")
    return HTMLResponse(content=html_content)


@app.get("/departments", response_class=HTMLResponse)
async def show_departments():
    html_content = generate_graph(data, "department")
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
