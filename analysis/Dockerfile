ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

LABEL Matt Downs <lifeofabit.com>

# Switch to root and install needed libraries
USER root
RUN pip install pandas numpy seaborn plotly scikit-learn

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
