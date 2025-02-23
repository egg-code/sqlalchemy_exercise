from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Books(Base):
    __tablename__ = "books"
    
    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column()
    price_usd: Mapped[float] = mapped_column()

    author_id:Mapped[int] = mapped_column(ForeignKey("author_details.author_id"), nullable=False)
    author_details: Mapped["Author_Details"] = relationship("Author_Details")

    def __repr__(self):
        return f"author_id:{self.author_id}\nTitle:{self.title}\nPrice:{self.price_usd}"

class Author_Details(Base):
    __tablename__ = "author_details"

    author_id: Mapped[int] = mapped_column(primary_key=True)
    author_name: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"author_id:{self.author_id}\nauthor_name:{self.author_name}"
