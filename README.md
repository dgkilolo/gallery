# Gallery.
# A gallery application that displays various images that have been added by the admin {version: 25/05/2020}
# By: David Kilolo
# Description
Gallery is an application that displays various images post by the admin.
Users can view all images, search for particular image as well as view the images based on their location.
## Setup/Installation Requirements
* Gallery has its main page as the page that displays all the images from there the user can search for various images based on their category and their location. The user can also click on images to see additional information about those images.
## Technologies Used
This project was created using Python.
SQL database provides storage from the various writer and reader features
It is deployed on Heroku.
## Support and contact details
Feel free to contact me incase of any issues with the site as well as any ideas or contributions on how to improve the code.
### License
MIT (c) David 2020

## Gallery
- A gallery application that displays various images that have been added by the admin.
- It allows the user to post their photos for others to see

### Required Features
- View posted pictures on the homepage.
- Search for photos based on category.
- Click on a photos to view the details of the photo.
- Search for photos based on location.

### Additional Features
- Copy a link to the photo to share with my friends.

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

## Technologies & Languages

- Django 3.0.6
- Python 3.6.9
- Html
- Css
- Bootstrap4

# Installation and Setup

Clone the repository below

```
git clone https://github.com/dgkilolo/gallery
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| GET    |        /search                  | search projects using category        | users         |
| GET    |        /location                | search projects using location        | users         |


## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
Copyright{ 2020 }