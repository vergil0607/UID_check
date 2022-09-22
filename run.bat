

set original_dir=%CD%
echo %original_dir%

set venv_root_dir=%original_dir%\venv
cd %venv_root_dir%

call Scripts\activate.bat
cd %original_dir%

set python_path = %original_dir% and "venv\Scripts\python.exe"
set python_file = %original_dir% and "UIDBOT\ValidateUIDs.py"


"%original_dir%\venv\Scripts\python.exe" "%original_dir%\manage.py" "runserver"

pause

