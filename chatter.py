import random as rd
import time
from datetime import datetime
import sys


class Food:
    FoodTags = ["Еда", "Поесть", "Перекусить", "Покушать"]
    # Теги слова "легкий"
    LightTags = ("Легкий", "Лёгкий", "Легкое", "Лёгкое")
    # Легкие блюда
    Light = {"Завтрак": ("Греческий йогурт с ягодами", "Кашу на молоке с бананом", "Творог с орехами и фруктами"),
             "Обед": ("Яичные конвертики с сыром и ветчиной", "Булгур с тыквой и грибами",
                      "Салат с семгой, апельсином и кунжутом"),
             "Ужин": ("Говяжий салат с луком и морковью", "Салат с базиликовыми митболами",
                      "Курицу в медово-чесночной глазури")
             }

    # Теги слова "сытный"
    SatisfyingTags = ("Сытный", "сытный", "Сытное", "сытное")
    # Сытные блюда
    Satisfying = {"Завтрак": ("Яичницу с бобами, беконом и помидорами", "Тосты с пастой из авокадо и соевого соуса",
                              "Бутерброды с омлетом, сыром и ветчиной"),
                  "Обед": ("Картофельную запеканку с курицей, помидорами и сыром",
                           "Куриное филе с грибами, запечённое в сметанно-сырном соусе", "Солянку мясная"),
                  "Ужин": ("Бефстроганов из говядины с грибами", "Пиццу c колбасой, шампиньонами и оливками",
                           "Говядину с баклажанами по-китайски")
                  }


class Movies:
    MoviesTags = ("Фильм", "Фильмы", "Кино", "Кинофильм")
    # Теги "20-ый век"
    Century20thTags = ("20", "20ый", "20-ый", "XX", "Двадцатый", "20 век", "20ый век", "20-ый век", "XX век",
                       "Двадцатый век")
    # Фильмы 20-го века
    Century20th = {"Драма": (("Крестный Отец", 1972), ("Зеленая миля", 1999), ("Форрест Гамп", 1994),
                             ("Побег из Шоушенка", 1994), ("Список Шиндлера", 1993), ("Достучаться до небес", 1997),
                             ("Криминальное чтиво", 1994)),
                   "Триллер": (("Леон", 1994), ("Молчание ягнят", 1990), ("Семь", 1995), ("Матрица", 1999),
                               ("Бойцовский клуб", 1999)),
                   "Комедия": (("Джентльмены удачи", 1971), ("Иван Васильевич меняет профессию", 1973),
                               ('Операция "Ы" и другие приключения Шурика', 1965),
                               ("Удивительные приключения мистера Бина", 1989), ("Шоу Трумана", 1998),
                               ("Один дома", 1990)),
                   "Мультфильм": (("Король Лев", 1994), ("История игрушек", 1995), ("Ну, погоди!", 1969),
                                  ("Красавица и чудовище", 1991), ("Бемби", 1942), ("Приключения Винни Пуха", 1977))
                   }

    # Теги "20-ый" век
    Century21stTags = ("21", "21ый", "21-ый", "XXI", "Двадцать первый", "21 век", "21ый век", "21-ый век", "XXI век",
                       "Двадцать первый век")
    # Фильмы 21-го века
    Century21st = {"Драма": (("Зеленая книга", 2018), ("Ла-Ла Ленд", 2016), ("Интерстеллар", 2014), ("1+1", 2011),
                             ("Невидимая сторона", 2009), ("Хатико: Самый верный друг", 2008),
                             ("В погоне за счастьем", 2006), ("Терминал", 2004), ("Игры разума", 2001)),
                   "Триллер": (("Джанго освобожденный", 2012), ("Темный рыцарь", 2008), ("Остров проклятых", 2009)),
                   "Комедия": (('Отель "Гранд Будапешт"', 2014), ("Мальчишник в Вегасе", 2009),
                               ("Бесславные ублюдки", 2009), ("Диктатор", 2012)),
                   "Мультфильм": (("Вверх", 2009), ("ВАЛЛИ-И", 2008), ("Шрэк", 2001), ("Ледниковый период", 2002),
                                  ("Девять", 2009))
                   }


