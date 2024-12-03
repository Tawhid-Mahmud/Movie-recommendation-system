# Movie Recommendation System

This is a simple movie recommendation system built using Streamlit. It recommends movies based on cosine similarity of movie features.

## Features

- Select a movie from a dropdown list to get recommendations.
- Displays the top 10 recommended movies with their posters.

## Installation

1. **Clone the repository:**

   ```bash
   https://github.com/Tawhid-Mahmud/Movie-recommendation-system.git
   cd movierecommendation
   ```app.py

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   streamlit run app.py
   ```

## Files

- `app.py`: The main application file.
- `movies.pkl`: Pickle file containing movie data and cosine similarity matrix.
- `requirements.txt`: List of required Python packages.

## Requirements

- Python 3.6 or higher
- Internet connection for fetching movie posters

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [The Movie Database (TMDb)](https://www.themoviedb.org/) for movie data and posters.
