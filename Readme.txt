Selenium Webdriver
Module 23:
MouseHover---ActionChains
Drag and Drop
Slider
module 24
-With the logging module imported, you can use something called a “logger” to log messages that you want to see
-Logger:This is the class whose objects will be used in the application code directly to call the functions.
-LogRecord: Loggers automatically create LogRecord objects that have all the information related 
to the event being logged, like the name of the logger,the function, the line number, the message, and more
-Handler: Handlers send the LogRecord to the required output destination, like the console or a file.
-Formatter: This is where you specify the format of the output by specifying a string format 
that lists out the attributes that the output should contain.
-unlike the root logger, a custom logger can’t be configured using basicConfig().
You have to configure it using Handlers and Formatters:
-Handlers send the log messages to configured destinations like the standard output 
stream or a file or over HTTP or to your email via SMTP.
UnitTest:
https://towardsdatascience.com/level-up-your-code-with-python-decorators-c1966d78607---decorators
@decorator
def func():
is equivalent to:
def func():
    …
func = decorator(func)
The difference manifests itself when you have more than one test method in your class. setUpClass and tearDownClass are run once for the whole class; setUp and tearDown are run before and after each test method.
setUpClass is called only once and that is before all the tests, while setUp is called immediately before each and every test
If the setUp() method it self raises an exception while executing tests, the test methods will not be executed. But If setUp() is executed successfully, tearDown() will run even if the test method is passed or not.
If we import the module, then __name__ is the module's filename, without a directory path or file extension:
verbosity argument to the main(). It’ll get the test result details displayed on the console.
setUpClass() and tearDownClass() methods along with the @classmethod decorator. These methods enable us to set the values at the class level rather than at the method level. The values initialized at class level are shared between the test methods.
