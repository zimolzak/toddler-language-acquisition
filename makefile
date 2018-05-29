# Depends on https://github.com/holman/spark
all :
	python nonpandas.py
	python nonpandas.py --spark | spark
