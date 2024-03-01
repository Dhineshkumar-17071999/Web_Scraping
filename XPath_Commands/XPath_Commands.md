### XPath Commands

#### XPath stands for XML Path Language

XPath is a query language for selecting notes from an XML document, but we can also use it to select elements from HTML pages.

Another way to select elements from website is using CSS selectors.

CSS and XPath have some similarities in their syntax.

##### Commands
	1. //tagName - We can select an element by using the double slash and then we write that element name.
	
	2. //tagName[1] - We can select an element based on its position by using the square brackets.
	
	3. //tagName[@AttributeName="Value"]
	
	4. //tagName[contains(@AttributeName, "Value")]
	
	5. //tagName[(expression 1) and (expression 2)]
	
	6. //tagName[(expression 1) or (expression 2)]
	
##### Examples
	1. //h1
	2. //h1/text()
	3. //p
	4. //div
	5. //div/text()
	6. //p[1]
	7. //p[2]
	8. //div[@class = "full-script"]
	9. //div[@class = "full-script"]/text()
	10. //p[(@class = "plot") and (@class = "plot1")]
	11. //p[(@class = "plot") or (@class = "plot1")]
	12. //p[contains(@class, "plot")]
	13. //div[contains(@class, "full-script")]
	
	
##### Special Characters
	1. / : Select <u>the children</u> from the node set on the left side of this character.
	
	2. // : Specifies that the matching node set should be located ***at any level*** within the document.
	
	3. .(dot) : Specifies the current context should be used (refers to **present node**).
	
	4. ..(double dot) : Refers to a **parent** node.
	
	5. * : A wildcard character that **selects all elements** or attributes regardless of names.
	
	6. ./* : Select all the chidren nodes considering the current context.
	
	7. @ : Select an attribute.
	
	8. () : Grouping an XPath expression.
	
	9. [n] : Indicates that a node with index "n" should be selected
	
##### Examples
	1. //h1/.
	2. //h1/..
	3. //h1/*