class Game:
    GameTags = ("Игра", "Игры", "Играть", "Угадай число", "Число", "Угадайка")
    Rules = ("Правила игры следующие: Вы загадываете и запоминаете число от 1 до 100. В ходе игры число менять "
             "нельзя.\nУ меня есть 7 попыток, за которые я должен отгадать загаданное Вами число. Я буду писать число,"
             ' а вы будете отвечать.\nЕсли загаданное число больше, чем то, которое написал я, вы пишете "Больше". '
             'Если число меньше, чем мое, вы пишете "Меньше". Если я угадал Ваше число, вы пишете "Да"\n'
             'Мухлевать нельзя, и пусть победит сильнейший!')


class Feelings:
    Good = ("Хорошо", "Отлично", "Супер", "Превосходно", "Великолепно", "Удивительно", "Прекрасно", "Замечательно",
            "Классно", "Славно")

    Neutral = ("Нормально", "Ок", "Окей", "Неплохо", "Обычно")

    Bad = ("Плохо", "Не очень", "Никак", "Грустно", "Ужасно", "Скучно")


class Constants:
    # Пустая строка
    Blank = '\n'

    # Открывающее сообщение
    LetsMeet = "Давайте познакомимся! Как Вас зовут?"

    # Сообщение "Что делать?"
    WhatToDo = ("Чтобы я посоветовал фильм, напишите Фильм. Чтобы я посоветовал блюдо, напишите Еда.\n"
                'Чтобы поиграть со мной в игру "Угадай число", напишите Игра. Чтобы узнать мой секрет, напишите Секрет')

    # Приветствия
    Greetings = ("Привет", "Здравствуй", "Здравствуйте", "Приветствую")

    # Прощания
    GoodbyesStart = ("Было приятно с Вами общаться", "Мы хорошо побеседовали", "Вы прекрасный собеседник",
                     "Мне понравился наш с Вами разговор", "Спасибо за интереснейшую беседу")
    GoodbyesEnd = ("Пока", "До свидания", "До скорой встречи", "Увидимся")

    # Как Ваше "ничего"?
    HowsYours = ("Как Ваше настроение?", "Как проходит Ваш день?", "Как Вы себя чувствуете?", "Как Ваши дела?")
    HowsYoursHint = "(Хорошо / Нормально / Не очень)"

    # Функции бота
    OpeningGreeting = ("Привет! Я чат-бот, очень люблю помогать людям.\n"
                       "Я могу помочь Вам выбрать, какой фильм посмотреть. Также могу подсказать, что покушать.\n"
                       'Мы можем поиграть в игру "Угадай число", где я буду отгадывать загаданное Вами число от 1 до'
                       ' 100 за 7 попыток.'
                       f'\nЧтобы прекратить диалог со мной, в любой момент напишите "{"!стоп"}", "{"!пока"}" или '
                       f'"{"!завершить"}".\n')

    Endings = ("!стоп", "!пока", "!завершить")

Blank = '\n'


file = open("dialogue.txt", "w")


# Функция приветствия и знакомства с пользователем
def LetsMeet() -> bool:
    # Необходимая информация для знакомства
    MeetingError: bool = False
    MeetingMessage: str

    # Собираем имя пользователя
    UserName: str = input(f'{Constants.LetsMeet}\n').strip().capitalize()

    file.write(f'Бот:\n{Constants.LetsMeet}\n')
    file.write(f'Пользователь:\n{UserName}\n')

    CheckGoodbye(UserName)

    currentHours = int(datetime.now().strftime("%H"))
    greeting: str

    # Специализируем обращение по времени запроса
    if 5 <= currentHours < 12:
        greeting = "Доброе утро"
    elif 12 <= currentHours < 18:
        greeting = "Добрый день"
    elif 18 <= currentHours < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    # Генерируем сообщение
    MeetingMessage = f'{greeting}, {UserName}! Рад нашему знакомству!\n'
    print(MeetingMessage)

    file.write(f'Бот:\n{MeetingMessage}')

    return MeetingError


