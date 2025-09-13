import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from openai import OpenAI

local_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
admins = 1239638813

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token='',
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
