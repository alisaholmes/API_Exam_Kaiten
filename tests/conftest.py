import os
from dotenv import load_dotenv
import pytest



@pytest.fixture(autouse=True, scope='session')
def base_url():
    load_dotenv()
    base_url = os.getenv('URL')
    return f'https://{base_url}.kaiten.ru/'