# Функция, проверяющая ввод пользователя на команду выхода
def CheckGoodbye(SomeRequest: str) -> None:
    if SomeRequest in Constants.Endings:
        Goodbye(CountTalks)
        sys.exit()
    return


# Функция прощания с пользователем
def Goodbye(NumberOfTalks) -> None:
    GoodbyeMessage: str

    if NumberOfTalks < 4:
        GoodbyeMessage = f'{rd.choice(Constants.GoodbyesEnd)}!'
    else:
        GoodbyeMessage = f'{rd.choice(Constants.GoodbyesStart)}! {rd.choice(Constants.GoodbyesEnd)}!'

    print(GoodbyeMessage)
    file.write(f'Бот:\n{GoodbyeMessage}')

    return


# Функция, узнающая о самочувствии или настроении пользователя. Ответ бота зависит от ответа пользователя
def HowYouDoing() -> bool:
    # Необходимая информация, чтобы узнать настроение и вывести ответ
    HowYouDoingError = False
    UsersFeelings: str
    FeelingsMessage: str

    # Пользователю задается вопрос, на который он отвечает
    DataRequest = rd.choice(Constants.HowsYours)
    UsersFeelings = input(f'{DataRequest} Ответьте одним словом.\n').strip().capitalize()

    file.write(f'Бот:\n{DataRequest} Ответьте одним словом.\n')
    file.write(f'Пользователь:\n{UsersFeelings}\n')

    CheckGoodbye(UsersFeelings)

    # Другой вариант, с подсказкой
    # UsersFeelings = input(f'{rd.choice(Constants.HowsYours)} {Constants.HowsYours}\n').strip().capitalize()

    # Генерация ответа в зависимости от ответа пользователя
    if UsersFeelings in Feelings.Good:
        FeelingsMessage = "Очень рад это слышать! Не думайте ничего менять, просто радуйтесь жизни!"
    elif UsersFeelings in Feelings.Neutral:
        FeelingsMessage = "Я Вас понял. Надеюсь, мне удастся улучшить ситуацию и сделать Ваш день чуточку лучше!"
    elif UsersFeelings in Feelings.Bad:
        FeelingsMessage = "Мне жаль, что это так. Улучшить Ваше настроение и скрасить сегодняшний день - моя миссия!"
    else:
        FeelingsMessage = ("Похоже, что я не знаком с таким чувством...\n"
                           "Я стараюсь понимать людей, но не всегда получается( Попоробуете объяснить мне снова?")
        HowYouDoingError = True

    print(FeelingsMessage + Blank)
    file.write(f'Бот:\n{FeelingsMessage + Blank}')

    return HowYouDoingError


# Функция, собирающая запрос от пользователя
def GetRequest() -> str:
    print(Constants.WhatToDo)
    UserRequest: str = input().strip().capitalize()
    file.write(f'Пользователь:\n{UserRequest}\n')

    CheckGoodbye(UserRequest)

    return UserRequest


# Функция для сбора информация, необходимой для определения блюда
def MealtimeAndSatiety():
    # Необходимые данные
    MealtimeRequest: str
    SatietyRequest: str

    # Собираем у пользователя прием пищи
    print("Подскажите, какой прием пищи Вас интересует? (Завтрак / Обед / Ужин)")
    file.write(f'Бот:\nПодскажите, какой прием пищи Вас интересует? (Завтрак / Обед / Ужин)')

    MealtimeRequest = input().strip().capitalize()
    file.write(f'Пользователь:\n{MealtimeRequest}\n')

    CheckGoodbye(MealtimeRequest)

    # Собираем у пользователя уровень сытности
    print("Вас интересует сытный или легкий прием пищи?")
    file.write(f'Бот:\nВас интересует сытный или легкий прием пищи?\n')

    SatietyRequest = input().strip().capitalize()
    file.write(f'Пользователь:\n{SatietyRequest}\n')

    CheckGoodbye(SatietyRequest)

    return MealtimeRequest, SatietyRequest


