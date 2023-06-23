"""update models

Revision ID: 9e55c48c021b
Revises: 
Create Date: 2023-06-23 02:47:20.732657

"""
import sqlalchemy as sa
from fastapi_utils.guid_type import GUID

from alembic import op

# revision identifiers, used by Alembic.
revision = "9e55c48c021b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "course",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", GUID(), nullable=True),
        sa.Column("course_name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_course_course_name"), "course", ["course_name"], unique=False
    )
    op.create_index(op.f("ix_course_id"), "course", ["id"], unique=False)
    op.create_table(
        "student",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", GUID(), nullable=True),
        sa.Column("first_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.Column("date_of_birth", sa.Date(), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_student_email"), "student", ["email"], unique=True)
    op.create_index(
        op.f("ix_student_first_name"), "student", ["first_name"], unique=False
    )
    op.create_index(op.f("ix_student_id"), "student", ["id"], unique=False)
    op.create_index(
        op.f("ix_student_last_name"), "student", ["last_name"], unique=False
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", GUID(), nullable=True),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("password", sa.String(length=128), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=True)
    op.create_table(
        "gradecard",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", GUID(), nullable=True),
        sa.Column("course_uuid", GUID(), nullable=True),
        sa.Column("student_uuid", GUID(), nullable=True),
        sa.Column("grade", sa.Enum("A", "B", "C", "D", "F"), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_uuid"],
            ["course.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["student_uuid"],
            ["student.uuid"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_gradecard_id"), "gradecard", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_gradecard_id"), table_name="gradecard")
    op.drop_table("gradecard")
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_student_last_name"), table_name="student")
    op.drop_index(op.f("ix_student_id"), table_name="student")
    op.drop_index(op.f("ix_student_first_name"), table_name="student")
    op.drop_index(op.f("ix_student_email"), table_name="student")
    op.drop_table("student")
    op.drop_index(op.f("ix_course_id"), table_name="course")
    op.drop_index(op.f("ix_course_course_name"), table_name="course")
    op.drop_table("course")
    # ### end Alembic commands ###