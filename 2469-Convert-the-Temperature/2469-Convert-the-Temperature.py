class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        return [round(celsius + 273.15, 5), round((celsius * (9 / 5)) + 32, 5)]
