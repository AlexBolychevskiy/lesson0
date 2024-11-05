import time
class User:
    users = []

    def __new__(cls, *args, **kwargs):
        cls.users.append(args)
        cls.users.append(kwargs)
        return super().__new__(cls)
    def __init__(self, nickname,password,age):
        if isinstance(nickname, str):
            self.nickname = nickname
        if isinstance(password, str):
           self.password = hash(password)
        if isinstance(age, int):
            self.age = age
"""
if __name__=='__main__':
database = Database()
user = User(input("Введите логин: "), input("Введите пароль:" ))
database.add_user(user.username,user.password)
#if isinstance(password, hash(int)):
        # if password == password-confirm?:
"""
class Video:
    videos = []

    def __new__(cls, *args, **kwargs):
        cls.videos.append(args)
        cls.videos.append(kwargs)
        return super().__new__(cls)
    def __init__(self,title,duration,time_now,adult_mode):
        if isinstance(title, str):
            self.title = title
        self.duration = duration
        self.duration = time.time()
        self.time_now = time_now
        self.time_now = 0
        self.adult_mode = adult_mode
        self.adult_mode = False
class UrTube:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user
    def log_in(self,nickname,password):
        for nickname in self.users:
            setattr(self, nickname, password)
        if hasattr(self, nickname):
            self.current_user = nickname
        return self
    def register(self,nickname,password,age):
        self.users [nickname] = password
        self.age = age
        if nickname is None:
            self.users.append(nickname)
        else:
            print( f'Пользователь {nickname} уже существует"')
        return self
    def log_out(self):
        self.current_user = None
    def add(self,*args):
        if args is None:
            self.videos.append(args)
        return self

    def get_videos(self, word):
        if isinstance(word, str):
            word.upper()
            self.videos.upper()
        if word in self.videos:
            return self.videos
    def watch_video(self,title):
        if not UrTube.log_in:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif self.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        if title in self.videos:
            time.sleep(10)
            Video.__init__(self)
            time.time()
            print("Конец видео")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

 # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



