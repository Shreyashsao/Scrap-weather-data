# Scrap-weather-data
BeautifulSoup | Python

### **Objective:**

Scrape the last 10 days' weather data from [`Weather.com`,](https://weather.com/en-IN/weather/tenday/l/a5f0fe2ff9a40acc9ce62d67cd99439a71cde78cc0c5c1fbf6da052bef4cdba9) including the columns `day`, `day name`, `Day high temprature`, `Day low temprature`, `weather_conditions`, `rain_percentage`, `wind_speed,  wind_direction`

### **Learning Outcomes:**

- Understand and apply basic web scraping techniques.
- Learn how to extract and parse specific data from a webpage.
- Gain experience in data cleaning and structuring.

### **Pre-requisites:**

- Basic knowledge of Python.
- Python environment with libraries: BeautifulSoup, requests.

### **Tools and Libraries:**

- Python: Download Python
- BeautifulSoup: A Python library for parsing HTML and XML documents.
- Requests: A Python library for making HTTP requests.

### **Installation:**

Open your terminal or command prompt and install the required libraries:

```python
pythonCopy code
pip install beautifulsoup4
pip install requests

```

### Assignment **Guidelines:**

1. **Understanding the Webpage Structure:**
    - Visit Weather.com and find the section where historical weather data is displayed.
    - Use your browser’s developer tools (right-click on the page and select “Inspect”) to understand the HTML structure.
2. **Fetching the Webpage:**
    - Write a Python script that uses the **`requests`** library to fetch the content of the webpage.
    - Ensure you handle network errors and response status codes appropriately.
3. **Parsing the HTML Content:**
    - Create a BeautifulSoup object to parse the fetched HTML content.
    - Identify and understand the HTML elements and classes that contain the required data (`day`, `day name`, `Day high temprature`, `Day low temprature`, `weather_conditions`, `rain_percentage`, `wind_speed,  wind_direction`)
4. **Extracting Required Data:**
    - Write code to navigate the HTML tree and extract the needed data.
    - Pay attention to data formats and units
5. **Data Cleaning and Structuring:**
    - Clean the extracted data, if necessary, to remove unwanted characters or whitespace.
    - Structure the data in a readable format like a CSV file.
6. **Storing the Data:**
    - Save the cleaned and structured data into a CSV file using Python's CSV library or a similar method.
    - Final Output should look like -:
        
        
        ![Screenshot 2024-01-23 145549.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f7bbda13-6f21-4b53-9418-792104a18c8c/da1c291d-d83e-4300-acdd-4e729b2a0074/Screenshot_2024-01-23_145549.png)
        
7. **Error Handling and Debugging:**
    - Add error handling in your script to manage unexpected issues (e.g., missing data, webpage structure changes).
    - Test your script thoroughly to ensure it works correctly.
8. **Submission:**
    - Submit the final Python script along with the output CSV file in a google drive folder and share link of that folder on LMS.

**Helpful Links**

- Basics of HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
- https://pypi.org/project/beautifulsoup4/
- https://beautiful-soup-4.readthedocs.io/en/latest/
