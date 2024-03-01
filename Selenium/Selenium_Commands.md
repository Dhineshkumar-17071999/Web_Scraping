### Selenium Commands

#### Find elements with Selenium

##### Locate Single Element
1. driver.find_element_by_id('id') - 

2. driver.find_element_by_class_name('class_name')

3. driver.find_element_by_tag_name('tag')

4. driver.find_element_by_xpath('//tagName[@AttributeName = "value"]')

5. driver.find_element_by_css_selector()

6. driver.find_element_by_name()

7. driver.find_element_by_link_text()

##### Locate Multiple Elements
1. driver.find_elements_by_class_name() - > list = [a,b,c,d]

##### Example :

![Alt Text](html_example.png)

##### Commands : 
	1. driver.find_element_by_class_name('main-article')
	
	2. driver.find_element_by_class_name('plot')
	
	3. driver.find_element_by_tag_name('h1')
	
	4. driver.find_element_by_tag_name('p')
