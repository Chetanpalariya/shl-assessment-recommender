SHL Assessment Recommender
This web application helps recommend SHL assessments based on a candidate's attributes. Built using Streamlit, the app allows users to upload candidate data, analyze it, and receive tailored recommendations for suitable assessments.

🚀 Features
📂 Upload CSV: Upload a file with candidate data (e.g., age, experience, skills, etc.)

🧠 Assessment Recommendations: Get SHL assessment suggestions based on candidate characteristics

📊 Visualizations: View data insights using interactive charts and tables

🛠 Technologies Used
Streamlit – for building the web UI

pandas – for data handling

scikit-learn – for prediction logic

matplotlib – for visualizations

📦 Prerequisites
Python 3.x

Git (optional, for cloning)

Virtual environment tool (optional but recommended)

🔧 Installation
# 1. Clone the repository
git clone https://github.com/Chetanpalariya/shl-assessment-recommender.git

# 2. Navigate into the project directory
cd shl-assessment-recommender

# 3. (Optional) Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
▶️ Usage
streamlit run app.py
Once running, the app will open in your browser. You can upload a CSV file and receive assessment recommendations based on candidate data.

🌐 Deployment
To deploy on Streamlit Cloud:

Push your code to GitHub

Visit Streamlit Cloud

Click "New App"

Select your GitHub repo and set app.py as the main file

Click Deploy

That's it! You'll get a shareable link to your live app.

📁 Example Dataset
The repo includes a sample dataset:
shl_sample_assessments.csv

Example columns:

Candidate Name

Age

Experience

Skills

Current Role

You can replace this file with your real candidate data.

🤝 Contributing
Contributions are welcome!
Feel free to:

Fork this repo

Submit a pull request

Open issues for suggestions or bugs

📄 License
This project is licensed under the MIT License.
