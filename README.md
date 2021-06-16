## DevelopsToday NewsBoard TestTask
First we must create `.env` file:
```
echo "PROJECT_NAME=DevelopsTodayTestTask" > .env
```

Then run `docker-compose`:
```
sudo docker-compose up --build -d
```

Now you can access the API on `http://localhost:8920/`

### Admin panel
```
Username: admin
Password: admin12345
```

### Additional
Run ```./manage.py runjobs -l``` to see the job that runs once a day and resets upvotes

Link to PostmanCollectionsDocs: https://documenter.getpostman.com/view/13600661/TzeWFnLv