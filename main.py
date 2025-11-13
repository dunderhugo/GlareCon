from flask import Flask
from pywizlight import wizlight, PilotBuilder, discovery
import json, pprint
from lights import Lights

app = Flask(__name__)

def get_json_data():
  with open("bulbs.json", "r") as f:
    data = json.load(f)
  return data

def compare_ips(stored_data, discovered_data):
  stored_ips = set(stored_data.keys())
  discovered_ips = set(discovered_data.keys())
  
  new_ips = discovered_ips - stored_ips
  missing_ips = stored_ips - discovered_ips
  
  return new_ips, missing_ips


@app.route('/get-state')
async def get_state():
  return "NYI"

@app.route('/change-light-name')
async def change_light_name():
  return "NYI"

@app.route('/add-light-to-group')
async def add_light_to_group():
  return "NYI"

@app.route('/')
async def index():
  light = wizlight("192.168.1.232")
  await light.updateState()
  is_on = light.state.get_state()
  print(f"Is the light on? {is_on}")


  bulb_type = await light.get_bulbtype()
  pprint.pprint(bulb_type)
  return "Hello, World!"

@app.route('/detect-devices')
async def detect_devices():
  devices_to_store = {}
  
  devices = await discovery.discover_lights(broadcast_space="192.168.1.255")
  
  for device in devices:
    device_info = {
      "given_name" : "",
      "group": [],
      "room": "",
    }
    devices_to_store[device.ip] = device_info
    

  with open("bulbs.json", "w") as f:
    json.dump(devices_to_store, f, indent=2)
  
  return f"Discovered and stored {len(devices_to_store)} devices."

if __name__ == '__main__':
  app.run(debug=True, port=8080)
