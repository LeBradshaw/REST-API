# REST-API
The goal of this project will be to build a simple REST API in Python and containerize it using Docker. This container image will then be uploaded to the Docker public repository and I will be downloading this image to run it in my local Docker environment for testing. You are free to use any Python web framework you want, but I strongly recommend Flask (http://flask.pocoo.org (Links to an external site.)) for its simplicity and ease of use. Your API should run on the default Flask port (5000) and expose the following URIs:

/md5/<string>
This endpoint will return the MD5 hash of the string that is passed as the input. Ex.: for a string of Hello World the MD5 hash should be b10a8db164e0754105b7a99be72e3fe5. Don’t forget to handle spaces and other special HTTP characters correctly!

/factorial/<int>
This endpoint will return the factorial (product of the integer and all integers below it) for the integer that is passed as input. If the input is not a positive integer, the output should contain and error description.

/fibonacci/<int>
This input will return an array of integers with all the Fibonacci numbers (in order) that are less than or equal to the input number. If the input is not a positive integer, return an error description. 

/is-prime/<int>
This endpoint will return a boolean value depending on whether the input is a prime number. Again, return a descriptive error if the input is invalid.

/slack-alert/<string>
This endpoint is the only one that has a side-effect. Your API should attempt to post the value of the input into a Slack channel in our class Slack team, then return a boolean value that indicates whether the message was successfully posted to the channel. 

Each URI endpoint should return the same result: a JSON payload that consists of an input and an output value. The data type of the two values should vary depending on the endpoint that is being called, like this example for the /factorial/ URI:
  
{
  "input": 4,
  "output": 24
}
  
I will be automating the grading of this assignment using a script that will pull the Docker image, launch the container, then test the JSON output for an expected result. I would suggest you assign one or two members of your team to build your own automated “deploy and test” script so that you can be sure that what I do will perform as expected. The grade for this project will rest on two criteria: does the project build and run? What does the electronic record or group collaboration in both GitHub and Slack tell me about your team affinity and effectiveness?
