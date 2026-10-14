"""Manage smart-home devices and their power usage."""

import json
import os
import subprocess
from pathlib import Path

HUB_HOST = os.getenv("SMART_HOME_HUB_HOST", "127.0.0.1")
HUB_PORT = 8080
POWER_USAGE = {"light": 10, "fan": 60, "thermostat": 1500, "tv": 120}
devices = {}


def add_device(device_name, kind, room="Living Room", settings=None):
    """Add a device to the smart-home system."""
    if settings is None:
        settings = {}

    devices[device_name] = {
        "kind": kind,
        "room": room,
        "on": False,
        "settings": settings.copy(),
    }


def toggle_device(device_name):
    """Toggle a device's power state."""
    device = devices.get(device_name)
    if device is None:
        print("Device not found:", device_name)
        return None

    device["on"] = not device["on"]
    return device["on"]


def set_temperature(device_name, value):
    """Set a thermostat temperature between 16 and 30 degrees."""
    device = devices.get(device_name)
    if device is None:
        print("Device not found:", device_name)
        return False

    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False

    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room):
    """Return the names of devices located in the given room."""
    return [
        name for name, info in devices.items()
        if info["room"] == room
    ]


def power_usage():
    """Return total power usage, in watts, for switched-on devices."""
    return sum(
        POWER_USAGE.get(info["kind"], 0)
        for info in devices.values()
        if info["on"]
    )


def save_state(file_name="home_state.json"):
    """Save the current device state to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as state_file:
        json.dump(devices, state_file, indent=2)


def hub_address():
    """Return the configured hub host and port."""
    return f"{HUB_HOST}:{HUB_PORT}"


def run_scene(scene_script):
    """Run a scene script after validating its location.

    Scene scripts are expected to be directly inside the local 'scenes'
    directory. Shell interpretation is disabled to avoid shell injection.
    """
    scenes_dir = Path(__file__).resolve().parent / "scenes"
    requested_script = (scenes_dir / scene_script).resolve()

    if requested_script.parent != scenes_dir.resolve():
        raise ValueError(
            "Scene script must be directly inside the scenes directory."
        )
    if not requested_script.is_file():
        raise FileNotFoundError(
            f"Scene script not found: {requested_script.name}"
        )

    subprocess.run(
        ["bash", str(requested_script)],
        check=True,
        shell=False,
    )


def main():
    """Run a short demonstration of the smart-home manager."""
    devices.clear()
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")

    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")
    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)

    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address())
    print("Light settings:", devices["Ceiling Light"]["settings"])
    print(
        "Devices on:",
        [name for name, info in devices.items() if info["on"]],
    )
    save_state()


if __name__ == "__main__":
    main()
