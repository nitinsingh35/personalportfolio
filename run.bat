@echo off
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask server...
echo Open your browser and navigate to http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
