# Human Benchmark Bot 🤖

Because clicking a mouse manually is way too much work.

I decided that instead of spending 5 minutes actually doing these tests, I'd rather spend 30+ minutes writing a script that does them for me with superhuman accuracy. Is it cheating? Maybe. Is it satisfying to see a 10ms reaction time? Absolutely.

## Current Progress

* [x] **Reaction Time**: Consistently hitting speeds faster than any human alive.
* [ ] **Sequence Memory**: (WIP) Let the script remember the squares so I don't have to.
* [ ] **Aim Trainer**: Automating the clicking of targets.
* [ ] **Verbal Memory**: Keeping track of words in a dictionary object.
* [ ] **Number Memory**: Because numbers freak me out.

## How it Works

The scripts use **Selenium** to interact with the browser. It monitors the DOM for specific class changes (like the screen turning green) and triggers a click event immediately.

I'm aiming for "efficient-ish" code—it's not production-grade, it's "it works on my machine" grade.

## Getting Started

1. **Clone the repo:**
```bash
git clone https://github.com/UdontKnowMe-git/human-benchmark-bot.git

```


2. **Install dependencies:**
```bash
pip install selenium

```


3. **Driver:** Make sure you have the correct `chromedriver` installed for your version of Chrome (or use `webdriver-manager`).
4. **Run a script:**
```bash
python reaction_speed.py

```



## Disclaimer

Don't use this to flex on your friends and pretend you're a god. Or do. I'm a README, not a cop.
