from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import NewPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "helloworld99"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


@app.route('/')
def show_home_page():
    """Show Home Page with Links to Available and Adopted Pets """
    return render_template('home.html')


@app.route('/available')
def show_available_pets():
    """Page displaying Available Pets"""
    pets = Pet.query.all()
    return render_template('available_pets.html', pets=pets)


@app.route('/adopted')
def show_adopted_pets():
    """Page displaying Adopted Pets"""
    pets = Pet.query.all()
    return render_template('adopted_pets.html', pets=pets)


@app.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    """Form for adding pets"""
    form = NewPetForm()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        name = form.name.data
        species = form.species.data
        pet = Pet(**data)
        # Inserts placeholder IMG if url is blank in form
        if form.photo_url.data:
            pet.photo_url = form.photo_url.data
        else:
            pet.photo_url = '/static/placeholder.jpg'
        db.session.add(pet)
        db.session.commit()
        flash(f'{pet.name} successfully added', 'success')
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/pets/<int:pet_id>')
def display_pet_info(pet_id):
    """Displays information on Pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)


@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_info(pet_id):
    """Change Pet Information"""
    pet = Pet.query.get_or_404(pet_id)
    # Inserts placeholder IMG if url is blank in form
    if pet.photo_url == '/static/placeholder.jpg':
        pet.photo_url = ''
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        if form.photo_url.data:
            pet.photo_url = form.photo_url.data
        else:
            pet.photo_url = '/static/placeholder.jpg'
        pet.age = form.age.data
        pet.species = form.species.data
        pet.notes = form.notes.data
        if form.available.data == 'True':
            pet.available = True
        else:
            pet.available = False
        db.session.commit()
        flash(f'{pet.name} successfully edited', 'success')
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', pet=pet, form=form)
