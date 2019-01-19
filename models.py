from sqlalchemy import Integer, Float, Column, create_engine, ForeignKey,MetaData, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tariffs(Base):
    __tablename__ = 'tariffs'
    id = Column(Integer, primary_key=True, nullable=False)
    date_begin = Column(Date, nullable=False)
    date_end = Column(Date)
    cold_water = Column(Float, nullable=False)
    hot_water = Column(Float, nullable=False)
    electricity_day = Column(Float, nullable=False)
    electricity_night = Column(Float, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Tariffs, self).__init__(*args, **kwargs)    

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, nullable=False)
    payment_date = Column(Date, nullable=False)
    summ_of_pay = Column(Float)
    cold_water = relationship("MeterReading", uselist=False, back_populates="payment")
    hot_water = relationship("MeterReading", uselist=False, back_populates="payment")
    electricity_day = relationship("MeterReading", uselist=False, back_populates="payment")
    electricity_night = relationship("MeterReading", uselist=False, back_populates="payment")
    ethernet_pay = Column(Float)


    def __init__(self, *args, **kwargs):
        super(Payment, self).__init__(*args, **kwargs)
        self.summ_of_pay = calculate_the_amount()

    def calculate_the_amount(self):
        return self.ethernet_pay + self.cold_water.sum + self.hot_water.sum + self.electricity_day.sum + self.electricity_night.sum
    
    def __repr__(self):
        return '<Payment id: {}, date: {}>'.format(self.id, self.payment_date)

class MeterReading(Base):
    __tablename__ = 'meterreding'
    id = Column(Integer, primary_key =True)
    child_id = Column(Integer, ForeignKey('payment.id'))
    parent = relationship("Payment", back_populates = 'meterreding')
    score = Column(Float)
    sum = Column(Float)

    def __init__(self, *args, **kwargs):
        super(MeterReading, self).__init__(*args, **kwargs)

engine = create_engine('sqlite:///:memory:', echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
