class bookk:
    title = "my life"
    author = "Darkrai"
    reviews = []
    count = 0
    def __init__(self,review):
        self.reviews = review
        bookk.reviews.append(self.reviews)
        bookk.count += 1
    def print_reviews(self):
        print(self.reviews)
    @classmethod
    def print_all_reviews(cls):
        print(cls.reviews)
    @classmethod
    def reviews_count(cls):
        print("no. of reviews-", cls.count)
sumit = bookk("best book")
kunal = bookk("it was good")
ravi = bookk("intresting")
sumit.print_reviews()
bookk.reviews_count()
bookk.print_all_reviews()
