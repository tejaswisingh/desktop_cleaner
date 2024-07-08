This script can take all the files in the specified directory and move them to your specified folder. 

To convert the script into a windows executable one would need to install pyinstaller. 
  1. You could use the command below to install it(you might need admin rights, so you would need to run command prompt as Administrator) :-

    `pip3 install pyinstaller`


  2. Then navigate to the directory containing the script and run the following command:-

    `pyinstaller --onefile -w 'desktop_cleanup.py'`

To run the unit tests, use the following command:-

    `python -m unittest test_desktop_cleanup`
