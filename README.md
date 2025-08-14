# 🌤️ Modern Weather App

A beautiful, responsive weather application built with Flask and modern web technologies. Get real-time weather information and 5-day forecasts for any city worldwide.

![Weather App Screenshot](https://via.placeholder.com/800x400/667eea/ffffff?text=Modern+Weather+App)

## ✨ Features

- **🌍 Global Weather Data**: Get weather information for any city worldwide
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **🎨 Modern UI**: Beautiful glassmorphism design with smooth animations
- **📊 Detailed Information**: Temperature, humidity, wind speed, pressure, visibility
- **📅 5-Day Forecast**: Extended weather predictions with daily highs and lows
- **⚡ Real-time Updates**: Live weather data from OpenWeatherMap API
- **🔍 Smart Search**: Auto-suggestions and error handling for city searches
- **🌙 Weather Icons**: Dynamic weather icons that change based on conditions

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key ([Get it free here](https://openweathermap.org/api))

### Installation

1. **Clone or download this repository**
   ```bash
   cd Weather
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Configure your API key**
   
   **Option A: Using environment variable (recommended)**
   ```bash
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```
   
   **Option B: Using config file**
   - Keep your existing `config.ini` file with your API key

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Open your browser** and go to `http://localhost:8080`

## 🛠️ Technical Improvements

### Backend Enhancements
- **🏗️ Modern Architecture**: Converted from Tkinter to Flask web application
- **📦 Class-based Design**: Organized code with proper OOP structure
- **🛡️ Error Handling**: Comprehensive error handling with user-friendly messages
- **📊 Enhanced Data**: Additional weather metrics (feels like, wind direction, visibility)
- **⏱️ Timeout Protection**: Network request timeouts to prevent hanging
- **📈 Forecast API**: 5-day weather forecast functionality
- **🔧 Better Configuration**: Support for environment variables and config files

### Frontend Improvements
- **🎨 Modern Design**: Beautiful glassmorphism UI with gradient backgrounds
- **📱 Responsive Layout**: Mobile-first design that works on all screen sizes
- **⚡ Smooth Animations**: CSS transitions and animations for better UX
- **🔍 Smart Search**: Real-time search with loading states and error handling
- **📊 Rich Weather Display**: Visual weather icons and comprehensive data presentation
- **📅 Interactive Forecast**: Expandable 5-day forecast with hover effects
- **♿ Accessibility**: Proper contrast ratios and semantic HTML

## 📂 Project Structure

```
Weather/
├── main.py              # Main Flask application
├── run.py               # Application launcher script
├── config.ini           # API key configuration
├── requirement.txt      # Python dependencies
├── .env.example         # Environment variables example
├── templates/
│   └── index.html       # Main web interface
└── README.md           # This file
```

## 🔧 Configuration

### API Key Setup

The application supports two ways to configure your OpenWeatherMap API key:

1. **Environment Variable** (recommended for security)
   ```bash
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```

2. **Config File** (config.ini)
   ```ini
   [gfg]
   api=your_api_key_here
   ```

### Environment Variables

You can also set these optional environment variables:

```bash
export FLASK_ENV=development    # or production
export FLASK_DEBUG=True         # Enable debug mode
```

## 🌐 API Endpoints

The application provides REST API endpoints:

- `GET /` - Main web interface
- `GET /api/weather/<city>` - Get current weather for a city
- `GET /api/forecast/<city>?days=5` - Get weather forecast (1-5 days)

### Example API Response

```json
{
  "success": true,
  "data": {
    "city": "London",
    "country": "GB",
    "temperature": 15.2,
    "feels_like": 14.1,
    "humidity": 73,
    "pressure": 1013,
    "description": "Partly Cloudy",
    "wind_speed": 3.6,
    "visibility": 10.0,
    "sunrise": "07:42",
    "sunset": "18:31"
  }
}
```

## 🎨 Customization

### Styling
The application uses modern CSS with:
- CSS Grid and Flexbox for layouts
- CSS Custom Properties for theming
- Glassmorphism effects with backdrop filters
- Smooth transitions and hover effects

### Adding Features
You can easily extend the application by:
- Adding new weather metrics to the `WeatherAPI` class
- Creating additional API endpoints in `main.py`
- Enhancing the frontend with new components
- Adding data persistence with a database

## 🐛 Troubleshooting

### Common Issues

1. **"Cannot start application without API key"**
   - Make sure you've set your API key in config.ini or as an environment variable
   - Verify your API key is valid at OpenWeatherMap

2. **"City not found" errors**
   - Check the spelling of the city name
   - Try using the format "City, Country" (e.g., "London, UK")

3. **Connection errors**
   - Check your internet connection
   - Verify OpenWeatherMap API is accessible

### Debug Mode

Run with debug information:
```bash
FLASK_DEBUG=True python run.py
```

## 📊 Performance

The application is optimized for performance:
- **⚡ Fast Loading**: Optimized CSS and JavaScript
- **🌐 CDN Resources**: External libraries loaded from CDN
- **📱 Mobile Optimized**: Responsive images and layouts
- **🔄 Caching**: Browser caching for static resources

## 🔒 Security

Security features implemented:
- **🔐 API Key Protection**: Environment variable support
- **🛡️ Input Validation**: Sanitized user inputs
- **⏱️ Request Timeouts**: Prevents hanging requests
- **📝 Error Handling**: No sensitive data in error messages

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Font Awesome](https://fontawesome.com/) for the beautiful icons
- [Google Fonts](https://fonts.google.com/) for the Inter font family

---

**Made with ❤️ by [Your Name]**

*Enjoy your beautiful new weather app!* 🌈

# WeatherApp
