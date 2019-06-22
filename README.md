# Python Automation Framework
This is a project for a web automation framework using Selenium, Python, allure reports and page object model. This automates the free demo HRM https://opensource-demo.orangehrmlive.com/.

# How to install it
* Make sure you have python installed on your machine by typing in console "python --version" if not go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.
* Clone the repository to any local path.
* Note: This has been created using Python environment in order to have all dependencies in the same folder rather than taking the packages for the global python configuration. If you wish to clone without env folder you have to download following python packages by running following pip commands:
  - pip install selenium (for webdriver)
  - pip install pytest (for pytest framework)
  - pip install pytest-html (for pytest html report)
  - pip install allure-pytest (for allure reporting)
  - pip install moment (for time functions)
  - pip install webdriver_manager (for web driver download without need of .exe)

# How to run it
#####1. Run directly
* Run `run.py`in project folder via Pycham or any other python editor
#####2. Command line
* Enter the following command in cmd being located in the folder path
  - `python -m pytest`
* Optional parameters
  - --html=reports/report1.html For Pytest html reporting
  - --self-contained-html For having Pytest html report with inline CSS
  - --browser <firefox, chrome> To choose different browser, default is chrome
  - --alluredir=<path> To create files needed for allure reports, run this every time your code changes
    or new funtionality exists, in this case "alluredir=reports/allure-reports"
* Example: `python -m pytest --alluredir=report/json --browser=chrome`
* To generate allure reports you need to type the following in the project path
  - allure serve <path where allure files are>, in this case "allure serve report/json"
   

# Technologies used
* Python 3.
* Selenium Package.
* Chromedriver.exe and geckodriver.exe for Chrome and Firefox web drivers respectively.
* Pytest in order to have test cases, init and tear down.

# Jenkins CI
* Allure plugin have benn installed on Jenkins
* Allure-commandline on executor have been set in PATH of environment variables
* Make sure the allure report have benn set correctly on Jenkins
  - Manage Jenkins -> Global Tool Configuration -> Allure Commandline  set commandline path
* Create job and set in the Configure:
  - General -> click the Advanced button -> Use custom workspace set project path
  - Build -> Execute Windows batch Command:
    - `call venv\Scripts\activate.bat`
    - `python -m pytest --alluredir=report/json --browser=chrome`
    - `exit 0`
  - Post-build Actions -> Allure report -> Result:Path [report/json] -> Report:Path 
  [report/html]
* **Note**: Better to download "jenkins.war" package and start it by command if OS is windows,installed directly in the form of MIS package, it starts in the form of service process, and runs script commands in the form of process when calling commands, which results in the failure of Google Browser.