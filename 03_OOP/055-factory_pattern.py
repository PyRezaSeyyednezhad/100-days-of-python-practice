from abc import ABC, abstractmethod


# Factory Pattern Example: AI Models
# About this Example: This example demonstrates the Factory Pattern by creating a factory for different AI models. The `AIModelFactory` class is responsible for instantiating the appropriate AI model based on user input. Each AI model class implements the `AIModel` interface, which defines a method to describe the model. This design allows for easy extension by simply adding new AI model classes and updating the factory without modifying existing code.
class AIModel(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

class ChatGPTModel(AIModel):
    def describe(self) -> str:
        return "ChatGPT: A powerful language model for natural language processing tasks."


class DalleModel(AIModel):
    def describe(self) -> str:
        return "DALL·E: An AI model that generates images from textual descriptions."


class GeminiModel(AIModel):
    def describe(self) -> str:
        return "Gemini: An AI model designed for advanced reasoning and problem-solving tasks."

class AIModelFactory:
    @staticmethod
    def create(model_type: str) -> AIModel:
        model_type = model_type.lower()

        if model_type == "chatgpt":
            return ChatGPTModel()
        elif model_type == "dall_e":
            return DalleModel()
        elif model_type == "gemini":
            return GeminiModel()
        else:
            raise ValueError(f"Unknown model type: {model_type}")

def ui():
    model_type = input("Enter AI model type (ChatGPT/DALL_E/Gemini): ")
    model = AIModelFactory.create(model_type)
    print(model.describe())


# if __name__ == "__main__":
#     ui()



# Factory Pattern Example: Cars
# About this Example: This example illustrates the Factory Pattern by creating a factory for different car types. The `CarFactory` class is responsible for creating instances of specific car classes based on user input. Each car class implements the `Car` interface, which defines methods to retrieve the brand and color of the car, as well as a method to describe the car. This design promotes flexibility and scalability, allowing for easy addition of new car types without modifying existing code.

class Car(ABC):
    def __init__(self, brand: str, color: str):
        self._brand = brand
        self._color = color
    
    @abstractmethod
    def brand(self) -> str:
        pass
    
    @abstractmethod
    def color(self) -> str:
        pass
    
    @abstractmethod
    def describe(self) -> str:
        pass
    


class ChevroletCar(Car):
    def brand(self) -> str:
        return self._brand
    
    def color(self) -> str:
        return self._color
    
    def describe(self):
        return f"Chevrolet Car - Brand: {self.brand()}, Color: {self.color()}"


class DodgeCar(Car):
    def brand(self) -> str:
        return self._brand
    
    def color(self) -> str:
        return self._color
    
    def describe(self):
        return f"Dodge Car - Brand: {self.brand()}, Color: {self.color()}"


class FordCar(Car):
    def brand(self) -> str:
        return self._brand
    
    def color(self) -> str:
        return self._color
    
    def describe(self):
        return f"Ford Car - Brand: {self.brand()}, Color: {self.color()}"
    


class CarFactory:
    @staticmethod
    def create(car_type: str, brand: str, color: str) -> Car:
        car_type = car_type.lower()

        if car_type == "chevrolet":
            return ChevroletCar(brand, color)
        elif car_type == "dodge":
            return DodgeCar(brand, color)
        elif car_type == "ford":
            return FordCar(brand, color)
        else:
            raise ValueError(f"Unknown car type: {car_type}")


def car_ui():
    car_type = input("Enter car type (Chevrolet/Dodge/Ford): ")
    brand = input("Enter car brand: ")
    color = input("Enter car color: ")
    
    car = CarFactory.create(car_type, brand, color)
    print(car.describe())



# if __name__ == "__main__":
#     car_ui()