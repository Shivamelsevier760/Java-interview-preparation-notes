# Semarchy Certification Training notes

**Presentation: Overview of the Intelligent Data Hub**

[Slides_  Intelligent Data Hub Overview.pdf](semarchy-certification-training-notes/slides-intelligent-data-hub-overview.pdf)

![Untitled](semarchy-certification-training-notes/untitled.png)

[Semarchy xDM Overview.pdf](semarchy-certification-training-notes/semarchy-xdm-overview.pdf)

[Discovering Datasources.pdf](semarchy-certification-training-notes/discovering-datasources.pdf)

![Untitled](semarchy-certification-training-notes/untitled-1.png)

![Untitled](semarchy-certification-training-notes/untitled-2.png)

![Untitled](semarchy-certification-training-notes/untitled-3.png)

![Untitled](semarchy-certification-training-notes/untitled-4.png)

![Untitled](semarchy-certification-training-notes/untitled-5.png)

![Untitled](semarchy-certification-training-notes/untitled-6.png)

![Untitled](semarchy-certification-training-notes/untitled-7.png)

[DataType.pdf](semarchy-certification-training-notes/datatype.pdf)

1) To create a new model, navigate to the Semarchy main page and select the Application Builder.

![Untitled](semarchy-certification-training-notes/untitled-8.png)

Click on the "New Model" option:

![Untitled](semarchy-certification-training-notes/untitled-9.png)

![Untitled](semarchy-certification-training-notes/untitled-10.png)

Here, the name automatically generates the label.

![Untitled](semarchy-certification-training-notes/untitled-11.png)

In the image above, you'll see the default view immediately after creating a new model. At this point, nothing else has been created; we've merely established our model. The next step is to create the entity.

So, here we are going to create our first complex type.

Complex types are collections of other attribute types.

An address, like a name, has multiple attributes such as street name, town, city, country, and zip code.

![Untitled](semarchy-certification-training-notes/untitled-12.png)

Afterwards, click on the 'Create' option.

![Untitled](semarchy-certification-training-notes/untitled-13.png)

![Untitled](semarchy-certification-training-notes/untitled-14.png)

![Untitled](semarchy-certification-training-notes/untitled-15.png)

In the above screen, we can add our definition attributes:

![Untitled](semarchy-certification-training-notes/untitled-16.png)

![Untitled](semarchy-certification-training-notes/untitled-17.png)

![Untitled](semarchy-certification-training-notes/untitled-18.png)

![Untitled](semarchy-certification-training-notes/untitled-19.png)

![Untitled](semarchy-certification-training-notes/untitled-20.png)

Similarly, we will add another.

![Untitled](semarchy-certification-training-notes/untitled-21.png)

![Untitled](semarchy-certification-training-notes/untitled-22.png)

Let's now create a list of values.

![Untitled](semarchy-certification-training-notes/untitled-23.png)

Lists of values are used for lookups or to offer a selection of options in a dropdown menu within a form or data entry interface. They are commonly used to maintain consistency in data entry, especially for fields with a limited number of valid options.

List of values are crucial for maintaining data quality and standard data preferences. By restricting inputs to a specific set of values, they help avoid errors and inconsistencies in the data, which can be critical for analysis and reporting. They also make it easier to standardize data across different systems or platforms, which can be important for data integration and interoperability. that rarely changes overtime

![Untitled](semarchy-certification-training-notes/untitled-24.png)

![Untitled](semarchy-certification-training-notes/untitled-25.png)

![Untitled](semarchy-certification-training-notes/untitled-26.png)

In the country LOV's, we can either add the value or import the values.

![Untitled](semarchy-certification-training-notes/untitled-27.png)

Assignment Lab1

# **Lab 1 - Create Model and Data Types**

Lab 1
Task 1: Create the new model and the diagram
Create a new Model named CustomerTraining.
Hint: In the Application builder, click New model...

Task 2: Create a list of values
Some of the data could be static and users should only be allowed to enter certain values. To prevent users from editing these values or just entering any value, create the following List of Values (LOV):

Create a List of Value for country codes, named CountryCodeLOV, set the length to 2
Hint: The length of the attribute must match the length of the codes, in that case 2 characters country codes (FR, GB, US, etc).
Add the following values and then save the LOV:
FR – France
GB – Great Britain
US – United States
IT – Italy
Import more code from the xDM_training-countries-lov.xlsx  file.
Note: It is important you use exactly the same Codes as listed above otherwise when you load data, later on, you may get errors if your codes cannot be found.

Task 3: Create a user-defined type
Before creating any entity we want to define some custom types that will be used by our entities.

Create a user-defined type named PostalCode.
Data Type: String
Length: 16

Task 4: Create a complex type
Create a complex type named AddressType with the following definition attributes:
StreetName – String(80)
City - String(80)
PostalCode - use the Postal Code user-defined type you created previously.
Country - use the CountryCodeLOV list of values you created earlier.
Create a Display Name for this complex type that displays all attributes with a comma separator.

Solution :

![Untitled](semarchy-certification-training-notes/untitled-28.png)

![Untitled](semarchy-certification-training-notes/untitled-29.png)

[xDM_training-countries-lov.xlsx](semarchy-certification-training-notes/xdm-training-countries-lov.xlsx)

![Untitled](semarchy-certification-training-notes/untitled-30.png)

![Untitled](semarchy-certification-training-notes/untitled-31.png)

![Untitled](semarchy-certification-training-notes/untitled-32.png)

![Untitled](semarchy-certification-training-notes/untitled-33.png)

![Untitled](semarchy-certification-training-notes/untitled-34.png)

![Untitled](semarchy-certification-training-notes/untitled-35.png)

![Untitled](semarchy-certification-training-notes/untitled-36.png)

