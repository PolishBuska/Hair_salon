
from sqlalchemy.orm import mapped_column, Mapped, relationship, registry
from sqlalchemy.types import DECIMAL


from infrastructure.database import get_base
from sqlalchemy import ForeignKey, TIMESTAMP, Column, func, Time

Base = get_base()


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str]


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    nickname: Mapped[str] = mapped_column(unique=True)
    status: Mapped[bool] = mapped_column(default=True)
    password: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), default=1)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())


class Timing(Base):
    __tablename__ = "times"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    from_t = Column(Time)
    to_t = Column(Time)


class Service(Base):
    __tablename__ = "services"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price = Column(DECIMAL)
    description: Mapped[str]
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())


class Schedule(Base):
    __tablename__ = "schedules"
    id: Mapped[int] = mapped_column(primary_key=True)
    day_of_week: Mapped[int]
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))
    timing_id: Mapped[int] = mapped_column(ForeignKey('times.id'))

    service = relationship("Service")
    timing = relationship("Timing")
