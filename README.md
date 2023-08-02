# ntf-backend

The Django backend of the [Twitter Image Scraper](https://github.com/marcomartinscastanho/twitter-image-scraper) project.  
It manages an image gallery, serving a REST API through Django REST Framework that allows to store/access images in the gallery.

It was once also possible to asynchronously publish images saved in the gallery to a Tumblr-like blog website, but that's no longer possible.  
Still, the code to do that was kept for purposes of future consultation.  

The purpose of this project was to learn and practice useful technologies.

## Installing

Clone this repository.  
Create a virtual environment.  
Install the `requirements.txt` inside the virtual environment.  
Run the `migrations.sh` script in the root repository.
