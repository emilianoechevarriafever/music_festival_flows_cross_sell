#!/usr/bin/env python3
"""
Screenshot script for Fabrik Madrid tables page
Takes screenshots and analyzes the page structure
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def main():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--headless')  # Run in background
    
    print("Starting browser...")
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        url = 'https://emilianoechevarriafever.github.io/fabrik-madrid-tables/'
        print(f"Navigating to {url}...")
        driver.get(url)
        
        # Wait for page to load
        time.sleep(3)
        
        # Take initial screenshot
        print("Taking initial screenshot...")
        driver.save_screenshot('fabrik-screenshot-1-initial.png')
        
        # Analyze page state
        print("Analyzing page...")
        
        # Check selected tab
        selected_tab = "None"
        try:
            tabs = driver.find_elements(By.CSS_SELECTOR, '.nav-link, [role="tab"]')
            for tab in tabs:
                if 'active' in tab.get_attribute('class'):
                    selected_tab = tab.text.strip()
                    break
        except Exception as e:
            print(f"Error finding tabs: {e}")
        
        # Check for blue zones - look for SVG elements
        blue_zones = []
        try:
            svg_elements = driver.find_elements(By.CSS_SELECTOR, 'svg path, svg g[id], svg rect, svg polygon')
            for el in svg_elements:
                el_id = el.get_attribute('id') or ''
                el_class = el.get_attribute('class') or ''
                fill = el.value_of_css_property('fill')
                stroke = el.value_of_css_property('stroke')
                
                # Check if blue-ish color
                if any(color_check in str(fill).lower() or color_check in str(stroke).lower() 
                       for color_check in ['blue', '#007bff', 'rgb(0, 123, 255)', '007bff']):
                    blue_zones.append({
                        'id': el_id,
                        'class': el_class,
                        'fill': fill,
                        'stroke': stroke
                    })
        except Exception as e:
            print(f"Error finding blue zones: {e}")
        
        # Get ticket items
        ticket_items = []
        try:
            tickets = driver.find_elements(By.CSS_SELECTOR, '.ticket-item, .list-group-item, [class*="ticket"]')
            for ticket in tickets[:5]:  # First 5
                ticket_items.append(ticket.text.strip()[:100])
        except Exception as e:
            print(f"Error finding tickets: {e}")
        
        # Scroll down to ticket selector
        print("Scrolling to ticket selector...")
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        
        print("Taking ticket selector screenshot...")
        driver.save_screenshot('fabrik-screenshot-2-tickets.png')
        
        # Scroll to top
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        # Take full page screenshot
        print("Taking full page screenshot...")
        # Get full page height
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)
        time.sleep(1)
        driver.save_screenshot('fabrik-screenshot-3-fullpage.png')
        
        # Prepare analysis
        analysis = {
            'selected_tab': selected_tab,
            'blue_zones_count': len(blue_zones),
            'blue_zones': blue_zones[:10],  # First 10
            'ticket_items_count': len(ticket_items),
            'ticket_items': ticket_items,
            'page_url': url,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save analysis
        with open('fabrik-analysis.json', 'w') as f:
            json.dump(analysis, f, indent=2)
        
        print("\n=== PAGE ANALYSIS ===")
        print(f"Selected Tab: {selected_tab}")
        print(f"Blue Zones Found: {len(blue_zones)}")
        if blue_zones:
            print("Blue Zones Details:")
            for zone in blue_zones[:5]:
                print(f"  - ID: {zone['id']}, Class: {zone['class']}")
        print(f"Ticket Items Found: {len(ticket_items)}")
        if ticket_items:
            print("Ticket Items:")
            for item in ticket_items:
                print(f"  - {item[:80]}")
        
        print("\nScreenshots saved:")
        print("- fabrik-screenshot-1-initial.png")
        print("- fabrik-screenshot-2-tickets.png")
        print("- fabrik-screenshot-3-fullpage.png")
        print("- fabrik-analysis.json")
        
    finally:
        print("\nClosing browser...")
        driver.quit()

if __name__ == '__main__':
    main()
