# Base class
class Phone:
    def __init__(self, brand, model):
        self._brand = brand         # Encapsulated functionality.
        self._model = model

    def get_info(self):
        return f"{self._brand} {self._model}"

    def power_on(self):
        return f"{self.get_info()} is now powered on."

# Subclass added with functionality.
class Smartphone(Phone):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage          # in GB    
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)
        return f"{app_name} has been installed on your {self.get_info()}."

    def get_storage_info(self):
        return f"{self.storage}GB total storage."

    def list_apps(self):
        return f"Installed apps: {', '.join(self.apps)}" if self.apps else "No apps installed."

# Another subclass to demonstrate polymorphism
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, os, storage, cooling_system):
        super().__init__(brand, model, os, storage)
        self.cooling_system = cooling_system

    # Polymorphic method override
    def install_app(self, app_name):
        if app_name.lower() in ["call of duty", "game of thrones", "genshin impact"]:
            return f"{app_name} installed with high-performance mode enabled."
        return super().install_app(app_name)

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Gaming Edition with {self.cooling_system} cooling"

# Example usage:
phone1 = Smartphone("Android", "Samsung Galaxy S25", "iOS", 12)
print(phone1.power_on())
print(phone1.install_app("Jumia"))
print(phone1.list_apps())

phone2 = GamingSmartphone("Asus", "iphone 14 Pro", "Android", 256, "liquid")
print(phone2.power_on())
print(phone2.install_app("Game of Thrones"))
print(phone2.list_apps())
print(phone2.get_info())
