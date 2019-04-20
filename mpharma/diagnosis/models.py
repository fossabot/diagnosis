# -*- coding: utf-8 -*-
"""diagnosis models."""
from mpharma.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Category(SurrogatePK, Model):
    """Table for category codes and corresponding titles"""

    __tablename__ = 'categories'
    code = Column(db.String(10), unique=True, nullable=False)
    title = Column(db.String(250), nullable=False)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Category({code})>'.format(code=self.code)


class Code(SurrogatePK, Model):
    """A DX code"""

    __tablename__ = 'codes'
    category_id = reference_col('categories')
    category = relationship('Category', backref='categories')
    diagnosis_code = Column(db.String(10), nullable=True)
    full_code = Column(db.String(10), unique=True, nullable=True)
    abbreviated_description = Column(db.String(250), nullable=True)
    full_description = Column(db.String(600), nullable=True)

    def as_dict(self):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        data.pop('category_id')
        data['category'] = self.category.as_dict()
        return data

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Code({full_code!r})>'.format(full_code=self.full_code)
