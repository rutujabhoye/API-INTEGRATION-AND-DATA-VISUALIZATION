# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: RUTUJA SUBHASH BHOYE

*INTERN ID*: CT04DY1213

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

##INTERNSHIP TASK 1

API Integration and Data Visualization using Python

Introduction

In today’s digital era, APIs (Application Programming Interfaces) play a crucial role in enabling applications to interact with external services and fetch real-time data. API integration is one of the most essential skills in modern software development, as it allows developers to connect their applications with third-party data sources and provide more meaningful functionality to users. Alongside API integration, data visualization is equally important because raw data is often not easy to interpret. Visualization tools like charts and graphs transform numerical datasets into a more understandable and visually appealing format, allowing users to quickly extract patterns, trends, and insights.

This project has been developed as part of Internship Task – 1, where the requirement was to use Python to fetch data from a public API and then create visualizations using either Matplotlib or Seaborn. The specific objective was to demonstrate the complete workflow of connecting to an API, processing the returned data, and displaying it in a meaningful way. For this implementation, I selected the OpenWeatherMap API, which provides real-time weather data and forecasts for cities around the world. The visualization component was created using Matplotlib and Seaborn libraries, which are popular tools for data visualization in Python.

Objective of the Project:

1. The primary objective of this task is to:

2. Integrate with a public API using Python.

3. Fetch real-time weather forecast data from OpenWeatherMap.

4. Parse and process the data into a usable format.

5. Create meaningful visualizations for better understanding of weather patterns.

6. Ensure safe and secure coding practices by hiding API keys using environment variables.

7. Present the entire workflow as a professional and complete project ready for GitHub submission.

8. This project not only meets the internship requirement but also reflects a practical use case of combining API integration with visualization to solve real-world problems.

Tools and Technologies Used:

1. For successful implementation, the following tools and technologies were utilized:

2. Programming Language: Python

3. API Provider: OpenWeatherMap (Free API Key)

Libraries Used:

1. Requests: To send HTTP requests and fetch API data.

2. Matplotlib: To create plots and graphs for data visualization.

3. Seaborn: To create more advanced and visually appealing visualizations.

4. Python-dotenv: To load API keys securely from an environment file.

5. Development Environment: Python 3.10+ with any code editor (such as VS Code).

6. Version Control: GitHub for project storage and submission.

Project Workflow:

Step 1: Setting Up the Environment

A new project folder was created with the following structure:


│── main.py           # Python script
│── .env              # Secret API key (ignored from GitHub)
│── .gitignore        # Prevents sensitive files from being uploaded


All required libraries were installed using the command:

pip install requests matplotlib seaborn python-dotenv

Step 2: Obtaining the API Key

An account was created on the OpenWeatherMap website
. After logging in, an API key was generated from the API Keys section
. This key was copied and stored in a .env file as follows:

OPENWEATHER_API_KEY=your_api_key_here


This ensures the API key is never directly exposed in the Python script or in the GitHub repository.

Step 3: Writing the Python Script

The script performs three major tasks:

1. Fetching Data: A request is sent to the OpenWeatherMap forecast API, and the JSON response is captured.

2. Parsing Data: Important fields such as date, temperature, and humidity are extracted and stored in lists.

3. Visualizing Data: The extracted data is plotted using Seaborn and Matplotlib to display temperature and humidity trends over time.

4. The script allows the user to input any city name, making it dynamic and reusable for different locations.

Step 4: Visualization Dashboard

The visualization presents a line chart with two parameters:

Temperature (°C): Displayed as a red line.

Humidity (%): Displayed as a blue line.

The x-axis represents the date and time for each forecast interval, while the y-axis represents the respective values of temperature and humidity. This makes it easy to see how weather conditions change over a period of five days.

Step 5: Execution

To run the script, the user simply opens the terminal in the project folder and executes:

python main.py


The program prompts for a city name and then generates the visualization dashboard accordingly.

Key Features of the Project:

1. Secure API Key Management: API keys are hidden in a .env file, ensuring safe coding practices.

2. Dynamic Input: Users can enter any city name to view its weather forecast.

3. Clear Visualization: Temperature and humidity are displayed together for easy comparison.

4. User-Friendly Workflow: Simple structure, clear code, and professional organization of files.

5. Ready for GitHub: .gitignore ensures sensitive files are not exposed when uploading the project.

Output Example:

When executed, the program produces a graph that shows the forecasted temperature and humidity trends for the selected city. For instance, entering Mumbai generates a chart with temperature fluctuations in red and humidity levels in blue over the next five days.

This visualization helps in identifying daily trends, weather patterns, and possible correlations between temperature and humidity.

Deliverables:

1. The final deliverables for this project include:

2. main.py – Python script containing the logic for API integration and visualization.

3. .gitignore – Ensures sensitive files like .env are not uploaded.
  
4. Visualization Dashboard – The graphical output produced by running the script.

Learning Outcomes:

1. This project provided hands-on experience in the following areas:

2. How to integrate Python applications with external APIs.

3. Secure management of API keys using environment variables.

4. Extracting and processing JSON data from APIs.

5. Using Matplotlib and Seaborn to create professional visualizations.

6. Structuring and preparing a project for GitHub submission in a professional manner.

Conclusion

This project successfully demonstrates the integration of a public API with Python for real-time data fetching and the creation of meaningful visualizations. By combining API integration with data visualization techniques, the project not only satisfies the requirements of Internship Task – 1 but also provides a practical foundation for real-world applications. Weather forecasting is one of the most commonly used services across mobile and web platforms, and this implementation mirrors how such services work internally.

Overall, this project highlights the importance of combining backend data integration with frontend visualization to deliver impactful insights to end users. The knowledge and skills gained from completing this task will serve as a strong base for tackling more advanced projects in data science, machine learning, and software development in the future.

#OUTPUT

<img width="1800" height="956" alt="Image" src="https://github.com/user-attachments/assets/e75ec80d-7c0b-4692-a4f2-66808c04c62d" />
