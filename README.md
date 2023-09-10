# Dolphinido Audio Fingerprint

## Configuration 

### Database

#### Open `.env` file at the root of the directory

Add database connection details
````
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=dolphinido
DB_USERNAME=root
DB_PASSWORD=root
````
### Migrations
1. Run `$ masonite-orm migrate` to run database migrations
1. Run `$ masonite-orm migrate:reset` to reset database migrations

## Usage 
1. Run `$ python artisan --fingerprint /path/to/mp3/file` to fingerprint mp3 file
1. Run `$ python artisan --radio station` to listen to radio station
1. Run `$ python artisan --recogmic 20` to record and recognize audio from microphone for 20 seconds
1. Run `$ python artisan --recogfile /path/to/mp3/file` to recognize audio file
1. Run `$ python artisan --recogradio station` to recognize audio from fm radio
