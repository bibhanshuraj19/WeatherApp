import os
import sys
from main import app

if __name__ == '__main__':
    # Check if API key is configured
    from main import load_config
    
    api_key = load_config()
    if not api_key:
        print("❌ API key not found!")
        print("\n📝 To fix this, either:")
        print("1. Set environment variable: export OPENWEATHER_API_KEY='your_key_here'")
        print("2. Or update config.ini with your API key")
        print("\n🔑 Get a free API key from: https://openweathermap.org/api")
        sys.exit(1)
    
    print("🌤️  Starting Weather App...")
    print("📡 API key configured ✓")
    print("🌐 Server will be available at: http://localhost:8080")
    print("🔄 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print("\n👋 Weather App stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

