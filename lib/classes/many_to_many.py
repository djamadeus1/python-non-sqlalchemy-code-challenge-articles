class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a String between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    class Author:
        def __init__(self, name):
            if not isinstance(name, str) or len(name) ==0:
                raise ValueError("Author name must be a non-empty string.")
            self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be an instance of the Magazine class.")
        self._magazine = value

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        """Returns a list of all articles written by this author."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Returns a list of all magazines the author has contributed to."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Creates and adds a new article for the author."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns a list of unique topic areas of the author's articles."""
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))



class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError(
                "Magazine name must be a string between 2 and 16 characters."
            )

        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Magazine category must be a non-empty string.")

        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError(
                "Magazine name must be a string between 2 and 16 characters."
            )
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]
        if not magazines_with_articles:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))