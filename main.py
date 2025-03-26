from pprint import pprint
import logging
import logging.handlers
from procyclingstats import Race, RaceClimbs, Stage
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

def scraper():
    # RACE_URL can be replaced with any valid stage race URL
    RACE_URL = "race/volta-a-catalunya/2025"
    race = Race(f"{RACE_URL}/overview")
    stages = race.stages()
    today = datetime.today().strftime('%Y-%m-%d')
    for stage in stages:
        url = stage.get('stage_url')
        stage_detail = Stage(url)
        if stage_detail.date() == today:
            logger.info(f'Winner: {stage_detail.results()[0].get('rider_name')} with {stage_detail.avg_speed_winner()} km/h')



if __name__ == "__main__":
    scraper()