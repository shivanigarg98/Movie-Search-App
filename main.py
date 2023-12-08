import subprocess
import os
import time
import threading
from data_collection.data_collection import collect_data
from data_processing.data_processing import process_data
from database.database import create_db

def run_tasks():
    
    task1 = collect_data()
    
    if task1:
        task2 = process_data()
    
    if task1 and task2:
        task3 = create_db()
        
    
    if task1 and task2 and task3:
        print("All tasks runned successfully!")
        return True
    else:
        print("Stopping as all tasks didn't run")
        return False

def run_app():
    if run_tasks():
        # Function to run Flask app
        def run_flask():
            try:
                print("Flask is Starting ....")
                current_directory = os.getcwd() 
                flask_app_path = current_directory + '/website/backend.py'
                subprocess.run(["python", flask_app_path])
            except Exception as e:
                print(f"Flask is not Starting : {e}")
                

        # Function to run Streamlit app
        def run_streamlit():
            try:
                print("Streamlit is Starting ....")
                current_directory = os.getcwd()
                streamlit_app_path = current_directory + '/website/frontend.py'
                subprocess.run(["streamlit", "run", streamlit_app_path])
            except Exception as e:
                print(f"Streamlit is not Starting : {e}")
            
        # Start Flask app in a separate thread
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.start()
            
        # Wait for Flask app to start (adjust the time as needed)
        time.sleep(10)
        
        # Start Streamlit app in another thread
        streamlit_thread = threading.Thread(target=run_streamlit)
        streamlit_thread.start()
        print("App is Starting ...")
    else:
        print("Not able to start the app")
if __name__ == "__main__":
    run_app()
    print("App is Running ... ")
    
    
