"""empty message

Revision ID: 0cf6cb1ed5ac
Revises: 
Create Date: 2017-07-24 11:06:09.590713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf6cb1ed5ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=63), nullable=True),
    sa.Column('password', sa.String(length=252), nullable=True),
    sa.Column('user_email', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(length=256), nullable=True),
    sa.Column('model_user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['model_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_user_id', sa.Integer(), nullable=True),
    sa.Column('project_name', sa.String(length=252), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tstresults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Test_user_id', sa.Integer(), nullable=True),
    sa.Column('test_num', sa.Integer(), nullable=True),
    sa.Column('pass_num', sa.Integer(), nullable=True),
    sa.Column('fail_num', sa.Integer(), nullable=True),
    sa.Column('skip_num', sa.Integer(), nullable=True),
    sa.Column('test_time', sa.DateTime(), nullable=True),
    sa.Column('hour_time', sa.Integer(), nullable=True),
    sa.Column('test_rep', sa.String(length=252), nullable=True),
    sa.Column('test_log', sa.String(length=252), nullable=True),
    sa.ForeignKeyConstraint(['Test_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interfaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('projects_id', sa.Integer(), nullable=True),
    sa.Column('Interface_name', sa.String(length=252), nullable=True),
    sa.Column('Interface_url', sa.String(length=252), nullable=True),
    sa.Column('Interface_meth', sa.String(length=252), nullable=True),
    sa.Column('Interface_par', sa.String(length=252), nullable=True),
    sa.Column('Interface_back', sa.String(length=252), nullable=True),
    sa.Column('Interface_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Interface_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['models.id'], ),
    sa.ForeignKeyConstraint(['projects_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interfacetests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('projects_id', sa.Integer(), nullable=True),
    sa.Column('Interface_name', sa.String(length=252), nullable=True),
    sa.Column('Interface_url', sa.String(length=252), nullable=True),
    sa.Column('Interface_meth', sa.String(length=252), nullable=True),
    sa.Column('Interface_pase', sa.String(length=252), nullable=True),
    sa.Column('Interface_assert', sa.String(length=252), nullable=True),
    sa.Column('Interface_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Interface_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['models.id'], ),
    sa.ForeignKeyConstraint(['projects_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interfacetests')
    op.drop_table('interfaces')
    op.drop_table('tstresults')
    op.drop_table('projects')
    op.drop_table('models')
    op.drop_table('users')
    # ### end Alembic commands ###
