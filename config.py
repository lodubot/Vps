"""
⚙️ VPS Bot Manager - Configuration File
Edit this file with your bot token and admin IDs
"""

# ============ BOT SETTINGS ============
# Get token from @BotFather on Telegram
BOT_TOKEN = "8918061668:AAGPsp1BnQkMG_Rr8Apx6o47RPXfZeo5hEc"

# Admin Telegram User IDs (comma separated)
# Get your ID from @userinfobot
ADMIN_IDS = [8100453801]

# ============ SYSTEM PATHS ============
HOSTED_BOTS_DIR = "/opt/hosted-bots"
LOGS_DIR = "/var/log/bot-manager"

# ============ LIMITS ============
MAX_BOTS = 100           # Maximum bots per user
MAX_ZIP_SIZE_MB = 500    # Max zip file size in MB
START_VIDEO_URL = "https://files.catbox.moe/k099rv.mp4"

# ============ DEPLOYMENT ============
# Auto-start bot after deploy?
AUTO_START_AFTER_DEPLOY = True

# Restart delay in seconds (if bot crashes)
RESTART_DELAY = 5

# Max restarts per hour (prevents infinite loops)
MAX_RESTARTS_PER_HOUR = 10
