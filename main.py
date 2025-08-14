"""
Enhanced Weather Application
A modern weather app with Flask web interface and improved functionality
"""

import os
import sys
from datetime import datetime, timedelta
from configparser import ConfigParser
from typing import Dict, Optional, List
import requests
from flask import Flask, render_template, request, jsonify
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WeatherAPI:
    """Enhanced Weather API class with better error handling and features"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        
    def get_current_weather(self, city: str) -> Optional[Dict]:
        """Get current weather for a city with enhanced error handling"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Get temperature in Celsius directly
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Parse and format the weather data
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': round(data['main']['temp'], 1),
                'feels_like': round(data['main']['feels_like'], 1),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].title(),
                'main': data['weather'][0]['main'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'wind_direction': data['wind'].get('deg', 0),
                'visibility': data.get('visibility', 0) / 1000,  # Convert to km
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
                'timezone': data['timezone'],
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return weather_data
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout while fetching weather for {city}")
            return None
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.error(f"City '{city}' not found")
            else:
                logger.error(f"HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            return None
        except KeyError as e:
            logger.error(f"Unexpected API response format: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None
    
    def get_weather_forecast(self, city: str, days: int = 5) -> Optional[List[Dict]]:
        """Get weather forecast for specified number of days"""
        try:
            url = f"{self.forecast_url}"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'cnt': days * 8  # 8 forecasts per day (every 3 hours)
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Group forecasts by day
            daily_forecasts = []
            current_date = None
            day_data = []
            
            for item in data['list']:
                forecast_date = datetime.fromtimestamp(item['dt']).date()
                
                if current_date != forecast_date:
                    if day_data:
                        daily_forecasts.append(self._process_daily_forecast(day_data))
                    current_date = forecast_date
                    day_data = []
                
                day_data.append(item)
            
            # Add the last day
            if day_data:
                daily_forecasts.append(self._process_daily_forecast(day_data))
            
            return daily_forecasts[:days]
            
        except Exception as e:
            logger.error(f"Error fetching forecast for {city}: {e}")
            return None
    
    def _process_daily_forecast(self, day_data: List[Dict]) -> Dict:
        """Process a day's worth of forecast data"""
        temps = [item['main']['temp'] for item in day_data]
        
        # Find midday forecast for main description and icon
        midday_forecast = min(day_data, key=lambda x: abs(
            datetime.fromtimestamp(x['dt']).hour - 12
        ))
        
        return {
            'date': datetime.fromtimestamp(day_data[0]['dt']).strftime('%Y-%m-%d'),
            'day_name': datetime.fromtimestamp(day_data[0]['dt']).strftime('%A'),
            'temp_max': round(max(temps), 1),
            'temp_min': round(min(temps), 1),
            'description': midday_forecast['weather'][0]['description'].title(),
            'icon': midday_forecast['weather'][0]['icon'],
            'humidity': midday_forecast['main']['humidity'],
            'wind_speed': midday_forecast['wind']['speed']
        }

# Initialize Flask app
app = Flask(__name__)

# Load configuration
def load_config():
    """Load API key from config file or environment variable"""
    config_file = "config.ini"
    
    # Try environment variable first
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if api_key:
        return api_key
    
    # Fallback to config file
    if os.path.exists(config_file):
        config = ConfigParser()
        config.read(config_file)
        try:
            return config['gfg']['api']
        except KeyError:
            logger.error("API key not found in config file")
            return None
    
    logger.error("No API key found. Please set OPENWEATHER_API_KEY environment variable or create config.ini")
    return None

# Initialize weather API
api_key = load_config()
if not api_key:
    logger.error("Cannot start application without API key")
    sys.exit(1)

weather_api = WeatherAPI(api_key)

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/weather/<city>')
def get_weather(city):
    """API endpoint to get current weather"""
    weather_data = weather_api.get_current_weather(city)
    
    if weather_data:
        return jsonify({
            'success': True,
            'data': weather_data
        })
    else:
        return jsonify({
            'success': False,
            'error': f'Could not find weather data for "{city}". Please check the city name and try again.'
        }), 404

@app.route('/api/forecast/<city>')
def get_forecast(city):
    """API endpoint to get weather forecast"""
    days = request.args.get('days', 5, type=int)
    days = min(max(days, 1), 5)  # Limit between 1-5 days
    
    forecast_data = weather_api.get_weather_forecast(city, days)
    
    if forecast_data:
        return jsonify({
            'success': True,
            'data': forecast_data
        })
    else:
        return jsonify({
            'success': False,
            'error': f'Could not find forecast data for "{city}". Please check the city name and try again.'
        }), 404

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=8080)
