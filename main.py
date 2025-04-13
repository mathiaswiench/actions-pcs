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
        # Break down the statement to avoid nested quotes entirely
        if stage_detail.date() < today:
            results = stage_detail.results()
            rider_name = results[0].get('rider_name')
            avg_speed = stage_detail.avg_speed_winner()
            logger.info(f"Winner: {rider_name} with {avg_speed} km/h")
        else:
            continue



if __name__ == "__main__":
    scraper()