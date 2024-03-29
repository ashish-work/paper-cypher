"""update embedding dims

Revision ID: 0b65f52c1eb7
Revises: 5b57f2ec9428
Create Date: 2024-01-25 20:58:34.664389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import pgvector


# revision identifiers, used by Alembic.
revision: str = '0b65f52c1eb7'
down_revision: Union[str, None] = '5b57f2ec9428'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('embeddings', 'vector',
               existing_type=pgvector.sqlalchemy.Vector(dim=5000),
               type_=pgvector.sqlalchemy.Vector(dim=4096),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('embeddings', 'vector',
               existing_type=pgvector.sqlalchemy.Vector(dim=4096),
               type_=pgvector.sqlalchemy.Vector(dim=5000),
               existing_nullable=True)
    # ### end Alembic commands ###
