migrate:
	python noreeter/manage.py makemigrations users interests activities towns
	python noreeter/manage.py migrate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.swp" -exec rm -rf {} \;
	find . -name "*.swo" -exec rm -rf {} \;
	find . -name "*.DS_Store" -exec rm -rf {} \;