# Функция, обрабатывающая запрос на тему еды
def FoodRequest(mealtime: str, satiety: str) -> bool:
    FoodMessage: str = ""
    FoodRequestError: bool = False
    meal: str = ""

    # Проверка, какого века фильм требует пользователь
    if satiety in Food.LightTags and mealtime in Food.Light.keys():
        meal = rd.choice(Food.Light[mealtime])
    elif satiety in Food.SatisfyingTags and mealtime in Food.Satisfying.keys():
        meal = rd.choice(Food.Satisfying[mealtime])
    else:
        FoodMessage = ("Не нашел ничего съедобного по этим параметрам в своей базе данных(\n"
                       "Давайте еще разок уточним параметры\n")
        FoodRequestError = True

    # Скрипты ответов на запрос, связанный с фильмами
    FoodScripts = (f'На {mealtime.lower()} Вам стоит попробовать {meal.lower()}.',
                   f'{mealtime.capitalize()}? Приготовьте {meal.lower()}.',
                   f'Попробуйте {meal}, должно быть вкусно!',
                   f'Порадуйте себя! Приготовьте на {mealtime.lower()} {meal.lower()}.',
                   f'Приготовьте {meal.lower()}! Это будет вкусный и полезный {mealtime.lower()}.',
                   f'Если бы я был человеком, я бы обязательно сделал себе на {mealtime.lower()} {meal.lower()})',
                   f'На Вашем месте я бы с удовольствием отведал {meal.lower()}!')

    # Проверка указателя ошибки
    if FoodRequestError is False:
        FoodMessage = rd.choice(FoodScripts)

    print(FoodMessage)
    file.write(f'Бот:\n{FoodMessage}')

    # Возврат сообщения, выбранного случайным образом и статуса работы программы
    return FoodRequestError


# Определение жанра и века для выбора фильма
def GenreAndCentury():
    # Необходимые данные
    GenreRequest: str
    CenturyRequest: str

    # Собираем у пользователя прием пищи
    print("Подскажите, какой жанр Вас интересует? (Драма / Триллер / Комедия / Мультфильм)")
    file.write(f'Бот:\nПодскажите, какой жанр Вас интересует? (Драма / Триллер / Комедия / Мультфильм)')

    GenreRequest = input().strip().capitalize()
    file.write(f'Пользователь:\n{GenreRequest}\n')

    CheckGoodbye(GenreRequest)

    # Собираем у пользователя уровень сытности
    print("Фильм какого столетия вам хотелось бы посмотреть? (20 / 21)")
    file.write(f'Бот:\nФильм какого столетия вам хотелось бы посмотреть? (20 / 21)')

    CenturyRequest = input().strip().capitalize()
    file.write(f'Пользователь:\n{CenturyRequest}\n')

    CheckGoodbye(CenturyRequest)

    return GenreRequest, CenturyRequest


# Функция, обрабатывающая запрос на тему еды
def FilmRequest(genre: str, century: str) -> bool:
    FilmMessage: str = ""
    FilmRequestError: bool = False
    movie: str = ""
    year: int = 0

    # Проверка, какое по сытости блюдо требует пользователь
    if century in Movies.Century20thTags and genre in Movies.Century20th.keys():
        movie, year = rd.choice(Movies.Century20th[genre.capitalize()])
    elif century in Movies.Century21stTags and genre in Movies.Century21st.keys():
        movie, year = rd.choice(Movies.Century21st[genre.capitalize()])
    else:
        FilmMessage = ("Перебрал все кассеты и диски в моей фильмотеке, но ничего не нашел(\n"
                       "Давайте попробуем еще раз\n")
        FilmRequestError = True

    # Скрипты ответов на запрос, связанный с едой
    FilmScripts = (f'Советую посмотреть "{movie}", классика!',
                   f'В {year} был выпущен прекрасный фильм: "{movie}". Что насчет него?',
                   f'Однажды в онлайн-кинотеатре я увидел "{movie}". С тех пор это один из моих любимых фильмов)',
                   f'Мне не придется говорить много. "{movie}" {year} года. На этом все...',
                   f'По-моему, картина "{movie}" входит в 250 лучших фильмов всех времен. '
                   f'Наверное она там не просто так...',
                   f'{year} - год рождения такого шедевра, как "{movie}". Предлагаю насладиться!')

    # Проверка на ошибку
    if FilmRequestError is False:
        FilmMessage = rd.choice(FilmScripts)

    print(FilmMessage)
    file.write(f'Бот:\n{FilmMessage}')

    return FilmRequestError


