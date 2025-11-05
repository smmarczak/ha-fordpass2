"""
RCC Diagnostic Script for 2024 Bronco
This will help us see what RCC data is being received from Ford's API
"""

# Add this as a temporary diagnostic sensor to your Home Assistant

# In configuration.yaml, add:
# sensor:
#   - platform: template
#     sensors:
#       fordpass_rcc_diagnostic:
#         friendly_name: "FordPass RCC Diagnostic"
#         value_template: >
#           {% set rcc_data = states.sensor.YOUR_VEHICLE_NAME_metrics.attributes.get('coordinator_data', {}).get('rcc', {}) %}
#           {{ rcc_data | tojson }}

# Instructions:
# 1. Replace YOUR_VEHICLE_NAME with your actual vehicle sensor name
# 2. Add to configuration.yaml
# 3. Restart Home Assistant
# 4. Check the sensor state - it should show the RCC data structure
