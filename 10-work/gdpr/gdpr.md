# GDPR

### **Summary of the Project**

The project revolves around automating **Data Subject Requests (DSRs)** for Elsevier's DSR tool. It involves building a RESTful API that handles **Subject Access Requests (SARs)** and **Erasure Requests** in compliance with data privacy regulations (e.g., GDPR). The system is designed to process requests asynchronously, upload results to an S3 bucket, and notify the DSR application via a callback API.

---

### **Key Components**

1. **DSR Application**:
    - Initiates the DSR process by sending requests to the Wrapper API.
    - Provides details like `dsrCaseId`, `dsrFunction`, `applications`, and `subjectIdentifiers`.
2. **Wrapper Service**:
    - Validates requests from the DSR Application.
    - Creates an S3 folder for each request.
    - Calls the appropriate API (your system) to process the request.
3. **Your System**:
    - Implements the API to handle SARs and Erasure Requests.
    - Validates incoming requests and processes them asynchronously.
    - Uploads results (e.g., CSV files) to the specified S3 location.
    - Notifies the DSR Application of the results via the Callback API.
4. **Callback Service**:
    - Receives notifications from your system about the completion of requests.
    - Updates the DSR Application with the results.

---

### **Workflow**

1. **Request Initiation**:
    - A DPO submits a request in the DSR Application.
    - The DSR Application sends the request to the Wrapper API.
2. **Wrapper Processing**:
    - The Wrapper validates the request and creates an S3 folder.
    - It calls your system's API with the request details.
3. **Your System Processing**:
    - Your system validates the request and acknowledges it with a **202 Accepted** response.
    - It processes the request asynchronously:
        - For SARs: Collects and transforms data into a CSV file, then uploads it to S3.
        - For Erasure Requests: Anonymizes or deletes the specified data.
    - It notifies the DSR Application of the results via the Callback API.
4. **Callback Notification**:
    - The Callback API receives the results from your system.
    - It updates the DSR Application with the status of the request.

---

### **Key Features**

1. **Asynchronous Processing**:
    - Requests are processed asynchronously to handle long-running operations.
    - Results are communicated via the Callback API.
2. **S3 Integration**:
    - CSV files containing SAR results are uploaded to an S3 bucket.
    - The folder structure is organized by `dsrCaseId` and `application`.
3. **Error Handling**:
    - Invalid requests are rejected with a **400 Bad Request** response.
    - Errors during processing are communicated via the Callback API.
4. **Compliance**:
    - The system ensures compliance with data privacy regulations by handling SARs and Erasure Requests appropriately.

---

### **Technical Implementation**

1. **Spring Boot API**:
    - Built using Spring Boot for RESTful API development.
    - Handles SARs and Erasure Requests via two endpoints:
        - `/subject-access-requests`
        - `/erasure-requests`
2. **AWS S3 Integration**:
    - Uses the AWS SDK for Java to upload CSV files to S3.
3. **Callback API**:
    - Uses `RestTemplate` to send notifications to the DSR Application.
4. **Asynchronous Processing**:
    - Uses `ExecutorService` to handle requests asynchronously.

---

### **Example Scenarios**

### **1. Subject Access Request (SAR)**

- **Request**:
    
    json
    
    Copy
    
    ```
    {
      "dsrCaseId": "REQ7777777",
      "application": "JDW",
      "subjectIdentifiers": [
        {
          "subjectIdentifier": "test@elsevier.com",
          "subjectIdentifierType": "emailAddress"
        }
      ],
      "responseFileLocation": "REQ7777777/JDW/"
    }
    ```
    
- **Processing**:
    - Collects data for the specified email addresses.
    - Transforms the data into a CSV file.
    - Uploads the CSV file to S3.
- **Callback**:
    
    json
    
    Copy
    
    ```
    {
      "dsrCaseId": "REQ7777777",
      "application": "JDW",
      "subjectExists": true,
      "responseFileLocation": "REQ7777777/JDW/",
      "dataReturnComplete": true
    }
    ```
    

### **2. Erasure Request**

- **Request**:
    
    json
    
    Copy
    
    ```
    {
      "dsrCaseId": "REQ7777777",
      "application": "JDW",
      "subjectIdentifiers": [
        {
          "subjectIdentifier": "test@elsevier.com",
          "subjectIdentifierType": "emailAddress"
        }
      ],
      "responseFileLocation": "REQ7777777/JDW/"
    }
    ```
    
- **Processing**:
    - Anonymizes or deletes data for the specified email addresses.
- **Callback**:
    
    json
    
    Copy
    
    ```
    {
      "dsrCaseId": "REQ7777777",
      "application": "JDW",
      "subjectExists": true,
      "responseFileLocation": "REQ7777777/JDW/",
      "dataReturnComplete": true
    }
    ```
    

---

### **Summary of What I Understood**

The project is a **data privacy compliance tool** that automates the handling of **Subject Access Requests (SARs)** and **Erasure Requests**. It involves:

- A **DSR Application** that initiates requests.
- A **Wrapper Service** that validates requests and calls your system.
- **Your System**, which processes requests asynchronously, uploads results to S3, and notifies the DSR Application via a callback API.
- A **Callback Service** that updates the DSR Application with the results.

The implementation uses **Spring Boot** for the API, **AWS S3** for storing results, and **asynchronous processing** to handle long-running operations. The system ensures compliance with data privacy regulations by providing a structured and automated workflow for handling DSRs.

Let me know if you need further clarification or additional details!