def GuessTheNumber() -> None:
    print(f'{Game.Rules}\n')
    file.write(f'Бот:\n{Game.Rules}\n')

    LeftSide: int = 1
    RightSide: int = 100
    AttemptsLeft: int = 7
    Attempt: int
    UsersAnswer: str

    time.sleep(5)
    while AttemptsLeft > 0:
        Attempt = (LeftSide + RightSide) // 2

        Question = f'Ваше число {Attempt}?\n'
        file.write(f'Бот:\n{Question}')

        UsersAnswer = input(Question).strip().capitalize()
        file.write(f'Пользователь:\n{UsersAnswer}\n')

        CheckGoodbye(UsersAnswer)

        if UsersAnswer == "Больше":
            LeftSide = Attempt
        elif UsersAnswer == "Меньше":
            RightSide = Attempt
        elif UsersAnswer == "Да":
            WinAttempts: int = 8 - AttemptsLeft
            print(f'Хорошая игра! Чтобы отгадать ваше число мне понадобилось ровно столько попыток - {WinAttempts}')
            file.write(f'Бот:\nХорошая игра! Чтобы отгадать ваше число, мне понадобилось ровно столько '
                       f'попыток - {WinAttempts}')
            break
        else:
            print(f'Я Вас не понял, попробуйте еще раз')
            file.write(f'Бот:\nЯ Вас не понял, попробуйте еще раз')
            continue

        if LeftSide > RightSide:
            print('Мне кажется, что вы играете нечестно. Я отказываюсь играть не по правилам.')
            file.write(f'Бот:\nМне кажется, что вы играете нечестно. Я отказываюсь играть не по правилам.')
            break

        AttemptsLeft -= 1

    else:
        print(f'Прекрасная игра! Вы переиграли меня, поздравляю!')
        file.write(f'Бот:\nПрекрасная игра! Вы переиграли меня, поздравляю!')

    return


# Переменная, которая будет определять длительность беседы в темах (модулях)
CountTalks: int = 0
SecretsTold: int = 0


def main() -> None:
    # Использование двух выше заданных применений в модуле main
    global CountTalks, SecretsTold

    # Открываем диалог сообщением
    print(Constants.OpeningGreeting)
    file.write(f'Бот:\n{Constants.OpeningGreeting}')

    # Если произошла ошибка при знакомстве
    if LetsMeet() is True:
        Goodbye(CountTalks)
        sys.exit()
    CountTalks += 1

    # Цикл, пока функция не выйдет из стадии ошибки (True)
    while HowYouDoing() is True:
        pass
    CountTalks += 1

    # Основной цикл, из него выходим уже в завершении диалога
    while True:
        # Получаем запрос пользователя
        Request = GetRequest()
        # Работаем с едой
        if Request in Food.FoodTags:
            mealtime, satiety = MealtimeAndSatiety()
            while FoodRequest(mealtime, satiety) is True:
                mealtime, satiety = MealtimeAndSatiety()

        # Работаем с фильмами
        elif Request in Movies.MoviesTags:
            genre, century = GenreAndCentury()
            # Пока (FilmRequestError is True)
            while FilmRequest(genre, century) is True:
                genre, century = GenreAndCentury()

        # Работаем с игрой
        elif Request in Game.GameTags:
            GuessTheNumber()

        # Выводим пустую строку для смыслового различия и добавляем 1 к счетчику стадий диалога
        print(Blank)
        file.write(Blank)
        CountTalks += 1


if __name__ == "__main__":
    main()
