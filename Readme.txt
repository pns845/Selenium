dropdown selection:
value,index,visible text.
navigation commands:
it is used to refresh---driver.refresh()
it is used to navigate back---driver.back()
it is used to move forward---driver.forward()
close--it closes the browser window on which the focus is set.
Actions class is an ability provided by Selenium for handling keyboard and mouse events.

-With the logging module imported, you can use something called a “logger” to log messages that you want to see
-Logger:This is the class whose objects will be used in the application code directly to call the functions.
the objects of the Logger class, which are instantiated using the module-level function logging.getLogger(name)
-LogRecord: Loggers automatically create LogRecord objects that have all the information related 
to the event being logged, like the name of the logger,the function, the line number, the message, and more
-Handler: Handlers send the LogRecord to the required output destination, like the console or a file.
-Formatter: This is where you specify the format of the output by specifying a string format 
that lists out the attributes that the output should contain.
-unlike the root logger, a custom logger can’t be configured using basicConfig().
You have to configure it using Handlers and Formatters:
-Handlers send the log messages to configured destinations like the standard output 
stream or a file or over HTTP or to your email via SMTP.
inspect.stack[1][3]---gets the name of class/method from where the method is called.
-add handler--Add handlers to the logger

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
---------------------------------------------------------------------------
test suite preparation:
from module import the classes
get all tests from classes using TestLoader().loadTestsfromTestcase()
create a test suite ---final= [tc1,tc2]
run the test suite using unittest.TextTestRunner(verbosity=2).run(final)
---------------------------------------
pytest
need to install pytest-------- pip3 install pytest
run only particular test:
py.test testname -s-v        -s is for printing messages
run the whole package
py.test -s-v   it runs the whole package
run only partcular test case from test script
py.test modulename::testcasename
------------------

for the test runs to run in order you need to install py-test ordering module
@pytest.mark.run(order=1)
-------------
to run from different browsers from command line
--------------------
drag and drop:
import Action Chains
create object:  action_onj=ActionChains(driver)
action_obj.movetoelement(source,target).perform()
----------
mousehover
import Action Chains
create object:  action_onj=ActionChains(driver)
action_obj.movetoelement(element_name).perform()
-----------
to move to specific co-ordinate
action_obj.move_to_offset(horizon,vertical)
-------------
unitTest Default methods-----setUp,setUp Class,tearDown,tearDownClass
-----------
pass means no operation to be done
------------
a='123'
int(a)---converts it into int
------------------------------------------
RUNNING THROGH COMMAND LINE
write in conftest 
then add parser as argument
parser.addoption("--browser")---which we need to get from command line
parser.request.getoption("--browser")
a decorator @pytest.fixture(scope='')
def a method to return the calue
def browser(request):
   return request.config.getoption("--browser")
----------------------
By using the pytest.mark helper you can easily set metadata on your test functions. There are some builtin markers, for example:
skip - always skip a test function
skipif - skip a test function if a certain condition is met
xfail - produce an “expected failure” outcome if a certain condition is met
parametrize to perform multiple calls to the same test function.
-------------------------------------
framework:
conftest file is always placed in tescase package
autouse--- it will be instantiated before other fixtures within the same scope.
An optional parameter to the fixture decorator is ‘autouse’.
It defaults to ‘False’.
With the value of ‘False’, tests that wish to use the fixture need to either name it in their parameter list, or have a use fixtures decorator applied to the test.
With the value set to ‘True’, all tests in this session just use the fixture automatically.
https://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/#return_value
------------------------------------
A method is a function declared inside class definition and has a variable self passed as a first parameter,to be able to let the instance of that class access it.
@classmethod--
https://medium.com/@rahulkp220/methods-classmethods-and-staticmethods-in-python-4f65c0e0d417
let the class know that we are going to pass a classmethod?
---------------------------
conftest.py is a file which resides at base of your test directory tree. In this file you can store all test fixtures and these are then automatically discovered by Pytest, so you don't even need to import them.
This is also helpful if you need to share data between multiple tests — just create fixture that returns the test data.
traceback.print()--This function prints a stack trace from its invocation point. The optional f argument can be used to specify an alternate stack frame to start. The optional limit and file arguments have the same meaning as for print_exception().

