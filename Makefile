migrate:
	python noreeter/manage.py makemigrations users interests
	python noreeter/manage.py migrate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.swp" -exec rm -rf {} \;
	find . -name "*.swo" -exec rm -rf {} \;
