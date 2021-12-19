
from app import db,Person

db.create_all()

man1 = Person('taro',18)
man2 = Person('jiro',19)
man3 = Person('Saburo',20)

print(man1,man2,man3)

db.session.add_all([man1,man2])
db.session.add(man3)

db.session.commit()
print(man1,man2,man3)