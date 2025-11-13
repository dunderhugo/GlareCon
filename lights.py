from dataclasses import dataclass
from pywizlight import wizlight, PilotBuilder, discovery

@dataclass
class Lights:
  user_name: str
  group: str

  wiz_device: wizlight