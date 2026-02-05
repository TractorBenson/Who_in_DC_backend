import json
import logging
from pathlib import Path
from datetime import datetime, timezone

logger = logging.getLogger("widc")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

DATA_DIR = Path("/app/data")
DATA_FILE = DATA_DIR / "data.json"

def _load_data() -> dict:
    if not DATA_FILE.exists():
        return {"dc": []}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_data(data: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    

def get_people() -> list[dict]:
    people_list = _load_data()["dc"]
    return people_list


def enter_dc(name: str) -> None:
    logger.info("Entering DC: %s", name)

    data = _load_data()
    people_list = data["dc"]
    entered_at = datetime.now(timezone.utc).isoformat()

    for person in people_list:
        if person["name"] == name:
            logger.info("Person %s already in DC", name)
            return
    
    data["dc"].append({
        "name": name,
        "entered_at": entered_at
    })

    _save_data(data)

    logger.info("Person %s added to the list", name)
    

def leave_dc(name: str) -> None:
    logger.info("Leaving DC: %s", name)

    data = _load_data()
    people_list = data["dc"]

    for i, person in enumerate(people_list):
        if person["name"] == name:
            data["dc"].pop(i)
            _save_data(data)
            logger.info("Person %s removed from the list", name)
            return
    else:
        logger.info("Person %s not found in the list", name)
