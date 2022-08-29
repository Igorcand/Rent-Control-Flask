from flask_uploads import UploadSet, configure_uploads, IMAGES
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def init_app(app):
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
    photos = UploadSet("photos", IMAGES)
    configure_uploads(app, photos)