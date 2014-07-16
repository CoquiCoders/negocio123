"""empty message

Revision ID: 1993c8d9b834
Revises: 34e59d01c042
Create Date: 2014-07-16 11:39:45.406580

"""

# revision identifiers, used by Alembic.
revision = '1993c8d9b834'
down_revision = '34e59d01c042'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step', 'short_title', new_column_name="titulo_corto_de_agencia")
    op.alter_column('step', 'full_title', new_column_name="nombre_de_agencia")
    op.alter_column('step', 'description', new_column_name="descripcion")
    op.alter_column('step', 'time_period', new_column_name="duracion")
    op.alter_column('step', 'online', new_column_name="tramite_online")
    op.alter_column('step', 'offline', new_column_name="tramite_offline")
    op.alter_column('step', 'type_of_process', new_column_name="tipo_de_tramite")
    op.alter_column('step', 'step_cost', new_column_name="costo_de_tramite")
    op.alter_column('step', 'papers_to_fill', new_column_name="requisitos")
    op.alter_column('step', 'attention', new_column_name="consideraciones")
    op.alter_column('step', 'questions', new_column_name="preguntas_frecuentes")
    op.alter_column('step', 'step_url', new_column_name="url_de_agencia")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step', 'nombre_de_agencia', new_column_name='full_title')
    ### end Alembic commands ###
