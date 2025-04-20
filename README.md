# 750-tech-demo **🧠 Web Summariser**

A fullstack application that allows users to **input a website URL**, then scrapes and summarises the content using **Flask**, **BeautifulSoup**, and **OpenAI GPT-4.1-mini**.

> Built with a focus on backend logic and AI integration, this project demonstrates scraping from static and authenticated sites, structured API design, and summarisation via openai API.

---

## 🔧 Installation

### Clone the repo

```bash
git clone https://github.com/markkwang/750-tech-demo.git
cd 750-tech-demo
```

### 1. Set up Backend environment

- Make sure you have python3 installed (3.11.11 recommended).
- Suggested to use Conda for virtual environment.

#### Install libraries

```bash
cd backend
pip install -r requirements.txt
```

#### Create `.env` file

- `backend/.env`
- The key will be provided in **_Assignment - Private info / API key / etc submission_**

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

#### Run the Flask server

```bash
python run.py
OR
python3 run.py
```

### 2. Frontend Setup

- Open up another terminal
- Make sure you have node installed (v18.20.8 recommended)

#### Install dependencies

```bash
cd frontend
npm install
```

#### Start the development server

```bash
npm run dev
```

### 3. Open the Website

By default:

- The **frontend** runs on [http://localhost:5173](http://localhost:5173)
- The **backend** runs on [http://localhost:5321](http://localhost:5321)

> **Important:**  
> Make sure that **ports 5173 and 5321 are not already in use** on your machine.  
> If they are, you can close the processes using them.

Once both servers are running, open your browser at [http://localhost:5173](http://localhost:5173) to use the app.

## 📝 How to Use the App

1. **Enter a Valid URL**  
   In the chat input field, type a **valid and complete URL** (e.g.,  
   `https://americanliterature.com/childrens-stories/little-red-riding-hood`).  
   Make sure the URL is correctly formatted and accessible.

2. **Submit the URL**  
   Press the **Enter** key or the **Enter button**.  
   The application will scrape the website, send the content to GPT, and display a summary in the chat window.

3. **Continue the Conversation**  
   After receiving the summary, you may ask **follow-up questions** or discuss the content further.  
   GPT will respond in context, maintaining the flow of the conversation.

### Recommended Test Websites

Some websites may block scraping tools due to bot protection, rate limiting, or CAPTCHAs.  
To ensure consistent and reliable results, it is **recommended to use the following websites**, which are known to work with this project:

- https://www.bbc.com
- https://quotes.toscrape.com
- https://the-internet.herokuapp.com

These are already used in the provided `/test_crawler_*` endpoints and allow scraping without advanced headers, cookies, or JavaScript rendering.

> Using other websites may result in blocked requests or incomplete content.

## ⚠️ Warning

> Basic error handling is not implemented in the current version.

Invalid or inaccessible URLs may cause the application to return an error or behave unexpectedly.

## 🖋️ Author

Mark Wang _(zwan633@aucklanduni.ac.nz)_
