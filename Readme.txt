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
