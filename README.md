# USPSFreeAdVal

A FOSS Address Validation Script using USPS.com's Address Validation Page. A dirty but free solution to validate addresses with USPS. 

Requirements:
  Python
  Selenium ChromeDriver

To-Do:
  Support CLI Arguments
  Support Input of CSV
  Memory Management - Stop Selenium from Crashing when large amounts of data are thrown.
  
  
How this works:
  This script takes advantage of how USPS's website is programmed. Which is why it could be volatile, as any changes to USPS' website could cause the need for a change. When a      user enters an address into USPS's website, one of two things can happen:
  
  1. USPS finds the address, and a box pops up with Address Information:
  ![image](https://user-images.githubusercontent.com/22941285/136595746-172ea6c6-6a2c-4ca5-9548-95a1c5ae6d98.png)
  
  2. USPS does NOT find an address, and errors:
  ![image](https://user-images.githubusercontent.com/22941285/136595825-8ea3c860-8b88-4a24-8719-d036b2f969d3.png)

  I(as the only developer right now) have taken advantage of this fact, to validate addresses. If the box pops up, address valid! If it doesn't, it obviously isn't a valid address. This may need to be improved in the future.
  
  Using a "wait-and-see" function in Selenium (webdriver.Wait), will throw a TimeoutException when an element is not found in time. I use this to tell the script when an address is invalidated. 
  
  As for typos: Yes. This script does NOT account for typos. As does the USPS. USPS won't send a mail-piece to 123 Mian St even if you meant it for 123 Main St! 

  
