import os
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

command_prefixes = ['.','!','/']

a = 0

ghoul_table_command = 'ghoul-c'

end_message = 'l l let me die' # Сообщение после конца цикла, если не нужно - оставляем пустым
messages_per_second = 7 # Для ghoul_spam
sleep_time_ghoul = 0.1 