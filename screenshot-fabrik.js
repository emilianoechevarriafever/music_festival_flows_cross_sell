const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: {
      width: 1920,
      height: 1080
    }
  });
  
  const page = await browser.newPage();
  
  console.log('Navigating to page...');
  await page.goto('https://emilianoechevarriafever.github.io/fabrik-madrid-tables/', {
    waitUntil: 'networkidle2',
    timeout: 30000
  });
  
  // Wait a bit for any animations or lazy loading
  await page.waitForTimeout(2000);
  
  console.log('Taking initial screenshot...');
  await page.screenshot({
    path: 'fabrik-screenshot-1-full.png',
    fullPage: false
  });
  
  console.log('Taking full page screenshot...');
  await page.screenshot({
    path: 'fabrik-screenshot-2-fullpage.png',
    fullPage: true
  });
  
  // Scroll down to see ticket selector
  console.log('Scrolling to ticket selector...');
  await page.evaluate(() => {
    window.scrollBy(0, 600);
  });
  
  await page.waitForTimeout(1000);
  
  console.log('Taking ticket selector screenshot...');
  await page.screenshot({
    path: 'fabrik-screenshot-3-ticket-selector.png',
    fullPage: false
  });
  
  // Get information about the page state
  const pageInfo = await page.evaluate(() => {
    // Check which tab is selected
    const tabs = document.querySelectorAll('.nav-link, [role="tab"]');
    let selectedTab = 'None';
    tabs.forEach(tab => {
      if (tab.classList.contains('active')) {
        selectedTab = tab.textContent.trim();
      }
    });
    
    // Check for blue zones on the map
    const blueElements = [];
    const svgPaths = document.querySelectorAll('svg path, svg g, svg rect, svg polygon');
    svgPaths.forEach((el, idx) => {
      const fill = window.getComputedStyle(el).fill;
      const stroke = window.getComputedStyle(el).stroke;
      if (fill.includes('0, 0, 255') || fill.includes('rgb(0, 123, 255)') || 
          stroke.includes('0, 0, 255') || stroke.includes('rgb(0, 123, 255)') ||
          fill.includes('#007bff') || fill.includes('blue') || stroke.includes('blue')) {
        blueElements.push({
          id: el.id,
          class: el.className.baseVal || el.className,
          fill: fill,
          stroke: stroke
        });
      }
    });
    
    // Get ticket items
    const ticketItems = [];
    const tickets = document.querySelectorAll('.ticket-item, .list-group-item, [class*="ticket"]');
    tickets.forEach(ticket => {
      ticketItems.push(ticket.textContent.trim().substring(0, 100));
    });
    
    return {
      selectedTab,
      blueElementsCount: blueElements.length,
      blueElements: blueElements.slice(0, 10), // First 10
      ticketItemsCount: ticketItems.length,
      ticketItems: ticketItems.slice(0, 5) // First 5
    };
  });
  
  console.log('\n=== PAGE ANALYSIS ===');
  console.log('Selected Tab:', pageInfo.selectedTab);
  console.log('Blue Elements Found:', pageInfo.blueElementsCount);
  console.log('Blue Elements Details:', JSON.stringify(pageInfo.blueElements, null, 2));
  console.log('Ticket Items Found:', pageInfo.ticketItemsCount);
  console.log('Ticket Items:', pageInfo.ticketItems);
  
  fs.writeFileSync('fabrik-analysis.json', JSON.stringify(pageInfo, null, 2));
  
  console.log('\nScreenshots saved:');
  console.log('- fabrik-screenshot-1-full.png');
  console.log('- fabrik-screenshot-2-fullpage.png');
  console.log('- fabrik-screenshot-3-ticket-selector.png');
  console.log('- fabrik-analysis.json');
  
  await browser.close();
})();