[](https://lh3.googleusercontent.com/a/AAcHTtdaNTKFzH5Z_50Cc1mEyCVdc99yLcWcK8keVqAo=s96-c)

Semarchy Doubts:

1. Workflows
2. Database views - Are these stored in the RDS or in a buffer? Is the location the repository or data location?
3. Retention policy
4. Matching
5. Duplicates
6. enricher cache
7. diagrams - data model

![Untitled](semarchy-certification-training-notes/untitled-37.png)

![Untitled](semarchy-certification-training-notes/untitled-38.png)

![Untitled](semarchy-certification-training-notes/untitled-39.png)

![Untitled](semarchy-certification-training-notes/untitled-40.png)

![Untitled](semarchy-certification-training-notes/untitled-41.png)

frequent doubts :

How to create "Display name"?

![Untitled](semarchy-certification-training-notes/untitled-42.png)

![Untitled](semarchy-certification-training-notes/untitled-43.png)

How could I associate the Country and Postal Code with the Address Type field

![Untitled](semarchy-certification-training-notes/untitled-44.png)

![Untitled](semarchy-certification-training-notes/untitled-45.png)

I created complex Type but not sure how to establish relationship between already created list of values and complex type such as PostalCode and CountryCode

Q1. For "Create a complex type", Do we have create PostalCode and Country attribute again, or is there any way we can fetch it from user defined type.

Q2. Where is the option to create Display Name?

1. After you have created the Complex Type called

*AddressType* Set the **Name** to *BillingAddress* and select the **Type** *AddressType*

![Untitled](semarchy-certification-training-notes/untitled-46.png)

![Untitled](semarchy-certification-training-notes/untitled-47.png)

Your **Complex Type** *AddressType* should look something like this:

![Untitled](semarchy-certification-training-notes/untitled-48.png)

**Presentation: Entity Types (EN)**

![Untitled](semarchy-certification-training-notes/untitled-49.png)

Entity Creation :

there are three ways that we can do that

![Untitled](semarchy-certification-training-notes/untitled-50.png)

![Untitled](semarchy-certification-training-notes/untitled-51.png)

we can create entity via diagrama as well as an add diagram

![Untitled](semarchy-certification-training-notes/untitled-52.png)

![Untitled](semarchy-certification-training-notes/untitled-53.png)

![Untitled](semarchy-certification-training-notes/untitled-54.png)

![Untitled](semarchy-certification-training-notes/untitled-55.png)

![Untitled](semarchy-certification-training-notes/untitled-56.png)

![Untitled](semarchy-certification-training-notes/untitled-57.png)

![Untitled](semarchy-certification-training-notes/untitled-58.png)

![Untitled](semarchy-certification-training-notes/untitled-59.png)

![Untitled](semarchy-certification-training-notes/untitled-60.png)

![Untitled](semarchy-certification-training-notes/untitled-61.png)

![Untitled](semarchy-certification-training-notes/untitled-62.png)

![Untitled](semarchy-certification-training-notes/untitled-63.png)

![Untitled](semarchy-certification-training-notes/untitled-64.png)

![Untitled](semarchy-certification-training-notes/untitled-65.png)

![Untitled](semarchy-certification-training-notes/untitled-66.png)

![Untitled](semarchy-certification-training-notes/untitled-67.png)

![Untitled](semarchy-certification-training-notes/untitled-68.png)

![Untitled](semarchy-certification-training-notes/untitled-69.png)

[Entities-compressed.pdf](semarchy-certification-training-notes/entities-compressed.pdf)

![Untitled](semarchy-certification-training-notes/untitled-70.png)

XDM_DEV_EN_045_Modeling Solution

In this module you will find solutions to the Hands On Labs for

Lab 1 - Create Model, LOV, User Defined Type and Complex Type
Lab 2 - Create Entity, Diagram and Add Reference

**Lab 1 - Create Model, LOV, User Defined Type and Complex Type - Solution**

![Untitled](semarchy-certification-training-notes/untitled-71.png)

![Untitled](semarchy-certification-training-notes/untitled-72.png)

![Untitled](semarchy-certification-training-notes/untitled-73.png)

![Untitled](semarchy-certification-training-notes/untitled-74.png)

![Untitled](semarchy-certification-training-notes/untitled-75.png)

![Untitled](semarchy-certification-training-notes/untitled-76.png)

![Untitled](semarchy-certification-training-notes/untitled-77.png)

![Untitled](semarchy-certification-training-notes/untitled-78.png)

![Untitled](semarchy-certification-training-notes/untitled-79.png)

![Untitled](semarchy-certification-training-notes/untitled-80.png)

![Untitled](semarchy-certification-training-notes/untitled-81.png)

![Untitled](semarchy-certification-training-notes/untitled-82.png)

![Untitled](semarchy-certification-training-notes/untitled-83.png)

![Untitled](semarchy-certification-training-notes/untitled-84.png)

![Untitled](semarchy-certification-training-notes/untitled-85.png)

![Untitled](semarchy-certification-training-notes/untitled-86.png)

![Untitled](semarchy-certification-training-notes/untitled-87.png)

![Untitled](semarchy-certification-training-notes/untitled-88.png)

![Untitled](semarchy-certification-training-notes/untitled-89.png)

![Untitled](semarchy-certification-training-notes/untitled-90.png)

![Untitled](semarchy-certification-training-notes/untitled-91.png)

![Untitled](semarchy-certification-training-notes/untitled-92.png)

XDM_DEV_EN_050_Understanding the Certification Process

![Untitled](semarchy-certification-training-notes/untitled-93.png)

![Untitled](semarchy-certification-training-notes/untitled-94.png)

![Untitled](semarchy-certification-training-notes/untitled-95.png)

[Data Certification Process.pdf](semarchy-certification-training-notes/data-certification-process.pdf)

![Untitled](semarchy-certification-training-notes/untitled-96.png)

The correct order of the Data Certification process is :

Enrichment
Validation
Matching
Consolidation

**XDM_DEV_EN_060_Enriching and Validating Data**

![Untitled](semarchy-certification-training-notes/untitled-97.png)

![Untitled](semarchy-certification-training-notes/untitled-98.png)

![Untitled](semarchy-certification-training-notes/untitled-99.png)

![Untitled](semarchy-certification-training-notes/untitled-100.png)

![Untitled](semarchy-certification-training-notes/untitled-101.png)

![Untitled](semarchy-certification-training-notes/untitled-102.png)

![Untitled](semarchy-certification-training-notes/untitled-103.png)

![Untitled](semarchy-certification-training-notes/untitled-104.png)

![Untitled](semarchy-certification-training-notes/untitled-105.png)

![Untitled](semarchy-certification-training-notes/untitled-106.png)

![Untitled](semarchy-certification-training-notes/untitled-107.png)

![Untitled](semarchy-certification-training-notes/untitled-108.png)

![Untitled](semarchy-certification-training-notes/untitled-109.png)

[Enrichers.pdf](semarchy-certification-training-notes/enrichers.pdf)

[https://www.semarchy.com/doc/semarchy-xdm/xdm/2023.2/Plugins/develop/overview.html](https://www.semarchy.com/doc/semarchy-xdm/xdm/2023.2/Plugins/develop/overview.html)

**Demo - Rest API enricher**

![Untitled](semarchy-certification-training-notes/untitled-110.png)

![Untitled](semarchy-certification-training-notes/untitled-111.png)

**Demo - Validation**

![Untitled](semarchy-certification-training-notes/untitled-112.png)

![Untitled](semarchy-certification-training-notes/untitled-113.png)

![Untitled](semarchy-certification-training-notes/untitled-114.png)

[Validations.pdf](semarchy-certification-training-notes/validations.pdf)

![Untitled](semarchy-certification-training-notes/untitled-115.png)

how do References drive validations?

references:[https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Design/logical-model/reference-relationships.html](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Design/logical-model/reference-relationships.html)

![Untitled](semarchy-certification-training-notes/untitled-116.png)

Lab 3: Enrichers and Validations

Task 1: Create a SemQL enricher
Create a new SemQL enricher on Customer
Give it a good name. Practice good naming conventions
Uppercase and remove all punctuation in customer names and store it in the NormalizedName attribute (which you created in Lab2)
Hint: Click on the “Expression” column to enable SemQL editor
Hint: UPPER(REGEXP_REPLACE( CustomerName, '[[:punct:]]', ' ', 'g' ) )
Check for SemQL parsing errors

Task 2: Create a SemQL validation rule
Create a new SemQL Validation rule on Customer to ensure that we have a customer name of sufficient length.
Provide a meaningful Name.
Add a rule to check that all customer names are longer than one character.
Hint: LENGTH(CustomerName) > 1
Check for SemQL parsing errors

Note: Remember, for validation rules; if the condition evaluates to true, the record passes through successfully, if the evaluation evaluates to false, the record is rejected.

Task 3: Create a unique key constraint
Add a unique key constraint to Customer using the CustomerName and Email attributes
Task 4: Create a plug-in enricher
Add an API enricher to the Customer entity, using the Java Plug-in option with the Semarchy Text Enricher.
Use the transformation DOUBLEMETAPHONE to have a phonetic version of the NormalizedName attribute. Use PhoneticName as the output.

[Lab 3  Enrichers and validations.pdf](semarchy-certification-training-notes/lab-3-enrichers-and-validations.pdf)

![Untitled](semarchy-certification-training-notes/untitled-117.png)

![Untitled](semarchy-certification-training-notes/untitled-118.png)

![Untitled](semarchy-certification-training-notes/untitled-119.png)

Use the transformation DoubleMetaPhone to have a phonetic version of the NormalizedName attribute. Use PhoneticName as the output. - how to solve this?

1. Right click on Enrichers node of Customer entity, select Add API Enricher.
2. Select Java plug-in option, choose Semarchy Text Enricher, set Name to PhoneticiseName, click Finish.
3. In the enricher form go to Plug-in Params section set the Transformation value to DOUBLEMETAPHONE and in Inputs section, set Input Text value to NormalizedName
4. Click on Define Outputs button on top of the Outputs table. Add PhoneticName
5. Finally set Output Name to Transformed Text

![Untitled](semarchy-certification-training-notes/untitled-120.png)

![Untitled](semarchy-certification-training-notes/untitled-121.png)

![Untitled](semarchy-certification-training-notes/untitled-122.png)

![Untitled](semarchy-certification-training-notes/untitled-123.png)

![Untitled](semarchy-certification-training-notes/untitled-124.png)

Hi, Does SemQL editor has a validation check for parenthesis to validate if open and close parenthesis match each other? This validation is available in other editors, hence want to understand how can we validate the parenthesis when used in expressions.I can see an error message shown " ERROR 1:62 missing ')' at '<EOF>'" but it doesnt show dynamically on the editor, we have to validate manually.

In the Expression Editor you can click on 'Display parsing messages' to see syntax errors:

![Untitled](semarchy-certification-training-notes/untitled-125.png)

XDM_DEV_EN_065_Enriching and and Validating data - Solution

In this module you will find the Hands On Labs solutions for Lab 3

Lab 3 Task 1 - SemQL Enricher
Lab 3 Tasks 2 & 3 - SemQL Validation and Unique Key
Lab 3 Task 4 - API Phonetic Enricher

**Lab 3 Task 1 Add SemQL Enricher**

![Untitled](semarchy-certification-training-notes/untitled-126.png)

![Untitled](semarchy-certification-training-notes/untitled-127.png)

![Untitled](semarchy-certification-training-notes/untitled-128.png)

![Untitled](semarchy-certification-training-notes/untitled-129.png)

![Untitled](semarchy-certification-training-notes/untitled-130.png)

**Lab 3 Tasks 2&3 - Validation Rule & Unique Key**

![Untitled](semarchy-certification-training-notes/untitled-131.png)

![Untitled](semarchy-certification-training-notes/untitled-132.png)

![Untitled](semarchy-certification-training-notes/untitled-133.png)

![Untitled](semarchy-certification-training-notes/untitled-134.png)

**Lab 3 Task 4 - Plug-in Enricher**

![Untitled](semarchy-certification-training-notes/untitled-135.png)

![Untitled](semarchy-certification-training-notes/untitled-136.png)

![Untitled](semarchy-certification-training-notes/untitled-137.png)

XDM_DEV_EN_070_Configure Match and Merge

**Demo: Configure Publishers**

![Untitled](semarchy-certification-training-notes/untitled-138.png)

![Untitled](semarchy-certification-training-notes/untitled-139.png)

![Untitled](semarchy-certification-training-notes/untitled-140.png)

[Configuring Match and Merge.pdf](semarchy-certification-training-notes/configuring-match-and-merge.pdf)

**Presentation: Matching Process**

![Untitled](semarchy-certification-training-notes/untitled-141.png)

![Untitled](semarchy-certification-training-notes/untitled-142.png)

![Untitled](semarchy-certification-training-notes/untitled-143.png)

![Untitled](semarchy-certification-training-notes/untitled-144.png)

![Untitled](semarchy-certification-training-notes/untitled-145.png)

![Untitled](semarchy-certification-training-notes/untitled-146.png)

![Untitled](semarchy-certification-training-notes/untitled-147.png)

![Untitled](semarchy-certification-training-notes/untitled-148.png)

**Demo; Match Rule**

![Untitled](semarchy-certification-training-notes/untitled-149.png)

![Untitled](semarchy-certification-training-notes/untitled-150.png)

![Untitled](semarchy-certification-training-notes/untitled-151.png)

![Untitled](semarchy-certification-training-notes/untitled-152.png)

![Untitled](semarchy-certification-training-notes/untitled-153.png)

**Matching - Fuzzy Matching Algorithms**

[Matching - Fuzzy Matching Algorithms.pdf](semarchy-certification-training-notes/matching-fuzzy-matching-algorithms.pdf)

[Configuring Match and Merge (1).pdf](Semarchy%20Certification%20Training%20notes/Configuring_Match_and_Merge_(1).pdf)

notes :

When you deploy new rules and this will also include Enrichers, Validations as well as Match Rules, the existing golden data is not affected.
So any new match rules you add to the Matcher will only apply to new data loaded.

In a dev environment, you can reset the matching by removing the data, add new match rule(s) and then re-load the dataset.

![Untitled](semarchy-certification-training-notes/untitled-154.png)

![Untitled](semarchy-certification-training-notes/untitled-155.png)

![Untitled](semarchy-certification-training-notes/untitled-156.png)

Lab 4 - Publishers and Matching

Lab 4
Task 1: Create publishers
We need to create publishers so we can identify which systems the data has come from. They will be used in any loading process.

Create 4 publishers
DataEntry – MDM
Marketo – MKT
Salesforce – CRM
NetSuite – ERP
Task 2: Create matcher
Create a SemQL matcher for the Customer entity to identify duplicate data
Give it a good description – this will be seen by data stewards that will review data.
Task 3: Create an exact match rule with an exact match condition
Add a Match Rule for an exact match on NormalizedName and call it ExactNameAndSameCity which compares the name and location for both records
Hint: Record1.NormalizedName = Record2.NormalizedName
AND Record1.BillingAddress.City = Record2.BillingAddress.City
AND Record1.BillingAddress.Country = Record2.BillingAddress.Country
Set the match score to 100.
Task 4: Create another match rule with a fuzzy match condition
Add a second match rule to the Customer Entity and call it SimiliarNameAndSimiliarAddress
Add the following Match Condition which compares the similarity of name and address for both records
Hint: Record1.PhoneticName = Record2.PhoneticName

and SEM_EDIT_DISTANCE_SIMILARITY( Record1.BillingAddress.StreetName, Record2.BillingAddress.StreetName ) > 65

and Record1.BillingAddress.City = Record2.BillingAddress.City

and Record1.BillingAddress.Country = Record2.BillingAddress.Country

Add a match score to the rule and leave the defaults for all other settings.
Hint: This score should be lower than the exact match rule

![Untitled](semarchy-certification-training-notes/untitled-157.png)

![Untitled](semarchy-certification-training-notes/untitled-158.png)

![Untitled](semarchy-certification-training-notes/untitled-159.png)

![Untitled](semarchy-certification-training-notes/untitled-160.png)

how to Create a SemQL matcher for the Customer entity to identify duplicate data?

1. Right click on Matchers node of Customer entity, select Define SemQL Matcher
2. Set the Description and click Finish
3. Click on Add Match Rule on top of the Match Rules table

4. Set Name to ExactNameAndSameCity and click on Edit Expression button

![Untitled](semarchy-certification-training-notes/untitled-161.png)

![Untitled](semarchy-certification-training-notes/untitled-162.png)

What is Binning Expressions in the context of match rule?

Binning is an exact match statement. Matching is more efficient by using exact matches.

We have already got binning in our match rule:

Record1.BillingAddress.Country = Record2.BillingAddress.Country

AND
Record1.BillingAddress.City = Record2.BillingAddress.City

So that we only compare NormalizedName within the same City AND the same Country

The same result and performance could be acheived by using a Binning Expression :

![Untitled](semarchy-certification-training-notes/untitled-163.png)

**Demo: Survivorship**

![Untitled](semarchy-certification-training-notes/untitled-164.png)

;

![Untitled](semarchy-certification-training-notes/untitled-165.png)

![Untitled](semarchy-certification-training-notes/untitled-166.png)

![Untitled](semarchy-certification-training-notes/untitled-167.png)

![Untitled](semarchy-certification-training-notes/untitled-168.png)

[https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Design/matching/advanced-match-rules.html#_matching_on_parent_records](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Design/matching/advanced-match-rules.html#_matching_on_parent_records)

[XDM_ENV_EN_070_Slides_Survivorship_.pdf](semarchy-certification-training-notes/xdm-env-en-070-slides-survivorship.pdf)

Notes : The use case of override setting 'Always Authored in MDM' is for any attributes that you do not or never want to be updated by source systems.

![Untitled](semarchy-certification-training-notes/untitled-169.png)

![Untitled](semarchy-certification-training-notes/untitled-170.png)

[Lab 5 - Survivorship.pdf](semarchy-certification-training-notes/lab-5-survivorship.pdf)

Lab 5 - Survivorship
Lab 5

Create survivorship rules to determine how the Golden Record will be constructed from the best data from the master Records.

Task 1: Create a survivorship rule
Create a new survivorship rule to the Customer entity for the CustomerName.
Add CustomerName to the Attributes.
In the Consolidation Rule, set the Consolidation Strategy to Most Frequent Value.
Set the Override Rule so that changes by the users are allowed and take precedence over the source systems: Override - until next user change.

Task 2: Update the default survivorship rule
We must remember to change the DefaultRule from Custom Ranking to use a Preferred Publishers consolidation strategy, in this order:
DataEntry-MDM
Salesforce-CRM
Marketo-MKT
NetSuite-ERP
In case of a tie, use the latest record.
Hint: Use UpdateDate DESC (descending) as the ranking expression UpdateDate DESC.
Set the Override Rule such that updated data from Publishers will overwrite any user changes.

Task 3: Create a field specific survivorship rule

Define another Survivorship rule for TotalRevenue which will take the Largest Value but not allow the users to edit the value in the application.
Hint: Override Strategy –‘No Override’

![Untitled](semarchy-certification-training-notes/untitled-171.png)

![Untitled](semarchy-certification-training-notes/untitled-172.png)

![Untitled](semarchy-certification-training-notes/untitled-173.png)

![Untitled](semarchy-certification-training-notes/untitled-174.png)

![Untitled](semarchy-certification-training-notes/untitled-175.png)

![Untitled](semarchy-certification-training-notes/untitled-176.png)

XDM_DEV_EN_075_Configure Match and Merge - Solution

In this module you will find the solutions to

Lab 4 - Task 1 Publishers
Lab 4 - Tasks 2, 3 & 4 - Create a Matcher
Lab 5 - Survivorship Rules

**Lab 4 Task 1 Create Publishers - Solution**

![Untitled](semarchy-certification-training-notes/untitled-177.png)

![Untitled](semarchy-certification-training-notes/untitled-178.png)

**Lab 4 Create Matcher - Solution**

![Untitled](semarchy-certification-training-notes/untitled-179.png)

![Untitled](semarchy-certification-training-notes/untitled-180.png)

**Lab 5 - Create Survivorship Rules - Solution**

![Untitled](semarchy-certification-training-notes/untitled-181.png)

![Untitled](semarchy-certification-training-notes/untitled-182.png)

![Untitled](semarchy-certification-training-notes/untitled-183.png)

XDM_DEV_EN_080_Deploy and Browse

**Demo: Deploy to a Data Location**

![Untitled](semarchy-certification-training-notes/untitled-184.png)

![Untitled](semarchy-certification-training-notes/untitled-185.png)

![Untitled](semarchy-certification-training-notes/untitled-186.png)

![Untitled](semarchy-certification-training-notes/untitled-187.png)

![Untitled](semarchy-certification-training-notes/untitled-188.png)

**Slides: Deploying and Browsing**

[Deploying and Browsing.pdf](semarchy-certification-training-notes/deploying-and-browsing.pdf)

**Lab 6: Deploying and Browsing**

2.7 - Deploying and Browsing

Lab 6

Task 1: Validate your model
Return to the application builder section.
Under the Model Edition tab (Model Design), right-click on the  model name and select Validate
Any errors should be resolved.
You will have multiple warnings. We will fix these in the next sessions. A model can be deployed with warnings but not with errors.

Task 2: Create a data location
Select the Management perspective in the application builder
Create a new Data Location
Select the Data Source Name DATA_LOCATION_1 (might also be called DLOC1)
Set the Location Type to Development Location
Select a Model Edition to deploy
Click Finish to deploy the model into the Data Location. This should happen automatically.
Note: Review Console tab for any issues (there should not be any)

Task 3: Open your application
Go to your Semarchy Welcome page
Look for your new Application (should be called Default) and click on the logo.
Hint: Refresh the page if necessary
What do you see?
Set up your profile

XDM_DEV_EN_085_Deploy and Browse - Solution

**Lab 6 - Validating and Deploying Model - Solution**

![Untitled](semarchy-certification-training-notes/untitled-189.png)

**XDM_DEV_EN_090_Introduction to Visual Bricks**

![Untitled](semarchy-certification-training-notes/untitled-190.png)

![Untitled](semarchy-certification-training-notes/untitled-191.png)

![Untitled](semarchy-certification-training-notes/untitled-192.png)

![Untitled](semarchy-certification-training-notes/untitled-193.png)

[Intro.pdf](semarchy-certification-training-notes/intro.pdf)

![Untitled](semarchy-certification-training-notes/untitled-194.png)

![Untitled](semarchy-certification-training-notes/untitled-195.png)

XDM_DEV_EN_100_Display Cards

In this module you will learn

What is a Display Card
How Display Cards are used in an application
How to configure Display Cards in the Model Design

**Presentation: What is a Display Card?**

[Display card.pdf](semarchy-certification-training-notes/display-card.pdf)

**Demo: How to Configure a Display Card**

![Untitled](semarchy-certification-training-notes/untitled-196.png)

XDM_DEV_EN_110_Collections

In this module you will learn about Collections

You will see

What is a Collection
How to Configure a Collection

[Collection.pdf](semarchy-certification-training-notes/collection.pdf)

![Untitled](semarchy-certification-training-notes/untitled-197.png)

![Untitled](semarchy-certification-training-notes/untitled-198.png)

![Untitled](semarchy-certification-training-notes/untitled-199.png)

![Untitled](semarchy-certification-training-notes/untitled-200.png)

![Untitled](semarchy-certification-training-notes/untitled-201.png)

XDM_DEV_EN_120_Forms

This module will

Show you what is a Form
Show you how Forms are used in Applications
You will learn how to create a  Form in the Model Design

**Presentation: FORMS - What is a Form?**

[Forms.pdf](semarchy-certification-training-notes/forms.pdf)

**Demo: Create a Form**

![Untitled](semarchy-certification-training-notes/untitled-202.png)

![Untitled](semarchy-certification-training-notes/untitled-203.png)

![Untitled](semarchy-certification-training-notes/untitled-204.png)

![Untitled](semarchy-certification-training-notes/untitled-205.png)

![Untitled](semarchy-certification-training-notes/untitled-206.png)

XDM_DEV_EN_130_Application Components Wizard

In this module you will learn how to use the Create Application Components wizard to create your application components

**Demo: Create Applications Component Wizard**

![Untitled](semarchy-certification-training-notes/untitled-207.png)

![Untitled](semarchy-certification-training-notes/untitled-208.png)

[Component Wizard.pdf](semarchy-certification-training-notes/component-wizard.pdf)

Lab 7

Task 1: Create application components using the wizard
Semarchy xDM is a very agile product to work with. This means it is fairly quick to design a model, deploy it and see it live in the Application UI. Although our model is not finished, we can take a few more steps to enable you to see part of the model you have built and load data into it.

Use the Create Application Components wizard for the BankDetail entity only (leave Customer until later).
Use the default settings on the ‘Applications and Features’ first step
Change the Primary Text Expression for the Display Card to BankName || '-' || AccountNumber
Take note of what components have been created and review them
Collections
Forms
Steppers
Action Sets
Business Views
Folders and Actions for the Default Application
Right click the Data Location and ‘Deploy Model Edition’
Hint: Since we created steppers since the last deployment, we should re-deploy the model.
Follow the ‘Deploy Model Edition’ wizard.
In the Application, Refresh Application to see your changes.

Task 2: Create a display card
Change the default Display Card for Customer (CustomerDisplayCard)
Change the primary text to something meaningful like the CustomerName
Set the secondary text to something meaningful, like the CustomerID
Add an avatar – search for ‘account-multiple’

Task 3: Create a collection
Create a Collection for Customer that displays:
CustomerName
NormalizedName
PhoneticName
TotalRevenue
BillingAddress.StreetName
BillingAddress.City
BillingAddress.PostalCode
BillingAddress.Country
MastersCount
GoldenType
ConfidenceScore
Display the default display card in the first column of the collection

Task 4: Create forms
It is a best practice to separate data entry forms from browsing forms. So we’ll create different forms, one for viewing and another one for editing/data entry.

Create a Form for Customer that displays the following information
CustomerID
CustomerName
TotalRevenue
BillingAddress
Create another Form named CustomerEditForm for Customer that displays:
CustomerID
CustomerName
Email
Phone
BillingAddress.StreetName
BillingAddress.PostalCode
BillingAddress.City
BillingAddress.Country

XDM_DEV_EN_135 Component Wizard - Solution

In this module you will find solutions for Lab 7

Lab 7 Task 1 - Create Application Components
Lab 7 Task 2 - Create a Display Card
Lab 7 Task 3 - Create a Collection
Lab 7 Task 4 - Create Forms

**Lab 7 Task 1 Solution - Create Application Components**

![Untitled](semarchy-certification-training-notes/untitled-209.png)

![Untitled](semarchy-certification-training-notes/untitled-210.png)

![Untitled](semarchy-certification-training-notes/untitled-211.png)

![Untitled](semarchy-certification-training-notes/untitled-212.png)

![Untitled](semarchy-certification-training-notes/untitled-213.png)

![Untitled](semarchy-certification-training-notes/untitled-214.png)

![Untitled](semarchy-certification-training-notes/untitled-215.png)

**Lab 7 Task 2 Solution - Create Display Card**

![Untitled](semarchy-certification-training-notes/untitled-216.png)

**Lab 7 Task 3 Solution - Create a Collection**

![Untitled](semarchy-certification-training-notes/untitled-217.png)

![Untitled](semarchy-certification-training-notes/untitled-218.png)

![Untitled](semarchy-certification-training-notes/untitled-219.png)

**Lab 7 Task 4 Solution - Create Forms**

![Untitled](semarchy-certification-training-notes/untitled-220.png)

![Untitled](semarchy-certification-training-notes/untitled-221.png)

![Untitled](semarchy-certification-training-notes/untitled-222.png)

![Untitled](semarchy-certification-training-notes/untitled-223.png)

XDM_DEV_EN_140_Business Views

In this module you will learn about Business Views.

You will see how to assemble all the previous created components (Display Cards, Collections and Forms) in a Business View to allow users to browse their data.

**Presentation: What is a Business View?**

[Building Business Views_compressed.pdf](semarchy-certification-training-notes/building-business-views-compressed.pdf)

**Demo: Configure a Business View**

![Untitled](semarchy-certification-training-notes/untitled-224.png)

![Untitled](semarchy-certification-training-notes/untitled-225.png)

![Untitled](semarchy-certification-training-notes/untitled-226.png)

![Untitled](semarchy-certification-training-notes/untitled-227.png)

![Untitled](semarchy-certification-training-notes/untitled-228.png)

![Untitled](semarchy-certification-training-notes/untitled-229.png)

![Untitled](semarchy-certification-training-notes/untitled-230.png)

![Untitled](semarchy-certification-training-notes/untitled-231.png)

![Untitled](semarchy-certification-training-notes/untitled-232.png)

![Untitled](semarchy-certification-training-notes/untitled-233.png)

![Untitled](semarchy-certification-training-notes/untitled-234.png)

![Untitled](semarchy-certification-training-notes/untitled-235.png)

Business Views can be configured:

To include more entities in a Business View, for example child Employees working in a Department or child Contacts working in a Company, you can use transitions to navigate to other child entities
Transitions to parent entities cannot be defined in the Transitions table but navigation to parent entities can be configured in Reference Browsing on the root business entity
To select an Action Set that will define which actions are available to manage data on that entity
To add search capabilities including your own custom Search Forms
To add pre-canned Built-in filters which the user can enable or disable
To enable hierarchy tree views which users can expand and select transitions and child records

![Untitled](semarchy-certification-training-notes/untitled-236.png)

Lab 8 - Create a Business View

Lab 8
Task 1: Create a Business View
Create a Business View for Customer and name it Customers. Accept all defaults settings and click on Finish
Under Transitions , select Customer and click on the Add Transition button
Note: We need to add a transition to the customers business view to be able to see the master records that have been consolidated into the Golden record.
Select a Transition Path for MasterRecords (don’t drill down any further) and click Finish
Select a Transition Path for BankDetails and click Finish
Save the Business View

**Lab 8 Solution - Create a Business View**

![Untitled](semarchy-certification-training-notes/untitled-237.png)

![Untitled](semarchy-certification-training-notes/untitled-238.png)

![Untitled](semarchy-certification-training-notes/untitled-239.png)

![Untitled](semarchy-certification-training-notes/untitled-240.png)

![Untitled](semarchy-certification-training-notes/untitled-241.png)

![Untitled](semarchy-certification-training-notes/untitled-242.png)

![Untitled](semarchy-certification-training-notes/untitled-243.png)

![Untitled](semarchy-certification-training-notes/untitled-244.png)

![Untitled](semarchy-certification-training-notes/untitled-245.png)

![Untitled](semarchy-certification-training-notes/untitled-246.png)

![Untitled](semarchy-certification-training-notes/untitled-247.png)

XDM_DEV_EN_150_Enable Search and Filtering

In this module you will learn how to create a search form to add in the business view in order to allow the user to search data.

**Slides: Enabling search and filtering**

[3.3 - Enabling search and filtering.pdf](semarchy-certification-training-notes/3-3-enabling-search-and-filtering.pdf)

**Presentation: Built-in Search Types**

![Untitled](semarchy-certification-training-notes/untitled-248.png)

![Untitled](semarchy-certification-training-notes/untitled-249.png)

![Untitled](semarchy-certification-training-notes/untitled-250.png)

![Untitled](semarchy-certification-training-notes/untitled-251.png)

![Untitled](semarchy-certification-training-notes/untitled-252.png)

![Untitled](semarchy-certification-training-notes/untitled-253.png)

![Untitled](semarchy-certification-training-notes/untitled-254.png)

![Untitled](semarchy-certification-training-notes/untitled-255.png)

![Untitled](semarchy-certification-training-notes/untitled-256.png)

![Untitled](semarchy-certification-training-notes/untitled-257.png)

**Demo: Creating a customized Search Form**

![Untitled](semarchy-certification-training-notes/untitled-258.png)

![Untitled](semarchy-certification-training-notes/untitled-259.png)

![Untitled](semarchy-certification-training-notes/untitled-260.png)

![Untitled](semarchy-certification-training-notes/untitled-261.png)

![Untitled](semarchy-certification-training-notes/untitled-262.png)

![Untitled](semarchy-certification-training-notes/untitled-263.png)

![Untitled](semarchy-certification-training-notes/untitled-264.png)

![Untitled](semarchy-certification-training-notes/untitled-265.png)

![Untitled](semarchy-certification-training-notes/untitled-266.png)

![Untitled](semarchy-certification-training-notes/untitled-267.png)

![Untitled](semarchy-certification-training-notes/untitled-268.png)

![Untitled](semarchy-certification-training-notes/untitled-269.png)

![Untitled](semarchy-certification-training-notes/untitled-270.png)

![Untitled](semarchy-certification-training-notes/untitled-271.png)

**Lab 9 - Search Form**

Lab 9 - Search Form
Task 1: Create a Search Form
Add a Search Form to the Customer entity and add a Search Tip
Add a search parameters for CustomerName
Add a SemQL condition to allow searching for CustomerName using the search parameter.                                                                          Hint: UPPER(CustomerName) LIKE '%' || UPPER(:SEARCH_PARAM_CUSTOMER_NAME) || '%'
Refresh the Search Configurations in your Customers Business View.   

                                                                                                           

Hint: Look in the ‘Display Properties’  finger tab
Make the custom search form the first search type available
In the next lab, you will be able to see your search form once you have added the Customers business view in the application.

XDM_DEV_EN_155_Enable Search - Solution

In this module you will find the solution to Lab 9

Lab 9 Task 1 - Create Search Form

![Untitled](semarchy-certification-training-notes/untitled-272.png)

![Untitled](semarchy-certification-training-notes/untitled-273.png)

![Untitled](semarchy-certification-training-notes/untitled-274.png)

![Untitled](semarchy-certification-training-notes/untitled-275.png)

![Untitled](semarchy-certification-training-notes/untitled-276.png)

![Untitled](semarchy-certification-training-notes/untitled-277.png)

XDM_DEV_EN_160_Organizing and Branding the Application

In this module, you will learn

How to organize and brand your application
Arrange the Folders and Actions
Show the Navigation Drawer

**Demo: Application Folders and Actions and Navigation Drawer**

![Untitled](semarchy-certification-training-notes/untitled-278.png)

![Untitled](semarchy-certification-training-notes/untitled-279.png)

![Untitled](semarchy-certification-training-notes/untitled-280.png)

![Untitled](semarchy-certification-training-notes/untitled-281.png)

![Untitled](semarchy-certification-training-notes/untitled-282.png)

![Untitled](semarchy-certification-training-notes/untitled-283.png)

![Untitled](semarchy-certification-training-notes/untitled-284.png)

![Untitled](semarchy-certification-training-notes/untitled-285.png)

![Untitled](semarchy-certification-training-notes/untitled-286.png)

![Untitled](semarchy-certification-training-notes/untitled-287.png)

**Slides: Organizing and branding the application**

[3.4 - Organizing and branding the application_compressed.pdf](semarchy-certification-training-notes/3-4-organizing-and-branding-the-application-compressed.pdf)

**Demo: Documentation**

![Untitled](semarchy-certification-training-notes/untitled-288.png)

![Untitled](semarchy-certification-training-notes/untitled-289.png)

![Untitled](semarchy-certification-training-notes/untitled-290.png)

![Untitled](semarchy-certification-training-notes/untitled-291.png)

![Untitled](semarchy-certification-training-notes/untitled-292.png)

![Untitled](semarchy-certification-training-notes/untitled-293.png)

he question is asking what can be shown from the following items in the navigation drawer. It is using the Folders that are created in “Folders and Actions” to arrange what you see in the Navigation sidebar. We can discuss in the next session but in the meantime here is a link that explains the Folders and Actions and Navigation drawer in further detail. 

[https://www.semarchy.com/doc/semarchy-xdm/xdm/5.3/Design/applications/application-actions-and-folders.html](https://www.semarchy.com/doc/semarchy-xdm/xdm/5.3/Design/applications/application-actions-and-folders.html)

**Lab 10 - Organizing and Branding the Application**

Task 1: Configure folders and actions
Go to Folders and Actions  add an Action to the Root folder, name it BrowseCustomers with the Action Type Browse Business View
Put the Customers [Business View] in the folder.
Select an icon to represent the entity
e.g.: ‘account-multiple’
Set the icon color
e.g.: md:red, md:blue etc
Save and refresh the application UI. Do you see your changes? Find the search form you set up in the previous lab.

Task 2: Name the application
Double click on your application

Change the name, label, and title

Task 3: Set up documentation configuration
Go to the Default Application node and set up the Documentation Configuration
Add the Diagram you have created
Write a small description that will be displayed to the end-users.

Task 4: Configure the Global Search
Go to the Global Search Configuration, add the corresponding Businesss Views to search through Customers and BankDetails.

XDM_DEV_EN_165_Organizing and Branding Solution

In this module you will find the solution to Hands On Lab 10

Lab 10 Task 1 Confgure Folders and Actions
Lab 10 Tasks 2 & 3 Name the Application & Set up Documentation Confguration
Lab 10 Task 4 Confgure Global Search

**Lab 10 Task 1 Solution - Configure Folders and Actions**

![Untitled](semarchy-certification-training-notes/untitled-294.png)

![Untitled](semarchy-certification-training-notes/untitled-295.png)

![Untitled](semarchy-certification-training-notes/untitled-296.png)

![Untitled](semarchy-certification-training-notes/untitled-297.png)

![Untitled](semarchy-certification-training-notes/untitled-298.png)

![Untitled](semarchy-certification-training-notes/untitled-299.png)

![Untitled](semarchy-certification-training-notes/untitled-300.png)

![Untitled](semarchy-certification-training-notes/untitled-301.png)

**Lab 10 Tasks 2 & 3 Solution - Name Application & Setup Documentation**

![Untitled](semarchy-certification-training-notes/untitled-302.png)

![Untitled](semarchy-certification-training-notes/untitled-303.png)

![Untitled](semarchy-certification-training-notes/untitled-304.png)

![Untitled](semarchy-certification-training-notes/untitled-305.png)

![Untitled](semarchy-certification-training-notes/untitled-306.png)

![Untitled](semarchy-certification-training-notes/untitled-307.png)

![Untitled](semarchy-certification-training-notes/untitled-308.png)

![Untitled](semarchy-certification-training-notes/untitled-309.png)

![Untitled](semarchy-certification-training-notes/untitled-310.png)

**Lab 10 Task 4 Solution - Configure Global Search**

![Untitled](semarchy-certification-training-notes/untitled-311.png)

![Untitled](semarchy-certification-training-notes/untitled-312.png)

![Untitled](semarchy-certification-training-notes/untitled-313.png)

![Untitled](semarchy-certification-training-notes/untitled-314.png)

XDM_DEV_EN_170_Steppers

In this module, you will learn about  Steppers and Guided Authoring:

What is a Stepper?
You'll see an example of a Stepper in action!
How to configure a Stepper

**Information: What are Steppers?**

- 

```
**Steppers are a wizard like sequence of steps that drive the user through a data authoring operation such as aCreate or anEditThey guide business users through the correct steps that are needed toCreateorEdit recordsor performing anImport/Mass Update on a set of records.**
```

![Untitled](semarchy-certification-training-notes/untitled-315.png)

![Untitled](semarchy-certification-training-notes/untitled-316.png)

![Untitled](semarchy-certification-training-notes/untitled-317.png)

![Untitled](semarchy-certification-training-notes/untitled-318.png)

![Untitled](semarchy-certification-training-notes/untitled-319.png)

![Untitled](semarchy-certification-training-notes/untitled-320.png)

**Demo: Guided Data Authoring: Using the Product Stepper**

![Untitled](semarchy-certification-training-notes/untitled-321.png)

![Untitled](semarchy-certification-training-notes/untitled-322.png)

![Untitled](semarchy-certification-training-notes/untitled-323.png)

![Untitled](semarchy-certification-training-notes/untitled-324.png)

![Untitled](semarchy-certification-training-notes/untitled-325.png)

**Demo: How to configure a Stepper - Part ONE**

![Untitled](semarchy-certification-training-notes/untitled-326.png)

![Untitled](semarchy-certification-training-notes/untitled-327.png)

![Untitled](semarchy-certification-training-notes/untitled-328.png)

![Untitled](semarchy-certification-training-notes/untitled-329.png)

![Untitled](semarchy-certification-training-notes/untitled-330.png)

![Untitled](semarchy-certification-training-notes/untitled-331.png)

![Untitled](semarchy-certification-training-notes/untitled-332.png)

![Untitled](semarchy-certification-training-notes/untitled-333.png)

![Untitled](semarchy-certification-training-notes/untitled-334.png)

![Untitled](semarchy-certification-training-notes/untitled-335.png)

![Untitled](semarchy-certification-training-notes/untitled-336.png)

**Demo: Configure a Stepper - Part Two: Validations**

![Untitled](semarchy-certification-training-notes/untitled-337.png)

![Untitled](semarchy-certification-training-notes/untitled-338.png)

![Untitled](semarchy-certification-training-notes/untitled-339.png)

![Untitled](semarchy-certification-training-notes/untitled-340.png)

![Untitled](semarchy-certification-training-notes/untitled-341.png)

![Untitled](semarchy-certification-training-notes/untitled-342.png)

![Untitled](semarchy-certification-training-notes/untitled-343.png)

![Untitled](semarchy-certification-training-notes/untitled-344.png)

![Untitled](semarchy-certification-training-notes/untitled-345.png)

![Untitled](semarchy-certification-training-notes/untitled-346.png)

![Untitled](semarchy-certification-training-notes/untitled-347.png)

![Untitled](semarchy-certification-training-notes/untitled-348.png)

**Slides: Designing Authoring Steppers**

[4.1 - Designing authoring steppers_compressed.pdf](semarchy-certification-training-notes/4-1-designing-authoring-steppers-compressed.pdf)

**Lab 11 - Steppers - Your Turn!**

We can now browse our data within your application, the next step will be about defining the processes and actions available to enable authoring. First we will create a stepper and workflow to offer a guided experience when creating/updating records, then we will configure action sets that set what features are available to users and finally we will enable the duplicate manager to help data stewards make decisions.

Lab 11
Task 1: Create a stepper
Create a stepper AuthorCustomers (no need to select a job) - use the CustomerCollection collection.
Create steps  - use the CustomerEditForm (dedicated to edit customers)
Hint: It is the Form with the Main Section (select this one)

XDM_DEV_EN_175_Designing Steppers - Solution

In this module you will find the solution for Hands On Lab 11

Lab 11 - Create a Stepper

![Untitled](semarchy-certification-training-notes/untitled-349.png)

![Untitled](semarchy-certification-training-notes/untitled-350.png)

![Untitled](semarchy-certification-training-notes/untitled-351.png)

XDM_DEV_EN_180_Action Sets

In this module, you will learn about Action Sets and Actions:

What is an Action Set
How to add and configure Actions
How to add the Create Action to create a new record in the application
How to export data from xDM using the Export Action
How to Import data to xDM using the Import Action

At the end of this module, you will be able to Import Customer Data for the Hands On Lab exercise 12

[Information What are Action Sets.pdf](semarchy-certification-training-notes/information-what-are-action-sets.pdf)

**Demo: How to configure an Action Set - Part One**

![Untitled](semarchy-certification-training-notes/untitled-352.png)

![Untitled](semarchy-certification-training-notes/untitled-353.png)

![Untitled](semarchy-certification-training-notes/untitled-354.png)

![Untitled](semarchy-certification-training-notes/untitled-355.png)

![Untitled](semarchy-certification-training-notes/untitled-356.png)

![Untitled](semarchy-certification-training-notes/untitled-357.png)

![Untitled](semarchy-certification-training-notes/untitled-358.png)

![Untitled](semarchy-certification-training-notes/untitled-359.png)

![Untitled](semarchy-certification-training-notes/untitled-360.png)

![Untitled](semarchy-certification-training-notes/untitled-361.png)

**Slides: Configuring Action Sets**

[4.2 - Configuring action sets.pdf](semarchy-certification-training-notes/4-2-configuring-action-sets.pdf)

**Demo: Configure an Action Set - Part Two: EXPORT action**

![Untitled](semarchy-certification-training-notes/untitled-362.png)

![Untitled](semarchy-certification-training-notes/untitled-363.png)

![Untitled](semarchy-certification-training-notes/untitled-364.png)

![Untitled](semarchy-certification-training-notes/untitled-365.png)

![Untitled](semarchy-certification-training-notes/untitled-366.png)

![Untitled](semarchy-certification-training-notes/untitled-367.png)

![Untitled](semarchy-certification-training-notes/untitled-368.png)

![Untitled](semarchy-certification-training-notes/untitled-369.png)

**Demo: Configure an Action Set - Part Three: IMPORT action for Hands On Lab**

![Untitled](semarchy-certification-training-notes/untitled-370.png)

![Untitled](semarchy-certification-training-notes/untitled-371.png)

![Untitled](semarchy-certification-training-notes/untitled-372.png)

![Untitled](semarchy-certification-training-notes/untitled-373.png)

![Untitled](semarchy-certification-training-notes/untitled-374.png)

![Untitled](semarchy-certification-training-notes/untitled-375.png)

![Untitled](semarchy-certification-training-notes/untitled-376.png)

![Untitled](semarchy-certification-training-notes/untitled-377.png)

**Information: Action Sets - Authoring Actions**

[Information Action Sets -  Authoring Actions.pdf](semarchy-certification-training-notes/information-action-sets-authoring-actions.pdf)

# **Information: Action Sets - Duplicate Management actions**

`The following Duplicates Management Actions require a **Duplicate Manager**
 
• **REVIEW AND CONFIRM DUPLICATES**
• **CONFIRM DUPLICATES** 
• **MERGE OR SPLIT DUPLICATES**
• **REVIEW DUPLICATE SUGGESTIONS**`

**Lab 12 - Action Sets**

[Lab 12 - Action Sets.pdf](semarchy-certification-training-notes/lab-12-action-sets.pdf)

XDM_DEV_EN_185_Configuring Action Sets - Solution

In this module you will find the solution to Hands On Lab 12

Lab 12 Task 1- Configure Action Set
Lab 12 Task 2 - Use the Actions
This also includes a demo of the use of the Default Entities folder

![Untitled](semarchy-certification-training-notes/untitled-378.png)

![Untitled](semarchy-certification-training-notes/untitled-379.png)

![Untitled](semarchy-certification-training-notes/untitled-380.png)

![Untitled](semarchy-certification-training-notes/untitled-381.png)

![Untitled](semarchy-certification-training-notes/untitled-382.png)

![Untitled](semarchy-certification-training-notes/untitled-383.png)

![Untitled](semarchy-certification-training-notes/untitled-384.png)

**Lab 12 Task 2 Solution - Use Action Set**

![Untitled](semarchy-certification-training-notes/untitled-385.png)

![Untitled](semarchy-certification-training-notes/untitled-386.png)

![Untitled](semarchy-certification-training-notes/untitled-387.png)

![Untitled](semarchy-certification-training-notes/untitled-388.png)

![Untitled](semarchy-certification-training-notes/untitled-389.png)

![Untitled](semarchy-certification-training-notes/untitled-390.png)

XDM_DEV_EN_200_Duplicate Managers

In this module you will learn:

What are Duplicate Managers
How to configure a Duplicate Manager

**Presentation: DUPLICATE MANAGERS: What are Duplicate Managers?**

![Untitled](semarchy-certification-training-notes/untitled-391.png)

![Untitled](semarchy-certification-training-notes/untitled-392.png)

![Untitled](semarchy-certification-training-notes/untitled-393.png)

![Untitled](semarchy-certification-training-notes/untitled-394.png)

![Untitled](semarchy-certification-training-notes/untitled-395.png)

![Untitled](semarchy-certification-training-notes/untitled-396.png)

**Slides: Duplicate Managers**

[4.4 - Creating duplicate managers.pdf](semarchy-certification-training-notes/4-4-creating-duplicate-managers.pdf)

**Demo: Configure Duplicate Managers**

![Untitled](semarchy-certification-training-notes/untitled-397.png)

![Untitled](semarchy-certification-training-notes/untitled-398.png)

![Untitled](semarchy-certification-training-notes/untitled-399.png)

![Untitled](semarchy-certification-training-notes/untitled-400.png)

![Untitled](semarchy-certification-training-notes/untitled-401.png)

![Untitled](semarchy-certification-training-notes/untitled-402.png)

![Untitled](semarchy-certification-training-notes/untitled-403.png)

![Untitled](semarchy-certification-training-notes/untitled-404.png)

![Untitled](semarchy-certification-training-notes/untitled-405.png)

![Untitled](semarchy-certification-training-notes/untitled-406.png)

Lab 14 - Duplicate Managers
Lab 14
Task 1: Create a duplicate manager
Add a duplicate manager to the customer entity.
Select a collection, display card and form tab and save.
In the action set for this entity, assign a duplicate manager.
Check Confirm duplicates, Review and confirm duplicates,  Merge or split duplicates and Review duplicates suggestions.
Task 2: Use the duplicate manager
Use the Explain record action with the record Semarchy record. Browse through the different tabs.
Use the Review And Confirm Duplicates action to review the record Walmart

XDM_DEV_EN_205_Creating Duplicate Managers - Solution

In this module you will find the solution to Hands On Lab 14

Lab 14 Task 1 - Create Duplicate Manager
Lab 14 Task 2 - Use Duplicate Management Actions

**Lab 14 Task 1 Solution - Create a Duplicate Manager**

![Untitled](semarchy-certification-training-notes/untitled-407.png)

![Untitled](semarchy-certification-training-notes/untitled-408.png)

![Untitled](semarchy-certification-training-notes/untitled-409.png)

![Untitled](semarchy-certification-training-notes/untitled-410.png)

![Untitled](semarchy-certification-training-notes/untitled-411.png)

![Untitled](semarchy-certification-training-notes/untitled-412.png)

![Untitled](semarchy-certification-training-notes/untitled-413.png)

**Lab 14 Task 2 Solution - Using Duplicate Management Actions**

![Untitled](semarchy-certification-training-notes/untitled-414.png)

![Untitled](semarchy-certification-training-notes/untitled-415.png)

![Untitled](semarchy-certification-training-notes/untitled-416.png)

![Untitled](semarchy-certification-training-notes/untitled-417.png)

![Untitled](semarchy-certification-training-notes/untitled-418.png)

![Untitled](semarchy-certification-training-notes/untitled-419.png)

XDM_DEV_EN_210_Physical Structure

In this module we will present the physical structure of the database that stores xDM data.

You will learn

Recap on the certification process
Basic entities'  tables
Matched entities' tables
Difference between Basic Entities and Fuzzy Matched Entities

**Presentation: PHYSICAL STRUCTURE - Certification Process and Tables**

![Untitled](semarchy-certification-training-notes/untitled-420.png)

![Untitled](semarchy-certification-training-notes/untitled-421.png)

![Untitled](semarchy-certification-training-notes/untitled-422.png)

![Untitled](semarchy-certification-training-notes/untitled-423.png)

![Untitled](semarchy-certification-training-notes/untitled-424.png)

![Untitled](semarchy-certification-training-notes/untitled-425.png)

![Untitled](semarchy-certification-training-notes/untitled-426.png)

**Demo: Table Structure**

![Untitled](semarchy-certification-training-notes/untitled-427.png)

![Untitled](semarchy-certification-training-notes/untitled-428.png)

![Untitled](semarchy-certification-training-notes/untitled-429.png)

![Untitled](semarchy-certification-training-notes/untitled-430.png)

**Slides: Physical Structure**

[Physical Structure.pdf](semarchy-certification-training-notes/physical-structure.pdf)

![Untitled](semarchy-certification-training-notes/untitled-431.png)

XDM_DEV_EN_220_Integrating Data - Overview

In this module we will explain how to integrate data into Semarchy xDM

You will learn about

External Load Process
Continuous Load
Configuring an Integration Job
Understand the logs in order to know what happened during the certification process

**Presentation: EXTERNAL LOAD PROCESS (EN)**

![Untitled](semarchy-certification-training-notes/untitled-432.png)

![Untitled](semarchy-certification-training-notes/untitled-433.png)

![Untitled](semarchy-certification-training-notes/untitled-434.png)

![Untitled](semarchy-certification-training-notes/untitled-435.png)

![Untitled](semarchy-certification-training-notes/untitled-436.png)

![Untitled](semarchy-certification-training-notes/untitled-437.png)

![Untitled](semarchy-certification-training-notes/untitled-438.png)

**Demo: Continuous Load (EN)**

![Untitled](semarchy-certification-training-notes/untitled-439.png)

![Untitled](semarchy-certification-training-notes/untitled-440.png)

![Untitled](semarchy-certification-training-notes/untitled-441.png)

![Untitled](semarchy-certification-training-notes/untitled-442.png)

![Untitled](semarchy-certification-training-notes/untitled-443.png)

**Demo: Configuring an Integration Job**

![Untitled](semarchy-certification-training-notes/untitled-444.png)

![Untitled](semarchy-certification-training-notes/untitled-445.png)

![Untitled](semarchy-certification-training-notes/untitled-446.png)

![Untitled](semarchy-certification-training-notes/untitled-447.png)

![Untitled](semarchy-certification-training-notes/untitled-448.png)

![Untitled](semarchy-certification-training-notes/untitled-449.png)

![Untitled](semarchy-certification-training-notes/untitled-450.png)

![Untitled](semarchy-certification-training-notes/untitled-451.png)

![Untitled](semarchy-certification-training-notes/untitled-452.png)

![Untitled](semarchy-certification-training-notes/untitled-453.png)

![Untitled](semarchy-certification-training-notes/untitled-454.png)

**Slides: Integrating Data**

[Integrating Data - Overview.pdf](semarchy-certification-training-notes/integrating-data-overview.pdf)

![Untitled](semarchy-certification-training-notes/untitled-455.png)

**Information: External Load Lifecycle**

External Load Lifecycle

An external load lifecycle is described below:

Initialize the External Load

- The middleware initializes an external load with the SQL Interface or the REST API.
- It receives from the platform a Load ID identifying the external load.
- At that stage, an external load transaction is open with the platform.

Load Data

The middleware inserts data into the landing tables in the data location schema. This is done using the SQL Interface or the REST API.

When loading data, the middleware provides both the Load ID and a Publisher Code corresponding to the publisher application.

Submit the External Load

The middleware uses the SQL Interface or the REST API to submit the external load.

It provides the Load ID as well as the name of the Integration Job to trigger with this submission.

The platform creates a Batch to run the integration job that certifies the data published in this external load.

It receives from the platform a Batch ID identifying the batch that is processed by the platform for this external load.

At that stage, the external load transaction is closed.

The middleware can alternately Cancel the External Load with the SQL Interface or the REST API to abort the external load instead of submitting it.

|  | [**Continuous Loads**](https://www.semarchy.com/doc/semarchy-xdm/xdm/5.3/Integrate/publish-data-with-continuous-loads.html) facilitate the publishing process. A continuous load is an open external load into which data is published. The hub polls and processes this data automatically. |
| --- | --- |

|  | Data locations may be moved to a **Maintenance** status by their administrator. When a data location is in that state, it is not possible to initialize external loads. |
| --- | --- |

![Untitled](semarchy-certification-training-notes/untitled-456.png)

![Untitled](semarchy-certification-training-notes/untitled-457.png)

![Untitled](semarchy-certification-training-notes/untitled-458.png)

![Untitled](semarchy-certification-training-notes/untitled-459.png)

![Untitled](semarchy-certification-training-notes/untitled-460.png)

![Untitled](semarchy-certification-training-notes/untitled-461.png)

![Untitled](semarchy-certification-training-notes/untitled-462.png)

**Lab 15 - Integrating Data**

![Untitled](semarchy-certification-training-notes/untitled-463.png)

![Untitled](semarchy-certification-training-notes/untitled-464.png)

XDM_DEV_EN_225_Integrating Data - Solution

In this module you will find the solutions to Hands On Lab 15

Lab 15 Task 1 - Create Integration Job
Lab 15 Task 2 - Create Continuous Load
Lab 15 Task 3 - Using the Continuous Load

**Lab 15 Task 1 Solution - Create Integration Job**

![Untitled](semarchy-certification-training-notes/untitled-465.png)

![Untitled](semarchy-certification-training-notes/untitled-466.png)

![Untitled](semarchy-certification-training-notes/untitled-467.png)

![Untitled](semarchy-certification-training-notes/untitled-468.png)

![Untitled](semarchy-certification-training-notes/untitled-469.png)

![Untitled](semarchy-certification-training-notes/untitled-470.png)

![Untitled](semarchy-certification-training-notes/untitled-471.png)

**Lab 15 Task 2 Solution - Create Continuous Loads**

![Untitled](semarchy-certification-training-notes/untitled-472.png)

![Untitled](semarchy-certification-training-notes/untitled-473.png)

![Untitled](semarchy-certification-training-notes/untitled-474.png)

![Untitled](semarchy-certification-training-notes/untitled-475.png)

![Untitled](semarchy-certification-training-notes/untitled-476.png)

**Lab 15 Task 3 Solution - Using the Continuous Load**

![Untitled](semarchy-certification-training-notes/untitled-477.png)

![Untitled](semarchy-certification-training-notes/untitled-478.png)

![Untitled](semarchy-certification-training-notes/untitled-479.png)

![Untitled](semarchy-certification-training-notes/untitled-480.png)

![Untitled](semarchy-certification-training-notes/untitled-481.png)

![Untitled](semarchy-certification-training-notes/untitled-482.png)

![Untitled](semarchy-certification-training-notes/untitled-483.png)

![Untitled](semarchy-certification-training-notes/untitled-484.png)

XDM_DEV_EN_230_DELETION - Deleting Records

In this module we will be discussing Deletion

You will learn:

What does Deletion mean?
How to Configure Deletion

**PRESENTATION: Deletion**

![Untitled](semarchy-certification-training-notes/untitled-485.png)

![Untitled](semarchy-certification-training-notes/untitled-486.png)

![Untitled](semarchy-certification-training-notes/untitled-487.png)

![Untitled](semarchy-certification-training-notes/untitled-488.png)

**DEMO: Configuring Deletion**

![Untitled](semarchy-certification-training-notes/untitled-489.png)

![Untitled](semarchy-certification-training-notes/untitled-490.png)

![Untitled](semarchy-certification-training-notes/untitled-491.png)

![Untitled](semarchy-certification-training-notes/untitled-492.png)

![Untitled](semarchy-certification-training-notes/untitled-493.png)

![Untitled](semarchy-certification-training-notes/untitled-494.png)

![Untitled](semarchy-certification-training-notes/untitled-495.png)

![Untitled](semarchy-certification-training-notes/untitled-496.png)

![Untitled](semarchy-certification-training-notes/untitled-497.png)

**Slides: Deleting Records**

[DeletingRecords.pdf](semarchy-certification-training-notes/deletingrecords.pdf)

# 

![Untitled](semarchy-certification-training-notes/untitled-498.png)

# **Slides: Data Retention Policies**

[XDM_DEV_230_Retention_Policies.pdf](semarchy-certification-training-notes/xdm-dev-230-retention-policies.pdf)

XDM_DEV_EN_240_Consuming Data using SQL

In this module you will learn to how consume data using SQL

You will learn about

Executing basic queries in SQL
Using SQL to cross reference Golden Data to Source Systems
Creating Database Views

**Demo: Consuming Data - Basic SQL Queries**

![Untitled](semarchy-certification-training-notes/untitled-499.png)

![Untitled](semarchy-certification-training-notes/untitled-500.png)

**Demo: Consuming Data - Advanced SQL Query**

![Untitled](semarchy-certification-training-notes/untitled-501.png)

![Untitled](semarchy-certification-training-notes/untitled-502.png)

**Slides: Consuming data using SQL**

[5.3 - Manipulating data - SQL.pdf](semarchy-certification-training-notes/5-3-manipulating-data-sql.pdf)

![Untitled](semarchy-certification-training-notes/untitled-503.png)

**Demo: Consuming Data - Creating Database Views**

![Untitled](semarchy-certification-training-notes/untitled-504.png)

![Untitled](semarchy-certification-training-notes/untitled-505.png)

![Untitled](semarchy-certification-training-notes/untitled-506.png)

![Untitled](semarchy-certification-training-notes/untitled-507.png)

![Untitled](semarchy-certification-training-notes/untitled-508.png)

![Untitled](semarchy-certification-training-notes/untitled-509.png)

![Untitled](semarchy-certification-training-notes/untitled-510.png)

![Untitled](semarchy-certification-training-notes/untitled-511.png)

![Untitled](semarchy-certification-training-notes/untitled-512.png)

XDM_DEV_EN_260_Dashboard Builder

This module is an introduction to the dashboard builder that will allow you to integrate KPI in your xDM application.

- If you need more information about the dashboard builder we have an Advanced Dashboard training available.

**Slides: Designing dashboards**

[6.1 - Designing dashboards.pdf](semarchy-certification-training-notes/6-1-designing-dashboards.pdf)

**Demo: Dashboard Builder**

![Untitled](semarchy-certification-training-notes/untitled-513.png)

![Untitled](semarchy-certification-training-notes/untitled-514.png)

![Untitled](semarchy-certification-training-notes/untitled-515.png)

![Untitled](semarchy-certification-training-notes/untitled-516.png)

![Untitled](semarchy-certification-training-notes/untitled-517.png)

![Untitled](semarchy-certification-training-notes/untitled-518.png)

![Untitled](semarchy-certification-training-notes/untitled-519.png)

![Untitled](semarchy-certification-training-notes/untitled-520.png)

![Untitled](semarchy-certification-training-notes/untitled-521.png)

![Untitled](semarchy-certification-training-notes/untitled-522.png)

![Untitled](semarchy-certification-training-notes/untitled-523.png)

![Untitled](semarchy-certification-training-notes/untitled-524.png)

![Untitled](semarchy-certification-training-notes/untitled-525.png)

![Untitled](semarchy-certification-training-notes/untitled-526.png)

![Untitled](semarchy-certification-training-notes/untitled-527.png)

![Untitled](semarchy-certification-training-notes/untitled-528.png)

![Untitled](semarchy-certification-training-notes/untitled-529.png)

![Untitled](semarchy-certification-training-notes/untitled-530.png)

![Untitled](semarchy-certification-training-notes/untitled-531.png)

![Untitled](semarchy-certification-training-notes/untitled-532.png)

![Untitled](semarchy-certification-training-notes/untitled-533.png)

![Untitled](semarchy-certification-training-notes/untitled-534.png)

![Untitled](semarchy-certification-training-notes/untitled-535.png)

![Untitled](semarchy-certification-training-notes/untitled-536.png)

![Untitled](semarchy-certification-training-notes/untitled-537.png)

![Untitled](semarchy-certification-training-notes/untitled-538.png)

![Untitled](semarchy-certification-training-notes/untitled-539.png)

![Untitled](semarchy-certification-training-notes/untitled-540.png)

![Untitled](semarchy-certification-training-notes/untitled-541.png)

![Untitled](semarchy-certification-training-notes/untitled-542.png)

![Untitled](semarchy-certification-training-notes/untitled-543.png)

![Untitled](semarchy-certification-training-notes/untitled-544.png)

![Untitled](semarchy-certification-training-notes/untitled-545.png)

![Untitled](semarchy-certification-training-notes/untitled-546.png)

![Untitled](semarchy-certification-training-notes/untitled-547.png)

XDM_DEV_EN_250_REST API

In this module we will cover all the REST API that you can use to interact with the data hub.

**Presentation: Consuming Data using REST APIs - Basic Queries**

![Untitled](semarchy-certification-training-notes/untitled-548.png)

![Untitled](semarchy-certification-training-notes/untitled-549.png)

![Untitled](semarchy-certification-training-notes/untitled-550.png)

![Untitled](semarchy-certification-training-notes/untitled-551.png)

![Untitled](semarchy-certification-training-notes/untitled-552.png)

![Untitled](semarchy-certification-training-notes/untitled-553.png)

![Untitled](semarchy-certification-training-notes/untitled-554.png)

![Untitled](semarchy-certification-training-notes/untitled-555.png)

![Untitled](semarchy-certification-training-notes/untitled-556.png)

**Slides: Rest API documentation**

[5.4 - Manipulating data - REST APIs.pdf](semarchy-certification-training-notes/5-4-manipulating-data-rest-apis.pdf)

**Demo: Consuming Data using REST API - Named Queries**

![Untitled](semarchy-certification-training-notes/untitled-557.png)

![Untitled](semarchy-certification-training-notes/untitled-558.png)

![Untitled](semarchy-certification-training-notes/untitled-559.png)

![Untitled](semarchy-certification-training-notes/untitled-560.png)

![Untitled](semarchy-certification-training-notes/untitled-561.png)

![Untitled](semarchy-certification-training-notes/untitled-562.png)

![Untitled](semarchy-certification-training-notes/untitled-563.png)

![Untitled](semarchy-certification-training-notes/untitled-564.png)

![Untitled](semarchy-certification-training-notes/untitled-565.png)

![Untitled](semarchy-certification-training-notes/untitled-566.png)

![Untitled](semarchy-certification-training-notes/untitled-567.png)

![Untitled](semarchy-certification-training-notes/untitled-568.png)

![Untitled](semarchy-certification-training-notes/untitled-569.png)

**Slides: Consuming Data using REST API**

[Manipulating data - REST APIs (2).pdf](Semarchy%20Certification%20Training%20notes/Manipulating_data_-_REST_APIs_(2).pdf)

**Lab 16 - Manipulating Data using REST API**

![Untitled](semarchy-certification-training-notes/untitled-570.png)

![Untitled](semarchy-certification-training-notes/untitled-571.png)

![Untitled](semarchy-certification-training-notes/untitled-572.png)

[Lab 16 - Manipulating Data using REST API.pdf](semarchy-certification-training-notes/lab-16-manipulating-data-using-rest-api.pdf)

**Slides: REST API - Administration Tasks**

[REST APIs - Administrative Actions.pdf](semarchy-certification-training-notes/rest-apis-administrative-actions.pdf)

XDM_DEV_EN_255_REST API - Solution

In this module you will find the solution to Hands On Lab 16 REST API

Lab 16 Task 1 - Load Customer
Lab 16 Task 2 - Query Data

**Lab 16 Task 1 - Create a Customer record**

![Untitled](semarchy-certification-training-notes/untitled-573.png)

![Untitled](semarchy-certification-training-notes/untitled-574.png)

![Untitled](semarchy-certification-training-notes/untitled-575.png)

**Lab 16 Task 2 - Query Data**

![Untitled](semarchy-certification-training-notes/untitled-576.png)

![Untitled](semarchy-certification-training-notes/untitled-577.png)

XDM_DEV_EN_270_Deploying Model to Data Location

In this module, you will learn about Open and Closed Model Editions and Branching

**Demo: Deployment Process**

![Untitled](semarchy-certification-training-notes/untitled-578.png)

![Untitled](semarchy-certification-training-notes/untitled-579.png)

![Untitled](semarchy-certification-training-notes/untitled-580.png)

![Untitled](semarchy-certification-training-notes/untitled-581.png)

![Untitled](semarchy-certification-training-notes/untitled-582.png)

![Untitled](semarchy-certification-training-notes/untitled-583.png)

![Untitled](semarchy-certification-training-notes/untitled-584.png)

![Untitled](semarchy-certification-training-notes/untitled-585.png)

![Untitled](semarchy-certification-training-notes/untitled-586.png)

![Untitled](semarchy-certification-training-notes/untitled-587.png)

![Untitled](semarchy-certification-training-notes/untitled-588.png)

![Untitled](semarchy-certification-training-notes/untitled-589.png)

![Untitled](semarchy-certification-training-notes/untitled-590.png)

![Untitled](semarchy-certification-training-notes/untitled-591.png)

**Slides: Model Editions and Deployment Process**

[7.1 - Deploying models to data locations.pdf](semarchy-certification-training-notes/7-1-deploying-models-to-data-locations.pdf)

![Untitled](semarchy-certification-training-notes/untitled-592.png)

![Untitled](semarchy-certification-training-notes/untitled-593.png)

XDM_DEV_EN_280_Applying Role Based Security

In this module you will learn how to configure

Users
Roles
Privileges
to manage security on your data hub.

![Untitled](semarchy-certification-training-notes/untitled-594.png)

![Untitled](semarchy-certification-training-notes/untitled-595.png)

![Untitled](semarchy-certification-training-notes/untitled-596.png)

![Untitled](semarchy-certification-training-notes/untitled-597.png)

![Untitled](semarchy-certification-training-notes/untitled-598.png)

![Untitled](semarchy-certification-training-notes/untitled-599.png)

![Untitled](semarchy-certification-training-notes/untitled-600.png)

![Untitled](semarchy-certification-training-notes/untitled-601.png)

![Untitled](semarchy-certification-training-notes/untitled-602.png)

![Untitled](semarchy-certification-training-notes/untitled-603.png)

**Demo: How to add Users and Roles**

![Untitled](semarchy-certification-training-notes/untitled-604.png)

![Untitled](semarchy-certification-training-notes/untitled-605.png)

![Untitled](semarchy-certification-training-notes/untitled-606.png)

![Untitled](semarchy-certification-training-notes/untitled-607.png)

![Untitled](semarchy-certification-training-notes/untitled-608.png)

![Untitled](semarchy-certification-training-notes/untitled-609.png)

![Untitled](semarchy-certification-training-notes/untitled-610.png)

![Untitled](semarchy-certification-training-notes/untitled-611.png)

![Untitled](semarchy-certification-training-notes/untitled-612.png)

![Untitled](semarchy-certification-training-notes/untitled-613.png)

![Untitled](semarchy-certification-training-notes/untitled-614.png)

![Untitled](semarchy-certification-training-notes/untitled-615.png)

![Untitled](semarchy-certification-training-notes/untitled-616.png)

![Untitled](semarchy-certification-training-notes/untitled-617.png)

![Untitled](semarchy-certification-training-notes/untitled-618.png)

![Untitled](semarchy-certification-training-notes/untitled-619.png)

![Untitled](semarchy-certification-training-notes/untitled-620.png)

**Slides: Applying Role Based Security**

[ApplyingRoleBasedSecurity.pdf](semarchy-certification-training-notes/applyingrolebasedsecurity.pdf)

![Untitled](semarchy-certification-training-notes/untitled-621.png)

XDM_DEV_EN_290_Administering the platform

In this module you will learn about configuring platform features such as

Integrated Authentication
Startup Configuration
Datasources
Secrets

**Slides: Administering the Platform**

[Administering the Platform.pdf](semarchy-certification-training-notes/administering-the-platform.pdf)

**Demo: Configure a Datasource**

![Untitled](semarchy-certification-training-notes/untitled-622.png)

![Untitled](semarchy-certification-training-notes/untitled-623.png)

![Untitled](semarchy-certification-training-notes/untitled-624.png)

![Untitled](semarchy-certification-training-notes/untitled-625.png)

![Untitled](semarchy-certification-training-notes/untitled-626.png)

![Untitled](semarchy-certification-training-notes/untitled-627.png)

![Untitled](semarchy-certification-training-notes/untitled-628.png)

![Untitled](semarchy-certification-training-notes/untitled-629.png)

ALL_EN_Training satisfaction survey and last information

[https://www.semarchy.com/tutorials-documentation/](https://www.semarchy.com/tutorials-documentation/)

[Information Semarchy Documentation.pdf](semarchy-certification-training-notes/information-semarchy-documentation.pdf)

[Information Semarchy Community.pdf](semarchy-certification-training-notes/information-semarchy-community.pdf)