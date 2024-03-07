
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.types import DECIMAL, UUID


from infrastructure.database import get_base
from sqlalchemy import ForeignKey, TIMESTAMP, Column, func, Time, UniqueConstraint

Base = get_base()


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str]


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    nickname: Mapped[str] = mapped_column(unique=True)
    status: Mapped[bool] = mapped_column(default=True)
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
    name: Mapped[str] = mapped_column(nullable=False)
    price = Column(DECIMAL, nullable=False)
    description: Mapped[str]
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    __table_args__ = (UniqueConstraint("user_id", "name", name="_user_name_uc"),)


class Schedule(Base):
    __tablename__ = "schedules"
    id: Mapped[int] = mapped_column(primary_key=True)
    day_of_week: Mapped[int]
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))
    timing_id: Mapped[int] = mapped_column(ForeignKey('times.id'))

    service = relationship("Service")
    timing = relationship("Timing")

