# herobot
Telegram bot skeleton for Heroku using Python. This bot is designed to send timed
remainders to one channel.

This project uses pipenv to make deployment to Heroku super simple.


## How to
### 1. Fork this repo
### 2. Set up Heroku
  You can run the bot on a free dyno but this bot is not designed to sleep so keep in mind that it will consume your hours.
  Connect your repo for easy deployment.
  Add config variables to store your bot token and other sensitive data.
### 3. Code your bot
  Remember to use pipenv. It keeps track of your dependencies and Heroku uses it to find the correct packages.
### 4. Test locally
  By setting up a config file locally you can test your bot locally without having to deploy after every change.
### 5. Deploy
  Push to github and Heroku will automatically fetch the changes and restart your bot.
