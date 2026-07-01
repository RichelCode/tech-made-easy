# 🌸 Iris Flower Predictor

Hi, I'm Richel, and this is a tiny machine learning web app you can run on your own laptop.

You move four sliders to describe a flower, click a button, and a model guesses which species of iris it is. That's it. No web-dev background needed, I promise. If you've never deployed or trained anything before, you're exactly who I built this for.

This is part of my "Tech Made Easy" series, where I explain machine learning as someone who is still learning it too.

**🌐 See it live:** [link coming soon]  (deployed free on Streamlit Community Cloud)

## What's inside

- **scikit-learn** trains the model (a Random Forest) on the classic iris flower dataset that ships right inside the library.
- **Streamlit** turns a plain Python script into a real web page with sliders and buttons.
- **pandas** helps us look at the data in a friendly table.

## What you need

- Python 3.9 or newer installed on your computer.
- A few minutes. That's honestly it.

## How to run it

First, open a terminal in this folder. Then create a little sandbox for the project's packages so they don't clash with anything else on your machine:

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

Install the three packages we need:

```bash
pip install -r requirements.txt
```

Now run the app. This is the important part: use `streamlit run`, not `python`. If you run it with plain `python`, Streamlit will politely tell you you're doing it wrong.

```bash
streamlit run app.py
```

Your browser should pop open with the app. If it doesn't, the terminal prints a local link (something like `http://localhost:8501`). Click it, and you're in.

## The files

- `app.py` is the web app itself.
- `train.py` is a standalone script that trains the model and prints its accuracy, if you want to see the learning happen in the terminal.
- `explore.py` is a quick peek at the data before any modeling.
- `requirements.txt` holds the three packages, nothing extra.
- `.streamlit/config.toml` gives the app my brand colors (the Midnight & Sky palette).

## Deploy your own copy, free

Once the app runs on your laptop, you can put it on the real internet for free, no server and no web-dev background required. Here's the short version.

1. Push this project to your own GitHub repository (public is easiest).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app**, pick your repository and the `main` branch.
4. Set the **Main file path** to `01-ml-web-app/app.py`. This is the step people forget when their app lives in a subfolder like this one.
5. Click **Deploy** and wait a couple of minutes while it installs the packages from `requirements.txt`.

That's it. You get a shareable link anyone can open. The full walkthrough is in the Medium post linked below.

## A note on secrets

This little app doesn't need any API keys. But as a good habit for future projects: never commit secrets to git. Keep them in a `.env` file (already ignored here) and load them from environment variables.

## 📖 Read the full walkthrough on Medium: https://medium.com/@richelattafuah/i-built-an-ml-web-app-with-zero-web-skills-63e4f87be17a

---

Richel makes tech easy 💕
