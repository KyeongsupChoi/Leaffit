## ✨ Leaffit

> Generate Wendler Exercise Sheets based on your One Rep Max weights  
> 
> Hosted on https://kyeongsupchoi.pythonanywhere.com/wendler.html
> 
> Wendler Program explanation at https://www.t-nation.com/workouts/5-3-1-how-to-build-pure-strength/

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- mysite/                               # Main app directory
   |    |
   |    |-- home/                            # Holds the html template files
   |    |    |-- wendler.html                # Wendler html file with Django tags and Bootstrap          
   |    |
   |    |-- asgi.py                          # ASGI config for mysite project.
   |    |-- forms.py                         # Define Wendler forms
   |    |-- models.py                        # Define Wendler models
   |    |-- settings.py                      # Define Global Settings
   |    |-- urls.py                          # Define URLs served by all apps/nodes 
   |    |-- views.py                         # Handles Wendler input and calculations
   |    |-- wsgi.py                          # Deploys app in production
   |    |
   |    |-- venv/                            # Virtual env directory
   |
   |-- db.sqlite3                            # SQLite storage
   |-- README.md                             # Standard readme documentation
   |-- requirements.txt                      # Development modules
   |-- manage.py                             # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Libraries Used

- ✅ `Django` - Basic Web Framework and MVT design pattern
- ✅ `ReportLab` - Exporting in PDF format
- ✅ `Docx` Exporting in DOCX format for Word and Google Docs
