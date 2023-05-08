class human():

    def __init__(self, first_name, last_name, surname):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        print(f"Имя: {self.first_name}", f"\nФамилия: {self.last_name} " , f"\nОтчество: {self.surname}")

a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = input("Введите отчество: ")
human_1 = human(a, b, c)

##################################################

class drib():

    def __init__(self, chiselnik, znamenik):
        self.chiselnik = int(chiselnik)
        self.znamenik = int(znamenik)
        print(f"Дробь: {chiselnik} / {znamenik}")
        print(f"Сума чисельника і знаменника = ", self.chiselnik+self.znamenik)
        print(f"Різниця чисельника і знаменника = ", self.chiselnik-self.znamenik)
        print(f"Результат множення чисельника і знаменника = ", self.chiselnik*self.znamenik)
        print(f"Результат ділення чисельника і знаменника = ", self.chiselnik/self.znamenik)

a1 = input("\nВведіть чисельник ")
b1 = input("Введіть знаменник ")
drib(a1,b1)

