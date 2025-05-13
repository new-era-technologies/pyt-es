# Завдання 1
# Створіть клас, який описує книгу.
# Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок.
# Визначте для нього методи _repr_ та _str_.


class Book:

    def __init__(self, author: str, name: str, year_publ: int, genre: str):
        self.author = author
        self.name = name
        self.year_publ = year_publ
        self.genre = genre
        self.review_list = []

    def append(self, el):
        self.review_list.append(el)

    def getReviewList(self):
        return self.review_list

    def __str__(self):
        return f"Book: {self.name} \nGenre: {self.genre} \nAuthor: {self.author} \nPublish year: {self.year_publ} \nReview: {self.getReviewList()}"

    # def __repr__(self):
    #     return f"Book: {self.name} \nGenre: {self.genre} \nAuthor: {self.author} \nPublish year: {self.year_publ} \nReview: {self.getReviewList()}"


book1 = Book("Abraham 'Bram' Stoker ", "Dracula", 1897, "horror")
book2 = Book("Margaret Eleanor Atwood", "The Handmaids Tale", 1985, "dystopian novel")
book3 = Book("Victor-Marie Hugo", "Les Miserables", 1862, "love and romance")

# print(book1.__str__())
# print(book2.__str__())
# print(book3.__str__())


# Завдання 2
# Створіть клас, який описує відгук до книги.
# Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.


class Review:

    def __init__(self, review: str):
        self.review = review

    def __repr__(self):
        return self.review


review1 = Review("omg, its Dracula")
review2 = Review("Amazing!")
review3 = Review("Who trust in love???")

book1.append(review1)
book1.append(review2)
book3.append(review3)

print(book1)
print(book2)
print(book3)
