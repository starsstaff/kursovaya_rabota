import json
import uuid
from uuid import uuid4

from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, ForeignKey, UUID
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import csv

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(UUID, primary_key=True)
    contacts = Column(String)
    tickets_num = Column(Integer)

    # Определение отношения с классом TourSample
    tours = relationship("TourSample", back_populates="client")  # Обратите внимание на имя класса


class TourSample(Base):
    __tablename__ = 'ToursSample'

    id = Column(String, primary_key=True)
    client_id = Column(UUID, ForeignKey('clients.id'))
    tour_id = Column(UUID, ForeignKey('Tour.id'))
    name = Column(String)
    season = Column(String)
    duration = Column(Integer)
    clients = Column(Integer)
    price = Column(Float)
    mark = Column(Integer)

    # Определение отношения с классом Client
    client = relationship("Client", back_populates="tours")  # Используйте back_populates для связи
    tour = relationship("Tour")


class Tour(Base):
    __tablename__ = 'Tour'

    id = Column(UUID, primary_key=True)
    name = Column(String)
    season = Column(String)
    region = Column(String)
    duration_range = Column(JSON)
    clients_max = Column(JSON)

# Создание подключения к базе данных
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

# Создание сессии
Session_maker = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)  # Удаление всех таблиц
Base.metadata.create_all(engine)

def create_new_tour(session, tour_id, name, season, region, duration, clients, price, mark):
    # Создание новой записи
    new_tour = TourSample(
        id=tour_id,  # UUID передается как строка
        name=name,
        season=season,
        region=region,
        duration=duration,
        clients=clients,
        price=price,
        mark=mark
    )
    session.add(new_tour)
    session.commit()


# def print_first_rows(session, num_rows: int):
#     # Получаем все записи
#     tours = get_all_tours(session)
#
#     # Выводим первые несколько строк
#     for tour in tours[:num_rows]:
#         print(f"ID: {tour.id}, Name: {tour.name}, Season: {tour.season}, Region: {tour.region}, "
#               f"Duration: {tour.duration}, Clients: {tour.clients}, Price: {tour.price}, Mark: {tour.mark}")


def load_csv_to_db(csv_file_path: str, session):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Чтение CSV файла с заголовками
        a = 0
        for row in reader:
            tour_id = str(uuid.uuid4())  # Генерация UUID снаружи и преобразование в строку
            a += 1
            if a == 2000:
                break
            # Используем данные из каждой строки для создания новой записи в базе
            create_new_tour(
                tour_id=tour_id,
                session=session,
                name=row['Название тура'],
                season=row['Сезон'],
                region=row['Регион'],
                duration=int(row['Длительность']),
                clients=int(row['Кол-во туристов']),
                price=float(row['Цена']),
                mark=int(row['Оценка'])
            )
            print(a)
    print("Все записи из CSV добавлены в базу данных.")

def add_client(contacts: str, tickets_num: int):
    """Добавить клиента в базу данных."""
    session = Session_maker()
    new_client = Client(id=uuid4(), contacts=contacts, tickets_num=tickets_num)
    try:
        session.add(new_client)
        session.commit()
        print("Клиент добавлен")
    except IntegrityError:
        session.rollback()
        print("Error")
    finally:
        session.close()

def add_tour(name: str, season: str, region: str, duration_range: dict, clients_max: dict):
    """Добавить тур в базу данных."""
    session = Session_maker()
    new_tour = Tour(id=uuid4(), name=name, season=season, region=region,
                    duration_range=json.dumps(duration_range), clients_max=json.dumps(clients_max))
    try:
        session.add(new_tour)
        session.commit()
        print("Тур добавлен")
    except IntegrityError:
        session.rollback()
        print("Error")
    finally:
        session.close()

def add_tour_sample(client_id: UUID, tour_id: UUID, name: str, season: str, duration: int, clients: int, price: float, mark: int):
    """Добавить образец тура в базу данных."""
    session = Session_maker()
    new_tour_sample = TourSample(id=str(uuid4()), client_id=client_id, tour_id=tour_id,
                                 name=name, season=season, duration=duration,
                                 clients=clients, price=price, mark=mark)
    try:
        session.add(new_tour_sample)
        session.commit()
        print("Сделка добавлена")
    except IntegrityError:
        session.rollback()
        print("Error")
    finally:
        session.close()

def get_all_clients():
    """Получить всех клиентов из базы данных."""
    session = Session_maker()
    clients = session.query(Client).all()
    session.close()
    return clients

def get_all_tours():
    """Получить все туры из базы данных."""
    session = Session_maker()
    tours = session.query(Tour).all()
    session.close()
    return tours

def get_all_tour_samples():
    """Получить все образцы туров из базы данных."""
    session = Session_maker()
    tour_samples = session.query(TourSample).all()
    session.close()
    return tour_samples


client_id = uuid4()
add_client("Алена Аленова, +793456789", 2)

tour_id = uuid4()
add_tour("Весна в горах", "Весна", "Казахстан", {"min": 7, "max": 14}, {"max_clients": 30})

add_tour_sample(client_id=client_id, tour_id=tour_id, name="Sample Tour", season="Summer", duration=10, clients=5, price=1000.0, mark=4)

clients = get_all_clients()
print("Клиенты в бд")
for client in clients:
    print(f"ID: {client.id}, Contacts: {client.contacts}, Tickets: {client.tickets_num}")

tours = get_all_tours()
print("\nТуры в бд:")
for tour in tours:
    print(f"ID: {tour.id}, Name: {tour.name}, Season: {tour.season}")

# Получение всех образцов туров
tour_samples = get_all_tour_samples()
print("\nСделки в бд:")
for sample in tour_samples:
    print(f"ID: {sample.id}, Name: {sample.name}, Client ID: {sample.client_id}, Tour ID: {sample.tour_id}")